---
title: "devtunnel CLIの概要と活用事例について"
emoji: "🚇"
type: "tech"
topics: ["tunnel"]
published: true
published_at: 2025-05-27
---

<!-- 長いトンネルを抜けると、そこは localhost だった―― -->
<!-- 川端康成のファンじゃないので、やめとく -->

## devtunnel CLIとは

- devtunnel CLIとは、Microsoftが開発したトンネリングツール
- Microsoft または GitHubアカウントを使用してログインし、開発トンネルの管理とアクセスの承認を行う

## トンネリングツールとは

- トンネリングツールとは、ローカル環境で動作するWebアプリやAPIを、インターネット経由で外部からアクセス可能にする、ソフトウェアのこと
  - これにより、物理的に同じ場所にいなくても、クライアントやチームメンバーとの共有を図ることができ、リアルタイムでフィードバックを得ることができる
  - FWやNATのような「外部からの新規接続を止める仕組み」を超えて通信を可能にするため、注意が必要
- devtunnel CLI以外では、ngrokやCloudflare Tunnelなどが有名

![](/images/16/flowchart.png)

① hogehoge
② hogehoge
③ hogehoge
④ hogehoge

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

- 開発中のアプリで発生したバグを、チームメンバーと共有する
- ローカル環境を直接共有することができるので、バグの再現率が高い

![](/images/16/mushitori.png =150x)

### 2. APIテスト

- ローカル環境のAPIエンドポイントを公開する
- 開発段階で気づいた仕様の確認や懸念事項の共有に有効

![](/images/16/teacher_saiten_man.png =150x)

### 3. ビジネスサイドとの共有

- 開発中の機能をステークホルダーに迅速に共有し、フィードバックを得ることができる
- リモートワーク環境でのデモに最適

![](/images/16/business_online_syoudan_uchiawase.png =150x)

## まとめ

- devtunnel CLIは、開発プロセスにおける様々なシーンで活用できる便利ツール
- トンネリングツールは、手軽にローカル環境を公開できるため、技術的な理解と管理が重要
- 上手く取り入れることで、チームやクライアントとの情報共有の精度が高まる

## 参考資料

- [microsoft/dev-tunnels: Dev Tunnels SDK](https://github.com/microsoft/dev-tunnels)
- [トンネルを作成してホストする - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/get-started?tabs=linux)
- [開発トンネル コマンドライン リファレンス - Microsoft dev tunnels | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/developer/dev-tunnels/cli-commands)
