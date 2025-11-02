---
title: "Error 418 (I’m a teapot)!?"
emoji: "🫖"
type: "tech"
topics: ["teapot"]
published: true
published_at: 2025-11-02
---

## はじめに

Google には様々な隠れイースターエッグが存在しますが、その中でも特にユニークなのが `https://www.google.com/teapot` です。
このページにアクセスすると、HTTP ステータスコード 418 "I'm a teapot" というエラーメッセージが表示されます。

https://www.google.com/teapot

## Error 418 とは？

- HTTP ステータスコード 418 は、RFC 2324 で定義された「Hyper Text Coffee Pot Control Protocol (HTCPCP)」というエイプリルフールのジョーク RFC に由来しています
- このステータスコードは、コーヒーポットにコーヒーを淹れるよう要求したが、実際にはティーポットだった場合に返されるという、完全にジョーク仕様です

## RFC 2324 - HTCPCP/1.0

- このプロトコルは 1998 年 4 月 1 日（エイプリルフール）に発行された RFC 2324 で定義されています
  - コーヒーポットの制御プロトコル
  - BREW メソッド（コーヒーを淹れる）
  - WHEN メソッド（いつコーヒーが淹れられるか）
  - 418 I'm a teapot ステータスコード

https://www.rfc-editor.org/rfc/rfc2324

## 実装例

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/teapot') {
    res.writeHead(418, { 'Content-Type': 'text/plain' });
    res.end("I'm a teapot");
  } else {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello World');
  }
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});
```

## その他

- RFC 7168: HTCPCP をティー用に拡張した RFC（2014年4月1日）
- ステータスコード 418 は Save 418 運動により、正式な HTTP ステータスコードとして保護されています

https://www.rfc-editor.org/rfc/rfc7168

https://save418.com/

## まとめ

- Error 418 は、インターネットとプログラミングコミュニティのユーモアの精神を象徴する良い例
- Google のようなテック企業がこのようなジョークを実装し続けていることは、技術の楽しさを忘れないことの大切さを教えてくれる
