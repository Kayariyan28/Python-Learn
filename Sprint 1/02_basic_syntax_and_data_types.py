# ========================================================
# Python Journey: Module 1 - Basic Syntax and Data Types
# ========================================================
# This file covers Python's basic syntax rules and
# fundamental data types: integers, floats, strings, and booleans.
# ========================================================

print("=" * 50)
print("Python Basic Syntax and Data Types")
print("=" * 50)

# ------------------------------------------------------
# PYTHON SYNTAX BASICS
# ------------------------------------------------------
# Python has a few key syntax rules:
#
# 1. Indentation matters! Python uses indentation (spaces or tabs) 
#    to define code blocks instead of braces {} like other languages
#
# 2. Comments start with a '#' symbol and are ignored when the code runs
#
# 3. Statements typically go on separate lines (no semicolons needed)
#
# 4. Python is case-sensitive (variable, VARIABLE, and Variable are different)
# ------------------------------------------------------

print("\nPYTHON SYNTAX EXAMPLES:")

# Example 1: Indentation (we'll see more when we cover control flow)
print("Example of code with proper indentation:")
print("if True:")
print("    print('Indented code runs if condition is True')")
print("    print('This line is in the same block')")
print("print('This line runs regardless')")

# Example 2: Line separation
print("\nExample of multiple statements:")
print("statement_1")  # This is one statement
print("statement_2")  # This is another statement

# ------------------------------------------------------
# DATA TYPES: NUMBERS (INTEGERS & FLOATS)
# ------------------------------------------------------
# Python has several number types, the two most common are:
# - Integers (int): Whole numbers without decimal points
# - Floating point (float): Numbers with decimal points
# ------------------------------------------------------

print("\nNUMBER TYPES IN PYTHON:")

# Integers - whole numbers
age = 25
temperature_celsius = -10
population = 7900000000

# Floats - decimal numbers
height = 1.75
pi_approximate = 3.14159
average_score = 85.5

print(f"Example integer: {age} (type: {type(age)})")
print(f"Example float: {height} (type: {type(height)})")

# Number operations
print("\nBASIC NUMBER OPERATIONS:")
print(f"Addition: 5 + 3 = {5 + 3}")
print(f"Subtraction: 10 - 4 = {10 - 4}")
print(f"Multiplication: 6 * 7 = {6 * 7}")
print(f"Division: 20 / 4 = {20 / 4}")  # Always returns a float
print(f"Integer Division: 20 // 4 = {20 // 4}")  # Returns an integer (truncated)
print(f"Modulus (remainder): 10 % 3 = {10 % 3}")
print(f"Exponentiation: 2 ** 3 = {2 ** 3}")  # 2 raised to power 3

# Converting between number types
integer_number = 42
float_number = float(integer_number)  # Convert to float: 42.0
print(f"\nConverting int to float: {integer_number} → {float_number}")

pi_float = 3.14159
pi_integer = int(pi_float)  # Convert to integer (truncates): 3
print(f"Converting float to int: {pi_float} → {pi_integer} (decimal part is lost)")

# ------------------------------------------------------
# DATA TYPES: STRINGS
# ------------------------------------------------------
# Strings are sequences of characters, used to represent text.
# They can be defined with single quotes ('text') or double quotes ("text").
# ------------------------------------------------------

print("\nSTRINGS IN PYTHON:")

# Creating strings
name = "Alice"
greeting = 'Hello, World!'
multi_line = """This string
spans multiple
lines."""

print(f"Example string: {name} (type: {type(name)})")

# String operations
print("\nBASIC STRING OPERATIONS:")
# Concatenation (combining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Concatenation: {first_name} + ' ' + {last_name} = {full_name}")

# String repetition
cheer = "Hip Hip Hooray! "
print(f"Repetition: '{cheer}' * 3 = '{cheer * 3}'")

# String length
message = "Hello, Python!"
print(f"Length of '{message}' = {len(message)} characters")

# Accessing characters (indexing)
print(f"First character of '{message}' = '{message[0]}'")
print(f"Fifth character of '{message}' = '{message[4]}'")
print(f"Last character of '{message}' = '{message[-1]}'")

