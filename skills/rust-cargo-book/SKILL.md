---
name: rust-cargo-book
description: The Cargo Book 官方 Cargo 手冊的離線 markdown 副本。當用戶問 cargo、Cargo.toml／lock、workspace、features、依賴、發佈 crate、build scripts 時使用。Triggers：cargo, Cargo.toml, Cargo.lock, manifest, workspace, features, optional dependencies, dev-dependencies, target-specific dependencies, build.rs, build script, cargo publish, crates.io, cargo install, version requirements, 語義化版本, semver, resolver, edition, profiles, release profile, lto, codegen-units, debug-assertions, registry, git 依賴, 私有 registry, config.toml, .cargo/config, 環境變數, cargo FAQ, net.retry, patch 區段。
---

# The Cargo Book 離線副本

Rust 官方 Cargo 手冊《The Cargo Book》的離線 markdown 源碼，直接對應 https://doc.rust-lang.org/cargo/ 。上游：`github.com/rust-lang/cargo`（`doc/book/src`）。

## 使用方法

1. 先睇 `docs/SUMMARY.md`，掌握全書目錄。
2. `docs/` 下按主題分目錄：`docs/getting-started/…`、`docs/reference/…`（manifest、commands、環境）、`docs/commands/…`（每個 cargo 子命令）、`docs/appendix/…`（FAQ、profiles、features）。
3. 常用問題直達：`docs/reference/manifest.md`（Cargo.toml 全解）、`docs/reference/features.md`、`docs/reference/workspaces.md`、`docs/reference/profiles.md`、`docs/reference/resolution.md`。

## 佈局

- `docs/` — 全書 markdown 源碼（`SUMMARY.md` 係目錄索引）
- `UPSTREAM.txt` — 上游 repo、commit、同步時間
- `LICENSE-APACHE`、`LICENSE-MIT`、`LICENSE-THIRD-PARTY` — 上游授權（MIT OR Apache-2.0）

## 注意

- 內容係 mdbook 源碼，見到 `{{#…}}` 指令屬正常現象。
- 手冊對應最新穩定版 Cargo；舊 toolchain 的行為差異以該版本 `cargo --version` 實際輸出為準。
- 要同步最新版：喺 repo 根目錄行 `python update.py`。
