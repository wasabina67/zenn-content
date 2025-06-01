---
title: "60秒毎にtracertする"
emoji: "⚡"
type: "tech"
topics: ["batch"]
published: true
published_at: 2025-06-01
---

## スニペット

- Windows環境向けのbatファイル
- ファイル名は `tracert_loop.bat` など、エンコードは `ANSI` で保存する
- `Ctrl + C` から停止する

```batch
@echo off

setlocal EnableDelayedExpansion
set "TARGET=example.com"
set "INTERVAL=60"
set "LOG_DIR=logs"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "MAIN_LOG=%LOG_DIR%\tracert_log.txt"

:LOOP
    for /f "skip=1 tokens=2 delims==" %%a in ('wmic os get localdatetime /format:list') do set "dt=%%a"
    set "YY=%dt:~0,4%"
    set "MM=%dt:~4,2%"
    set "DD=%dt:~6,2%"
    set "HH=%dt:~8,2%"
    set "MN=%dt:~10,2%"
    set "SS=%dt:~12,2%"
    set "TS=%YY%%MM%%DD%_%HH%%MN%%SS%"
    echo ---------- %YY%/%MM%/%DD% %HH%:%MN%:%SS% %TARGET% ---------- >> "%MAIN_LOG%"

    tracert "%TARGET%" >> "%MAIN_LOG%" 2>&1

    echo. >> "%MAIN_LOG%"
    timeout /t %INTERVAL% >nul
goto LOOP
```
