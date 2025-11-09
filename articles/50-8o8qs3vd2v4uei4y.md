---
title: "uv, Ruff でPython開発環境を整える"
emoji: "🐍"
type: "tech"
topics: ["uv", "ruff"]
published: true
published_at: 2025-11-09
---

## はじめに

uv と Ruff を使用したPython開発環境のセットアップ例を紹介します。

https://github.com/wasabina67/uv-ruff-example

## uv とは

- uvは、Rust製の高速なPythonパッケージインストーラー兼リゾルバー
- pip や poetry の代替として使用可能で、従来のツールより大幅に高速
- プロジェクトの依存関係管理と仮想環境の作成を簡単に行える

## Ruff とは

- Ruffは、Rust製の高速なPythonリンター＆フォーマッター
- flake8、isort、pyupgrade などの複数ツールの機能を統合
- 従来のツールと比較して、10〜100倍高速に動作

## プロジェクトのセットアップ

### 1. プロジェクトの初期化

```bash
uv init --app --python 3.12
```

- `--app`: アプリケーションプロジェクトとして初期化
- `--python 3.12`: Python 3.12を指定

### 2. 依存関係の追加

本番用パッケージの追加:

```bash
uv add numpy
```

開発用パッケージの追加:

```bash
uv add --dev ruff
```

### 3. 依存関係の同期

```bash
uv sync
```

## Ruff の使い方

### コードチェック

```bash
uv run ruff check .
```

### 自動修正

```bash
uv run ruff check --fix .
```

### コードフォーマット

```bash
uv run ruff format .
```

## pyproject.toml の設定例

```toml
[tool.ruff]
target-version = "py312"
line-length = 120

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "SIM", # flake8-simplify
]

[tool.ruff.format]
indent-style = "space"
quote-style = "double"
```

## プログラムの実行

仮想環境をアクティベートせずに実行:

```bash
uv run python main.py
```

または、仮想環境をアクティベートして実行:

```bash
source .venv/bin/activate
python main.py
deactivate
```

## まとめ

- **uv**: 高速なパッケージ管理とプロジェクト初期化
- **Ruff**: 高速なリント＆フォーマット
- 両ツールともRust製で、従来のツールより大幅に高速
- `pyproject.toml` で一元的に設定管理が可能

これらのツールを組み合わせることで、効率的で快適なPython開発環境を構築できます。
