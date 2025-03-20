# ========================================================
# Python Journey: Module 1 - Introduction to Python
# ========================================================
# This file introduces Python, its applications, and contains
# your very first Python code examples to run.
# ========================================================

# Print a welcome message to the console when this file is run
print("=" * 50)
print("Welcome to Python Journey: Module 1!")
print("Let's start your Python adventure!")
print("=" * 50)

# ------------------------------------------------------
# WHAT IS PYTHON?
# ------------------------------------------------------
# Python is a high-level, interpreted programming language created
# by Guido van Rossum and first released in 1991.
#
# Key features that make Python great:
# - Easy to learn and read (clear, English-like syntax)
# - Versatile (web, data, AI, automation, games, etc.)
# - Large ecosystem of libraries and frameworks
# - Strong community support and documentation
# - Cross-platform (runs on Windows, Mac, Linux)
# ------------------------------------------------------

print("\nWHAT IS PYTHON?")
print("Python is a versatile programming language known for its")
print("readability and simplicity, making it perfect for beginners.")
print("It's used in web development, data science, AI, automation, and more!")

# Your first Python code - displaying text
print("\n--- Your First Python Code ---")
print("Hello, Python world!")

# ------------------------------------------------------
# RUNNING PYTHON CODE
# ------------------------------------------------------
# This file can be run in multiple ways:
# 1. Through a command line: python 01_introduction_to_python.py
# 2. In an IDE like PyCharm, VSCode, or IDLE
# 3. In Google Colab (upload this file and run it)
# 4. By copying the code into a Python interpreter
# ------------------------------------------------------

# ------------------------------------------------------
# APPLICATIONS OF PYTHON
# ------------------------------------------------------
# Python is used across many industries and domains:

print("\nAPPLICATIONS OF PYTHON:")

applications = [
    "Web Development - Django, Flask frameworks",
    "Data Analysis - Pandas, NumPy, Matplotlib",
    "Artificial Intelligence - TensorFlow, PyTorch",
    "Automation - Scripts to simplify repetitive tasks",
    "Game Development - Pygame library",
    "Scientific Computing - SciPy, research tools"
]

# Using a for loop to print each application (we'll learn more about loops later)
for app in applications:
    print("• " + app)

# ------------------------------------------------------
# BASIC PYTHON OPERATIONS
# ------------------------------------------------------
# Let's try some simple operations to demonstrate Python's capabilities

print("\n--- Basic Python Operations ---")

# Mathematical operations
print("2 + 3 =", 2 + 3)  # Addition
print("7 - 4 =", 7 - 4)  # Subtraction
print("2 * 6 =", 2 * 6)  # Multiplication
print("10 / 2 =", 10 / 2)  # Division

# Text operations
print("Combining " + "text " + "with + operator")
print("Repeating text: " + "Python! " * 3)

# ------------------------------------------------------
# EXERCISE: YOUR TURN!
# ------------------------------------------------------
# Try running this file, then modify it to:
# 1. Print your name
# 2. Calculate your age in days (age × 365)
# 3. Print a short message about why you're learning Python
# 
# To complete this exercise:
# 1. Copy the code below
# 2. Replace the placeholders with your information
# 3. Run the file again to see your changes
# ------------------------------------------------------

print("\n--- Your Turn! ---")
# Delete the '#' at the start of the next lines and replace the text in quotes
# print("My name is [YOUR NAME]")
# print("I am approximately", [YOUR AGE] * 365, "days old")
# print("I'm learning Python because [YOUR REASON]")

# ------------------------------------------------------
# ACHIEVEMENT: PYTHON PIONEER
# ------------------------------------------------------
# Congratulations! By running this file, you've taken your first
# step in your Python journey. You've officially earned the
# "Python Pioneer" achievement!
# ------------------------------------------------------

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: PYTHON PIONEER 🏆")
print("You've successfully run your first Python file!")
print("=" * 50)

print("\nWhat's next? Continue to 02_basic_syntax_and_data_types.py")