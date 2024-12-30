---
title: "npmコマンドについて"
emoji: "🚀"
type: "tech"
topics: ["npm"]
published: true
published_at: 2024-12-30
---

## Create a package.json file

```bash
npm init
```

```bash
npm init -y
```

## Install a package

```bash
npm i
```

```bash
npm install
```

```bash
npm i <package-name>
```

```bash
npm install <package-name>
```

### Save dev

```bash
npm i <package-name> --save-dev
```

### Global

```bash
npm i -g <package-name>
```

```bash
npm i --global <package-name>
```

## Remove a package

```bash
npm un <package-name>
```

```bash
npm uninstall <package-name>
```

## List installed packages

```bash
npm list
```

### Global

```bash
npm list -g
```

```bash
npm list -g --depth=0
```

## View registry info

```bash
npm info <package-name>
```

## Run arbitrary package scripts

```bash
npm run <command>
```

## Update packages

```bash
npm update
```

```bash
npm update <package-name>
```

### Global

```bash
npm update -g
```

```bash
npm update -g <package-name>
```
