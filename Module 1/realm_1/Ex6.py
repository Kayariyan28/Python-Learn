# ========================================================
# Python Journey: Module 1 - Functions Exercises
# ========================================================
# Practice exercises for creating and using functions
# ========================================================

print("=" * 60)
print("Python Journey: Functions - Exercises")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Basic Function Definition and Calling
# ------------------------------------------------------
# Practice creating simple functions and calling them
# ------------------------------------------------------

print("\nExercise 1: Basic Function Definition and Calling")
print("-" * 40)

# 1.1: Hello Function
# TODO: Create a function called 'say_hello' that prints "Hello, World!"
# TODO: Call the function
print("1.1: Hello Function")
# Your code here


# 1.2: Personalized Greeting
# TODO: Create a function called 'greet' that takes a name parameter
#       and prints a personalized greeting
# TODO: Call the function with different names
print("\n1.2: Personalized Greeting")
# Your code here


# 1.3: Time of Day Greeting
# TODO: Create a function called 'time_greeting' that takes a name and time of day
#       (morning, afternoon, or evening) and returns an appropriate greeting
# TODO: Print the results of calling this function with different inputs
print("\n1.3: Time of Day Greeting")
# Your code here


# 1.4: Calculator Functions
# TODO: Create four functions: add, subtract, multiply, and divide
#       Each should take two parameters and return the result
# TODO: Call each function with different values and print the results
print("\n1.4: Calculator Functions")
# Your code here


# ------------------------------------------------------
# Exercise 2: Function Parameters and Return Values
# ------------------------------------------------------
# Practice working with different parameter types and return values
# ------------------------------------------------------

print("\nExercise 2: Function Parameters and Return Values")
print("-" * 40)

# 2.1: Default Parameters
# TODO: Create a function called 'power' that takes two parameters: 
#       'base' and 'exponent' (with a default value of 2)
#       It should return base raised to the power of exponent
# TODO: Call the function with and without providing the exponent
print("2.1: Default Parameters")
# Your code here


# 2.2: Multiple Return Values
# TODO: Create a function called 'min_max' that takes a list of numbers
#       and returns both the minimum and maximum values as a tuple
# TODO: Call the function and unpack the returned values
print("\n2.2: Multiple Return Values")
# Your code here


# 2.3: Named Arguments
# TODO: Create a function called 'create_profile' that takes parameters:
#       name, age, occupation, and hobby
# TODO: Call the function using named arguments in different orders
print("\n2.3: Named Arguments")
# Your code here


# 2.4: Flexible Number of Arguments
# TODO: Create a function called 'sum_all' that takes any number of arguments
#       and returns their sum (use *args)
# TODO: Call the function with different numbers of arguments
print("\n2.4: Flexible Number of Arguments")
# Your code here


# 2.5: Keyword Arguments Dictionary
# TODO: Create a function called 'print_info' that takes any number of keyword arguments
#       and prints each key-value pair on a new line (use **kwargs)
# TODO: Call the function with different sets of keyword arguments
print("\n2.5: Keyword Arguments Dictionary")
# Your code here


# ------------------------------------------------------
# Exercise 3: Function Scope and Variable Visibility
# ------------------------------------------------------
# Practice understanding and working with variable scope in functions
# ------------------------------------------------------

print("\nExercise 3: Function Scope and Variable Visibility")
print("-" * 40)

# 3.1: Local and Global Variables
# TODO: Create a global variable 'message'
# TODO: Create a function that creates a local variable with the same name
#       and prints both the local and global variables (use 'global' keyword)
print("3.1: Local and Global Variables")
# Your code here


# 3.2: Modifying Global Variables
# TODO: Create a global counter variable
# TODO: Create a function that increments the counter
# TODO: Call the function multiple times and print the counter after each call
print("\n3.2: Modifying Global Variables")
# Your code here


# 3.3: Shadowing
# TODO: Create a variable 'value'
# TODO: Create a function that has a parameter also called 'value'
#       and prints both the parameter and the global variable
print("\n3.3: Shadowing")
# Your code here


# 3.4: Nested Functions and Scope
# TODO: Create a function with a local variable and a nested function
#       that accesses and modifies the local variable of the outer function
print("\n3.4: Nested Functions and Scope")
# Your code here


# ------------------------------------------------------
# Exercise 4: Lambda Functions
# ------------------------------------------------------
# Practice creating and using anonymous lambda functions
# ------------------------------------------------------

print("\nExercise 4: Lambda Functions")
print("-" * 40)

# 4.1: Basic Lambda
# TODO: Create a lambda function that takes a number and returns its square
# TODO: Use the lambda function with different values
print("4.1: Basic Lambda")
# Your code here


