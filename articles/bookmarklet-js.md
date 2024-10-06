---
title: "ブックマークレットのサンプルコード"
emoji: "📚"
type: "tech"
topics: ["bookmarklet"]
published: false
published_at: 2024-10-05
---

## サンプルコード

### alert

```javascript
javascript:(function(){alert('Hello, Bookmarklet!');})();
```

```javascript
javascript:alert(new Date().getFullYear() + '-' + ('0' + (new Date().getMonth() + 1)).slice(-2) + '-' + ('0' + new Date().getDate()).slice(-2));void(0);
```

### id/name に文字列を追加

```javascript
javascript:document.getElementById("id").value = "id";document.getElementById("name").value = "name";void(0);
```
