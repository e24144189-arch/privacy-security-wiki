---
title: NIST SP 800-63B 數位身分指引密碼安全技術摘要
tags: [NIST, SP800-63B, 密碼安全, 服務提供者, 驗證方, 文獻摘要]
sources: [raw/05_nist_sp800-63b_passwords.md]
target_audience: 服務提供者
last_updated: 2026-11-16
---

# NIST SP 800-63B 數位身分指引密碼安全技術摘要

本頁面為原始技術文獻 `raw/05_nist_sp800-63b_passwords.md`（NIST Special Publication 800-63B-4 Appendix A）之標準化精華摘要與元資料紀錄。

---

## 1. 來源文獻元資料 (Metadata)

* **文獻標準**：NIST Special Publication 800-63B (SP 800-63B-4 Appendix A)
* **發布機構**：美國國家標準暨技術研究院（National Institute of Standards and Technology, NIST）
* **來源網址**：https://pages.nist.gov/800-63-4/sp800-63b.html#appA
* **發布日期**：【raw 未載，待補來源】（原文標示為「（不適用／原頁未標示）」）
* **擷取日期**：2026-11-15
* **規範受眾**：提供身分驗證服務之一方（憑證服務提供者 Credential Service Provider, CSP / 驗證方 Verifier）

---

## 2. 核心技術規範六大要點

【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】

本文件原文係針對線上系統之驗證方（Verifier）所制定之架構與實施技術規範，文獻具體收錄之核心事實如下：

### 2.1 密碼長度（Password Length）的重要性
* 密碼長度是界定密碼強度的主要因素（「Password length is a primary factor in characterizing password strength」）。
* 密碼過短容易屈服於「暴力破解攻擊（Brute-force attacks）」與「字典攻擊（Dictionary attacks）」。
* 服務提供者應鼓勵使用者在合理範圍內設定盡可能長的密碼（「Users should be encouraged to make their passwords as long as they want within reason」）。
* 由於雜湊後的密碼長度與原始密碼長度無關，無理由禁止長密碼或「通行密語／密碼短語（Passphrases）」；但考量極端長度（如數 MB）可能需要過多運算時間進行雜湊，因此設定合理上限是適當的。

### 2.2 組成規則效益有限（Composition Rules Benefit is Less Significant）
* 傳統要求混用多種字元類型（如數字、大寫字母、符號）的「組成規則（Composition rules）」，其提升安全性的效益不如預期（「analyses of breached password databases reveal that the benefit of such rules is less significant than initially thought, and the impacts on usability and memorability are severe」）。
* 使用者對組成規則的反應非常可預測（例如將「password」改為「Password1」或「Password1!」）。
* 過度複雜的規則會嚴重損害可用性與記憶性，導致使用者感到挫折，並誘發將機密寫下或以不安全電子方式記錄等潛在弱點。

### 2.3 遭外洩密碼黑名單（Compromised Password Blocklist）
* 驗證方應將使用者選擇的密碼與不可接受的密碼「黑名單（Blocklist）」進行比對（「passwords chosen by users should be compared against a blocklist of unacceptable passwords」）。
* 黑名單內容應包含：過往外洩資料庫中的密碼、字典詞彙、以及使用者容易選擇的特定字詞（例如該服務本身的名稱）。
* 黑名單不需過度龐大或包山包海，其主要目的為在限速生效前防止線上攻擊猜中常見密碼。

### 2.4 加鹽雜湊儲存（Salted and Hashed Storage）
* 為防範攻擊者透過資料庫外洩取得密碼進行「離線攻擊（Offline attacks）」，密碼必須使用隨機值進行「加鹽（Salted）」並進行「雜湊（Hashed）」，且偏好使用運算成本高昂的演算法（「passwords are salted with a random value and hashed, preferably using a computationally expensive algorithm」）。
* 「集中式驗證（Central verification）」要求驗證方儲存加鹽且「迭代雜湊（Iteratively hashed）」的驗證機密。

### 2.5 限制登入嘗試速率／次數（Rate Limiting / Throttling）
* 防範「線上猜測攻擊（Online attacks）」的核心手段在於限制允許的登入嘗試速率（「limiting the permitted login attempt rate」）。
* 「節流／限速（Throttling）」是防範線上攻擊的主要防禦機制（「Throttling is the primary defense against online attacks」）。
* 密碼需具備足夠強度，使得在合理嘗試次數內猜中的機率極低，並在產生重大風險前觸發速率限制。

### 2.6 允許空格與通行密語／密碼短語（Multiple Words / Passphrases / Spaces）
* 使用包含多個單詞的「通行密語／密碼短語（Passphrases）」是建立長密碼的有效方式（「The use of passphrases (i.e., passwords with multiple words) is often an effective way to create a longer password」）。
* 驗證方系統應允許使用者包含「空格字符（Space characters）」，以利使用詞組短語（「Users should also be able to include space characters to allow the use of phrases」）。
* 重複的空格字元對強度助益不大且可能引發易用性問題，若初次驗證失敗，移除輸入中重複的空格可能有益。

---

## 3. 集中式驗證與本地驗證之威脅模型差異

【對象：服務提供者】【來源：raw/05 NIST SP 800-63B】
* **集中式驗證（Central Verification）**：由線上資源作為驗證方，須防範大規模離線雜湊破解與線上暴破，必須落實加鹽迭代雜湊與速率限制。
* **本地驗證（Local Verification）**：密碼作為多因素驗證器之啟動因子，威脅主要取決於驗證器之實體安全與端點完整性（防範惡意側錄軟體與側信道攻擊），長度與複雜度要求相對放寬。

---

## 4. 範疇排除說明

* 鍵盤側錄（Keystroke logging）、釣魚（Phishing）與社交工程（Social engineering）攻擊，對於長且複雜之密碼與簡單密碼同樣有效，文獻載明此類攻擊超出本附錄討論範疇。
* raw/05 原文未提及「不強制定期更換密碼」與「不使用安全提問」，本庫恪遵事實接地原則，嚴格不收錄此二項目。

---

## 5. 關聯頁面導航

* [服務提供者密碼驗證技術規範](../legal/password-authentication-guidelines.md)
