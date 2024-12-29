---
title: "ssh-agentを手動で起動する"
emoji: "🔑"
type: "tech"
topics: ["git", "sshagent"]
published: true
published_at: 2024-10-02
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
