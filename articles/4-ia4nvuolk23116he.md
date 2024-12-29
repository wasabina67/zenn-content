---
title: "PythonのLambda関数について"
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

## 引数として利用する

### sorted

```python
students = [
    {"name": "John", "age": 15},
    {"name": "Jane", "age": 17},
    {"name": "Dave", "age": 16},
]
sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)
```

### sort

```python
students = [
    {"name": "John", "age": 15},
    {"name": "Jane", "age": 17},
    {"name": "Dave", "age": 16},
]
students.sort(key=lambda student: student["age"])
print(students)
```

### max

```python
```

### min

```python
```

### map

```python
nums = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
```

### filter

```python
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
```

```python
tuple_list = [
    (1, 2, 3, False),
    (1, 2, 3, False),
    (1, 2, 3, False),
    (1, 2, 3, True),
]
result = list(filter(lambda x: x[3], tuple_list))
print(result)
```
