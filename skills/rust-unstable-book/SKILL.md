---
name: rust-unstable-book
description: The Unstable Book 官方 nightly-only 功能文件的離線 markdown 副本。當用戶用 nightly Rust、問 -Z flags、feature gates、unstable 功能時使用。Triggers：nightly, unstable book, -Z flags, feature gates, feature 屬性 feature(foo), unstable features, gate, jit, const 內嵌, specialization, generators, async closures unstable, let_chains, type_alias_impl_trait, polonius, pipelined compilation, codegen backend, Cranelift, rustc_private。
---

# The Unstable Book 離線副本

Rust 官方 nightly 功能文件《The Unstable Book》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/nightly/unstable-book/ 。上游：`github.com/rust-lang/rust`（`src/doc/unstable-book/src`）。

## 使用方法

1. 本書按 unstable feature 分檔（`docs/<feature-name>.md`），每檔說明 feature gate、狀態、用途；冇統一索引頁，用檔名（feature 名）定位。
2. 知道 feature 名 → 直接讀 `docs/<feature>.md`；不知道名 → 先按 SUMMARY-less 目錄逐個瀏覽（約 200+ 檔），或 grep docs/ 關鍵字。
3. 每個檔案對應一個追蹤 issue（rust 的 unstable tracking issue），檔內會說明現狀；功能一旦穩定化就會從本書移除。

## 佈局

- `docs/` — 全書 markdown 源碼（本書無 SUMMARY.md，按 feature 分檔）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間（同 `rustc-book`、`rustdoc-book` 來自同一 repo，commit 相同）
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 只適用於 nightly；穩定版用正式文檔（`rustc-book`、`rust-reference`）。
- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
