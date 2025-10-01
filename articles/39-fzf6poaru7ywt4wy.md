---
title: "Create React App の非推奨化について"
emoji: "🐙"
type: ""
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

```bash
npx create-next-app@latest my-app
```

### 2. Remix

```bash
npx create-remix@latest my-app
```

### 3. Vite + React

```bash
npm create vite@latest my-app -- --template react
```

### 4. Gatsby

```bash
npm init gatsby
```

## 既存プロジェクトの移行ガイド

### 1. Next.jsへの移行

1. **新しいNext.jsプロジェクトの作成**

```bash
npx create-next-app@latest my-new-app
```

2. **ファイル構造の調整**

- `src/pages/`ディレクトリにコンポーネントを移行
- `public/`ディレクトリの静的ファイルをコピー

3. **ルーティングの変更**

- React Routerからファイルベースルーティングへ移行

### 2. Viteへの移行

1. **依存関係の更新**
```bash
npm install vite @vitejs/plugin-react
```

2. **設定ファイルの作成**
```javascript
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
```

3. **package.jsonスクリプトの更新**
```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

## 注意点とベストプラクティス

### 移行時の注意点

- **環境変数の命名規則変更**: Next.jsでは`NEXT_PUBLIC_`、Viteでは`VITE_`プレフィックスが必要
- **絶対インポートの設定**: プロジェクトごとに設定方法が異なる
- **ビルド出力の違い**: 各ツールで出力形式やディレクトリ構造が異なる

### 新規プロジェクトでの選択指針

- **本格的なWebアプリケーション**: Next.js
- **シンプルなSPA**: Vite + React
- **静的サイト**: Gatsby
- **Web標準重視**: Remix

## まとめ

Create React Appの非推奨化は、Reactエコシステムの成熟と進化を示す重要な転換点です。
より高性能で柔軟性の高い代替ツールが豊富に存在する現在、プロジェクトの要件に応じて最適なツールを選択することが重要です。

既存のCRAプロジェクトは引き続き動作しますが、セキュリティアップデートやバグ修正は期待できないため、早期の移行を検討することを強く推奨します。
移行は一見複雑に見えますが、各ツールが提供する豊富なドキュメントとコミュニティサポートを活用すれば、スムーズに進めることができるでしょう。

## 参考資料
- [Create React App の非推奨化 – React](https://ja.react.dev/blog/2025/02/14/sunsetting-create-react-app)
- [facebook/create-react-app](https://github.com/facebook/create-react-app?tab=readme-ov-file#deprecated)
- [Reactアプリ開発の環境構築ツール「Create React App」が非推奨に|CodeZine（コードジン）](https://codezine.jp/news/detail/21035)
