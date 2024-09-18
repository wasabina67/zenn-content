---
title: "Windows11環境構築について"
emoji: "🪟"
type: "tech"
topics: ["windows11"]
published: false
# published_at: 2099-08-03
---

# はじめに

ラップトップのメイン機として使用している、ThinkPadを初期化しました。
初期設定からツールの導入までの手順を簡単にメモしておきます。

# 初期設定 1

- Windows Update
- 電源プランの編集
- OneDriveのログアウト、PCのリンク解除
- `タスクマネージャー > スタートアップアプリ`から不要なアプリを無効化
- `設定 > 個人用設定 > テーマ`からテーマを変更
- `設定 > 個人用設定 > タスクバー`から表示設定を変更
- `設定 > 個人用設定 > スタート`から表示設定を変更
- スタートメニューのピン留め済みアプリを整理

# 初期設定 2

- `デスクトップ > 表示`から小アイコンを設定
- `デスクトップ > ディスプレイ設定 > 拡大/縮小`からサイズを設定
- `タッチパッド設定 > カーソル速度`から速度を設定
- エクスプローラーから拡張子の表示を有効化
- `設定 > アカウント > サインインオプション`から`サインイン画面に電子メールアドレスなどのアカウントの詳細を表示します。`を有効化

# Google Chrome

https://www.google.com/intl/ja_jp/chrome/

# WSL

https://learn.microsoft.com/ja-jp/windows/wsl/install

https://learn.microsoft.com/ja-jp/windows/wsl/tutorials/linux

# VSCode

https://code.visualstudio.com/download

# GitHub

```bash
ssh -T git@github.com
```

https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux

https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

# Docker Desktop

https://docs.docker.jp/desktop/windows/wsl.html

# HeidiSQL

https://www.heidisql.com/
