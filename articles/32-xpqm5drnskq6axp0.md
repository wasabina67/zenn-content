---
title: "Pythonの辞書操作における参照コピーとディープコピーの違いについて"
emoji: "🐍"
type: "tech"
topics: ["python"]
published: true
published_at: 2025-06-03
---

- 単純な代入では、参照のコピーで両方の変数が同じオブジェクトを示す
- `copy.deepcopy()`では、ネストされたオブジェクトも含めて完全に新しいコピーを作成する
