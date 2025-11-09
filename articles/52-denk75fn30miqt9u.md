---
title: "JavaScriptのPrototype Pollution（プロトタイプ汚染）について"
emoji: "🔗"
type: "idea"
topics: ["prototype"]
published: true
published_at: 2025-11-09
---

## プロトタイプ汚染とは

プロトタイプベースの言語であるJavaScriptは、プロトタイプオブジェクトを元にオブジェクトを生成します。
攻撃者は、プロトタイプオブジェクトを改ざんすることにより、アプリケーションのあらゆるオブジェクトを改変させることができます。
結果として、アプリケーションに予期せぬ動作や悪意ある動作を発生させます。
