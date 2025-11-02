---
title: "レキシカルスコープ、ダイナミックスコープについて"
emoji: "🔍"
type: "idea"
topics: ["scope"]
published: true
published_at: 2025-11-02
---

## レキシカルスコープ（Lexical Scope / Static Scope）
- レキシカルスコープは、**変数のスコープがコードの記述位置（字句的な位置）によって決まる**仕組み
- 関数が**定義された場所**によって、変数の参照先が決定される

```javascript
const x = 10;

function outer() {
  const x = 20;

  function inner() {
    console.log(x); // 20 が出力される
  }

  return inner;
}

const innerFunc = outer();
innerFunc(); // 20
```

- `inner` 関数が `outer` 関数の中で**定義**されているため、`inner` 関数内の `x` は `outer` 関数のスコープにある `x = 20` を参照する

```javascript
const value = "グローバル";

function showValue() {
  console.log(value);
}

function execute() {
  const value = "ローカル";
  showValue(); // "グローバル" が出力される
}

execute();
```

- `showValue` 関数はグローバルスコープで定義されているため、`execute` 関数内で呼び出されても、グローバルスコープの `value` を参照する

## ダイナミックスコープ（Dynamic Scope）
- ダイナミックスコープは、**変数のスコープが関数の呼び出し時点での実行コンテキストによって決まる**仕組み
- 関数が**呼び出された場所**によって、変数の参照先が決定される

```bash
#!/bin/bash

x=10

function inner() {
  echo $x
}

function outer() {
  local x=20
  inner  # 20 が出力される
}

outer
```

- `inner` 関数が `outer` 関数から**呼び出される**ため、`outer` 関数のスコープにある `x = 20` を参照する
- 同じコードをレキシカルスコープで実行した場合、`inner` 関数はグローバルスコープの `x = 10` を参照する

## 比較

### レキシカルスコープ

- **スコープの決定**
  - 関数の**定義位置**で決まる
- **判断のタイミング**
  - コンパイル時（静的）
- **予測可能性**
  - 高
- **パフォーマンス**
  - 最適化しやすい
- **採用言語**
  - JavaScript、Python、Java、C++ など

### ダイナミックスコープ

- **スコープの決定**
  - 関数の**呼び出し位置**で決まる
- **判断のタイミング**
  - 実行時（動的）
- **予測可能性**
  - 低
- **パフォーマンス**
  - オーバーヘッドが大きい
- **採用言語**
  - Bash、Emacs Lisp、一部のシェル など

## なぜレキシカルスコープが主流なのか？

現代のほとんどのプログラミング言語がレキシカルスコープを採用している理由は以下の通りです：

### 1. 予測可能性
コードを読むだけで、どの変数が参照されるか判断できます。

### 2. デバッグのしやすさ
変数の参照先が静的に決まるため、バグの原因を特定しやすくなります。

### 3. 最適化
コンパイラやインタプリタが静的解析を行いやすく、パフォーマンスの最適化が可能です。

### 4. クロージャの実現
レキシカルスコープがあることで、関数が定義時の環境を保持する「クロージャ」が自然に実現できます。

```javascript
function makeCounter() {
  let count = 0;

  return function() {
    count++;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

## まとめ

- **レキシカルスコープ**： 関数の定義位置でスコープが決まる（静的）
  - 現代の多くの言語はレキシカルスコープを採用
  - レキシカルスコープは予測可能性が高く、デバッグや最適化がしやすい
- **ダイナミックスコープ**： 関数の呼び出し位置でスコープが決まる（動的）
- スコープの仕組みを理解することで、より堅牢で保守性の高いコードを書けるようになる
- JavaScriptのクロージャやモジュールパターンを理解する上で、レキシカルスコープの知識は不可欠

## 参考資料

- [クロージャ - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Closures)
- [変数スコープ、クロージャ](https://ja.javascript.info/closure)
