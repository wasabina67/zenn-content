---
title: "ripgrep (rg)について"
emoji: "🔍"
type: "tech"
topics: ["ripgrep", "rg"]
published: true
published_at: 2026-05-02
---

## カレントディレクトリ以下を再帰検索

```bash
rg "word"
```

## ディレクトリを指定

```bash
rg "word" path/to/dir
```

## ファイルを指定

```bash
rg "word" file.txt
```

## 検索の絞り込み

| Option | Description |
| --- | --- |
| `-i` | 大文字小文字を無視 |
| `-w` | 単語単位で一致 |
| `-v` | マッチしない行を表示 |

## ファイル絞り込み

| Option | Description |
| --- | --- |
| `-t py` | Pythonファイルのみ（`-t`で言語指定） |
| `-g "*.md"` | globパターンで絞る |
| `-g "!*.test.js"` | globパターンで除外 |
| `--hidden` | 隠しファイルも対象 |
| `--no-ignore` | .gitignoreを無視 |

## 出力の制御

| Option | Description |
| --- | --- |
| `-l` | ファイル名のみ表示 |
| `-c` | ファイルごとのマッチ行数を表示 |
| `-n` | 行番号を表示 |
| `-A 3` | マッチ行の後3行を表示 |
| `-B 3` | マッチ行の前3行を表示 |
| `-C 3` | マッチ行の前後3行を表示 |
