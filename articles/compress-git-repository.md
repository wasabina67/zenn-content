---
title: "Gitリポジトリを圧縮する"
emoji: "😺"
type: "tech"
topics: ["git"]
published: false
# published_at: 2099-08-03
---

# git-archive

:::message
`.git`ディレクトリは、**アーカイブに含まれません**。
:::

## 圧縮

※ リポジトリのトップディレクトリから実行

- HEADを指定

```bash
git archive --format=tar.gz -o your_repository.tar.gz HEAD
```

- 特定のブランチを指定

```bash
git archive --format=tar.gz -o your_repository.tar.gz your_branch
```

- 特定のコミットを指定

```bash
git archive --format=tar.gz -o your_repository.tar.gz your_commit_hash
```

## 展開

```bash
cd /path/to/destination
```

```bash
tar -xzf your_repository.tar.gz
```

# tar

:::message
`.git`ディレクトリは、**アーカイブに含まれます**。
:::

## 圧縮

※ リポジトリのトップディレクトリから実行

```bash
tar -czf your_repository.tar.gz .
```

## 展開
