---
title: ".htaccessでHTTPをすべてHTTPSにリダイレクトする"
emoji: "🕸"
type: "tech"
topics: ["htaccess"]
published: true
published_at: 2024-12-30
---

```bash
RewriteEngine On
RewriteBase /

RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://example.com/$1 [R=301,L]
```
