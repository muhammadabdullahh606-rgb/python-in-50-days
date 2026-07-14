# Day 04 — Input & Output

> **Today in one line:** Learn how to take input from the user and display it using `print()`.

---

# What is `input()`?

`input()` is a built-in Python function that allows a program to receive information from the user.

Instead of using fixed values, the program asks the user to enter data.

Example:

```python
name = input("Enter your name: ")
```

The message inside the quotation marks is called the **prompt**. It tells the user what information to enter.

---

# How `input()` Works

When Python executes:

```python
name = input("Enter your name: ")
```

it performs three steps:

1. Displays the prompt.
2. Waits for the user to type something.
3. Stores the entered value in the variable.

Example:

```text
Enter your name: Abdullah
```

Python stores:

```python
name = "Abdullah"
```

---

# Displaying User Input

Once the value is stored, it can be displayed using `print()`.

Example:

```python
name = input("Enter your name: ")

print(name)
```

Output:

```text
Enter your name: Abdullah
Abdullah
```

---

# Taking Multiple Inputs

You can ask the user for more than one value.

Example:

```python
name = input("Name: ")
age = input("Age: ")
city = input("City: ")
```

Each value is stored in its own variable.

---

# Using Variables with `print()`

```python
print(name)
print(age)
print(city)
```

You can also combine text with variables.

```python
print("Hello,", name)
```

Example Output:

```text
Hello, Abdullah
```

---

# Important Concept

`input()` always returns a **string**.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
21
```

The output is:

```text
<class 'str'>
```

Even though `21` looks like a number, Python stores it as text.

---

# Why is This Important?

Programs become interactive when they can receive information from users.

Examples:

- Login forms
- Registration forms
- Surveys
- Calculators
- Games

All of these use user input.

---

# Common Mistakes

## Mistake 1

Wrong:

```python
name = input
```

Correct:

```python
name = input()
```

---

## Mistake 2

Wrong:

```python
input(Enter Name)
```

Correct:

```python
input("Enter Name")
```

---

## Mistake 3

Thinking that:

```python
input()
```

returns an integer.

It does not.

It always returns a string.

---

# Key Points

- `input()` asks the user for information.
- The entered value is stored in a variable.
- `print()` displays the stored value.
- The prompt helps users know what to enter.
- `input()` always returns a string.

---

# Today's Outcome

By the end of Day 4, you should be able to:

- Use `input()` to receive information from the user.
- Store user input in variables.
- Display the entered values using `print()`.
- Understand that `input()` always returns a string.