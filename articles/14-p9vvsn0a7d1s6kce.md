---
title: "macOS環境構築について"
emoji: "🍎"
type: "tech"
topics: ["mac"]
published: true
published_at: 2025-05-11
---

## Xcode Command Line Tools

```zsh
xcode-select --install
```

## Homebrew

https://brew.sh/

```zsh
brew install wget
```

### 設定チェック

```zsh
brew doctor
```

### パッケージ定義を最新化

```zsh
brew list
```

```zsh
brew update
```

### VSCode, Chrome, iterm2, slack

- `cask`の定義の中で、VSCodeの実行ファイルに対するシンボリックリンクが自動で作成される
- そのため、`Command Palette`から`Shell Command: Install code in PATH`を実行しなくても、`code`コマンドが使用できる

```zsh
brew install --cask visual-studio-code
```

```zsh
brew install --cask google-chrome
```

```zsh
brew install --cask iterm2
```

```zsh
brew install --cask slack
```

### ohmyzsh

https://github.com/ohmyzsh/ohmyzsh

## Git

- Homebrewからインストールしたgitを使う

```zsh
brew install git
```

```zsh
which git
```

```zsh
/usr/bin/git --version
```

```zsh
/usr/local/bin/git --version
```

```zsh
/opt/homebrew/bin/git --version
```

## GitHub

- GitHubへSSHできるようにする

```zsh
ssh -T git@github.com
```

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

## GitHub CLI

```zsh
brew install gh
```

## nvm, npm, node

```zsh
brew install nvm
```

```zsh
nvm install --lts
```

```zsh
nvm ls
```

```zsh
nvm --version
```

```zsh
npm --version
```

```zsh
node --version
```

## uv

```zsh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

https://github.com/astral-sh/uv

https://docs.astral.sh/uv/

## poppler

```zsh
brew install poppler
```

## hugo

```zsh
brew install hugo
```
