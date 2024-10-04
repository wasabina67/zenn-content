---
title: "Gitブランチの削除について"
emoji: "🌿"
type: "tech"
topics: ["git", "branch"]
published: false
published_at: 2024-10-04
---

## ローカルブランチの削除

> ブランチがマージされている場合にのみ削除を許可

```bash
git branch -d <branch-name>
```

## ローカルブランチの削除

> 強制的に削除を許可

```bash
git branch -D <branch-name>
```

## リモートブランチの削除

```bash
git push origin --delete <branch-name>
```

## リモートで削除されたブランチをローカルの追跡ブランチから削除

```bash
git fetch --prune
```
