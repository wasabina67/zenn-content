---
title: "devtunnel CLIの概要と活用事例について"
emoji: "🚇"
type: "tech"
topics: ["tunnel"]
published: true
published_at: 2025-05-24
---

## devtunnel CLIとは

- devtunnel CLIは、Microsoftが開発したトンネリングツールです
- ローカル環境で動作するWebアプリやAPIを、インターネット経由で外部からアクセス可能にします
- Azure Active Directoryとの統合により、セキュアな認証機能を提供し、安全な共有を実現します

## トンネリングツールとは

- トンネリングツールとは、ネットワーク上で安全かつ効率的に、データ転送するためのソフトウェアを指します
- 他には、ngrokやCloudflare Tunnelなどが有名です
- localhostで動作しているWebアプリを、インターネット経由で外部からアクセス可能にします
  - これにより、物理的に同じ場所にいなくても、クライアントやチームメンバーとの共有を図ることができ、リアルタイムでフィードバックを得ることが可能になります
  - トンネリングツールはFWやNATを超えて通信を可能にするため、リモートデバッグやAPIテストなどの様々な開発シナリオで役立ちます

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

## 業務での利用事例

### 1. リモートデバッグ

- 開発中のアプリで発生したバグを、チームメンバーと共有する際に活用できます
- ローカル環境の問題を再現可能な状態で公開し、リアルタイムでのデバッグを実施できます

![](/images/16/mushitori.png =150x)

### 2. APIテスト

WIP

![](/images/16/teacher_saiten_man.png =150x)

### 3. ビジネスサイドとの共有

WIP

![](/images/16/business_online_syoudan_uchiawase.png =150x)

## まとめ

WIP

## 参考資料

- [microsoft/dev-tunnels: Dev Tunnels SDK](https://github.com/microsoft/dev-tunnels)
- [トンネルを作成してホストする - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/get-started?tabs=linux)
- [開発トンネル コマンドライン リファレンス - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/cli-commands)
