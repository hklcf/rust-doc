---
name: rustc-book
description: The rustc Book 官方 rustc 手冊的離線 markdown 副本。當用戶問 rustc 編譯器 flags、codegen options、lints、目標設定、或調試／優化編譯時使用。Triggers：rustc, rustc flags, -C codegen-units, lto, target-cpu, target-feature, -C opt-level, -C debuginfo, -Z flags, lint levels, allow warn deny, -W -D, --explain, emit, -L, --extern, crate-type, panic=abort, sanitizers, PGO, profile-guided optimization, incremental compilation, linker flavor, target specification, cross compile, raw dylib, --emit asm, 編譯器選項。
---

# The rustc Book 離線副本

Rust 官方 rustc 手冊《The rustc Book》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/rustc/ 。上游：`github.com/rust-lang/rust`（`src/doc/rustc/src`）。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全目錄。
2. `docs/` 下按主題分檔：`docs/what-is-rustc.md`、`docs/command-line-arguments.md` 及 `docs/codegen-options/…`（`-C` 系列詳解）、`docs/lint-levels.md`、`docs/linker-flavors.md`、`docs/sanitizers.md` 等。
3. 查 error/warning 語意解釋唔喺本書——用 `rust-error-index` skill；查 nightly flags 用 `rust-unstable-book`。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間（同 `rust-unstable-book`、`rustdoc-book` 來自同一 repo，commit 相同）
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 多數 `-Z`（nightly）flags 只在 `rust-unstable-book` 有文檔；穩定 flags 以本書為準。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
