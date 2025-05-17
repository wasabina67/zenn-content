---
title: "Docker上でKanboardを実行する"
emoji: ""
type: "tech"
topics: [""]
published: false
published_at: 2025-01-01
---

## `docker run`する

```bash
docker run -d --name kanboard -p 3000:80 -t kanboard/kanboard:latest
```

- Open http://localhost:3000/login
- Username & Password is `admin`

## 参考資料

- https://hub.docker.com/r/kanboard/kanboard
