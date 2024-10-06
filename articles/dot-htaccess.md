---
title: ".htaccessを使ったHTTPSリダイレクトのサンプルコード"
emoji: "🕸"
type: "tech"
topics: ["htaccess"]
published: true
published_at: 2024-10-06
---

## サンプルコード

```.htaccess
RewriteEngine On
RewriteBase /

# HTTPリクエストをすべてHTTPSにリダイレクト
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://example.com/$1 [R=301,L]
```
