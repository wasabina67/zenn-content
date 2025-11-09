---
title: "CVE、CWE、CVSSについて"
emoji: "🔒"
type: "idea"
topics: ["cve", "cwe", "cvss"]
published: true
published_at: 2025-11-09
---

セキュリティ脆弱性を管理・評価するための3つの重要な標準規格について解説します。

## CVE (Common Vulnerabilities and Exposures)

**共通脆弱性識別子** - 個別の脆弱性に付けられる**一意の識別番号**です。

### 基本情報

- **形式**: `CVE-年-番号`
- **目的**: 世界中で同じ脆弱性について話すときに、共通の名前を使えるようにする
- **管理**: MITRE Corporation
- **公式サイト**: https://cve.mitre.org/

### 具体例

- CVE-2025-57352  → min-documentのプロトタイプ汚染
- CVE-2021-44228  → Log4Shell（Log4jの脆弱性）
- CVE-2014-0160   → Heartbleed（OpenSSLの脆弱性）

### CVE番号の見方

- CVE-2025-57352
  - CVE: CVEの識別子
  - 2025: 発見・公開された年
  - 連番（その年に登録された脆弱性の番号）

## CWE (Common Weakness Enumeration)

**共通脆弱性タイプ一覧** - ソフトウェアやハードウェアの脆弱性の**種類**を分類したものです。

### 基本情報

- **形式**: `CWE-番号`
- **目的**: 脆弱性のパターンや原因を分類・体系化する
- **管理**: MITRE Corporation
- **公式サイト**: https://cwe.mitre.org/

### よくあるCWE

- CWE-79   → XSS
- CWE-89   → SQLインジェクション
- CWE-787  → バッファオーバーフロー
- CWE-1321 → プロトタイプ汚染
- CWE-20   → 不適切な入力検証
- CWE-200  → 情報漏洩
- CWE-276  → 不適切なパーミッション設定

### CWE Top 25

MITRE が毎年発表する「最も危険なソフトウェアの弱点トップ25」があり、開発者が特に注意すべき脆弱性タイプがまとめられています。

https://cwe.mitre.org/top25/

## CVSS (Common Vulnerability Scoring System)

**共通脆弱性評価システム** - 脆弱性の深刻度を数値化して評価する仕組みです。

### 基本情報

- **スコア範囲**: 0.0 〜 10.0
- **管理**: FIRST (Forum of Incident Response and Security Teams)
- **公式サイト**: https://www.first.org/cvss/

### 深刻度レベル

| スコア | レベル | 英語表記 | 対応の緊急度 |
|--------|--------|----------|--------------|
| 0.0 | なし | None | - |
| 0.1-3.9 | 低 | Low | 通常の対応 |
| 4.0-6.9 | 中 | Medium | 早めに対応 |
| 7.0-8.9 | 高 | High | 優先的に対応 |
| 9.0-10.0 | 緊急 | Critical | 即座に対応 |

### CVSSベクトル

脆弱性の特性を表す文字列です。

**例**: `AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`

#### 基本評価基準（Base Metrics）

CVSSスコアは以下の8つの評価項目から計算されます。

| 項目 | 略称 | 説明 | 値の例 |
|------|------|------|--------|
| **攻撃元区分** | AV (Attack Vector) | 攻撃可能な場所 | N:ネットワーク / A:隣接 / L:ローカル / P:物理 |
| **攻撃条件の複雑さ** | AC (Attack Complexity) | 攻撃の難易度 | L:低 / H:高 |
| **必要な特権レベル** | PR (Privileges Required) | 攻撃に必要な権限 | N:不要 / L:低 / H:高 |
| **利用者の関与** | UI (User Interaction) | ユーザー操作の必要性 | N:不要 / R:要 |
| **影響の想定範囲** | S (Scope) | 影響範囲の変化 | U:変更なし / C:変更あり |
| **機密性への影響** | C (Confidentiality) | 情報漏洩の程度 | N:なし / L:低 / H:高 |
| **完全性への影響** | I (Integrity) | データ改ざんの程度 | N:なし / L:低 / H:高 |
| **可用性への影響** | A (Availability) | サービス停止の程度 | N:なし / L:低 / H:高 |

### 具体例の解析

**CVE-2025-57352のCVSS評価**

```
ベクトル: AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
スコア: 5.3（中程度）
```

| 項目 | 値 | 意味 |
|------|-----|------|
| AV | N | インターネット経由で攻撃可能 |
| AC | L | 攻撃は簡単に実行できる |
| PR | N | 認証不要で攻撃できる |
| UI | N | ユーザーの操作なしで攻撃できる |
| S | U | 影響範囲は脆弱なコンポーネント内に限定 |
| C | L | 一部の情報が漏洩する可能性あり |
| I | N | データの改ざんは発生しない |
| A | N | サービスの停止は発生しない |

ネットワーク経由で簡単に攻撃できるが、影響は限定的（情報漏洩のみ）なため、中程度の深刻度となっています。

### CVSSスコアの計算

手動計算は複雑なため、通常は公式の計算ツールを使用します。

- **FIRST CVSS v3.1 Calculator**: https://www.first.org/cvss/calculator/3.1
- **FIRST CVSS v4.0 Calculator**: https://www.first.org/cvss/calculator/4.0
- **NVD CVSS Calculator**: https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator

## 3つの関係性

実際の脆弱性情報では、これら3つが組み合わせて使われます。

### CVE-2025-57352 の場合

```
【識別】CVE-2025-57352
  └─ この脆弱性を一意に識別する番号

【分類】CWE-1321（プロトタイプ汚染）
  └─ この脆弱性がどんな種類の問題なのか

【評価】CVSS 5.3（中程度）
  └─ この脆弱性がどれくらい危険なのか
```

## 脆弱性データベース

### NVD (National Vulnerability Database)

米国国立標準技術研究所（NIST）が運営する脆弱性データベース

- **URL**: https://nvd.nist.gov/
- **特徴**: CVE、CWE、CVSSを統合して提供

### JVN (Japan Vulnerability Notes)

日本の脆弱性対策情報ポータル

- **URL**: https://jvn.jp/
- **特徴**: 日本語で情報提供、日本製品の脆弱性情報も充実

### GitHub Advisory Database

GitHubが提供する脆弱性データベース

- **URL**: https://github.com/advisories
- **特徴**: オープンソースパッケージの脆弱性情報に特化

## まとめ

| 略語 | 正式名称 | 役割 | 例 |
|------|----------|------|-----|
| **CVE** | Common Vulnerabilities and Exposures | 個別の脆弱性の識別 | CVE-2025-57352 |
| **CWE** | Common Weakness Enumeration | 脆弱性の種類の分類 | CWE-1321（プロトタイプ汚染） |
| **CVSS** | Common Vulnerability Scoring System | 脆弱性の深刻度の評価 | 5.3（中程度） |

これらの標準規格により、世界中のセキュリティ専門家が共通の言葉で脆弱性について議論し、適切に対応できるようになっています。

## 参考資料

- [CVE - Common Vulnerabilities and Exposures](https://cve.mitre.org/)
- [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)
- [CVSS - Common Vulnerability Scoring System](https://www.first.org/cvss/)
- [NVD - National Vulnerability Database](https://nvd.nist.gov/)
- [JVN - Japan Vulnerability Notes](https://jvn.jp/)
