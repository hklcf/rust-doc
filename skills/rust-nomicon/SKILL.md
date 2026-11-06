---
name: rust-nomicon
description: The Rustonomicon 官方 unsafe Rust 聖經的離線 markdown 副本。當用戶寫/審 unsafe code、raw pointer、手動內存管理、FFI、並發原語、或問 undefined behavior、安全性契約時使用。Triggers：nomicon, unsafe, 安全抽象, undefined behavior, UB, raw pointer, uninitialized memory, MaybeUninit, 手動釋放, drop order, ManuallyDrop, PhantomData, variance, Send Sync, Sync 實作, 資料競爭, data race, atomics, Mutex 實作, 型別破壞記憶體安全的方式, 別名, aliasing, Stacked Borrows。
---

# The Rustonomicon（The ’Nomicon）離線副本

Rust 官方 unsafe 指南《The Rustonomicon》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/nomicon/ 。上游：`github.com/rust-lang/nomicon`。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/` 下按主題分檔（例如 `docs/vec.md`（手寫 Vec）、`docs/lifetime.md`、`docs/phantom.md`、`docs/uninitialized.md`、`docs/send-sync.md`、`docs/atomics.md`），檔名即 URL 路徑。
3. 凡涉及 unsafe 正確性論證（別名規則、drop 檢查、layout、variance），以此書為準。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 本書部分章節較舊（如某些 stacked borrows 討論）；最新語義仍可配合 `rust-reference` 與 rustc 實際行為。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