# String slicing (getting a substring)
print(f"Characters 0-4 of '{message}' = '{message[0:5]}'")
print(f"From 7th to end of '{message}' = '{message[7:]}'")

# Common string methods
print(f"\nUpper case: '{message.upper()}'")
print(f"Lower case: '{message.lower()}'")
print(f"Replace: '{message.replace('Python', 'World')}'")
print(f"Split by comma: {message.split(',')}")
print(f"Count 'o': {message.count('o')}")

# ------------------------------------------------------
# DATA TYPES: BOOLEANS
# ------------------------------------------------------
# Booleans represent one of two values: True or False
# They're essential for making decisions in code
# ------------------------------------------------------

print("\nBOOLEANS IN PYTHON:")

is_python_fun = True
is_coding_hard = False

print(f"Example boolean: {is_python_fun} (type: {type(is_python_fun)})")

# Boolean operations
print("\nBASIC BOOLEAN OPERATIONS:")
a = True
b = False
print(f"Logical AND: {a} and {b} = {a and b}")
print(f"Logical OR: {a} or {b} = {a or b}")
print(f"Logical NOT: not True = {not True}")

# Comparison operators (return boolean results)
print("\nCOMPARISON OPERATORS:")
a = 5
b = 10
print(f"{a} > {b} is {a > b}")  # Greater than
print(f"{a} < {b} is {a < b}")  # Less than
print(f"{a} == {b} is {a == b}")  # Equal to
print(f"{a} != {b} is {a != b}")  # Not equal to
print(f"{a} >= {b} is {a >= b}")  # Greater than or equal to
print(f"{a} <= {b} is {a <= b}")  # Less than or equal to

# ------------------------------------------------------
# TYPE CONVERSION
# ------------------------------------------------------
# Python allows you to convert between different data types
# ------------------------------------------------------

print("\nTYPE CONVERSION EXAMPLES:")

# String to number
age_str = "25"
age_int = int(age_str)
print(f"String to integer: '{age_str}' → {age_int} ({type(age_int)})")

# Number to string
score = 95
score_str = str(score)
print(f"Integer to string: {score} → '{score_str}' ({type(score_str)})")

# Check if a string can be converted to a number
numeric_string = "42"
non_numeric_string = "hello"

# Using isdigit() to check if the string is a number
print(f"Is '{numeric_string}' a digit? {numeric_string.isdigit()}")
print(f"Is '{non_numeric_string}' a digit? {non_numeric_string.isdigit()}")

# ------------------------------------------------------
# EXERCISE: TYPE EXPLORER
# ------------------------------------------------------
# Complete the following exercises to practice working with data types:
#
# 1. Create a string and print its length
# 2. Create two numbers and print their sum, difference, product, and quotient
# 3. Create a boolean by comparing two numbers
# 4. Convert a number to a string and concatenate it with another string
# ------------------------------------------------------

print("\n--- EXERCISES: TYPE EXPLORER ---")
print("Uncomment the following code and complete the exercises:")

# # Exercise 1: Create a string and print its length
# my_string = "Replace this with your own text"
# print(f"My string: '{my_string}'")
# print(f"Length: {len(my_string)} characters")
#
# # Exercise 2: Number operations
# num1 = 10  # Replace with your choice
# num2 = 5   # Replace with your choice
# print(f"Sum: {num1} + {num2} = {num1 + num2}")
# print(f"Difference: {num1} - {num2} = {num1 - num2}")
# print(f"Product: {num1} * {num2} = {num1 * num2}")
# print(f"Quotient: {num1} / {num2} = {num1 / num2}")
#
# # Exercise 3: Create a boolean by comparing numbers
# comparison_result = num1 > num2  # Try different comparisons
# print(f"{num1} > {num2} is {comparison_result}")
#
# # Exercise 4: Convert and concatenate
# favorite_number = 7  # Replace with your favorite number
# favorite_number_str = str(favorite_number)
# print("My favorite number is " + favorite_number_str)

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: DATA TYPE MASTER 🏆")
print("You've learned about Python's fundamental data types!")
print("=" * 50)

print("\nWhat's next? Continue to 03_variables_and_user_input.py")