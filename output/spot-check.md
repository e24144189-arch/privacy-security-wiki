# 人工抽查紀錄

- 抽查日期：2026-11-16
- 對應 SKILL.md：關卡 C（人工抽查）
- 抽查方式：從簡報找到該句 → 對應 wiki 頁面 → 回 `raw/` 原文，用 PowerShell `Select-String` 搜尋比對。
- 抽查者：本人（不經 AI 判讀，指令輸出直接對照簡報文字）
- 抽查標的：全簡報最容易出錯的三類內容——72 小時的歸屬（第 11 頁）、個資法條文授權（第 11 頁）、英文原文引文（第 14 頁）。

## 抽查結果

| # | 簡報頁 | 抽查內容 | wiki 頁面 | raw 位置 | 結果 |
|---|---|---|---|---|---|
| 1 | 第 11 頁 | GDPR 的 72 小時說法 | `legal/time-limits-comparison.md` § 2 | `raw/06` 第 14 行 | **一致** |
| 2 | 第 11 頁 | 個資法第 12 條第 4 項：辦法由主管機關定之 | `legal/data-breach-notification.md` § 4 | `raw/01` 第 132 行（4） | **一致** |
| 3 | 第 11 頁 | 個資法原文是否有「72 小時」 | `legal/time-limits-comparison.md` § 4 | `raw/01` 全檔搜尋 | **一致**（無） |
| 4 | 第 14 頁 | NIST：節流是線上攻擊的主要防線 | `legal/password-authentication-guidelines.md` § 1.5 | `raw/05` 第 40 行 | **一致** |

## 結論

四項抽查全部與 raw 原文一致，沒有發現需要修改的地方。本專案前面實際發現的錯誤（`source-06` 重現應排除的原句、`post-breach-defense` 多出 raw 沒有的「不回撥原電話」、簡報第 10 頁 72 小時提示框矛盾等），都是在 lint 抽查或新對話審查時找到並修正的，紀錄見 `output/loop-log.md` 與 git 歷史。
