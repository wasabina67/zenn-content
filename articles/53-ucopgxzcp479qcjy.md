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
