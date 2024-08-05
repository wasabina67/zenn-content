---
title: "macOS環境構築について"
emoji: "🍎"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["mac"]
published: true
published_at: 2024-08-05
---

# Command Line Tools

```zsh
xcode-select --install
```

# Homebrew

https://brew.sh/

```zsh
brew install google-chrome
```

```zsh
brew install visual-studio-code
```

```zsh
brew install git
```

```zsh
brew list
```

```zsh
brew upgrade
```

## VSCode

`code`コマンドをインストールする

- `command` + `shift` + `P`からコマンドパレットを開く
- `shell command install`からインストールする

## git

Homebrewからインストールしたgitを使う

```zsh
which git
```

```zsh
/usr/bin/git --version
```

```zsh
/usr/local/bin/git --version
```

# GitHub

GitHubへSSHできるようにする

```zsh
ssh -T git@github.com
```

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
