---
title: ".batファイルで、timeoutしてから、.lnkファイルを実行する"
emoji: "🦇"
type: "tech"
topics: ["bat", "lnk"]
published: false
published_at: 2025-04-28
---

```bat
@echo off
timeout /t 60 /nobreak
start "" "C:\Shortcuts\run.exe - ショートカット.lnk"
```
