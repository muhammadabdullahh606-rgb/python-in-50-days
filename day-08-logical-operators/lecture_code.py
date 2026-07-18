# ======================================================
# Day 08 - Logical Operators
# ======================================================

print("========== Day 08 - Logical Operators ==========\n")

# -----------------------------------------------------
# AND Operator
# -----------------------------------------------------

print("1. AND Operator")

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("\n---------------------------------\n")

# -----------------------------------------------------
# OR Operator
# -----------------------------------------------------

print("2. OR Operator")

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("\n---------------------------------\n")

# -----------------------------------------------------
# NOT Operator
# -----------------------------------------------------

print("3. NOT Operator")

print(not True)
print(not False)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Logical Operators with Comparisons
# -----------------------------------------------------

print("4. Using Logical Operators with Comparisons")

print(10 > 5 and 20 > 15)
print(10 > 20 and 5 > 2)

print(10 > 20 or 5 > 2)
print(10 > 20 or 5 > 10)

print(not (10 > 5))

print("\n---------------------------------\n")

# -----------------------------------------------------
# Voting Eligibility
# -----------------------------------------------------

print("5. Voting Eligibility")

age = int(input("Enter your age: "))

print("Eligible to vote:", age >= 18)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Driving Eligibility
# -----------------------------------------------------

print("6. Driving Eligibility")

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ")

print(age >= 18 and has_license == "yes")

print("\n---------------------------------\n")

# -----------------------------------------------------
# Weekend Checker
# -----------------------------------------------------

print("7. Weekend Checker")

day = input("Enter day: ")

print(day == "Saturday" or day == "Sunday")

print("\n---------------------------------\n")

# -----------------------------------------------------
# User Access
# -----------------------------------------------------

print("8. User Access")

is_banned = False

print("Access Allowed:", not is_banned)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Multiple Conditions
# -----------------------------------------------------

print("9. Multiple Conditions")

age = 25
salary = 60000
experience = 3

print(age >= 18 and salary >= 50000 and experience >= 2)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Student Scholarship Example
# -----------------------------------------------------

print("10. Scholarship Example")

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

print(marks >= 80 and attendance >= 75)

print("\n---------------------------------\n")

print("End of Day 08 Lecture")