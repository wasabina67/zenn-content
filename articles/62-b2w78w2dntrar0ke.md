---
title: "Google Chrome: OptGuideOnDeviceModel ディレクトリの概要と役割"
emoji: "🔍"
type: "tech"
topics: ["chrome", "windows11"]
published: true
published_at: 2026-02-10
---

## 概要

Google Chrome がオンデバイスで機械学習推論を実行するために使用する、学習済みモデルデータを格納するキャッシュディレクトリです。

### ディレクトリ

```
C:\Users\<YourName>\AppData\Local\Google\Chrome\User Data\OptGuideOnDeviceModel
```

## 名称の由来

- **OptGuide**: `Optimization Guide`（最適化ガイド）。Chrome のリソース使用やページ読み込みを最適化する内部コンポーネント。
- **OnDeviceModel**: クラウド（サーバーサイド）ではなく、端末上で推論を行うモデルであることを示唆。

## 主な用途

Chrome のバージョンや設定によりますが、以下の機能で利用されます。

1. **ナビゲーション予測**: ユーザーが次にクリックしそうなリンクを予測し、プリロードして表示速度を向上させる。
2. **ローカル生成 AI 機能**: 「Help me write（文書作成支援）」や「タブの整理」など、プライバシーやレイテンシを考慮してローカル LLM で処理される機能。
3. **セーフブラウジング**: URL を送信せずに、ローカルでフィッシングやマルウェアサイトを判定する。

## 技術的補足

- **ファイル形式**: 主に `TensorFlow Lite`（`.tflite`）形式や Chrome 独自のバイナリ形式が含まれます。
- **データサイズ**: 生成 AI 機能が有効な場合、数 GB 規模になることがあります。
- **削除時の挙動**: 削除してもシステムに影響はありませんが、次回 Chrome 起動時や機能利用時に**自動的に再ダウンロード**されます。
