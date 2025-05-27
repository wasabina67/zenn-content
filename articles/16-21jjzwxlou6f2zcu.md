---
title: "devtunnel CLIの概要と活用事例について"
emoji: "🚇"
type: "tech"
topics: ["tunnel"]
published: true
published_at: 2025-05-27
---

## devtunnel CLIとは

- devtunnel CLIとは、Microsoftが開発したトンネリングツール
- Microsoft または GitHubアカウントを使用してログインし、開発トンネルの管理とアクセスの承認を行う

## トンネリングツールとは

- トンネリングツールとは、ネットワーク上で安全かつ効率的に、データ転送するためのソフトウェアを指します
- 他には、ngrokやCloudflare Tunnelなどが有名です
- localhostで動作しているWebアプリを、インターネット経由で外部からアクセス可能にします
  - これにより、物理的に同じ場所にいなくても、クライアントやチームメンバーとの共有を図ることができ、リアルタイムでフィードバックを得ることができます
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

- ローカルのAPIエンドポイントを公開できます
- 開発段階でのAPI仕様確認にも有効です

![](/images/16/teacher_saiten_man.png =150x)

### 3. ビジネスサイドとの共有

- 開発中の機能をステークホルダーに迅速に共有し、フィードバックを確認できます
- デプロイ前の段階で、UIやユーザビリティの確認を行い、要件との齟齬を早期に発見できます
- リモートワーク環境でのデモンストレーションにも最適です

![](/images/16/business_online_syoudan_uchiawase.png =150x)

## まとめ

- devtunnel CLIは、開発プロセスにおける様々なシーンで活用できる便利なツールです
- セキュアな認証機能により、安全性を保ちながらローカル環境を外部に公開できます
- チーム開発の効率化や、ステークホルダーとのコミュニケーション改善に大きく貢献します

## 参考資料

- [microsoft/dev-tunnels: Dev Tunnels SDK](https://github.com/microsoft/dev-tunnels)
- [トンネルを作成してホストする - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/get-started?tabs=linux)
- [開発トンネル コマンドライン リファレンス - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/cli-commands)
