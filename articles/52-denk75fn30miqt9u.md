---
title: "JavaScriptのPrototype Pollution（プロトタイプ汚染）について"
emoji: "🔗"
type: "idea"
topics: ["prototype", "javascript"]
published: true
published_at: 2025-11-09
---

## プロトタイプ汚染とは

プロトタイプベースの言語であるJavaScriptは、プロトタイプオブジェクトを元にオブジェクトを生成します。
攻撃者は、プロトタイプオブジェクトを改ざんすることにより、アプリケーションのあらゆるオブジェクトを改変させることができます。
結果として、アプリケーションに予期せぬ動作や悪意ある動作を発生させます。

## 参考資料

- [Raynos/min-document: A minimal DOM implementation](https://github.com/Raynos/min-document)
- [Prototype Pollution in min-document · Issue #54 · Raynos/min-document](https://github.com/Raynos/min-document/issues/54)
- [Fix prototype pollution in removeAttributeNS by jameswassink · Pull Request #55 · Raynos/min-document](https://github.com/Raynos/min-document/pull/55)
- [NVD - CVE-2025-57352](https://nvd.nist.gov/vuln/detail/CVE-2025-57352)
- [PoCs/JavaScript/prototype-pollution/CVE-2025-57352/index.js at main · OrangeShieldInfos/PoCs](https://github.com/OrangeShieldInfos/PoCs/blob/main/JavaScript/prototype-pollution/CVE-2025-57352/index.js)
- [[GHSA-rx8g-88g5-qh64] min-document vulnerable to prototype pollution by G-Rath · Pull Request #6392 · github/advisory-database](https://github.com/github/advisory-database/pull/6392)
- [min-document vulnerable to prototype pollution | GitLab Advisory Database](https://advisories.gitlab.com/pkg/npm/min-document/CVE-2025-57352/)
