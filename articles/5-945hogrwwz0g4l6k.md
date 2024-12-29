---
title: "Bookmarkletについて"
emoji: "📚"
type: "tech"
topics: ["bookmarklet"]
published: true
published_at: 2024-10-06
---

## alert

```javascript
javascript:(function(){alert('Hello, Bookmarklet!');})();
```

```javascript
javascript:alert(new Date().getFullYear() + '-' + ('0' + (new Date().getMonth() + 1)).slice(-2) + '-' + ('0' + new Date().getDate()).slice(-2));void(0);
```

## name, scoreに文字列を追加

```javascript
javascript:document.getElementById("name").value = "name";document.getElementById("score").value = "123";void(0);
```
