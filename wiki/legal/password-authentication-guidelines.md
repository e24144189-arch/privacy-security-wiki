---
title: 服務提供者密碼驗證技術規範
tags: [NIST, SP800-63B, 服務提供者, 驗證方, 密碼架構, 技術規範]
sources: [raw/05_nist_sp800-63b_passwords.md]
target_audience: 服務提供者
last_updated: 2026-11-16
---

# 服務提供者密碼驗證技術規範

本頁面依據美國國家標準暨技術研究院《數位身分指引》（NIST SP 800-63B-4 Appendix A，`raw/05`），整理**提供登入驗證服務之一方（憑證服務提供者 CSP / 驗證方 Verifier）**應遵循之技術規範架構與威脅防禦原則。

> [!IMPORTANT]
> **受眾定位宣告**：  
> 本規範原文嚴格針對**驗證方（Verifier）與服務提供者（CSP）**之系統後台設計與伺服器端驗證機制，**絕非直接對終端個人使用者設定密碼之操作規則**。

---

## 1. 核心技術規範六大要點

### 1.1 密碼長度（Password Length）作為主要強度指標
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 密碼長度是衡量密碼強度的主要核心因素（「Password length is a primary factor in characterizing password strength」）。過短之密碼容易遭受「暴力破解攻擊（Brute-force attacks）」與「字典攻擊（Dictionary attacks）」。
* 驗證方應鼓勵使用者在合理範圍內設定盡可能長的密碼（「Users should be encouraged to make their passwords as long as they want within reason」）。
* 由於雜湊後的資料大小與原始長度無關，系統無理由禁止較長的密碼或密碼短語；惟極端長度（如數 MB）會耗費過量雜湊運算時間，驗證方設定合理上限是適當的。

> **【譯為個人視角】**（非 NIST 對個人之直接建議，僅為協助使用者理解系統原理）：  
> 在服務提供者支援長度且不強制限制短位元的情況下，較長的密碼能大幅提升對抗暴力破解的運算門檻。

### 1.2 組成規則（Composition Rules）效益有限與可用性衝擊
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 分析外洩密碼資料庫顯示，強制混用大小寫字母、數字與符號之「組成規則（Composition rules）」，其提升安全性的效益「不如原先預期（less significant than initially thought）」，且對可用性與記憶性造成嚴重衝擊（「impacts on usability and memorability are severe」）。
* 研究表明使用者對組成規則之回應極易預測（例如將「password」改為「Password1」或「Password1!」）。
* 過度複雜的規則容易引發使用者受挫，進而導致使用者將機密記錄於紙張或以不安全電子方式儲存。

> **【譯為個人視角】**（非 NIST 對個人之直接建議，僅為協助使用者理解系統原理）：  
> 服務提供者若一味強制加入大小寫特殊符號，容易迫使個人採用規律化代換（如把 a 改成 @、尾端加 1!），反而降低好記性且未能顯著增加安全性。

### 1.3 遭外洩密碼黑名單（Compromised Password Blocklist）比對
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 驗證方應在使用者設定密碼時，將其選擇與不可接受的「黑名單（Blocklist）」進行比對（「passwords chosen by users should be compared against a blocklist of unacceptable passwords」）。
* 黑名單收錄範圍應包括：以往外洩資料集（Breach corpuses）中的密碼、作為密碼使用的字典詞彙、以及特定字詞（例如該服務本身的名稱）。
* 黑名單主要目的在於線上攻擊猜中常見密碼前提供防護，不需過度龐大或包山包海，以免增加使用者困擾。

> **【譯為個人視角】**（非 NIST 對個人之直接建議，僅為協助使用者理解系統原理）：  
> 當使用者設定密碼若被系統拒絕，往往是因為該組密碼已被收錄在已公開之外洩清單或常見字典名冊中。

### 1.4 加鹽雜湊儲存（Salted and Hashed Storage）防範離線攻擊
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 攻擊者自資料庫外洩中取得密碼時，會發動「離線攻擊（Offline attacks）」。由於現代攻擊者在不受限速的離線環境中每秒可計算數十億次雜湊，密碼必須具備更高抗性。
* 驗證方儲存密碼時，必須以隨機值進行「加鹽（Salted）」並進行「雜湊（Hashed）」，且偏好採用運算成本高昂之演算法（「passwords are salted with a random value and hashed, preferably using a computationally expensive algorithm」）。
* 集中式驗證資源必須為所有訂戶儲存加鹽且「迭代雜湊（Iteratively hashed）」的驗證機密。

### 1.5 登入嘗試速率限制／節流（Rate Limiting / Throttling）防範線上攻擊
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 攻擊者透過猜測密碼嘗試登入之「線上攻擊（Online attacks）」，應透過「限制允許的登入嘗試速率（Limiting the permitted login attempt rate）」來緩解。
* 「節流／限速（Throttling）」是防禦線上密碼猜測攻擊的主要核心手段（「Throttling is the primary defense against online attacks」）。
* 系統設定之密碼門檻應確保在合理嘗試次數內猜中機率極低，並在產生重大危害前及時套用速率限制。

### 1.6 允許空格字符與通行密語／密碼短語（Multiple Words / Passphrases / Spaces）
【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* 使用由多個單詞構成的「通行密語／密碼短語（Passphrases）」是建立長密碼的有效途徑（「The use of passphrases (i.e., passwords with multiple words) is often an effective way to create a longer password」）。
* 服務提供者系統必須允許使用者輸入「空格字符（Space characters）」，以容納詞組短語之使用（「Users should also be able to include space characters to allow the use of phrases」）。
* 未經雜湊之密碼不會原樣送至後端資料庫，故無須因擔憂 SQL 注入（SQL injection）等字符攻擊而禁止特定字元或空格。

> **【譯為個人視角】**（非 NIST 對個人之直接建議，僅為協助使用者理解系統原理）：  
> 在支援空格的合規系統中，個人可利用多個生活詞彙組合為長短語（通行密語 Passphrase），兼顧長度與個人記憶性。

---

## 2. 集中式驗證與本地驗證之架構差異

【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】

* **集中式驗證（Central Verification）**：  
  密碼作為獨立驗證因素由 CSP 驗證方於線上資源進行比對。驗證方是攻擊者之主要目標，必須落實加鹽迭代雜湊與集中速率限制。
* **本地驗證（Local Verification）**：  
  密碼作為多因素驗證器（Multi-factor authenticator）之啟動因子（Activation factor），由驗證器本地驗證或衍生驗證器輸出。其防護重點在於實體安全性、防範側信道攻擊（Side-channel attacks）及確保端點無側錄惡意軟體，長度與複雜度要求相對放寬。

---

## 3. 事實界限與不收錄宣告

依據 `AGENTS.md` 規範與事實接地原則：
* **不收錄外部衍生項目**：`raw/05` 原文完全未包含「不強制定期更換密碼」與「避免使用脆弱安全問題」，本庫嚴格不作外部擴充。
* **攻擊手法範疇**：鍵盤側錄（Keystroke logging）、釣魚（Phishing）與社交工程（Social engineering）等不受長度複雜度影響之攻擊，文獻載明超出本附錄範疇。

---

## 4. 關聯頁面導航

* [NIST SP 800-63B 數位身分指引密碼安全技術摘要](../sources/source-05-nist.md)
