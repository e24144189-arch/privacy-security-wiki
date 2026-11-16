# 知識庫操作日誌 (Operation Log)

本文件依時間由舊至新記錄知識庫所有重大操作（初始化、資料攝取 Ingest、問答沉澱 Query & Compounding、健康檢查 Lint）。
每筆日誌開頭採用標準格式：`## [YYYY-MM-DD] 操作類別 | 標題或說明`。

---

## [2026-11-16] init | 知識庫架構與規範初始化
- 完成 `AGENTS.md` 規範手冊之制定。
- 建立 `wiki/`（含 `defense/`, `legal/`, `sources/`, `entities/`）與 `output/` 目錄。
- 建立初始 `wiki/index.md` 與 `wiki/log.md`。
- 確認原始資料 `raw/` 包含 6 份文件，準備進入逐篇漸進式 Ingest 流程。

---

## [2026-11-16] ingest | 攝取 raw/01 臺灣個人資料保護法修正版
- 完成 `raw/01_pdpa_taiwan_law_2025-11-amended.md` 之資料攝取。
- 建立文獻精華摘要頁面：`wiki/sources/source-01-pdpa.md`。
- 建立知法知權篇頁面：
  - `wiki/legal/personal-data-definition.md`（個人資料之定義與第6條所列個人資料）
  - `wiki/legal/rights-of-data-subjects.md`（當事人法定權利與救濟規範）
  - `wiki/legal/data-breach-notification.md`（個人資料外洩事故通知與通報義務）
  - `wiki/legal/article-27-status.md`（個資法第 27 條狀態紀錄）
- 建立關鍵實體頁面：`wiki/entities/pdpc.md`（個人資料保護委員會）。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範：
  - 嚴守對象標記（個人／企業）、條號標註及限定三種法條狀態標籤。
  - 條文引用一律逐字照抄 raw 原文，不使用「特種個人資料」等外部名詞。
  - 第 51-1 條第 1、2 項引述完整句子與準確主詞。
  - 第 27 條嚴格中性記錄，不收錄任何舊文與修法去向。
  - 第 12 條事故通報罰則與第 20-1 條安全維護罰則嚴格分立。
  - 母法未載 72 小時、現行法狀態等均嚴格標註【raw 未載】與【待使用者確認】。

---

## [2026-11-16] ingest | 攝取 raw/03 數發部資安署 AI 網攻外洩新聞稿
- 完成 `raw/03_moda_ai_attack_data_breach_press.md` 之資料攝取。
- 建立來源摘要頁面：`wiki/sources/source-03-moda-ai-attack.md`。
- 建立個人自保篇頁面：`wiki/defense/post-breach-defense.md`（個資外洩後防詐自保四原則），專門收錄【對象：個人】之防詐與 2FA 指引。
- 建立知法知權專題頁面：`wiki/legal/time-limits-comparison.md`（個資外洩與資安通報時限比較專題），嚴格消歧義並區隔數發部四項 72 小時呼籲、一個月內改善計劃、個資法母法授權與 GDPR。
- 更新頁面：
  - `wiki/legal/article-27-status.md`：客觀並列 raw/01 標示刪除與 raw/03 引用第 27 條之文字，不寫舊文、不作裁決。
  - `wiki/legal/data-breach-notification.md`：增補數發部先行通知機制與實務指引。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範：
  - 企業因應建議與個人防詐自保受眾嚴格切分。
  - 數發部「十餘家」、「逾百萬份」、「近半數」明確標註為 2026-11-11 初查說法，非最終統計。
  - 引文一律逐字照抄 raw 原文。

---

## [2026-11-16] ingest | 攝取 raw/04 TWCERT/CC 社交工程防釣魚文獻
- 完成 `raw/04_twcert_social_engineering_phishing.md` 之資料攝取。
- 建立文獻精華摘要頁面：`wiki/sources/source-04-twcert.md`。
- 建立個人自保篇概念頁面：`wiki/defense/phishing-email-defense.md`（偽冒公務機關電子郵件與社交工程防範）。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範：
  - 原文筆誤保留原樣並標註【原文如此】（如「政府門」、「電子郵」）。
  - 原文提及之「圖1」流程圖依指示略過不收錄。
  - 嚴格分離溝通對象：個人防範指引收錄於 `wiki/defense/`【對象：個人】；企業宣導教育收錄於 `wiki/sources/`【對象：企業】。
  - 僅收錄辨認與預防措施，不提供攻擊腳本或話術。
  - `raw/04` 檔頭未記載來源網址，標註【raw 未載，待補來源】。

---

## [2026-11-16] ingest | 攝取 raw/02 165 全民防騙網常見詐騙手法清單
- 完成 `raw/02_165_common_scam_types.md` 之資料攝取。
- 建立文獻精華摘要頁面：`wiki/sources/source-02-165-scams.md`。
- 建立個人自保篇概念頁面：`wiki/defense/common-scams-recognition.md`（常見五大詐騙手法辨識特徵與自保防範）。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範：
  - 嚴格限定收錄 raw/02 記載之五大詐騙類型：假網拍詐騙、假投資詐騙、假交友(投資詐財)詐騙、猜猜我是誰詐騙、假廣告詐騙，名稱逐字照抄。
  - 嚴守紅線：僅提煉「辨識特徵」，不寫可照做的攻擊步驟或話術腳本。
  - 預防作為僅引述 raw/03 與 raw/04 已有內容並標明出處；兩者未載之特定防護措施均標註【raw 未載，待補來源】。
  - 全篇溝通對象嚴格標記【對象：個人】，範例全數使用虛構資料（王小明、`0900-000-000`、`user@example.com`、`https://example.com`）。

