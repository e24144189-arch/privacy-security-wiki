# 知識庫第一次完整健檢報告 (Lint Report 1)

* **報告編號**：LINT-20261116-01
* **執行日期**：2026-11-16
* **檢核依據**：`AGENTS.md` 第 5.3 節「健康檢查工作流（Linting SOP）」七大嚴格檢核項目
* **檢核模式**：純報告模式（不自動修改任何內容檔案）
* **資料集涵蓋**：`raw/01` 至 `raw/06` 全面 Ingest 完成後之 `wiki/` 知識庫全體頁面（共 20 份 Markdown 檔案）

---

## 執行摘要 (Executive Summary)

本次健檢針對全庫 20 份檔案進行了嚴格的事實接地、連結拓撲、受眾標記、時限消歧義及合規標籤審查。全庫整體架構完整，無孤立頁面，事實接地邊界嚴密，未檢測出任何惡意攻擊模板或未標註之外部事實幻覺。

| 檢核項目 | 判定結果 | 關鍵發現摘要 |
| :--- | :---: | :--- |
| **1. 孤立頁面檢查** | **PASS** | 全庫 18 篇內容頁面均具備 3 至 11 個雙向相對路徑反向連結，全數登錄於 `wiki/index.md`。 |
| **2. 缺乏 raw 出處標註** | **PASS** | 所有內容頁面 Frontmatter 均標註 `sources: [...]`，內文所有主要陳述均標註條號或來源段落。 |
| **3. 72 小時規範歸屬** | **PASS** | 建立 `time-limits-comparison.md` 專頁嚴格消歧義：精確區隔 GDPR、數發部四項行動與個資法第 12 條授權。 |
| **4. 個資法條號與狀態標籤** | **PASS** | 嚴格限定使用三種合法狀態標籤；涉及現行施行狀態均標註【待使用者確認】。 |
| **5. 溝通對象標記** | **PASS** | `wiki/defense/` 嚴格限定為個人自保；企業義務與 NIST 服務提供者技術規範嚴格隔離，無誤植為個人建議。 |
| **6. 00_sources_list 待辦追蹤** | **PASS** | CC BY-SA 授權已完整宣告；缺漏之原始網址與發布日期均已於 wiki 標註待補來源。 |
| **7. 事實真實性查核** | **PASS** | 嚴格排除「英國在2019年脫離歐盟」；未出現「特種個資」、舊第 27 條去向、定期換密碼等外部事實；初查數據均標註日期與初查性質。 |

---

## 七大檢核項目逐項檢驗結果

### 1. 孤立頁面檢查 (Orphan Pages)
* **檢核標準**：檢查是否存在沒有任何相對路徑連結反向指向它的孤兒頁面。
* **檢核數據**：
  * `wiki/index.md`：作為全庫根索引，完整包含 18 篇內容頁面之相對路徑連結。
  * 各檔案反向入站連結統計：
    * `wiki/defense/`（3 篇）：`common-scams-recognition.md` (3)、`phishing-email-defense.md` (5)、`post-breach-defense.md` (8)。
    * `wiki/legal/`（8 篇）：`article-27-status.md` (6)、`data-breach-notification.md` (11)、`gdpr-data-subject-rights.md` (4)、`gdpr-enterprise-obligations.md` (5)、`password-authentication-guidelines.md` (3)、`personal-data-definition.md` (4)、`rights-of-data-subjects.md` (5)、`time-limits-comparison.md` (7)。
    * `wiki/entities/`（1 篇）：`pdpc.md` (5)。
    * `wiki/sources/`（6 篇）：`source-01-pdpa.md` (7)、`source-02-165-scams.md` (3)、`source-03-moda-ai-attack.md` (6)、`source-04-twcert.md` (3)、`source-05-nist.md` (3)、`source-06-gdpr.md` (5)。
* **判定結果**：**PASS**（無任何孤立頁面）。

---

### 2. 缺乏 raw 出處標註 (Missing raw Attribution)
* **檢核標準**：檢查是否有陳述未標明 raw 檔名、條號或章節段落。
* **檢核結果**：
  * 全數內容頁面均具備標準 YAML Frontmatter 之 `sources` 清單，明確回溯至對應之 `raw/01` 至 `raw/06` 檔案。
  * 法律條文陳述逐一標記【條號：第 X 條】。
  * 政策與防護指引陳述逐一標記【來源：raw/0X 機構名稱】。
* **判定結果**：**PASS**。

---

### 3. 72 小時規範歸屬 (72-hour Attribution & Disambiguation)
* **檢核標準**：檢查所有「72 小時」敘述是否精確區隔法規主體（GDPR vs 數發部四項行動 vs 個資法授權）。
* **檢核結果**：
  * **專題設立**：設立 `wiki/legal/time-limits-comparison.md`，提供完整三方時限比對總表。
  * **歐盟 GDPR**：嚴格逐字照抄 `raw/06`「如果資料洩露對用戶隱私產生不利影響，企業必須在72小時內報告任何資料洩露。」其未記載之條號（第 33 條）與監管機關均標註【raw 未載，待補來源】。
  * **數發部資安署**：四項應變行動明確標記為行政呼籲之「72 小時之內」，並嚴格將第五項（一個月內改善計劃）獨立分開，無混用情事。
  * **臺灣個資法**：第 12 條第 4 項明確標記為授權主管機關訂定時限辦法，母法條文未載明 72 小時。
* **判定結果**：**PASS**。

---

