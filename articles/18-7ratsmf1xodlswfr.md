---
title: "Docker上でKanboardを実行する"
emoji: "🗒️"
type: "tech"
topics: ["kanban", "docker"]
published: true
published_at: 2025-05-17
---

## 実行方法

```bash
docker run -d --name kanboard -p 3000:80 -t kanboard/kanboard:latest
```

- Open http://localhost:3000/login
- Username & Password is `admin`

## 参考資料

- https://hub.docker.com/r/kanboard/kanboard
- https://kanboard-documentation-ja.readthedocs.io/ja/latest/admin_guide/docker.html
