---
title: "Content Security Policy (CSP)について"
emoji: "🔒"
type: "tech"
topics: ["csp"]
published: true
published_at: 2026-03-10
---

CSPは、Webサイトが「どこからリソースを読み込んでいいか」をブラウザに指示するセキュリティの仕組みです。

https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/CSP

## 何を防ぐのか

主にXSS攻撃を防ぎます。攻撃者がページに悪意あるスクリプトを注入しても、CSPのルールに合致しなければブラウザがそれをブロックしてくれます。

## どうやって設定するか

以下の例では「スクリプトは自分のサイトと`cdn.example.com`からだけ許可する」という意味になります。

### HTTPレスポンスヘッダー

サーバーのレスポンスに `Content-Security-Policy` ヘッダーを付与します。

```http
Content-Security-Policy: script-src 'self' cdn.example.com
```

### HTMLのmetaタグ

サーバー設定を変更できない場合は、HTMLの `<head>` 内に `<meta>` タグで記述できます。

```html
<meta http-equiv="Content-Security-Policy" content="script-src 'self' cdn.example.com">
```

ただし、`frame-ancestors` や `report-uri` など一部のディレクティブはmetaタグでは使用できないため、可能であればHTTPヘッダーでの設定が推奨されます。

## 主なディレクティブ

- `default-src` — 他のディレクティブが未指定の場合のフォールバック
- `script-src` — JavaScriptファイルやインラインスクリプト
- `style-src` — CSSファイルやインラインスタイル
- `img-src` — 画像
- `font-src` — Webフォント
- `connect-src` — fetch・XHR・WebSocketなどの通信先
- `frame-src` — `<iframe>` で読み込むURL
- `frame-ancestors` — `<iframe>` に埋め込まれる親ページのURL（クリックジャッキング対策）
- `form-action` — フォームの送信先URL
- `object-src` — `<object>` や `<embed>` などのプラグイン
- `base-uri` — `<base>` タグで指定できるURL

## よく使う値

- `'self'` — 同じオリジン（スキーム・ホスト・ポートが一致）のみ許可
- `'none'` — 一切許可しない
- `'unsafe-inline'` — インラインスクリプト・スタイルを許可（非推奨）
- `'unsafe-eval'` — `eval()` などの動的コード実行を許可（非推奨）
- `'nonce-<base64-value>'` — nonce属性が一致するインラインスクリプト・スタイルのみ許可（`'unsafe-inline'` の安全な代替）
- `'sha256-<hash>'` — ハッシュ値が一致するスクリプト・スタイルのみ許可（`'unsafe-inline'` の安全な代替）
- `https:` — HTTPSのURLをすべて許可
- `data:` — `data:` URIスキームを許可（Base64画像など）
- `cdn.example.com` — 特定のホストを許可（ワイルドカード `*.example.com` も使用可）

## 実際の流れ

例えば、 `script-src 'self'` と設定した状態で、ページ内に攻撃者が `<script src="https://evil.com/bad.js">` を注入しても、ブラウザが「許可リストにないドメイン」と判断してブロックします。
開発者ツールのコンソールにもエラーが表示されます。

## 導入のコツ

いきなり `Content-Security-Policy` ヘッダーを有効にすると、既存のスクリプトやスタイルがブロックされてページが壊れることがあります。
そこで、まずは `Content-Security-Policy-Report-Only` ヘッダーを使って影響を確認するのがおすすめです。

```http
Content-Security-Policy-Report-Only: script-src 'self' cdn.example.com
```

このヘッダーを使うと、ポリシー違反があってもリソースはブロックされず、開発者ツールのコンソールに警告が表示されるのみとなります。
実際にブロックする前に「どのリソースが引っかかるか」を安全に確認できます。
コンソールに意図しない違反が出なくなったら、`Content-Security-Policy` ヘッダーに切り替えて実際にブロックするようにします。
