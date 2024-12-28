---
title: "Dockerコマンドについて"
emoji: "🐋"
type: "tech"
topics: ["docker"]
published: true
published_at: 2024-09-30
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

## 新しいコンテナを作成して実行

```bash
docker run hello-world:latest
```

```bash
docker run -it --name mypython python:3.10-slim /bin/bash
```

## 全てのコンテナの一覧を表示

```bash
docker ps -a
```

## 実行中のコンテナの一覧を表示

```bash
docker ps
```

## コンテナを停止

```bash
docker stop mypython
```

## コンテナを開始

```bash
docker start mypython
```

## 実行中のコンテナに対してコマンドを実行

```bash
docker exec -it mypython /bin/bash
```

## コンテナにアタッチ

```bash
docker attach mypython
```

## コンテナを再起動

```bash
docker restart mypython
```

## コンテナを削除

```bash
docker rm mypython
```

# その他

```bash
docker info
```

```bash
docker version
```
