# ========================================================
# Python Journey: Module 1 - Basic Syntax and Data Types Exercises
# ========================================================
# Practice exercises for Python syntax and fundamental data types
# ========================================================

print("=" * 60)
print("Python Journey: Basic Syntax and Data Types - Exercises")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Working with Integers and Floats
# ------------------------------------------------------
# Complete the following exercises involving number operations
# ------------------------------------------------------

print("\nExercise 1: Working with Integers and Floats")
print("-" * 40)

# 1.1: Calculate the area of a rectangle with length 7.5 and width 3.2
# TODO: Write code to calculate and print the area
print("1.1: Area of rectangle with length 7.5 and width 3.2")
# Your code here


# 1.2: Convert temperature from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
# TODO: Convert 27 degrees Celsius to Fahrenheit
print("\n1.2: Convert 27 degrees Celsius to Fahrenheit")
# Your code here


# 1.3: Calculate how many whole slices can be obtained from 3 pizzas if each pizza 
# has 8 slices and 5 people want to have an equal number of slices
# TODO: Calculate and print the number of slices each person gets, and how many slices remain
print("\n1.3: Pizza slicing problem")
# Your code here


# 1.4: Use the modulo operator to check if a number is odd or even
# TODO: Check if 42 is odd or even
# TODO: Check if 97 is odd or even
print("\n1.4: Check if numbers are odd or even")
# Your code here


# ------------------------------------------------------
# Exercise 2: String Operations
# ------------------------------------------------------
# Practice different operations with strings
# ------------------------------------------------------

print("\nExercise 2: String Operations")
print("-" * 40)

# 2.1: Create a string containing your first and last name, then extract and 
# print your initials (first letter of first name and first letter of last name)
print("2.1: Extract initials from your name")
# Your code here


# 2.2: Take the sentence below and print it with all letters in:
# a) ALL CAPS
# b) lowercase
# c) Title Case (First Letter Of Each Word Capitalized)
original_sentence = "Python programming is fun and powerful."
print("\n2.2: Change case of sentence")
print(f"Original: {original_sentence}")
# Your code here


# 2.3: Create a string containing a 10-digit phone number (no spaces/dashes)
# Then use string slicing to print it in the format: (XXX) XXX-XXXX
print("\n2.3: Format a phone number")
# Your code here


# 2.4: Fix the typos in the following sentence using string replacement
typo_sentence = "Pythom is a populer progamming lnguage for begimners."
print("\n2.4: Fix the typos")
print(f"With typos: {typo_sentence}")
# Your code here


# ------------------------------------------------------
# Exercise 3: Boolean Logic and Comparison
# ------------------------------------------------------
# Practice working with boolean values and expressions
# ------------------------------------------------------

print("\nExercise 3: Boolean Logic and Comparison")
print("-" * 40)

# 3.1: Create two boolean variables and demonstrate the AND, OR, and NOT operations with them
print("3.1: Boolean operations")
# Your code here


# 3.2: Write expressions to check if:
# a) A number is between 10 and 20 (inclusive)
# b) A number is either less than 0 or greater than 100
# Test your expressions with different numbers
print("\n3.2: Comparison operations")
# Your code here


# 3.3: Create a complex boolean expression that combines at least 3 conditions using AND, OR, and parentheses
# For example, check if a number is divisible by 2 OR (divisible by 3 AND greater than 10)
print("\n3.3: Complex boolean expression")
# Your code here


# ------------------------------------------------------
# Exercise 4: Type Conversion
# ------------------------------------------------------
# Practice converting between different data types
# ------------------------------------------------------

print("\nExercise 4: Type Conversion")
print("-" * 40)

# 4.1: Convert the following strings to integers and perform a calculation
num_string1 = "42"
num_string2 = "73"
print("4.1: Convert strings to integers")
# Your code here


# 4.2: Convert the following strings to floats and perform a calculation
float_string1 = "3.14159"
float_string2 = "2.71828"
print("\n4.2: Convert strings to floats")
# Your code here


# 4.3: Convert the following float to an integer in two ways:
# a) By simple type conversion (which truncates the decimal part)
# b) By rounding to the nearest integer
pi_value = 3.14159
print("\n4.3: Convert float to integer")
# Your code here


# 4.4: Convert various data types to boolean values
# Try converting integers (including 0), strings (including empty string), and None to boolean
print("\n4.4: Convert to boolean values")
# Your code here


# 4.5: Safely convert user input to numbers
# Write code that tries to convert the following to a number, but handles the error if it's not convertible
test_input1 = "42"  # Should work
test_input2 = "3.14159"  # Should work
test_input3 = "hello"  # Should detect and handle this error
print("\n4.5: Safely convert to numbers")
# Your code here


# ------------------------------------------------------
# Bonus Challenge: String Formatting
# ------------------------------------------------------

print("\nBonus Challenge: String Formatting")
print("-" * 40)

# Create formatted output that displays the following data in a nice table:
# Product name, price, and quantity for 3 products

product1_name = "Laptop"
product1_price = 1299.99
product1_quantity = 5

product2_name = "Phone"
product2_price = 799.50
product2_quantity = 12

product3_name = "Headphones"
product3_price = 49.99
product3_quantity = 25

# TODO: Print a formatted table with headers and alignment
print("Bonus: Format product table")
# Your code here


# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------
# Track your progress by checking off completed exercises
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each exercise as you complete it:

Exercise 1: Working with Integers and Floats
[ ] 1.1: Calculate rectangle area
[ ] 1.2: Convert Celsius to Fahrenheit
[ ] 1.3: Pizza slicing problem
[ ] 1.4: Check odd or even numbers

Exercise 2: String Operations
[ ] 2.1: Extract initials
[ ] 2.2: Change string case
[ ] 2.3: Format phone number
[ ] 2.4: Fix typos in a sentence

Exercise 3: Boolean Logic and Comparison
[ ] 3.1: Basic boolean operations
[ ] 3.2: Comparison expressions
[ ] 3.3: Complex boolean expression

Exercise 4: Type Conversion
[ ] 4.1: Convert strings to integers
[ ] 4.2: Convert strings to floats
[ ] 4.3: Convert float to integer (two ways)
[ ] 4.4: Convert to boolean values
[ ] 4.5: Safely convert user input

Bonus Challenge:
[ ] String formatting table

Progress: [_____] 0% complete
""")