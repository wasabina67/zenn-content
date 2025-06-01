---
title: "curlコマンドのメモ"
emoji: "🥸"
type: "tech"
topics: ["curl"]
published: true
published_at: 2025-06-01
---

## 準備

```bash
echo "const express=require('express');const app=express();app.use(express.json());app.get('/',(req,res)=>{res.json({\"name\":\"wasabina67\",\"age\":\"100\"})});app.post('/',(req,res)=>{console.log(req.body);res.json({\"status\":\"success\"})});app.listen(3000,()=>console.log('Server running → http://localhost:3000'));" > server.js && \
npm i express && \
node server.js
```

## GET

```bash
curl http://localhost:3000/
```

```bash
curl -i http://localhost:3000/
```

```bash
curl -H "Authorization: Bearer MY_TOKEN" http://localhost:3000/
```

## POST

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"wasabina67", "age":"100"}' http://localhost:3000/
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"wasabina67", "age":"100"}' \
http://localhost:3000/
```
