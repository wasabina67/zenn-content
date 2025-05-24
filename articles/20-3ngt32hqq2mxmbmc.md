---
title: "Gitサブモジュールについて"
emoji: "😺"
type: "tech"
topics: ["git"]
published: true
published_at: 2025-05-24
---

### サブモジュールの追加

```bash
git submodule add <submodule-repository-url> <directory>
```

### サブモジュールの更新

```bash
git submodule update --remote
```

### サブモジュールを初期化して更新

```bash
git submodule update --init --recursive
```
