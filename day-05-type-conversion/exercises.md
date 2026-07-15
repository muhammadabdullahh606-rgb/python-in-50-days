# Day 05 - Exercises

Complete the following questions without looking at the lecture code. Think before answering.

---

## Part A - Theory

### 1.

What is type conversion?

---

### 2.

Why do we use `int()` with `input()`?

---

### 3.

What does the `float()` function do?

---

### 4.

What does the `str()` function do?

---

### 5.

What does the `bool()` function do?

---

## Part B - Predict the Output

### 6.

```python
print(int("50"))
```

Output:

---

### 7.

```python
print(float("25"))
```

Output:

---

### 8.

```python
print(str(99))
```

Output:

---

### 9.

```python
print(bool(0))
print(bool(100))
```

Output:

---

### 10.

```python
print(int(15.9))
```

Output:

---

### 11.

```python
print(type(float(10)))
```

Output:

---

### 12.

```python
print(int("100") + 20)
```

Output:

---

### 13.

```python
print(str(float("50")))
```

Output:

---

## Part C - Find the Mistake

### 14.

Why will this code produce an error?

```python
age = input("Enter age: ")

print(age + 5)
```

---

### 15.

How can you fix it?

---

### 16.

Why does this produce an error?

```python
int("25.5")
```

---

## Part D - Practical

### 17.

Write a program that:

- asks for your age
- converts it into an integer
- prints your age after five years

---

### 18.

Write a program that:

- asks for two decimal numbers
- converts both into floats
- prints their sum

---

### 19.

Write a program that converts an integer into a string and prints both the value and its data type.

---

### 20.

Write a program that prints the result of:

- `bool(0)`
- `bool(1)`
- `bool("")`
- `bool("Python")`

---

## Challenge

Without running Python, answer the following:

```python
number = "100"

print(int(number) + float("50"))
print(type(int(number)))
print(type(float("50")))
```

Explain every output.