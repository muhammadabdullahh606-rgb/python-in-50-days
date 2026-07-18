# Day 08 Exercises

## Theory Questions

### 1.

What are logical operators?

---

### 2.

Name the three logical operators in Python.

---

### 3.

What does the `and` operator do?

---

### 4.

What does the `or` operator do?

---

### 5.

What does the `not` operator do?

---

### 6.

What is the difference between comparison operators and logical operators?

---

## Predict the Output

### 7.

```python
print(True and True)
```

---

### 8.

```python
print(True and False)
```

---

### 9.

```python
print(False or True)
```

---

### 10.

```python
print(False or False)
```

---

### 11.

```python
print(not True)
```

---

### 12.

```python
print(not False)
```

---

### 13.

```python
print(10 > 5 and 20 > 15)
```

---

### 14.

```python
print(10 > 20 or 5 < 8)
```

---

### 15.

```python
print(not (10 > 5))
```

---

### 16.

```python
age = 20

print(age >= 18 and age < 30)
```

---

### 17.

```python
day = "Sunday"

print(day == "Saturday" or day == "Sunday")
```

---

### 18.

```python
is_banned = False

print(not is_banned)
```

---

## Coding Exercises

### 19.

Ask the user to enter their age.

Print whether they are eligible to vote using a logical expression.

---

### 20.

Ask the user to enter:

- Their age
- Whether they have a driving license (`yes` or `no`)

Print whether they are eligible to drive.

(Hint: Use `and`.)

---

### 21.

Ask the user to enter a day of the week.

Print `True` if it is Saturday or Sunday.

(Hint: Use `or`.)

---

### 22.

Create a variable:

```python
is_logged_in = True
```

Print:

```python
not is_logged_in
```

---

### 23.

Store the following values:

```python
marks = 85
attendance = 80
```

Print whether the student qualifies for a scholarship.

Condition:

- Marks ≥ 80
- Attendance ≥ 75

---

### 24.

Store these values:

```python
age = 25
salary = 60000
experience = 3
```

Print whether the person qualifies for a job.

Condition:

- Age ≥ 18
- Salary ≥ 50000
- Experience ≥ 2

---

## Challenge

### Challenge 1

Create a program that asks the user for:

- Age
- Has ID card? (`yes` or `no`)

Print:

- Eligible for entry: `True` or `False`

Condition:

- Age ≥ 18
- Has ID card = `yes`

---

### Challenge 2

Create a weekend checker.

Ask the user to enter a day.

Print:

- Weekend: `True` or `False`

The weekend is:

- Saturday
- Sunday

(Hint: Use the `or` operator.)

---

### Challenge 3

Create a login permission checker.

Create the following variables:

```python
is_admin = False
is_logged_in = True
```

Print:

- Admin Access
- User Access

Requirements:

- Admin Access is allowed only if `is_admin` is `True`.
- User Access is allowed only if the user is **not** logged out.

(Hint: Use the `not` operator.)

---

## Bonus Challenge

Ask the user to enter:

- Marks
- Attendance Percentage

Print whether the student passes the eligibility criteria.

Conditions:

- Marks ≥ 50
- Attendance ≥ 75

Use the `and` operator to combine both conditions.