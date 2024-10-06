---
title: "lambda関数のサンプルコード"
emoji: "🤖"
type: "tech"
topics: ["python"]
published: false
published_at: 2024-10-05
---

## 基本構文

```python
add = lambda x, y: x + y
print(add(3, 5))
```

## 関数の引数として渡す

### filter()

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```

```python
tuple_list = [(1, 2, 3, False), (1, 2, 3, False), (1, 2, 3, False), (1, 2, 3, True)]
print(list(filter(lambda x: x[3], tuple_list)))
```

### map()

```python
```

### sorted()

```python
```
