---
title: "ssh-agentを手動で起動する"
emoji: "🔑"
type: "tech"
topics: ["git", "sshagent"]
published: true
published_at: 2024-12-30
---

## 起動手順

### 1. バックグラウンドでssh-agentを開始

```bash
eval "$(ssh-agent -s)"
```

### 2. SSHプライベートキーをssh-agentに追加

```bash
ssh-add ~/.ssh/id_ed25519
```

### ワンライナー

```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
```

## 確認

### ssh-agentプロセス

```bash
ps -aef | grep ssh-agent | grep -v grep
```

### SSHプライベートキー

```bash
ssh-add -l
```

## 参考

https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux#adding-your-ssh-key-to-the-ssh-agent
