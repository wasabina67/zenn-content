---
title: "Dockerコマンドについて"
emoji: "🐋"
type: "tech"
topics: ["docker"]
published: true
published_at: 2024-10-02
---

# Dockerイメージ

## イメージを取得

```bash
docker pull hello-world:latest
```

```bash
docker pull python:3.10-slim
```

## イメージ一覧を表示

```bash
docker images
```

## イメージを削除

```bash
docker rmi hello-world:latest
```

```bash
docker rmi python:3.10-slim
```

## イメージをビルド

```Dockerfile
# Dockerfile
FROM hello-world:latest
```

```bash
docker build -t wasabina67/hello-world:0.1 .
```

```bash
# タグ付けして差分ビルド
docker build -t wasabina67/hello-world:0.2 .
```

## イメージをプッシュ

```bash
docker push wasabina67/hello-world:0.1
```

# Dockerコンテナ
