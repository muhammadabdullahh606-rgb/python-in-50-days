# ======================================================
# Day 05 - Type Conversion
# ======================================================

print("========== Day 05: Type Conversion ==========\n")

# -----------------------------------------------------
# 1. Why Type Conversion?
# -----------------------------------------------------

print("1. Why Type Conversion")

age = "20"

print(age)
print(type(age))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 2. String to Integer
# -----------------------------------------------------

print("2. String to Integer")

age = "20"

age = int(age)

print(age)
print(type(age))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 3. String to Float
# -----------------------------------------------------

print("3. String to Float")

price = "99.99"

price = float(price)

print(price)
print(type(price))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 4. Integer to String
# -----------------------------------------------------

print("4. Integer to String")

marks = 95

marks = str(marks)

print(marks)
print(type(marks))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 5. Float to Integer
# -----------------------------------------------------

print("5. Float to Integer")

number = 25.8

number = int(number)

print(number)
print(type(number))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 6. Boolean Conversion
# -----------------------------------------------------

print("6. Boolean Conversion")

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))

print("\n---------------------------------\n")

# -----------------------------------------------------
# 7. Using input() with int()
# -----------------------------------------------------

print("7. Using input() with int()")

age = int(input("Enter your age: "))

print("Next year you will be", age + 1)

print("\n---------------------------------\n")

# -----------------------------------------------------
# 8. Simple Calculator
# -----------------------------------------------------

print("8. Simple Calculator")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

print("Addition =", num1 + num2)

print("\n---------------------------------\n")

# -----------------------------------------------------
# 9. Summary
# -----------------------------------------------------

print("9. Summary")

print("int()    -> Converts to Integer")
print("float()  -> Converts to Float")
print("str()    -> Converts to String")
print("bool()   -> Converts to Boolean")

print("\n---------------------------------\n")

print("Tomorrow you'll learn Arithmetic Operators.")