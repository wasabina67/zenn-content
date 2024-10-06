---
title: "lambda関数のサンプルコード"
emoji: "🤖"
type: "tech"
topics: ["python"]
published: true
published_at: 2024-10-07
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
res = list(filter(lambda x: x[3], tuple_list))
print(res)
```

### map()

```python
numbers = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

### sorted()

```python
students = [
    {"name": "John", "age": 15},
    {"name": "Jane", "age": 17},
    {"name": "Dave", "age": 16},
]
sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)
```
