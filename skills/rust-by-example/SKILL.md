---
name: rust-by-example
description: Rust by Example（官方實戰入門）離線 markdown 副本。以大量可跑例子、少量文字講解 Rust，附 exercises。當用戶想快速查某個語法/標準庫用法的示範、睇 RBE 例子、或做 by example 練習時使用。Triggers：rust by example, RBE, rust 範例學習, 快速上手 rust 例子, 格式化輸出, primitives, flow control, iteration, conversions, String 轉換, closures 例子, iterators example, std 用法速查, exercises 練習。
---

# Rust by Example（RBE）離線副本

官方入門教程《Rust by Example》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/rust-by-example/ 。上游：`github.com/rust-lang/rust-by-example`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全教程目錄（Hello World → … → std / testing / macro）。
2. `docs/` 下按主題分檔（例如 `docs/hello.md`、`docs/trait/…`），檔名即 URL 路徑。
3. 大部分例子係直接寫喺 md 內的 rust code block；部分示範輸出以 `// Output:` 註解標示。

## 佈局

- `docs/` — 全教程 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，md 內可能見到 `{{#…}}` 指令或 playground 連結；語義照常理解即可。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
