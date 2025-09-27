---
title: "tmp"
emoji: "🦙"
type: "tech"
topics: ["uv", "llm", "ollama"]
published: true
published_at: 2025-09-27
---

## Install uv

https://github.com/astral-sh/uv?tab=readme-ov-file#installation

## Install llm

https://github.com/simonw/llm?tab=readme-ov-file#quick-start

## Install llm-ollama

https://github.com/taketwo/llm-ollama?tab=readme-ov-file#installation

### OLLAMA_HOST

```bash
export OLLAMA_HOST=http://192.168.xx.xx:11434
```

## llm

### List available models

```bash
llm models
```

```
...
Ollama: gemma3:27b
Ollama: gpt-oss:20b
Default: gpt-oss:20b
```

### Set default model

```bash
llm models default gpt-oss:20b
```

### Run

```bash
llm 'hello'
```
