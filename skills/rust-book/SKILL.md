---
name: rust-book
description: The Rust Programming Language（The Book / TRPL）官方教學書的離線 markdown 副本。當用戶問 Rust 基礎概念（ownership、borrowing、lifetimes、struct、enum、trait、pattern matching、錯誤處理、modules、cargo、collections、generics、closures、iterators、smart pointers、concurrency、async、OOP、unsafe、advanced）或想引用官方書的章節與範例 listings 時使用。Triggers：rust book, the book, TRPL, 所有權, 借用, 生命週期, trait 定義, match 窮盡檢查, Option Result, match 錯誤處理, cargo 專案, 猜數字遊戲, 猜數字教學。
---

# The Rust Programming Language（The Book）離線副本

Rust 官方入門書《The Rust Programming Language》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/book/ 。上游：`github.com/rust-lang/book`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/ch*-…md` 係各章節 markdown；檔案路徑即 doc.rust-lang.org/book/ 的 URL 路徑。
3. 章節 md 內的 `{{#include …}}`、`{{#rustdoc_include …}}` 係 mdbook 指令，路徑相對於該 md 檔，指向 skill 根目錄的 `listings/`（例如 `docs/ch02-00-guessing-game-tutorial.md` 內的 `../listings/ch02-…/src/main.rs` → `listings/ch02-…/src/main.rs`）。讀到這類指令時直接讀對應 listings 檔案即可，不要當語法錯誤。
4. 代碼裡 `{{#rustdoc_include file.rs:io}}` 的 `:io` 係行號錨點，代表只取該範圍——直接讀整個檔案也可以。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `listings/` — 書中所有範例代碼（mdbook `{{#include}}` 的來源）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（文件以 MIT OR Apache-2.0 釋出）

## 注意

- 內容係源碼，唔經 mdbook build，所以 md 內會見到 mdbook 指令而非最終渲染結果；理解其語義即可。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
