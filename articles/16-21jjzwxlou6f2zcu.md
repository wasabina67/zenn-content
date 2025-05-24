---
title: "devtunnel CLIの概要と活用事例について"
emoji: "🚇"
type: "tech"
topics: ["tunnel"]
published: false
published_at: 2025-05-24
---

## トンネリングツールとは

- トンネリングツールとは、ネットワーク上で安全かつ効率的に、データ転送するためのソフトウェアを指します
- 他には、ngrokやCloudflare Tunnelなどが有名です
- localhostで動作しているWebアプリを、インターネット経由で外部からアクセス可能にする際などに使用されます
  - これにより、物理的に同じ場所にいなくても、クライアントやチームメンバーとの共有を図ることができ、リアルタイムでフィードバックを得ることが可能になります
  - また、トンネリングツールはFWやNATを超えて通信を可能にするため、リモートデバッグやAPIテストなどの様々な開発シナリオで役立ちます

## 使い方

```bash
devtunnel user login
```

```bash
devtunnel host -p 4173
```

```bash
devtunnel host -p 4173 --allow-anonymous
```

## 実業務での利用例

### 1. リモートデバッグ

WIP

### 2. APIテスト

WIP

### 3. ビジネスサイドとの共有

WIP

## まとめ

WIP

## 参考資料

- https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/get-started?tabs=linux
- https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/cli-commands
- https://github.com/microsoft/dev-tunnels
