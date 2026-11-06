#!/usr/bin/env python3
"""同步 Rust 官方文檔到 skills/*/（維護者用）。

只需要 git + Python 3 + 網絡。每次執行都會由頭 clone（depth 1, blob filter），
然後 wipe 同重建 skills/<name>/docs，再更新 UPSTREAM.txt。

用法:  python update.py
"""
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / 'skills'

# (skill, git url, sparse paths) — 同一 repo 只 clone 一次
SOURCES = [
    ('rust-book',          'https://github.com/rust-lang/book.git',              ['src', 'listings']),
    ('rust-by-example',    'https://github.com/rust-lang/rust-by-example.git',   ['src']),
    ('rust-reference',     'https://github.com/rust-lang/reference.git',         ['src']),
    ('rust-nomicon',       'https://github.com/rust-lang/nomicon.git',           ['src']),
    ('rust-edition-guide', 'https://github.com/rust-lang/edition-guide.git',     ['src']),
    ('rust-embedded-book', 'https://github.com/rust-embedded/book.git',          ['src']),
    ('rust-cli-book',      'https://github.com/rust-cli/book.git',               ['src']),
    ('rust-cargo-book',    'https://github.com/rust-lang/cargo.git',             ['doc/book/src']),
    ('rustc-book',         'https://github.com/rust-lang/rust.git',              ['src/doc/rustc/src']),
    ('rustdoc-book',       'https://github.com/rust-lang/rust.git',              ['src/doc/rustdoc/src']),
    ('rust-unstable-book', 'https://github.com/rust-lang/rust.git',              ['src/doc/unstable-book/src']),
]

# skill -> [(repo 內路徑, skill 內目標目錄)]
DEST = {
    'rust-book': [('src', 'docs'), ('listings', 'listings')],
    'rust-by-example': [('src', 'docs')],
    'rust-reference': [('src', 'docs')],
    'rust-nomicon': [('src', 'docs')],
    'rust-edition-guide': [('src', 'docs')],
    'rust-embedded-book': [('src', 'docs')],
    'rust-cli-book': [('src', 'docs')],
    'rust-cargo-book': [('doc/book/src', 'docs')],
    'rustc-book': [('src/doc/rustc/src', 'docs')],
    'rustdoc-book': [('src/doc/rustdoc/src', 'docs')],
    'rust-unstable-book': [('src/doc/unstable-book/src', 'docs')],
}

ERROR_INDEX_URL = 'https://doc.rust-lang.org/error_codes/print.html'


def run(cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True)


def sync_git_sources():
    by_url = {}
    for skill, url, sparse in SOURCES:
        by_url.setdefault(url, []).append((skill, sparse))
    for url, entries in by_url.items():
        with tempfile.TemporaryDirectory(prefix='rust-doc-sync-') as tmp:
            clone = Path(tmp) / 'repo'
            print(f'clone {url}')
            run(['git', 'clone', '--depth', '1', '--filter=blob:none', '--sparse', url, str(clone)])
            paths = sorted({p for _, sparse in entries for p in sparse})
            run(['git', 'sparse-checkout', 'set', *paths], cwd=clone)
            commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=clone, text=True).strip()
            for skill, _ in entries:
                target = SKILLS / skill
                if not target.is_dir():
                    print(f'skip {skill}: skills/{skill}/ 唔存在（SKILL.md 要先寫好）')
                    continue
                for _, dest in DEST[skill]:
                    dest_dir = target / dest
                    if dest_dir.exists():
                        shutil.rmtree(dest_dir)
                for repo_path, dest in DEST[skill]:
                    shutil.copytree(clone / repo_path, target / dest)
                # license 跟源 repo 帶走，標明上游歸屬（license-*.json 之類係 REUSE metadata，唔算 license）
                for lic in clone.iterdir():
                    if lic.is_file() and re.fullmatch(r'(?i)LICENSE(-[A-Za-z0-9-]+)?$', lic.name):
                        shutil.copy2(lic, target / lic.name)
                write_upstream(skill, f'repo: {url}\npath: {", ".join(DEST[skill][i][0] for i in range(len(DEST[skill])))}\ncommit: {commit}')
                print(f'  ok {skill} @ {commit[:12]}')