---

## [2026-11-16] ingest | 攝取 raw/05 NIST SP 800-63B 密碼安全技術規範
- 完成 `raw/05_nist_sp800-63b_passwords.md` 之資料攝取。
- 建立文獻精華摘要頁面：`wiki/sources/source-05-nist.md`。
- 建立知法知權篇技術規範頁面：`wiki/legal/password-authentication-guidelines.md`（服務提供者密碼驗證技術規範）。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範：
  - 嚴格定位受眾為【對象：服務提供者】（驗證方 Verifier / CSP），frontmatter 標註 `target_audience: 服務提供者`。
  - 嚴格限定收錄 raw 原文六大事實：密碼長度、組成規則效益有限、遭外洩密碼黑名單、加鹽雜湊儲存、登入速率限制/節流、允許空格與通行密語短語。
  - 絕不收錄 raw 未記載之「不強制定期更換密碼」與「不使用安全提問」。
  - 英文術語均以「中文（English）」雙語呈現。
  - 與個人的關聯嚴格以「【譯為個人視角】」標註呈現，絕不寫成 NIST 對個人的直接建議。
  - 發布日期標註【raw 未載，待補來源】。

---

## [2026-11-16] output | 製作教學型 HTML 簡報（第 1 輪）

- 生成 `output/deck.html`：單一自足 HTML 簡報，共 16 頁，適合大學生之教學導向。
- 生成 `output/loop-log.md`：本輪品質紀錄。
- 簡報內容全部來自 `wiki/` 知識頁面，不補外部事實，所有引號內容逐字照抄 raw 原文。
- 採系統字型（Microsoft JhengHei, PingFang TC, sans-serif），不引用外部 URL，完全自足。
- 每頁標注來源 wiki 頁面；受眾標籤（個人 / 企業 / 服務提供者）完整呈現。
- **注意**：專案根目錄不存在 `SKILL.md` 與 `check.py`，兩者均未被建立；本輪未執行 `python check.py --round 1`。

---

## [2026-11-16] ingest | 攝取 raw/06 歐盟 GDPR 維基百科條目
- 完成 `raw/06_gdpr_wikipedia.md` 之資料攝取。
- 建立來源摘要頁面：`wiki/sources/source-06-gdpr.md`，完整載明維基百科來源與 CC BY-SA 4.0 授權條款聲明。
- 建立知法知權篇專頁（個人與企業嚴格分立）：
  - `wiki/legal/gdpr-data-subject-rights.md`（歐盟 GDPR 個人資料權利規範），frontmatter 標註 `target_audience: 個人`，每項標註【對象：個人】。
  - `wiki/legal/gdpr-enterprise-obligations.md`（歐盟 GDPR 企業處理與合規義務），frontmatter 標註 `target_audience: 企業`，每項標註【對象：企業】。
- 更新時限比較專題頁面：`wiki/legal/time-limits-comparison.md`，正式完整並列三大來源（歐盟 GDPR 72小時、數發部四項 72 小時應變呼籲及一個月改善計劃、臺灣個資法第 12 條第 4 項授權但母法未載 72 小時），客觀並陳，不作裁決、不下結論。
- 更新全庫目錄索引 `wiki/index.md`。
- 恪遵規範與事實檢核：
  - **排除有誤陳述**：原文第 12 行「隨著英國在2019年脫離歐盟，它於2018年5月23日御准批准了2018年資料保護法案」一句中，「英國在2019年脫離歐盟」疑似有誤，已排除不予收錄。
  - **72 小時嚴格消歧義**：僅逐字引用「如果資料洩露對用戶隱私產生不利影響，企業必須在72小時內報告任何資料洩露。」其餘條號（如第 33 條）、向監管機關報告等未記載事項均標註【raw 未載，待補來源】。
  - 發布日期標註【raw 未載，待補來源】。

---

## [2026-11-16] output | 製作教學型 HTML 簡報（第 1 輪）

- 生成 `output/deck.html`：單一自足 HTML 簡報，共 16 頁，適合大學生之教學導向。
- 生成 `output/loop-log.md`：本輪品質紀錄。
- 簡報內容全部來自 `wiki/` 知識頁面，不補外部事實，所有引號內容逐字照抄 raw 原文。
- 採系統字型（Microsoft JhengHei, PingFang TC, sans-serif），不引用外部 URL，完全自足。
- 每頁標注來源 wiki 頁面；受眾標籤（個人 / 企業 / 服務提供者）完整呈現。
- **注意**：專案根目錄不存在 `SKILL.md` 與 `check.py`，兩者均未被建立；本輪未執行 `python check.py --round 1`。

## [2026-11-16] output | 簡報紀錄更正（第 2、3 輪）

- 更正前一筆簡報紀錄：簡報實際為 15 頁（非 16 頁），且前一筆寫「未執行 check.py」是因為當時檔案尚未放入專案。
- 第 2、3 輪已在專案根目錄使用 `check.py` 檢查，並經新對話 AI 審查（`output/review-report-1.md`）。完整紀錄見 `output/loop-log.md`。