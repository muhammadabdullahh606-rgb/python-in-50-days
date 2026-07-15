# Day 05 - Type Conversion

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand what type conversion is.
- Convert strings into integers and floats.
- Convert integers and floats into strings.
- Convert values into boolean.
- Use `int()` with `input()` to perform calculations.
- Understand why type conversion is necessary in Python.

---

# What is Type Conversion?

Type conversion is the process of changing one data type into another.

For example:

- String → Integer
- String → Float
- Integer → String
- Float → Integer
- Integer → Float
- Value → Boolean

Python provides built-in functions to perform these conversions.

---

# Why Do We Need Type Conversion?

The `input()` function always returns data as a string.

Example:

```python
age = input("Enter your age: ")
```

If the user enters:

```
20
```

Python stores it as:

```python
"20"
```

not

```python
20
```

If you try:

```python
print(age + 5)
```

Python will produce an error because it cannot add a string and an integer.

To solve this problem:

```python
age = int(input("Enter your age: "))
```

Now Python stores:

```python
20
```

as an integer, allowing mathematical operations.

---

# int()

The `int()` function converts a value into an integer.

Example:

```python
number = int("25")

print(number)
print(type(number))
```

Output:

```
25
<class 'int'>
```

---

# float()

The `float()` function converts a value into a floating-point number.

Example:

```python
price = float("99.99")

print(price)
print(type(price))
```

Output:

```
99.99
<class 'float'>
```

---

# str()

The `str()` function converts a value into a string.

Example:

```python
marks = str(95)

print(marks)
print(type(marks))
```

Output:

```
95
<class 'str'>
```

---

# bool()

The `bool()` function converts a value into either `True` or `False`.

Examples:

```python
bool(0)
```

Output:

```
False
```

```python
bool(1)
```

Output:

```
True
```

```python
bool("")
```

Output:

```
False
```

```python
bool("Python")
```

Output:

```
True
```

---

# Float to Integer

A float can also be converted into an integer.

Example:

```python
number = int(25.8)

print(number)
```

Output:

```
25
```

**Important:**

`int()` does **not** round the number.

It simply removes the decimal part.

Examples:

```python
int(5.9)
```

Output:

```
5
```

```python
int(99.99)
```

Output:

```
99
```

---

# Using input() with int()

This is one of the most common uses of type conversion.

Example:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters:

```
20
```

Output:

```
21
```

Without `int()`, Python would treat the input as a string instead of a number.

---

# Common Mistakes

### Mistake 1

```python
age = input("Enter age: ")

print(age + 5)
```

This causes an error because `age` is a string.

Correct:

```python
age = int(input("Enter age: "))
```

---

### Mistake 2

Trying to convert an invalid value.

```python
int("25.5")
```

This produces a `ValueError` because `"25.5"` is not a valid integer.

Use:

```python
float("25.5")
```

instead.

---

### Mistake 3

Thinking `int()` rounds numbers.

Example:

```python
int(8.9)
```

Output:

```
8
```

The decimal part is removed.

---

# Summary

Today you learned:

- What type conversion is.
- Why `input()` usually needs `int()`.
- How to use `int()`.
- How to use `float()`.
- How to use `str()`.
- How to use `bool()`.
- How Python converts floats into integers.
- Common mistakes beginners make.

---

# Key Takeaways

- `input()` always returns a string.
- `int()` converts to an integer.
- `float()` converts to a float.
- `str()` converts to a string.
- `bool()` converts to a boolean.
- `int()` removes the decimal part instead of rounding.
- Type conversion allows Python to perform the correct operations.

---

# Homework

1. Convert `"150"` into an integer.
2. Convert `"19.75"` into a float.
3. Convert `500` into a string.
4. Convert `0` and `100` into booleans.
5. Create a program that asks the user for two numbers and prints their sum.

---

Tomorrow you will learn **Arithmetic Operators**, where you'll perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.