# 4.2: Lambda with Filter
# TODO: Create a list of numbers
# TODO: Use filter() with a lambda to keep only the even numbers
print("\n4.2: Lambda with Filter")
# Your code here


# 4.3: Lambda with Map
# TODO: Create a list of names
# TODO: Use map() with a lambda to convert each name to uppercase
print("\n4.3: Lambda with Map")
# Your code here


# 4.4: Lambda with Sort
# TODO: Create a list of tuples, each containing a name and an age
# TODO: Use sorted() with a lambda key function to sort the list by age
print("\n4.4: Lambda with Sort")
# Your code here


# ------------------------------------------------------
# Exercise 5: Functions as First-Class Objects
# ------------------------------------------------------
# Practice using functions as objects: passing them as arguments and
# returning them from other functions
# ------------------------------------------------------

print("\nExercise 5: Functions as First-Class Objects")
print("-" * 40)

# 5.1: Passing Functions as Arguments
# TODO: Create a function 'apply' that takes a function and a value
#       and returns the result of applying the function to the value
# TODO: Use this 'apply' function with different functions
print("5.1: Passing Functions as Arguments")
# Your code here


# 5.2: Returning Functions
# TODO: Create a function 'create_multiplier' that takes a number 'n'
#       and returns a function that multiplies its argument by 'n'
# TODO: Create a doubler and tripler using this function
print("\n5.2: Returning Functions")
# Your code here


# 5.3: Function Composition
# TODO: Create a function 'compose' that takes two functions f and g
#       and returns a function that computes f(g(x))
# TODO: Use this to compose some simple functions
print("\n5.3: Function Composition")
# Your code here


# ------------------------------------------------------
# Exercise 6: Recursive Functions
# ------------------------------------------------------
# Practice creating functions that call themselves
# ------------------------------------------------------

print("\nExercise 6: Recursive Functions")
print("-" * 40)

# 6.1: Factorial with Recursion
# TODO: Create a recursive function to calculate the factorial of a number
# TODO: Test it with different inputs
print("6.1: Factorial with Recursion")
# Your code here


# 6.2: Fibonacci with Recursion
# TODO: Create a recursive function to calculate the nth Fibonacci number
# TODO: Test it with different inputs
print("\n6.2: Fibonacci with Recursion")
# Your code here


# 6.3: Sum of Digits with Recursion
# TODO: Create a recursive function that calculates the sum of the digits of a number
# TODO: Test it with different inputs
print("\n6.3: Sum of Digits with Recursion")
# Your code here


# ------------------------------------------------------
# Exercise 7: Mini Project - Calculator Library
# ------------------------------------------------------
# Create a collection of functions for a calculator application
# ------------------------------------------------------

print("\nExercise 7: Mini Project - Calculator Library")
print("-" * 40)

# TODO: Create a module of calculator functions with the following features:
#       1. Basic operations (add, subtract, multiply, divide)
#       2. Advanced operations (power, square root, absolute value)
#       3. Memory functions (store value, recall value, clear memory)
#       4. Conversion functions (decimal to binary, binary to decimal)
#       5. A history feature that records the last 5 operations
#       6. A main function that provides a simple user interface to use these functions
#
#       Make sure to use docstrings to document each function!

print("7: Calculator Library")
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

Exercise 1: Basic Function Definition and Calling
[ ] 1.1: Hello Function
[ ] 1.2: Personalized Greeting
[ ] 1.3: Time of Day Greeting
[ ] 1.4: Calculator Functions

Exercise 2: Function Parameters and Return Values
[ ] 2.1: Default Parameters
[ ] 2.2: Multiple Return Values
[ ] 2.3: Named Arguments
[ ] 2.4: Flexible Number of Arguments
[ ] 2.5: Keyword Arguments Dictionary

Exercise 3: Function Scope and Variable Visibility
[ ] 3.1: Local and Global Variables
[ ] 3.2: Modifying Global Variables
[ ] 3.3: Shadowing
[ ] 3.4: Nested Functions and Scope

Exercise 4: Lambda Functions
[ ] 4.1: Basic Lambda
[ ] 4.2: Lambda with Filter
[ ] 4.3: Lambda with Map
[ ] 4.4: Lambda with Sort

Exercise 5: Functions as First-Class Objects
[ ] 5.1: Passing Functions as Arguments
[ ] 5.2: Returning Functions
[ ] 5.3: Function Composition

Exercise 6: Recursive Functions
[ ] 6.1: Factorial with Recursion
[ ] 6.2: Fibonacci with Recursion
[ ] 6.3: Sum of Digits with Recursion

Exercise 7: Mini Project
[ ] Calculator Library

Progress: [_____] 0% complete
""")