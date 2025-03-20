# ========================================================
# Python Journey: Module 1 - Variables and User Input Exercises
# ========================================================
# Practice exercises for variables and user interaction
# ========================================================

print("=" * 60)
print("Python Journey: Variables and User Input - Exercises")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Variable Creation and Naming
# ------------------------------------------------------
# Practice creating variables with appropriate names
# ------------------------------------------------------

print("\nExercise 1: Variable Creation and Naming")
print("-" * 40)

# 1.1: Create variables for a person's profile
# TODO: Create variables for: full name, age, height (in meters), is_student (boolean)
# Use appropriate variable names and data types
print("1.1: Create variables for a person's profile")
# Your code here


# 1.2: Create variables for a car's specifications
# TODO: Create variables for: make, model, year, engine_size, is_electric, fuel_efficiency
print("\n1.2: Create variables for a car's specifications")
# Your code here


# 1.3: Create variables related to a circle
# TODO: Create variables for: radius, diameter, circumference, area
# Use the value 5 for the radius and calculate the rest
# For pi, use 3.14159
print("\n1.3: Create variables related to a circle")
# Your code here


# 1.4: Fix the invalid variable names
# TODO: Correct the variable names below by making them valid Python identifiers
# Uncomment each line after you fix it

# 1st_place = "Gold"
# user-name = "JohnDoe"
# class = "Python 101"
# average$ = 75.5
# for = "loop keyword"
print("\n1.4: Fix invalid variable names")
# Your fixed variable declarations here


# ------------------------------------------------------
# Exercise 2: Variable Operations and Updates
# ------------------------------------------------------
# Practice operating on variables and updating their values
# ------------------------------------------------------

print("\nExercise 2: Variable Operations and Updates")
print("-" * 40)

# 2.1: Score calculation
# TODO: Create a variable for a game score starting at 0
# TODO: Update it using different operations:
#       - Add 10 points
#       - Add 5 more points
#       - Double the score
#       - Subtract 7 points
#       Print the score after each update
print("2.1: Score calculation")
# Your code here


# 2.2: Shopping cart
# TODO: Create variables for:
#       - item_price (a single item's price)
#       - quantity (number of items)
#       - discount_percentage
#       - tax_rate
# TODO: Calculate the final price after discount and tax
print("\n2.2: Shopping cart calculation")
# Your code here


# 2.3: Swapping variables
# TODO: Create two variables, a and b, with different values
# TODO: Swap their values (without using a third variable)
print("\n2.3: Swapping variables")
# Your code here


# 2.4: Create a "mad libs" sentence
# TODO: Create variables for parts of speech (noun, verb, adjective, etc.)
# TODO: Create a sentence using those variables with string formatting
print("\n2.4: Mad libs sentence")
# Your code here


# ------------------------------------------------------
# Exercise 3: Getting User Input
# ------------------------------------------------------
# Practice obtaining input from users
# ------------------------------------------------------

print("\nExercise 3: Getting User Input")
print("-" * 40)

# 3.1: Basic information collector
# TODO: Ask for and store the user's name, age, and favorite color
# TODO: Print a summary using the collected information
print("3.1: Basic information collector")
# Your code here


# 3.2: Calculator
# TODO: Ask the user for two numbers
# TODO: Perform and display: addition, subtraction, multiplication, and division
print("\n3.2: Simple calculator")
# Your code here


# 3.3: Temperature converter
# TODO: Ask the user for a temperature in Fahrenheit
# TODO: Convert it to Celsius (C = (F - 32) * 5/9)
# TODO: Display the result with proper formatting
print("\n3.3: Temperature converter")
# Your code here


# 3.4: Age calculator
# TODO: Ask the user for their birth year
# TODO: Calculate and display their approximate age
# TODO: Handle potential errors (non-numeric input, future years)
print("\n3.4: Age calculator")
# Your code here


# ------------------------------------------------------
# Exercise 4: String Formatting
# ------------------------------------------------------
# Practice formatting strings with variables
# ------------------------------------------------------

print("\nExercise 4: String Formatting")
print("-" * 40)

# 4.1: Format a greeting using variables and f-strings
# TODO: Create variables for name and time_of_day
# TODO: Create a greeting that varies based on the time of day
print("4.1: Formatted greeting")
# Your code here


# 4.2: Format a receipt
# TODO: Create variables for: store_name, item, quantity, price
# TODO: Format a receipt with aligned columns and currency formatting
print("\n4.2: Formatted receipt")
# Your code here


# 4.3: Format a progress display
# TODO: Create variables for: task_name, progress_percentage
# TODO: Create a progress bar like: "Downloading: [####    ] 40%"
# TODO: The number of # should reflect the progress percentage
print("\n4.3: Formatted progress bar")
# Your code here


# ------------------------------------------------------
# Exercise 5: Mini Project - Personal Data Form
# ------------------------------------------------------
# Combine variables and user input in a larger program
# ------------------------------------------------------

print("\nExercise 5: Mini Project - Personal Data Form")
print("-" * 40)

# TODO: Create a program that:
#       1. Asks the user for personal information:
#          - Full name
#          - Age
#          - Height (in cm)
#          - Weight (in kg)
#          - Occupation
#       2. Calculates:
#          - BMI (Body Mass Index): weight(kg) / height(m)²
#          - Birth year (approximate)
#          - Retirement year (assuming retirement at age 65)
#       3. Formats and displays all the collected and calculated information
#          in a nice, organized way
#       4. Handle potential errors in the input

print("5: Personal data form")
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

Exercise 1: Variable Creation and Naming
[ ] 1.1: Person's profile variables
[ ] 1.2: Car specification variables
[ ] 1.3: Circle-related variables
[ ] 1.4: Fix invalid variable names

Exercise 2: Variable Operations and Updates
[ ] 2.1: Score calculation
[ ] 2.2: Shopping cart calculation
[ ] 2.3: Swapping variables
[ ] 2.4: Mad libs sentence

Exercise 3: Getting User Input
[ ] 3.1: Basic information collector
[ ] 3.2: Simple calculator
[ ] 3.3: Temperature converter
[ ] 3.4: Age calculator

Exercise 4: String Formatting
[ ] 4.1: Formatted greeting
[ ] 4.2: Formatted receipt
[ ] 4.3: Formatted progress bar

Exercise 5: Mini Project
[ ] Personal data form

Progress: [_____] 0% complete
""")