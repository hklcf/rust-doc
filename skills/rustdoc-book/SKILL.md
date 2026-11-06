---
name: rustdoc-book
description: The rustdoc Book 官方 rustdoc 手冊的離線 markdown 副本。當用戶寫文檔註解、生成 API docs、設定 docs.rs、玩 intra-doc links、doctest、lints 時使用。Triggers：rustdoc, rustdoc flags, 文檔註解, doc comments, ///, //!, intra-doc links, 文檔內連結, unresolved link, rustdoc lint, broken_intra_doc_links, doctest, 文檔測試, doc test, docs.rs 設定, package.metadata.docs.rs, playground, doc 屬性, doc(cfg), doc(hidden), 顯示隱藏項, markdown 表格, JSON output, --output-format json。
---

# The rustdoc Book 離線副本

Rust 官方 rustdoc 手冊《The rustdoc Book》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/rustdoc/ 。上游：`github.com/rust-lang/rust`（`src/doc/rustdoc/src`）。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全目錄。
2. `docs/` 下按主題分檔：`docs/what-is-rustdoc.md`、`docs/command-line-arguments.md`、`docs/read-documentation/…`（in-doc settings、lints）、`docs/write-documentation/…`（markdown 語法、intra-doc links、doctests）。
3. 回答「cargo doc 出錯/連結失效」時，先查 `docs/…intra-doc` 相關章節與 lint 文檔。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間（同 `rustc-book`、`rust-unstable-book` 來自同一 repo，commit 相同）
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
