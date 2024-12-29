---
title: "Dockerコマンドについて"
emoji: "🐋"
type: "tech"
topics: ["docker"]
published: true
published_at: 2024-09-30
---

## Dockerイメージ

### イメージを取得

```bash
docker pull hello-world:latest
```

```bash
docker pull python:3.10-slim
```

### イメージ一覧を表示

```bash
docker images
```

### イメージを削除

```bash
docker rmi hello-world:latest
```

```bash
docker rmi python:3.10-slim
```

### イメージをビルド

- Dockerfile

```Dockerfile
FROM hello-world:latest
```

- ビルド

```bash
docker build -t wasabina67/hello-world:0.1 .
```

- Dockerfile

```Dockerfile
FROM hello-world:latest
CMD ["echo", "Hello, World!"]
```

- タグ付けして差分ビルド

```bash
docker build -t wasabina67/hello-world:0.2 .
```

### イメージをプッシュ

```bash
docker push wasabina67/hello-world:0.1
```

## Dockerコンテナ

### 新しいコンテナを作成して実行

```bash
docker run hello-world:latest
```

```bash
docker run -it --name mypython python:3.10-slim /bin/bash
```

## その他

```bash
docker info
```

```bash
docker version
```
