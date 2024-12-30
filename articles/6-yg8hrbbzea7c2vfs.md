---
title: "Gitブランチの削除について"
emoji: "🌿"
type: "tech"
topics: ["git", "branch"]
published: true
published_at: 2024-12-30
---

## ローカルブランチの削除

- 対象のブランチ(`your-branch-name`)が現在のブランチにマージされている場合にのみ削除

```bash
git branch -d your-branch-name
```

- 強制的に削除

```bash
git branch -D your-branch-name
```

- リモートリポジトリで削除されたブランチをローカルの追跡ブランチから削除

```bash
git fetch -p
```

## リモートブランチの削除

```bash
git push origin --delete your-branch-name
```
