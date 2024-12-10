---
title: "Dockerコンテナで無限待機する"
emoji: "😴"
type: "tech"
topics: ["sleep", "docker", "shell"]
published: true
published_at: 2024-12-10
---

- Dockerコンテナをデバッグしたり、特定のプロセスがない状態でもコンテナを起動したままにしておきたい場合、`sleep`コマンドを用いて無限に待機させることができる
- これにより、コンテナの中に入ってツールを実行したり、環境を整えたりといった調査・開発作業が容易になる
- 以下のようなスクリプトを`Dockerfile`で`ENTRYPOINT`や`CMD`に指定することで、コンテナは終了せずにずっと起動状態を保つことができる

```bash
#!/bin/bash

exec sleep infinity
```
