---
name: rust-cli-book
description: Command Line Applications in Rust（Rust CLI 書）的離線 markdown 副本。當用戶寫命令列工具、CLI 設計、clap 用法、分發給用戶時使用。Triggers：cli rust, 命令列工具, command line, clap, structopt, 15-minute app, 參數解析, subcommands, args, 終端輸出樣式, 進度條, colored output, 錯誤訊息給用戶, integration test, assert_cmd, 分發 cargo install, man page, 補全 completions, CLI UX。
---

# Rust CLI Book 離線副本

社區書《Command Line Applications in Rust》的離線 markdown 源碼（rust-lang.org Learn 頁亦有連結），直接對應 https://rust-cli.github.io/book/ 。上游：`github.com/rust-cli/book`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/` 下按主題分檔，重點：`docs/tutorial/…`（15 分鐘上手）、`docs/arguments/…`（clap）、`docs/input/…`、`docs/output/…`、`docs/testing/…`、`docs/distribution/…`。
3. 配合 `rust-cargo-book` 處理發佈（`cargo publish`／`cargo install`）與 `Cargo.toml` 設定。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引；含示範用 `.rs` 檔案）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼；部分例子含 `{{#include *.rs}}`，對應檔案都已放喺 `docs/` 內，路徑仍然相對。
- clap 版本演進快（derive API 為主流）；最新 API 細節以 docs.rs/clap 為準。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
