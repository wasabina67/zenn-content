---
title: "POST・PUT・PATCHの使い分けについて"
emoji: "🔍"
type: "tech"
topics: ["http"]
published: true
published_at: 2026-03-21
---

## POST
- 新しいリソースを作成する
- リクエストのたびに新しいリソースが作成される（**冪等ではない**）
- リクエストボディにリソース全体のデータを含める
- 例: ユーザーの新規登録

```
POST /users
{ "name": "Taro", "email": "taro@example.com" }
```

- [POST リクエストメソッド - HTTP | MDN](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/POST)

## PUT
- リソース全体を置き換える
- 同じリクエストを何度送っても結果が同じ（**冪等**）
- リクエストボディにリソース全体のデータを含める
- 例: ユーザー情報の全項目を更新

```
PUT /users/1
{ "name": "Taro Tanaka", "email": "ttanaka@example.com" }
```

- [PUT リクエストメソッド - HTTP | MDN](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/PUT)

## PATCH
- リソースの一部を更新する
- 冪等性は実装に依存する
- 変更したいフィールドだけをリクエストボディに含める
- 例: ユーザーのメールアドレスだけを更新

```
PATCH /users/1
{ "email": "t-tanaka@example.com" }
```

- [PATCH リクエストメソッド - HTTP | MDN](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/PATCH)
