---
title: "tmuxコマンドについて"
emoji: "🪟"
type: "tech"
topics: ["tmux"]
published: true
published_at: 2025-06-29
---

## 基本操作

### セッション管理

```bash
# 新しいセッションを作成
tmux new -s mysession

# セッション一覧を表示
tmux ls

# セッションに再接続
tmux attach -t mysession
```

### ペイン操作

- コマンドプレフィックス：`Ctrl + b`
- 垂直分割：`"`
- 水平分割：`%`
- ペイン切り替え：`矢印キー`
- ペインのサイズ調整：`Ctrl + 矢印キー`
- ペインを閉じる：`exit`

### ウィンドウ操作

- ウィンドウを新規作成：`c`
- ウィンドウの切り替え：`n` / `p`
- ウィンドウ一覧表示：`w`

### セッション操作

- 一時離脱：`d`
- 再接続：`tmux attach`
