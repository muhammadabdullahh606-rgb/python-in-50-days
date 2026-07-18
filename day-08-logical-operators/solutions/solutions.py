# ======================================================
# Day 08 - Solutions
# ======================================================

print("========== Day 08 Solutions ==========\n")

# -----------------------------------------------------
# Theory Questions
# -----------------------------------------------------

print("Theory Question 1")
print("Logical operators combine or modify Boolean expressions.")

print("\n---------------------------------\n")

print("Theory Question 2")
print("The three logical operators are: and, or, not.")

print("\n---------------------------------\n")

print("Theory Question 3")
print("'and' returns True only if all conditions are True.")

print("\n---------------------------------\n")

print("Theory Question 4")
print("'or' returns True if at least one condition is True.")

print("\n---------------------------------\n")

print("Theory Question 5")
print("'not' reverses a Boolean value.")

print("\n---------------------------------\n")

print("Theory Question 6")
print("Comparison operators compare values, while logical operators combine comparison results.")

print("\n---------------------------------\n")

# -----------------------------------------------------
# Predict the Output
# -----------------------------------------------------

print("Exercise 7")
print(True and True)

print("\n---------------------------------\n")

print("Exercise 8")
print(True and False)

print("\n---------------------------------\n")

print("Exercise 9")
print(False or True)

print("\n---------------------------------\n")

print("Exercise 10")
print(False or False)

print("\n---------------------------------\n")

print("Exercise 11")
print(not True)

print("\n---------------------------------\n")

print("Exercise 12")
print(not False)

print("\n---------------------------------\n")

print("Exercise 13")
print(10 > 5 and 20 > 15)

print("\n---------------------------------\n")

print("Exercise 14")
print(10 > 20 or 5 < 8)

print("\n---------------------------------\n")

print("Exercise 15")
print(not (10 > 5))

print("\n---------------------------------\n")

print("Exercise 16")

age = 20
print(age >= 18 and age < 30)

print("\n---------------------------------\n")

print("Exercise 17")

day = "Sunday"
print(day == "Saturday" or day == "Sunday")

print("\n---------------------------------\n")

print("Exercise 18")

is_banned = False
print(not is_banned)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Coding Exercises
# -----------------------------------------------------

print("Exercise 19")

age = int(input("Enter your age: "))
print("Eligible to vote:", age >= 18)

print("\n---------------------------------\n")

print("Exercise 20")

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ")

print("Eligible to drive:", age >= 18 and has_license.lower() == "yes")

print("\n---------------------------------\n")

print("Exercise 21")

day = input("Enter a day: ")

print("Weekend:", day.lower() == "saturday" or day.lower() == "sunday")

print("\n---------------------------------\n")

print("Exercise 22")

is_logged_in = True

print(not is_logged_in)

print("\n---------------------------------\n")

print("Exercise 23")

marks = 85
attendance = 80

print(marks >= 80 and attendance >= 75)

print("\n---------------------------------\n")

print("Exercise 24")

age = 25
salary = 60000
experience = 3

print(age >= 18 and salary >= 50000 and experience >= 2)

print("\n---------------------------------\n")

# -----------------------------------------------------
# Challenge 1
# -----------------------------------------------------

print("Challenge 1")

age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (yes/no): ")

print("Eligible for entry:", age >= 18 and has_id.lower() == "yes")

print("\n---------------------------------\n")

# -----------------------------------------------------
# Challenge 2
# -----------------------------------------------------

print("Challenge 2")

day = input("Enter a day: ")

print("Weekend:", day.lower() == "saturday" or day.lower() == "sunday")

print("\n---------------------------------\n")

# -----------------------------------------------------
# Challenge 3
# -----------------------------------------------------

print("Challenge 3")

is_admin = False
is_logged_in = True

print("Admin Access:", is_admin)
print("User Access:", not (not is_logged_in))

print("\n---------------------------------\n")

# -----------------------------------------------------
# Bonus Challenge
# -----------------------------------------------------

print("Bonus Challenge")

marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance percentage: "))

print("Eligible:", marks >= 50 and attendance >= 75)

print("\n---------------------------------\n")

print("Congratulations! You have completed Day 08.")