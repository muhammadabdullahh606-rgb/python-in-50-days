# Day 03 — Data Types

> **Today in one line:** Learn the four basic Python data types and use `type()` to identify them.

---

# What are Data Types?

Every value in Python has a **data type**.

A data type tells Python what kind of information a value represents.

For example:

- `21` is a whole number.
- `5.9` is a decimal number.
- `"Python"` is text.
- `True` represents a true/false value.

Python treats each of these differently.

---

# The Four Basic Data Types

## 1. Integer (`int`)

An integer is a whole number without a decimal point.

Examples:

```python
age = 21
students = 35
temperature = -5
```

---

## 2. Float (`float`)

A float is a number that contains a decimal point.

Examples:

```python
height = 5.9
price = 499.99
pi = 3.14159
```

---

## 3. String (`str`)

A string is text enclosed inside quotation marks.

Examples:

```python
name = "Abdullah"
language = "Python"
```

Remember:

```python
"123"
```

is still a string because it is inside quotes.

---

## 4. Boolean (`bool`)

A boolean has only two possible values:

```python
True
False
```

Examples:

```python
is_logged_in = True
is_raining = False
```

---

# The `type()` Function

Python provides the `type()` function to identify the data type of a value.

Example:

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

Another example:

```python
print(type("Python"))
```

Output:

```text
<class 'str'>
```

---

# Why Data Types Matter

Different data types behave differently.

For example:

- Numbers can be used in calculations.
- Strings store text.
- Booleans help make decisions in programs.

Understanding data types is the foundation for writing correct Python programs.

---

# Key Points

- Every value has a data type.
- `int` → Whole numbers.
- `float` → Decimal numbers.
- `str` → Text inside quotation marks.
- `bool` → `True` or `False`.
- Use `type()` to check a value's data type.

---

# Common Mistakes

❌ Thinking `"20"` and `20` are the same.

They are different:

```python
20
```

is an integer.

```python
"20"
```

is a string.

---

# Today's Outcome

By the end of Day 3, you should be able to:

- Identify the four basic Python data types.
- Understand the difference between numbers and strings.
- Use `type()` to inspect values.
- Recognize common beginner mistakes with data types.