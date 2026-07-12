# Day 02 — Variables & Assignment

> **Today in one line:** Learn how to store information in variables and reuse it throughout your program.

---

# Why this matters

Imagine writing a shopping program where the price of a product appears in many places. If the price changes, updating every occurrence would be slow and error-prone.

Variables solve this problem. They allow us to store a value once and reuse it whenever we need it.

Think of a variable as a **labeled storage box**:
- The **label** is the variable name.
- The **box** stores the value.

---

# The Lesson

## What is a Variable?

A variable is a **named location in memory that stores a value so it can be used later.**

Example:

```python
name = "Abdullah"

print(name)
```

**Output**

```
Abdullah
```

Whenever we print `name`, Python retrieves the value stored inside it.

---

## The Assignment Operator (=)

In Python, `=` means:

> **Assign the value on the right to the variable on the left.**

Example:

```python
age = 20
```

Read it as:

> Assign the value `20` to the variable `age`.

---

## Variables vs Strings

```python
city = "Lahore"

print(city)
print("city")
```

**Output**

```
Lahore
city
```

- `city` is a variable.
- `"city"` is a string.

Without quotation marks, Python looks for a variable.

With quotation marks, Python prints the text exactly as written.

---

## Updating Variables

Variables can change.

```python
score = 50

print(score)

score = 100

print(score)
```

**Output**

```
50
100
```

The second assignment replaces the first value.

A variable stores **only one current value at a time.**

---

## Assigning One Variable to Another

```python
x = 10

y = x

print(y)
```

**Output**

```
10
```

Python copies the current value stored in `x` into `y`.

Changing `x` later does **not** change `y`.

```python
x = 100

print(x)
print(y)
```

**Output**

```
100
10
```

---

## Variable Naming Rules

### ✅ Valid

```python
student_name
age
price2025
_student
marks
```

### ❌ Invalid

```python
2student
student-name
student name
class
```

Rules:

- Variable names cannot begin with numbers.
- Variable names cannot contain spaces.
- Hyphens (`-`) are not allowed.
- Avoid Python keywords like `class`, `if`, `for`, and `while`.

---

## Python Naming Convention

Python recommends using **snake_case**.

Example:

```python
student_name
total_marks
monthly_salary
```

Using meaningful variable names makes code easier to understand and maintain.

---

## Common Mistake

```python
age = 20

age = 25

print(age)
```

**Output**

```
25
```

The second assignment replaces the previous value.

A variable stores only **one current value** at any given time.

---

# Try It Yourself

Run `lecture_code.py`.

Then:

- Change your name.
- Change your age.
- Change the product price.
- Predict the output before running the program.

---

# Recap

- Variables store values for later use.
- `=` assigns values.
- Variables can be updated.
- Variables store one current value at a time.
- Use meaningful names.
- Follow Python's `snake_case` convention.

---

⬅️ **Day 01** | **Day 03** ➡️