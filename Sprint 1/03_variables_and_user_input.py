# ========================================================
# Python Journey: Module 1 - Variables and User Input
# ========================================================
# This file covers how to create variables, follow naming 
# conventions, and collect input from users in Python.
# ========================================================

print("=" * 50)
print("Python Variables and User Input")
print("=" * 50)

# ------------------------------------------------------
# VARIABLES IN PYTHON
# ------------------------------------------------------
# Variables are containers for storing data values.
# Unlike some languages, Python has no command for declaring 
# a variable - a variable is created the moment you first 
# assign a value to it.
# ------------------------------------------------------

print("\nVARIABLES IN PYTHON:")

# Creating variables
name = "Alex"  # string variable
age = 30       # integer variable
height = 1.75  # float variable
is_student = True  # boolean variable

# Printing variables and their types
print(f"name: {name} (type: {type(name)})")
print(f"age: {age} (type: {type(age)})")
print(f"height: {height} (type: {type(height)})")
print(f"is_student: {is_student} (type: {type(is_student)})")

# ------------------------------------------------------
# VARIABLE NAMING RULES AND CONVENTIONS
# ------------------------------------------------------
# Rules (must follow):
# - Can contain letters, numbers, and underscores
# - Must start with a letter or underscore
# - Cannot start with a number
# - Cannot use reserved Python keywords (like 'if', 'for', 'while')
# - Case-sensitive (age, Age, and AGE are three different variables)
#
# Conventions (good practice):
# - Use lowercase for simple variables
# - Use underscores for multi-word variables (snake_case)
# - Use meaningful names that describe the data
# - Avoid single letter names except for simple counters
# ------------------------------------------------------

print("\nVARIABLE NAMING EXAMPLES:")

# Good variable names
user_name = "johndoe"
total_score = 95
is_active = True
item_count = 10

# Examples of what NOT to do (commented out to avoid errors)
# 2nd_place = "Silver"  # Cannot start with a number
# user-name = "johndoe"  # Hyphens not allowed
# class = "Python 101"  # 'class' is a reserved word

print("Good variable name examples:")
print(f"user_name = '{user_name}'")
print(f"total_score = {total_score}")
print(f"is_active = {is_active}")
print(f"item_count = {item_count}")

# ------------------------------------------------------
# CHANGING VARIABLE VALUES
# ------------------------------------------------------
# Variables can be reassigned to store different values
# or updated based on their current value.
# ------------------------------------------------------

print("\nCHANGING VARIABLE VALUES:")

# Reassigning variables
count = 10
print(f"Initial count: {count}")

count = 20  # Completely replacing the old value
print(f"After reassignment: {count}")

# Updating based on current value
count = count + 5  # Add 5 to the current value
print(f"After adding 5: {count}")

# Shorthand operators for updating variables
count += 5  # Same as: count = count + 5
print(f"After += 5: {count}")

count -= 10  # Same as: count = count - 10
print(f"After -= 10: {count}")

count *= 2  # Same as: count = count * 2
print(f"After *= 2: {count}")

count //= 3  # Same as: count = count // 3 (integer division)
print(f"After //= 3: {count}")

# ------------------------------------------------------
# USER INPUT
# ------------------------------------------------------
# The input() function allows your program to receive 
# information from the user during execution.
# ------------------------------------------------------

print("\nUSER INPUT:")
print("Let's try collecting some input from you!\n")

# Basic input example
name_input = input("What is your name? ")
print(f"Hello, {name_input}! Nice to meet you.")

# Input is always stored as a string, even if the user enters a number
age_input = input("How old are you? ")
print(f"You entered: {age_input} (type: {type(age_input)})")

# To use numeric input for calculations, we need to convert it
# Converting string input to integer
try:
    age_number = int(age_input)
    years_to_100 = 100 - age_number
    print(f"You'll be 100 years old in {years_to_100} years.")
except ValueError:
    print("That doesn't seem to be a valid age!")

# Getting numeric input and converting in one step
try:
    height = float(input("What is your height in meters? "))
    print(f"Your height is {height} meters.")
except ValueError:
    print("That doesn't seem to be a valid height!")

# ------------------------------------------------------
# FORMATTED STRINGS (F-STRINGS)
# ------------------------------------------------------
# F-strings provide an easy way to embed expressions inside
# string literals, using curly braces {}
# ------------------------------------------------------

print("\nFORMATTED STRINGS (F-STRINGS):")

user = "Jamie"
score = 95
completion_percent = 0.85

# Basic formatting
print(f"User {user} scored {score} points.")

# Formatting numbers
print(f"Completion percentage: {completion_percent:.1%}")  # As percentage with 1 decimal
print(f"Score: {score:05d}")  # Padded with zeros to 5 digits

# Formatting with calculations
print(f"Half of your score is {score / 2}")

# ------------------------------------------------------
# EXERCISE: PERSONAL INFO COLLECTOR
# ------------------------------------------------------
# Let's practice variables and user input by creating a 
# simple program that collects and displays personal information.
#
# Instructions:
# 1. Collect the user's first name, last name, birth year, and favorite color
# 2. Calculate their approximate age (current year - birth year)
# 3. Format and display all the collected information in a nice summary
# ------------------------------------------------------

print("\n--- EXERCISE: PERSONAL INFO COLLECTOR ---")
print("Uncomment and run the following code:")

# # Get current year (you can replace this with the actual current year)
# current_year = 2025
#
# # Collect user information
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# 
# # Collect and convert birth year
# try:
#     birth_year = int(input("Enter your birth year: "))
#     # Calculate approximate age
#     age = current_year - birth_year
# except ValueError:
#     print("Invalid birth year! Using 0 as age.")
#     age = 0
#
# favorite_color = input("Enter your favorite color: ")
#
# # Display summary with nice formatting
# print("\n" + "=" * 30)
# print(f"| PERSONAL INFORMATION SUMMARY |")
# print("=" * 30)
# print(f"Full Name: {first_name} {last_name}")
# print(f"Age: {age} years old")
# print(f"Favorite Color: {favorite_color}")
# print("=" * 30)

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: VARIABLE VIRTUOSO 🏆")
print("You now know how to work with variables and user input!")
print("=" * 50)

print("\nWhat's next? Continue to 04_control_flow.py")