# ========================================================
# Python Journey: Module 3 - Functions
# ========================================================
# This file covers how to define and use functions in Python,
# including parameters, return values, and scope.
# ========================================================

print("=" * 50)
print("Python Functions")
print("=" * 50)

# ------------------------------------------------------
# INTRODUCTION TO FUNCTIONS
# ------------------------------------------------------
# Functions are reusable blocks of code that perform a specific task.
# They help make your code modular, reusable, and easier to understand.
# ------------------------------------------------------

print("\nINTRODUCTION TO FUNCTIONS:")

# A simple function definition
def greet():
    """This function prints a greeting message."""
    print("Hello, World!")

# Calling (executing) the function
print("Calling the greet function:")
greet()

# Function with a docstring (documentation string)
# The triple-quoted comment after the function header is a docstring.
# It documents what the function does and helps other developers
# understand your code.
def explain_functions():
    """
    This function explains what functions are and why they're useful.
    
    Docstrings like this one can be multi-line and provide detailed
    documentation about how to use the function.
    """
    print("Functions are reusable blocks of code.")
    print("They help you organize code and avoid repetition.")
    print("This makes your programs easier to understand and maintain.")

print("\nCalling the explain_functions function:")
explain_functions()

# ------------------------------------------------------
# FUNCTIONS WITH PARAMETERS
# ------------------------------------------------------
# Functions can accept parameters (inputs) that allow them
# to operate on different data each time they're called.
# ------------------------------------------------------

print("\nFUNCTIONS WITH PARAMETERS:")

