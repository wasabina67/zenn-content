---
title: "curlコマンドのメモ"
emoji: "🥸"
type: "tech"
topics: ["curl"]
published: true
published_at: 2025-06-01
---

## 準備

以下のコマンドで簡単なAPIサーバーを起動します：

```bash
# 簡易サーバーのコードを作成
echo "const express=require('express');
const app=express();
app.use(express.json());
app.get('/',(req,res)=>{
  res.json({\"name\":\"wasabina67\",\"age\":\"100\"})
});
app.post('/',(req,res)=>{
  console.log(req.body);
  res.json({\"status\":\"success\"})
});
app.listen(3000,()=>console.log('Server running → http://localhost:3000'));" > server.js && \
npm i express && \
node server.js
```

## GET

基本的なGETリクエスト：
```bash
curl http://localhost:3000/
```

レスポンスヘッダーを含めて表示（`-i`オプション）：
```bash
curl -i http://localhost:3000/
```

認証トークンを含むリクエスト（`-H`でヘッダーを指定）：
```bash
curl -H "Authorization: Bearer MY_TOKEN" http://localhost:3000/
```

## POST

JSONデータを送信するPOSTリクエスト：
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"wasabina67", "age":"100"}' http://localhost:3000/
```

読みやすく整形したバージョン：
```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"wasabina67", "age":"100"}' \
http://localhost:3000/
```

## よく使うオプション

| オプション | 説明 |
|----------|------|
| -X | HTTPメソッドを指定（GET、POST、PUT、DELETE等） |
| -H | HTTPヘッダーを指定 |
| -d | POSTするデータを指定 |
| -i | レスポンスヘッダーを表示 |
| -v | 詳細な情報（verbose）を表示 |
| -o | 結果をファイルに保存 |

## レスポンス例

GET時のレスポンス:
```json
{"name":"wasabina67","age":"100"}
```

POST時のレスポンス:
```json
{"status":"success"}
```