### 4. 個資法條號與狀態標籤 (PDPA Article Numbers & Status Tags)
* **檢核標準**：檢查個資法條號是否存在，且是否嚴格限定使用三種合法狀態標籤之一：
  1. `修正版條文（尚未生效）`
  2. `本版標示刪除`
  3. `本版未列為修正`
* **檢核結果**：
  * `wiki/sources/source-01-pdpa.md`：`status: 修正版條文（尚未生效）`
  * `wiki/legal/personal-data-definition.md`：`status: 本版未列為修正`
  * `wiki/legal/rights-of-data-subjects.md`：`status: 本版未列為修正`（頁內各條號均獨立標記各條狀態）
  * `wiki/legal/data-breach-notification.md`：`status: 修正版條文（尚未生效）`
  * `wiki/legal/article-27-status.md`：`status: 本版標示刪除`
  * `wiki/entities/pdpc.md`：`status: 修正版條文（尚未生效）`
  * `wiki/legal/time-limits-comparison.md`：`status: 修正版條文（尚未生效）`
  * 內文提及現行實務、現行施行法規或行政院施行日期者，全數標註【待使用者確認】。
* **判定結果**：**PASS**。

---

### 5. 溝通對象標記 (Audience Attribution)
* **檢核標準**：檢查每則陳述是否標記溝通對象（個人／企業／服務提供者），有無將企業/服務提供者規範誤植為個人建議。
* **檢核結果**：
  * **`wiki/defense/`**：收錄之 3 篇頁面全數標註 `target_audience: 個人`，每節均標記【對象：個人】；防禦範圍嚴格收錄 raw/02 之五大詐騙、raw/03 自保四原則與 raw/04 釣魚辨識，無企業義務。
  * **`wiki/legal/`**：個人權利（`personal-data-definition.md`、`rights-of-data-subjects.md`、`gdpr-data-subject-rights.md`）與企業義務（`data-breach-notification.md`、`article-27-status.md`、`gdpr-enterprise-obligations.md`、`time-limits-comparison.md`）徹底拆頁分立，Frontmatter 與內文完全吻合。
  * **NIST SP 800-63B**：`password-authentication-guidelines.md` 嚴格標記 `target_audience: 服務提供者`，每項標記【對象：服務提供者】；與個人之關聯嚴格標記為 `【譯為個人視角】`，並加註非 NIST 對個人之直接建議。
* **判定結果**：**PASS**。

---

### 6. 00_sources_list.md 待辦追蹤 (Sources List Todo Tracking)
* **檢核標準**：檢查來源清單所列待辦事項（補網址、補發布日期、CC BY-SA 宣告）之落實情形。
* **檢核狀態追蹤**：
  1. `raw/01`：待辦標記為 `-`（已完整收錄修正版條文）。
  2. `raw/02`：待辦標記為 `—`（原頁未標發布日期，已於 wiki 標註【raw 未載，待補來源】）。
  3. `raw/03`：待辦標記為 `-`（原文僅標「今（11）日」，wiki 依情境註記 2026-11-11 並標註【待使用者確認】）。
  4. `raw/04`：待辦標記為 `-`（raw 檔頭網址為空，wiki 標註【raw 未載，待補來源】並備註來源清單網址）。
  5. `raw/05`：待辦標記為 `-`（原頁未標發布日期，已於 wiki 標註【raw 未載，待補來源】）。
  6. `raw/06`：待辦標記為 `注意 CC BY-SA 標示出處`（已於 `wiki/sources/source-06-gdpr.md` 明確宣告維基百科 CC BY-SA 4.0 授權條款）。
* **判定結果**：**PASS**。

---

### 7. 事實真實性查核（防範外部事實，Factual Grounding）
* **檢核標準**：抽查數字、條號與關鍵詞，防範未記載於 raw 之外部事實與攻擊腳本。
* **抽查比對要點**：
  * **術語紅線**：未出現「特種個人資料／特種個資」，全數逐字寫為「有關病歷、醫療、基因、性生活、健康檢查及犯罪前科之個人資料」。
  * **第 27 條紅線**：未出現「訂定安全維護計畫」、「改列第三章之一」、「移交個資會」等修法去向字眼，客觀並列 01 與 03 之記載且未做裁決。
  * **初查數據**：資安署之「十餘家」、「逾百萬份」、「近半數」均標註為 2026-11-11 初查說法，未寫為最終統計。
  * **NIST 紅線**：未出現「不強制定期更換密碼」與「不使用安全提問」，嚴格限定於原文六大事實。
  * **GDPR 錯誤排除**：已排除「英國在2019年脫離歐盟」語句，並在日誌記錄排除原因。
  * **防詐內容紅線**：五大詐騙僅收錄「辨識特徵」，不收錄攻擊腳本或話術步驟；預防對策未見於 03/04 者全數標註【raw 未載，待補來源】。
  * **虛構資料規範**：範例全數嚴格使用王小明、`0900-000-000`、`user@example.com`、`https://example.com`。
* **判定結果**：**PASS**。

---

## 總結與後續建議

本次 Lint 健檢結果全數通過（**7 項檢驗全部合格**）。  
知識庫目前架構穩固、受眾分明、事實嚴格接地。

* **建議後續維護行動**：
  1. 請使用者針對內文標註 **【待使用者確認】** 之法律施行日期、現行實務效力與新聞稿發布年份進行確認。
  2. 請使用者針對標註 **【raw 未載，待補來源】** 之防詐對策（如租屋定金、投資登記）評估是否引入後續補充文獻（如 raw/07...）。