# Function with one parameter
def greet_person(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello, {name}!")

print("\nCalling greet_person with different arguments:")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def describe_pet(name, species):
    """
    Describe a pet.
    
    Args:
        name (str): The pet's name
        species (str): The type of animal
    """
    print(f"{name} is a {species}.")

print("\nCalling describe_pet with different arguments:")
describe_pet("Fido", "dog")
describe_pet("Whiskers", "cat")

# Function with default parameter values
def greet_with_message(name, message="Hope you're having a great day!"):
    """
    Greet a person with a custom message.
    
    Args:
        name (str): The name of the person to greet
        message (str, optional): The message to include in the greeting.
                                Defaults to "Hope you're having a great day!".
    """
    print(f"Hello, {name}! {message}")

print("\nCalling greet_with_message with and without the optional parameter:")
greet_with_message("Charlie")  # Uses default message
greet_with_message("David", "Welcome to Python!")  # Custom message

# Named arguments (keyword arguments)
print("\nUsing named arguments:")
describe_pet(species="goldfish", name="Bubbles")  # Order doesn't matter with named arguments

# ------------------------------------------------------
# RETURN VALUES
# ------------------------------------------------------
# Functions can return values that can be used elsewhere in your code.
# A function can return a single value, multiple values, or nothing at all.
# ------------------------------------------------------

print("\nRETURN VALUES:")

# Function that returns a single value
def square(number):
    """
    Calculate the square of a number.
    
    Args:
        number (float): The number to square
        
    Returns:
        float: The square of the input number
    """
    return number * number

# Using the returned value
result = square(5)
print(f"The square of 5 is {result}")

# Using the returned value directly in an expression
print(f"The square of 3 plus the square of 4 is {square(3) + square(4)}")

# Function that returns multiple values
def get_dimensions(radius):
    """
    Calculate various dimensions of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        tuple: (diameter, circumference, area)
    """
    diameter = radius * 2
    from math import pi
    circumference = 2 * pi * radius
    area = pi * radius * radius
    return diameter, circumference, area

# Unpacking multiple return values into variables
diameter, circumference, area = get_dimensions(5)
print("\nFor a circle with radius 5:")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")

# Function with conditional return
def get_grade(score):
    """
    Convert a numerical score to a letter grade.
    
    Args:
        score (float): The numerical score (0-100)
        
    Returns:
        str: The letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("\nGrades for different scores:")
print(f"Score of 95: {get_grade(95)}")
print(f"Score of 85: {get_grade(85)}")
print(f"Score of 65: {get_grade(65)}")
print(f"Score of 55: {get_grade(55)}")

# ------------------------------------------------------
# SCOPE AND VARIABLE VISIBILITY
# ------------------------------------------------------
# The scope of a variable determines where in your code
# the variable can be accessed. Python has local and global scope.
# ------------------------------------------------------

print("\nSCOPE AND VARIABLE VISIBILITY:")

# Global variable (defined outside any function)
message = "This is a global variable"

def print_message():
    """Print the global message variable."""
    print(message)  # This function can access the global variable

def create_local_variable():
    """Create and print a local variable."""
    local_message = "This is a local variable"  # Local to this function
    print(local_message)

def modify_global_incorrectly():
    """Try to modify a global variable without using 'global' keyword."""
    # This creates a new local variable, not modifying the global one
    message = "Attempted modification"
    print(f"Inside function: {message}")

def modify_global_correctly():
    """Modify a global variable using the 'global' keyword."""
    global message
    original = message
    message = "Modified global variable"
    print(f"Changed from '{original}' to '{message}'")

print("\nDemonstrating variable scope:")
print(f"Global message: {message}")
print("\nCalling print_message():")
print_message()

print("\nCalling create_local_variable():")
create_local_variable()
# print(local_message)  # This would cause an error because local_message is not visible here

print("\nCalling modify_global_incorrectly():")
modify_global_incorrectly()
print(f"Global message after incorrect attempt: {message}")  # Unchanged

print("\nCalling modify_global_correctly():")
modify_global_correctly()
print(f"Global message after correct modification: {message}")  # Changed

# ------------------------------------------------------
# FUNCTIONS AS FIRST-CLASS OBJECTS
# ------------------------------------------------------
# In Python, functions are "first-class citizens," which means
# they can be passed as arguments, returned from other functions,
# and assigned to variables.
# ------------------------------------------------------

print("\nFUNCTIONS AS FIRST-CLASS OBJECTS:")

# Assigning a function to a variable
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

print("\nAssigning functions to variables:")
operation = add  # Note: No parentheses, we're assigning the function itself, not calling it
print(f"Result of operation(5, 3) using add: {operation(5, 3)}")

operation = subtract
print(f"Result of operation(5, 3) using subtract: {operation(5, 3)}")

# Passing functions as arguments
def apply_operation(func, a, b):
    """
    Apply a function to two numbers.
    
    Args:
        func (function): A function that takes two arguments
        a (number): First number
        b (number): Second number
        
    Returns:
        The result of calling func(a, b)
    """
    return func(a, b)

print("\nPassing functions as arguments:")
print(f"apply_operation(add, 5, 3): {apply_operation(add, 5, 3)}")
print(f"apply_operation(subtract, 5, 3): {apply_operation(subtract, 5, 3)}")

# ------------------------------------------------------
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ------------------------------------------------------
# Lambda functions are small, anonymous functions defined with
# the 'lambda' keyword. They can take any number of arguments
# but can only have one expression.
# ------------------------------------------------------

print("\nLAMBDA FUNCTIONS:")

# Basic lambda function
print("\nBasic lambda function:")
square_lambda = lambda x: x * x
print(f"square_lambda(5): {square_lambda(5)}")

# Equivalent to:
# def square_lambda(x):
#     return x * x

# Lambda with multiple parameters
print("\nLambda with multiple parameters:")
sum_lambda = lambda a, b: a + b
print(f"sum_lambda(10, 20): {sum_lambda(10, 20)}")

# Using lambda with built-in functions
numbers = [1, 5, 3, 9, 7, 2, 8]
print(f"\nOriginal list: {numbers}")

sorted_numbers = sorted(numbers)
print(f"Sorted normally: {sorted_numbers}")

# Sort a list of numbers by their squared values
sorted_by_square = sorted(numbers, key=lambda x: x * x)
print(f"Sorted by square value: {sorted_by_square}")

# ------------------------------------------------------
# EXERCISE: FUNCTION CREATOR
# ------------------------------------------------------
# Practice writing functions with this exercise.
#
# Instructions:
# 1. Uncomment the code below
# 2. Implement the requested functions
# 3. Run the file to see your results
# ------------------------------------------------------

print("\n--- EXERCISE: FUNCTION CREATOR ---")

# # Exercise 1: Create a function that takes a temperature in Celsius
# # and returns the equivalent in Fahrenheit.
# # Formula: F = C * 9/5 + 32
# def celsius_to_fahrenheit(celsius):
#     """
#     Convert Celsius to Fahrenheit.
#     
#     Args:
#         celsius (float): Temperature in Celsius
#         
#     Returns:
#         float: Temperature in Fahrenheit
#     """
#     # Your code here
#     pass  # Replace this with your code
# 
# # Test your function
# print(f"0°C = {celsius_to_fahrenheit(0)}°F")
# print(f"100°C = {celsius_to_fahrenheit(100)}°F")
# print(f"37°C = {celsius_to_fahrenheit(37)}°F")
# 
# # Exercise 2: Create a function that counts the number of vowels in a string.
# # For extra challenge, make it case-insensitive.
# def count_vowels(text):
#     """
#     Count the number of vowels (a, e, i, o, u) in a string.
#     
#     Args:
#         text (str): The string to check
#         
#     Returns:
#         int: The number of vowels in the string
#     """
#     # Your code here
#     pass  # Replace this with your code
# 
# # Test your function
# print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
# print(f"Vowels in 'Python Programming': {count_vowels('Python Programming')}")
# 
# # Exercise 3: Create a function that generates the first n numbers
# # in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, ...)
# def fibonacci_sequence(n):
#     """
#     Generate the first n numbers in the Fibonacci sequence.
#     
#     Args:
#         n (int): How many Fibonacci numbers to generate
#         
#     Returns:
#         list: The first n Fibonacci numbers
#     """
#     # Your code here
#     pass  # Replace this with your code
# 
# # Test your function
# print(f"First 10 Fibonacci numbers: {fibonacci_sequence(10)}")

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: FUNCTION FANATIC 🏆")
print("You've mastered creating and using functions in Python!")
print("=" * 50)

print("\nWhat's next? Continue to 07_mini_project.py")