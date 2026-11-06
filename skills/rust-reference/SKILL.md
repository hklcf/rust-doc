---
name: rust-reference
description: The Rust Reference 官方語言參考的離線 markdown 副本。規格級講清楚每個語言特性的精確語義（並非教程，而是標準）。當用戶需要 Rust 語言的準確定義、語法、語義細節、邊界行為時使用。Triggers：rust reference, 語言參考, 規格, semantics, notation, grammar, expressions, types, traits coherence, method resolution, attributes, item kinds, statements, patterns, exhaustiveness, operator precedence, coercions, subtyping, variance, inline assembly, tool attributes, 宏的衛生性與展開規則, unsafe 契約。
---

# The Rust Reference 離線副本

Rust 官方語言參考《The Rust Reference》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/reference/ 。上游：`github.com/rust-lang/reference`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/` 下按主題分檔（例如 `docs/expressions/…`、`docs/types/…`、`docs/patterns.md`、`docs/attributes.md`），檔名即 URL 路徑。
3. Reference 係語義定義而非教程；回答「這段 code 到底合不合法/為什麼」時以此為準，比 The Book 更精確。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令或未 build 的交叉引用連結（如 `../syntax-index.html#xxx`）屬正常現象。
- Reference 本身未完成（incomplete），個別未定語義以 nightly/實際編譯器行為為準；此時可配合 `rust-unstable-book`、`rust-error-index` 或本地 `rustc --explain`。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
