---
name: rust-error-index
description: Rust 編譯器錯誤碼索引（Compiler Error Index）的離線 markdown 副本。當用戶貼上 rustc 編譯錯誤（E0xxx 或 "error[Exxxx]"）想知道意思同點修時使用。Triggers：E0xxx, rustc error, compiler error code, 編譯錯誤, borrow checker error, E0308, E0382, E0495, E0499, E0502, E0597, E0658, E0277, E0425, E0433, 錯誤碼解釋, error explain。
---

# Rust 編譯錯誤碼索引離線副本

官方《Rust error codes index》的離線 markdown 版，直接對應 https://doc.rust-lang.org/error-index.html 。來源：`https://doc.rust-lang.org/error_codes/print.html`（mdbook print 版）轉做 markdown。

## 使用方法

1. 收到 `error[E0308]: …` 之類的錯誤 → 直接讀 `docs/E0308.md`。
2. 不確定某錯誤碼存在與否 → 睇 `docs/index.md`（全部錯誤碼索引）。
3. 對應 `rustc --explain E0308` 的官方解釋；用法相同。

## 佈局

- `docs/E0xxx.md` — 每個錯誤碼一個檔案（含說明、錯誤範例、正確寫法）
- `docs/index.md` — 全部錯誤碼清單
- `UPSTREAM.txt` — 抓取時間（此頁隨穩定版發佈更新）

## 注意

- 內容由 HTML 自動轉 markdown，極少數格式（如 playground 連結、`{{#…}}` 殘留）可能不完美，但文字語義完整。
- 部分錯誤碼標注 "no longer emitted"（舊版本殘留），檔案內會有明示。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