def write_upstream(skill, body):
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    (SKILLS / skill / 'UPSTREAM.txt').write_text(body + f'\nsynced: {stamp}\n', encoding='utf-8')


class ErrorIndexMarkdown(HTMLParser):
    """把 error-index 的 print.html <main> 轉做 markdown。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.in_pre = False
        self.pre_buf = []
        self.boring_stack = []  # pre 內 <span class="boring"> 的隱藏示範行，唔輸出
        self.skip_depth = 0     # script/style/svg

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style', 'svg', 'head'):
            self.skip_depth += 1
        elif self.skip_depth:
            return
        elif tag == 'pre':
            self.in_pre = True
            self.pre_buf = []
        elif tag == 'span' and self.in_pre:
            self.boring_stack.append('boring' if 'boring' in a.get('class', '') else None)
        elif tag == 'code':
            if not self.in_pre:
                self.out.append('`')
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            level = int(tag[1])
            self.out.append('\n\n' + '#' * level + ' ')
        elif tag == 'p':
            self.out.append('\n\n')
        elif tag == 'li':
            self.out.append('\n- ')
        elif tag in ('ul', 'ol'):
            self.out.append('\n')
        elif tag == 'br':
            self.out.append('\n')
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg', 'head'):
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == 'pre':
            code = ''.join(self.pre_buf).rstrip('\n')
            self.out.append('\n\n```rust\n' + code + '\n```\n\n')
            self.in_pre = False
            self.boring_stack = []
        elif tag == 'span' and self.in_pre:
            if self.boring_stack:
                self.boring_stack.pop()
        elif tag == 'code' and not self.in_pre:
            self.out.append('`')
        elif tag in ('h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol'):
            self.out.append('\n\n')
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_pre:
            if any(self.boring_stack):
                return
            self.pre_buf.append(data)
        else:
            self.out.append(re.sub(r'\s*\n\s*', ' ', data))

    def markdown(self):
        text = ''.join(self.out)
        text = re.sub(r'(?m)^[ \t]+$', '', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip() + '\n'


def html_to_markdown(chunk):
    parser = ErrorIndexMarkdown()
    parser.feed(chunk)
    return parser.markdown()


RUST_LICENSES = {
    'LICENSE-APACHE': 'https://raw.githubusercontent.com/rust-lang/rust/master/LICENSE-APACHE',
    'LICENSE-MIT': 'https://raw.githubusercontent.com/rust-lang/rust/master/LICENSE-MIT',
}


def sync_error_index():
    target = SKILLS / 'rust-error-index'
    if not target.is_dir():
        print('skip rust-error-index: skills/rust-error-index/ 唔存在')
        return
    print(f'fetch {ERROR_INDEX_URL}')
    html = urllib.request.urlopen(ERROR_INDEX_URL, timeout=120).read().decode('utf-8')
    for name, url in RUST_LICENSES.items():
        (target / name).write_bytes(urllib.request.urlopen(url, timeout=60).read())
    parts = re.split(r'<h1 id="(error-code-e\d+)">', html)
    docs = target / 'docs'
    if docs.exists():
        shutil.rmtree(docs)
    docs.mkdir(parents=True)
    codes = []
    for i in range(1, len(parts), 2):
        anchor, chunk = parts[i], parts[i + 1]
        code = anchor.replace('error-code-', '').upper()  # E0308
        body = html_to_markdown('<h1>' + chunk)
        (docs / f'{code}.md').write_text(body, encoding='utf-8')
        codes.append(code)
    codes.sort()
    index = ['# Rust 編譯錯誤碼索引（Compiler Error Index）', '',
             '每個錯誤碼一個檔案，見 `docs/<CODE>.md`，例如 `docs/E0308.md`。', '',
             f'共 {len(codes)} 個錯誤碼：', '']
    index += [f'- {c}' for c in codes]
    (docs / 'index.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    write_upstream('rust-error-index', f'source: {ERROR_INDEX_URL}\nerrors: {len(codes)} 個')
    print(f'  ok rust-error-index ({len(codes)} 個錯誤碼)')


def main():
    if not SKILLS.is_dir():
        sys.exit('skills/ 目錄唔存在')
    sync_git_sources()
    sync_error_index()
    print('完成。')


if __name__ == '__main__':
    main()
