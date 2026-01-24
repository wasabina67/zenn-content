---
title: "Git Flowのブランチ戦略"
emoji: "🪵"
type: "tech"
topics: ["git", "gitflow"]
published: true
published_at: 2026-01-24
---

## ブランチの種類と用途

| ブランチ | 用途 | 派生元 | マージ先 |
| --- | --- | --- | --- |
| master | 本番環境にデプロイされるコード | - | - |
| develop | 開発中の最新コード | master | master |
| release | リリース準備用 | develop | master, develop |
| feature-* | 新機能の開発用 | develop | develop |
| hotfix-* | 緊急のバグ修正用 | master | master, develop |
