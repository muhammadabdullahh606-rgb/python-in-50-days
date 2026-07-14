# Day 04 — Input & Output

print("========== Day 04: Input & Output ==========\n")

# ----------------------------------------------------
# 1. Getting User Input
# ----------------------------------------------------

print("1. Getting User Input")

name = input("Enter your name: ")

print("Hello,", name)

print("\n---------------------------------\n")

# ----------------------------------------------------
# 2. Input is Stored in Variables
# ----------------------------------------------------

print("2. Input is Stored in Variables")

city = input("Enter your city: ")

print("You live in", city)

print("\n---------------------------------\n")

# ----------------------------------------------------
# 3. Multiple Inputs
# ----------------------------------------------------

print("3. Multiple Inputs")

student = input("Student Name: ")
age = input("Age: ")
country = input("Country: ")

print("\nStudent Information")
print("Name:", student)
print("Age:", age)
print("Country:", country)

print("\n---------------------------------\n")

# ----------------------------------------------------
# 4. input() Returns a String
# ----------------------------------------------------

print("4. input() Returns a String")

number = input("Enter a number: ")

print("You entered:", number)
print(type(number))

print("\n---------------------------------\n")

# ----------------------------------------------------
# 5. Another Example
# ----------------------------------------------------

print("5. Favorite Programming Language")

language = input("Favorite language: ")

print("Your favorite programming language is", language)

print("\n---------------------------------\n")

# ----------------------------------------------------
# 6. Summary
# ----------------------------------------------------

print("6. Summary")

print("input() asks the user for information.")
print("The entered value is stored in a variable.")
print("input() always returns a string.")

print("\n---------------------------------\n")

print("Tomorrow you'll learn Type Conversion.")