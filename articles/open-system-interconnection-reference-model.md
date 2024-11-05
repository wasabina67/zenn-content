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

- L7 | アプリケーション層 | Application Layer
- L6 | プレゼンテーション層 | Presentation Layer
- L5 | セッション層 | Session Layer
- L4 | トランスポート層 | Transport Layer
- L3 | ネットワーク層 | Network Layer
- L2 | データリンク層 | Data-Link Layer
- L1 | 物理層 | Physical Layer

## レイヤー詳細

### アプリケーション層

具体的な通信サービスを提供。

### プレゼンテーション層

- 役割
  - 暗号化、復号化、データ形式の変換
- 例
  - SSL/TLS、データ圧縮

### セッション層

- 役割
  - アプリケーション間のセッションの管理
- 例
  - セッションの確立、維持、終了

### トランスポート層

- 役割
  - E2Eの通信の信頼性を確保、エラーチェックと修正
- 例
  - TCP、UDP

### ネットワーク層

- 役割
  - データパケットのルーティング、異なるネットワーク間での送信
- 例
  - IP、ルータ

### データリンク層

- 役割
  - 物理層の上に直接接続された機器間での信頼性のあるデータ通信
- 例
  - Ethernet、Wi-Fi、MACアドレスの管理

### 物理層

- 役割
  - ビットレベルのデータ転送、電気的機械的接続
- 例
  - Ethernetケーブル、無線信号、光ファイバー
