# Day 08 - Logical Operators

## Objectives

By the end of this lesson, you will be able to:

- Understand logical operators in Python.
- Combine multiple conditions using `and`.
- Check if at least one condition is true using `or`.
- Reverse Boolean values using `not`.
- Solve simple real-world problems using logical operators.

---

# What are Logical Operators?

Logical operators are used to combine or modify comparison results.

They always work with Boolean values (`True` and `False`).

Python has three logical operators:

| Operator | Meaning |
|----------|---------|
| `and` | Returns `True` if **both** conditions are true |
| `or` | Returns `True` if **at least one** condition is true |
| `not` | Reverses a Boolean value |

---

# AND Operator

Both conditions must be true.

```python
print(True and True)
print(True and False)
```

Output

```
True
False
```

Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# OR Operator

At least one condition must be true.

```python
print(True or False)
print(False or False)
```

Output

```
True
False
```

Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# NOT Operator

The `not` operator reverses a Boolean value.

```python
print(not True)
print(not False)
```

Output

```
False
True
```

---

# Using Logical Operators with Comparisons

```python
age = 20
has_license = True

print(age >= 18 and has_license)
```

Output

```
True
```

---

```python
day = "Sunday"

print(day == "Saturday" or day == "Sunday")
```

Output

```
True
```

---

# Real-World Examples

Logical operators are commonly used for:

- Login systems
- Age verification
- Driving eligibility
- Voting eligibility
- Scholarship checks
- Weekend detection
- Access control
- AI decision-making

---

# Common Mistakes

Incorrect

```python
age >= 18 && has_license
```

Correct

```python
age >= 18 and has_license
```

---

Incorrect

```python
age >= 18 || has_license
```

Correct

```python
age >= 18 or has_license
```

---

Remember:

Python uses:

- `and`
- `or`
- `not`

It does **not** use `&&` or `||`.

---

# Summary

Today you learned:

- `and`
- `or`
- `not`
- Truth tables
- Combining multiple conditions
- Using logical operators with comparison operators
- Solving real-world problems using logical operators

Logical operators are one of the most important topics because they are heavily used with `if` statements, loops, functions, and real-world applications.