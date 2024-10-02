---
title: "ssh-agentを手動で起動する"
emoji: "🔑"
type: "tech"
topics: ["git", "sshagent"]
published: true
published_at: 2024-10-02
---

## 手順

### 1. バックグラウンドでssh-agentを開始

```bash
eval "$(ssh-agent -s)"
```

### 2. SSHプライベートキーをssh-agentに追加・確認

```bash
ssh-add ~/.ssh/id_ed25519
```

```bash
ssh-add -l
```

## 参考

https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent
