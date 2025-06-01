---
title: "curlコマンドのメモ"
emoji: "🥸"
type: "tech"
topics: ["curl"]
published: true
published_at: 2025-06-01
---

## APIを準備

```bash
echo "const express=require('express');const app=express();app.use(express.json());app.get('/',(req,res)=>{res.json({\"Name\":\"wasabina67\",\"Age\":\"100\"})});app.post('/',(req,res)=>{console.log(req.body);res.json({\"status\":\"success\"})});app.listen(3000,()=>console.log('Server running → http://localhost:3000'));" > server.js && \
npm i express && \
node server.js
```

## GET

```bash
curl http://localhost:3000/
```

```bash
curl -H "Authorization: Bearer MY_TOKEN" http://localhost:3000/
```

## POST

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Name":"wasabina67", "Age":"100"}' http://localhost:3000/
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"Name":"wasabina67", "Age":"100"}' \
http://localhost:3000/
```
