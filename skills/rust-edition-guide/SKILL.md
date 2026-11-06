---
name: rust-edition-guide
description: The Rust Edition Guide 官方版本指南的離線 markdown 副本。當用戶問 Rust edition（2015/2018/2021/2024）差異、遷移、edition 專屬語法或關鍵字時使用。Triggers：edition, edition guide, 2015 edition, 2018 edition, 2021 edition, 2024 edition, dyn Trait, impl Trait, async await edition, match ergonomics, disjoint closure capture, closures migration, try blocks, gen keyword, unsafe op in unsafe fn, let-else, 遷移 cargo fix, edition 遷移, rust_2018_idioms。
---

# The Rust Edition Guide 離線副本

Rust 官方版本指南《The Rust Edition Guide》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/edition-guide/ 。上游：`github.com/rust-lang/edition-guide`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄（按版本分章：2018／2021／2024）。
2. `docs/` 下按 edition 分檔（例如 `docs/edition-2018.md`、`docs/edition-2021.md`、`docs/edition-2024.md`）；各細項（closures、panic macros、unsafe_op_in_unsafe_fn 等）為獨立小節。
3. 回答「這段 code 喺新 edition 出 error/warning 點解」時，配合 `rust-cargo-book` 講 edition 遷移流程（`cargo fix --edition`）。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
