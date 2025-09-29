---
title: "Create React App の非推奨化について"
emoji: "🐙"
type: "tech"
topics: ["cra", "react"]
published: true
published_at: 2025-09-30
---

## Create React App（CRA）とは

Create React App（CRA）は、2016年にMeta（旧Facebook）によって開発されたReactアプリケーションの開発環境を迅速にセットアップするためのツールチェーンです。
webpackやBabelなどの複雑な設定を隠蔽し、開発者が即座にReactの開発を始められるように設計されていました。

```bash
% npx create-react-app my-app
% cd my-app
% npm start
```

このシンプルなコマンドで、本格的なReactアプリケーションの開発環境が整う手軽さから、多くの初心者から上級者まで幅広く利用されてきました。

## 非推奨化の背景

2025年2月14日、React公式ブログにてCreate React Appの非推奨化が正式に発表されました。

https://ja.react.dev/blog/2025/02/14/sunsetting-create-react-app

主な理由は以下の通りです：

### 1. メンテナンスの困難さ
- 複雑なビルドチェーンの抽象化により、内部の問題解決が困難
- webpackやBabelのアップデートに追随するのが困難
- セキュリティパッチの適用に時間がかかる状況

### 2. 現代的な開発ニーズとの乖離
- Server-Side Rendering（SSR）やStatic Site Generation（SSG）への対応不足
- モダンなJavaScript機能への対応の遅れ
- TypeScriptサポートの限界

### 3. エコシステムの進化
- より高性能で柔軟性の高い代替ツールの台頭
- 開発者のニーズの多様化
- ビルドツールの高速化技術の進歩

## 推奨される代替ツール

Reactチームが推奨する代替ツールは以下の通りです：

### 1. Next.js

### 2. Remix

### 3. Vite + React

## 既存プロジェクトの移行ガイド

### 1. Next.jsへの移行

### 2. Viteへの移行

## 注意点とベストプラクティス

### 移行時の注意点

### 新規プロジェクトでの選択指針

## まとめ

## 参考資料
- [facebook/create-react-app](https://github.com/facebook/create-react-app?tab=readme-ov-file#deprecated)
- [Reactアプリ開発の環境構築ツール「Create React App」が非推奨に|CodeZine（コードジン）](https://codezine.jp/news/detail/21035)
