---
title: "Gitブランチの削除について"
emoji: "🌿"
type: "tech"
topics: ["git", "branch"]
published: true
published_at: 2024-10-04
---

## ローカルブランチの削除

- ブランチがマージされている場合にのみ削除

```bash
git branch -d your-branch-name
```

- 強制的に削除

```bash
git branch -D your-branch-name
```

- hoge

```bash
git fetch --prune
```

## リモートブランチの削除

```bash
git push origin --delete your-branch-name
```
