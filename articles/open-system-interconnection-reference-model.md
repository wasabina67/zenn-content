---
title: "OSI参照モデルについて"
emoji: "🌐"
type: "tech"
topics: ["osi参照モデル", "tcpip"]
published: false
published_at: 2024-01-01
---

## OSI参照モデルとは

## レイヤー構成

| # | 名称 |
|---|---|
| L7 | アプリケーション層 / Application Layer |
| L6 | プレゼンテーション層 / Presentation Layer |
| L5 | セッション層 / Session Layer |
| L4 | トランスポート層 / Transport Layer |
| L3 | ネットワーク層 / Network Layer |
| L2 | データリンク層 / Data-Link Layer |
| L1 | 物理層 / Physical Layer |

## レイヤー詳細

### アプリケーション層

役割🏅
→ ファイル・メールの転送、DBアクセスなどの通信サービスを提供

例📌
→ HTTP、SCP、SMTP

### プレゼンテーション層

役割🏅
→ データ表現と暗号化

例📌
→ SSL/TLS

### セッション層

役割🏅
→ 通信プログラム間のセッションの管理

例📌
→ SSL/TLS

### トランスポート層

役割🏅
→ 通信の品質をコントロール

例📌
→ TCP、UDP

### ネットワーク層

役割🏅
→ データパケットのルーティング、中継

例📌
→ ルータ、IP

### データリンク層

役割🏅
→ 物理層の上に直接接続された機器間での信頼性のあるデータ通信

例📌
→ Ethernet、Wi-Fi、MACアドレスの管理

### 物理層

役割🏅
→ 物理的な接続

例📌
→ Ethernetケーブル、無線信号、光ファイバー
