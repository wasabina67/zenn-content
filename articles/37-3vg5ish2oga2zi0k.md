---
title: "WSL(Ubuntu)でVSCode/Cursorのpathを整理する"
emoji: "⚙️"
type: "tech"
topics: ["vscode", "cursor"]
published: true
published_at: 2025-07-28
---

## codeコマンドがCursorに上書きされる

Cursorのインストール後に、codeコマンドもCursorを使うようになってしまった

```
$ which cursor
/mnt/c/Users/wasab/AppData/Local/Programs/cursor/resources/app/bin/cursor
$ which code
/mnt/c/Users/wasab/AppData/Local/Programs/cursor/resources/app/bin/code
```

`codeコマンド` → 従来通り、VSCodeを開く
`cursorコマンド` → Cursorを開く
ようにする

## `/usr/local/bin`にスクリプトを置く

### cursor

```bash
#!/bin/bash

"/mnt/c/Users/wasab/AppData/Local/Programs/cursor/resources/app/bin/cursor" "$@"
```

### code

```bash
#!/bin/bash

"/mnt/c/Users/wasab/AppData/Local/Programs/Microsoft VS Code/bin/code" "$@"
```

それぞれに実行権限を付与する

## 確認

```bash
type -a cursor
```

```bash
type -a code
```
