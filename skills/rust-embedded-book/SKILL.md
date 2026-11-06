---
name: rust-embedded-book
description: The Rust Embedded Book 官方嵌入式 Rust 書的離線 markdown 副本。當用戶做嵌入式／no_std／微控制器（ARM Cortex-M、RISC-V）Rust 開發、或問 embedded HAL、no_std 設定、中斷、晶片外設、RTIC／RTFM、embedded-hal 時使用。Triggers：embedded rust, no_std, 嵌入式, 微控制器, MCU, ARM Cortex-M, RISC-V, thumbv6m cortex-m, embedded-hal, 外設, register access, volatile, MMIO, interrupt, 中斷處理, RTIC, RTFM, 開發版入門, QEMU 模擬。
---

# The Rust Embedded Book 離線副本

Rust 官方嵌入式書《The Embedded Book》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/embedded-book/ 。上游：`github.com/rust-embedded/book`（doc.rust-lang.org 內嵌此書）。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/` 下按主題分檔（例如 `docs/setup/…`（工具鏈）、`docs/intro/…`、`docs/printnb.md`、`docs/registers/…`、`docs/interrupts/…`、`docs/concurrency.md`、`docs/vendor-crates.md`），檔名即 URL 路徑。
3. 面向 no_std 環境；回答 embedded 問題時注意：標準庫不可用、多數例子假設 bare-metal 目標與 cross-compiling。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 嵌入式生態更新快（新晶片 support、RTIC 演進）；最新 crate 版本以 crates.io 及 `embedded-hal` 文件為準。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
