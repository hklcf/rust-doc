# rust-doc — Rust 官方文檔離線副本（OpenCode skills）

> Offline copy of the official Rust documentation (from <https://rust-lang.org/learn/>) packaged as [OpenCode](https://opencode.ai) skills, with a one-command updater.
> 把 rust-lang.org/learn 頁面上的官方 Rust 文檔全部做成 OpenCode skills（離線 markdown 源碼 + 一鍵更新腳本），方便 AI 助手隨時載入查閱。

只收錄英文官方文檔。不含標準庫 API 文檔（自動生成的 rustdoc，質素與體積都不適合作為 skill）；本機可用 `rustup doc --std` 隨時離線查閱。

## Skill 一覽

| Skill | 內容 | 上游 |
|---|---|---|
| `rust-book` | The Rust Programming Language（The Book / TRPL） | `rust-lang/book` |
| `rust-by-example` | Rust by Example（例子 + exercises） | `rust-lang/rust-by-example` |
| `rust-reference` | The Rust Reference（語言規格級參考） | `rust-lang/reference` |
| `rust-nomicon` | The Rustonomicon（unsafe Rust） | `rust-lang/nomicon` |
| `rust-edition-guide` | The Rust Edition Guide（2015/2018/2021/2024） | `rust-lang/edition-guide` |
| `rust-cargo-book` | The Cargo Book（cargo / workspace / features / 發佈） | `rust-lang/cargo`（`doc/book`） |
| `rustc-book` | The rustc Book（編譯器 flags、codegen、lints） | `rust-lang/rust`（`src/doc/rustc`） |
| `rustdoc-book` | The rustdoc Book（文檔註解、intra-doc links、doctests） | `rust-lang/rust`（`src/doc/rustdoc`） |
| `rust-unstable-book` | The Unstable Book（nightly feature gates、`-Z` flags） | `rust-lang/rust`（`src/doc/unstable-book`） |
| `rust-embedded-book` | The Embedded Book（no_std / 微控制器） | `rust-embedded/book` |
| `rust-cli-book` | Command Line Applications in Rust | `rust-cli/book` |
| `rust-error-index` | Compiler Error Index（`E0xxx` 錯誤碼解釋，HTML 轉 markdown） | <https://doc.rust-lang.org/error_codes/print.html> |

每個 skill 的 `docs/` 都是**上游 markdown 源碼**（mdbook），不是渲染後的 HTML；`UPSTREAM.txt` 記錄同步時的上游 repo／commit／時間。

## 安裝（OpenCode）

### 方法一：喺 opencode.json(c) 直接指住本 repo（推薦，零複製）

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/Documents/rust-doc/skills"]
}
```

之後 `git pull` 呢個 repo 就等於更新所有 skill。路徑支援 `~/`、絕對路徑、相對路徑（相對於當前工作目錄）。全域 (`~/.config/opencode/opencode.json(c)`) 或專案 (`.opencode/opencode.json(c)`) 都得。

### 方法二：junction / 複製到 skills 目錄

Windows（junction，`git pull` 即生效）：

```powershell
$repo = "$env:USERPROFILE\Documents\rust-doc"
foreach ($d in Get-ChildItem "$repo\skills" -Directory) {
  New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\$($d.Name)" -Target $d.FullName
}
```

macOS / Linux（symlink）：

```sh
for d in ~/path/to/rust-doc/skills/*/; do ln -sfn "$d" ~/.config/opencode/skills/$(basename "$d"); done
```

唔想用 junction/symlink：直接 `cp -r skills/* ~/.config/opencode/skills/`，但每次更新都要重新複製。

專案級安裝：將 skills 複製（或 junction）到專案的 `.opencode/skills/` 即可，OpenCode 會由當前目錄向上搜尋。

> 全部 12 個 skill 目錄名都唔會同（OpenCode 用目錄名作為 skill ID，且是 case-sensitive）；若已存在同名 skill，後註冊者優先。

## 更新

只需要 **git + Python 3 + 網絡**：

```sh
python update.py   # 或 python3 update.py
```

腳本會用 depth-1 sparse clone 重新抓取所有上游 repo（約 11 MB），wipe 同重建每個 `skills/<name>/docs/`（`rust-book` 另同步 `listings/`），重新複製上游 `LICENSE-*`，並更新每個 `UPSTREAM.txt`。`rust-error-index` 則由 print.html 即時轉換。

## 自動更新（GitHub Actions）

`.github/workflows/sync-docs.yml` 會喺 **每週一 03:00 UTC** 自動跑 `python3 update.py`（亦可喺 Actions 頁手動「Run workflow」）：

1. 冇上游改動 → 直接結束，唔會郁 main；
2. 有改動 → force-push 到 `docs-update` 分支，開（或更新）一個標題 `docs: sync with upstream` 的 PR，內文列出改動到的 skills；
3. 跟住**自動 squash merge 入 main 並刪除分支**，唔需要任何額外 secrets（只用預設 `GITHUB_TOKEN`）。

注意：呢個 flow **會自己 merge**，你唔會見到 PR 停留。如果自動 merge 唔成功（main 有衝突、或分支保護要求 review），job 會 fail 並留返個 PR 喺度等你手動處理。junction 安裝（方法二）之後 `git pull` 即生效；零複製安裝（方法一）亦然。

令佢生效前要留意：

- **要先 merge 入 main**：`schedule` 同 `workflow_dispatch` 都只喺 default branch 嘅 workflow 生效。
- 若 `gh pr create` 報 permission 錯：repo Settings → Actions → General → 勾選 *Allow GitHub Actions to create and approve pull requests*。
- 自動 merge 需要 `main` 冇 branch protection 擋住；若你有開 required review，就要改成唔自動 merge（見下）。
- 上游冇改動時，workflow 只會 `git clone` 一輪後以「up to date」結束——即使每個星期一跑都係正常無事。

想改做「有上游改動就 workflow fail 提醒」而非開 PR：將最後一個 step 改成 `exit 1`、刪掉 PR 邏輯即可。

mdbook 指令（如 `{{#include ../listings/…}}`）係源碼內容的一部分：`rust-book` 的範例代碼在 `skills/rust-book/listings/`，指令路徑相對於 `docs/<chapter>/*.md`，直接讀取即可，不會失效。

## 目錄結構

```
├── README.md
├── LICENSE              # 本 repo 的 glue 授權（MIT）；各文檔保留上游授權
├── update.py            # 一鍵同步腳本（唯一 glue 代碼）
└── skills/
    └── <skill>/         # 每個 skill 一個目錄 = 一個 OpenCode skill
        ├── SKILL.md     #   skill 元數據 + 使用說明
        ├── docs/        #   上游 markdown（BOOK 的書以 SUMMARY.md 為目錄）
        ├── UPSTREAM.txt #   上游 repo / commit / 同步時間
        └── LICENSE-*    #   上游授權副本
```

## 授權

- 本 repo 的 glue（README、`update.py`）以 [MIT](LICENSE) 釋出。
- 各文檔內容保留上游授權，副本見各 skill 目錄（多數為 MIT OR Apache-2.0；`rust-embedded-book` 內容另含 CC-BY-SA 4.0（`LICENSE-CC-BY-SA`）；`rust-cli-book` 為單一 `LICENSE` 檔）。
- 錯誤碼內容來自 rust-lang 官方 error index（rust-lang/rust，MIT OR Apache-2.0）。
- 文檔內容版權歸各自作者所有；本 repo 只是鏡像 + 索引，不修改內容本身。

## 回報問題

- 文檔內容錯誤 → 請到各上游 repo 報（見 `UPSTREAM.txt`）。
- 同步腳本 / skill 索引問題 → 本 repo 的 issues。
