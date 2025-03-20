# ========================================================
# Python Journey: Module 1 - Control Flow Exercises
# ========================================================
# Practice exercises for conditional statements and loops
# ========================================================

print("=" * 60)
print("Python Journey: Control Flow - Exercises")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Conditional Statements (if, elif, else)
# ------------------------------------------------------
# Practice making decisions in your code
# ------------------------------------------------------

print("\nExercise 1: Conditional Statements")
print("-" * 40)

# 1.1: Grade Classifier
# TODO: Write a program that asks for a numerical grade (0-100)
#       and prints the corresponding letter grade according to:
#       A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
#       Also handle invalid inputs (negative numbers or above 100)
print("1.1: Grade Classifier")
# Your code here


# 1.2: Leap Year Checker
# TODO: Write a program that checks if a given year is a leap year
#       A leap year is divisible by 4, but not by 100 unless it's also divisible by 400
#       Test with years: 1900, 2000, 2020, 2023, 2024
print("\n1.2: Leap Year Checker")
# Your code here


# 1.3: Number Analyzer
# TODO: Write a program that takes a number and prints:
#       - Whether it's positive, negative, or zero
#       - Whether it's even or odd
#       - Whether it's a multiple of 5
#       - Whether it's a prime number
print("\n1.3: Number Analyzer")
# Your code here


# 1.4: Rock, Paper, Scissors Game
# TODO: Create a simple rock-paper-scissors game where:
#       - The user enters their choice (rock, paper, or scissors)
#       - The computer's choice is hardcoded (you choose what the computer plays)
#       - The program determines and announces the winner
print("\n1.4: Rock, Paper, Scissors Game")
# Your code here


# ------------------------------------------------------
# Exercise 2: For Loops
# ------------------------------------------------------
# Practice repeating actions using for loops
# ------------------------------------------------------

print("\nExercise 2: For Loops")
print("-" * 40)

# 2.1: Number Summation
# TODO: Write a program that calculates the sum of all numbers from 1 to n
#       where n is provided by the user
print("2.1: Number Summation")
# Your code here


# 2.2: Factorial Calculator
# TODO: Write a program that calculates the factorial of a number n
#       Factorial is the product of all positive integers less than or equal to n
#       Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
print("\n2.2: Factorial Calculator")
# Your code here


# 2.3: Pattern Printer
# TODO: Write a program that prints the following pattern:
# *
# **
# ***
# ****
# *****
print("\n2.3: Pattern Printer")
# Your code here


# 2.4: FizzBuzz
# TODO: Write a program that prints numbers from 1 to 30
#       But for multiples of 3, print "Fizz" instead of the number
#       For multiples of 5, print "Buzz" instead of the number
#       For multiples of both 3 and 5, print "FizzBuzz"
print("\n2.4: FizzBuzz")
# Your code here


# ------------------------------------------------------
# Exercise 3: While Loops
# ------------------------------------------------------
# Practice using while loops for different scenarios
# ------------------------------------------------------

print("\nExercise 3: While Loops")
print("-" * 40)

# 3.1: Countdown
# TODO: Write a program that counts down from 10 to 1,
#       then prints "Blast off!"
print("3.1: Countdown")
# Your code here


# 3.2: Password Attempt Limiter
# TODO: Write a program that asks the user for a password
#       Give them at most 3 attempts to enter the correct password
#       The correct password is "python123"
print("\n3.2: Password Attempt Limiter")
# Your code here


# 3.3: Number Guessing Game
# TODO: Create a number guessing game where:
#       - The program selects a random number between 1 and 100
#       - The user tries to guess it
#       - The program tells them if the guess is too high or too low
#       - The game continues until the correct guess is made
#       - Track and display the number of attempts it took
import random  # Use this for generating a random number
print("\n3.3: Number Guessing Game")
# Your code here


# 3.4: Input Validator
# TODO: Write a program that keeps asking for a number between 1 and 10
#       until the user enters a valid input
print("\n3.4: Input Validator")
# Your code here


# ------------------------------------------------------
# Exercise 4: Loop Control Statements
# ------------------------------------------------------
# Practice using break, continue, and pass
# ------------------------------------------------------

print("\nExercise 4: Loop Control Statements")
print("-" * 40)

# 4.1: Find First Prime
# TODO: Write a program that finds and prints the first prime number after a given number n
#       Use a break statement to exit the loop once found
print("4.1: Find First Prime")
# Your code here


# 4.2: Skip Multiples
# TODO: Write a program that prints numbers from 1 to 20,
#       but skips multiples of 3 (use continue)
print("\n4.2: Skip Multiples")
# Your code here


# 4.3: Sum Until Threshold
# TODO: Calculate the sum of integers from 1 upward until the sum exceeds 100
#       Print the final sum and the last number added
print("\n4.3: Sum Until Threshold")
# Your code here


# 4.4: Process Positive Numbers
# TODO: Write a program that repeatedly asks the user for a number
#       - Processes positive numbers (print their square)
#       - Skips negative numbers (using continue)
#       - Exits when 0 is entered (using break)
print("\n4.4: Process Positive Numbers")
# Your code here


# ------------------------------------------------------
# Exercise 5: Nested Loops
# ------------------------------------------------------
# Practice using loops inside other loops
# ------------------------------------------------------

print("\nExercise 5: Nested Loops")
print("-" * 40)

# 5.1: Multiplication Table
# TODO: Generate and display a multiplication table for numbers 1 through 10
print("5.1: Multiplication Table")
# Your code here


# 5.2: Coordinate Grid
# TODO: Print all coordinate pairs (x,y) where x and y both range from 1 to 5
print("\n5.2: Coordinate Grid")
# Your code here


# 5.3: Pattern Pyramid
# TODO: Print a number pyramid pattern like:
# 1
# 22
# 333
# 4444
# 55555
print("\n5.3: Pattern Pyramid")
# Your code here


# ------------------------------------------------------
# Exercise 6: Mini Project - Adventure Game
# ------------------------------------------------------
# Create a simple text-based adventure game using control flow
# ------------------------------------------------------

print("\nExercise 6: Mini Project - Adventure Game")
print("-" * 40)

# TODO: Create a simple text-based adventure game where:
#       - The player starts in a room
#       - They can choose different directions to move (e.g., north, south, east, west)
#       - Different rooms have different descriptions and options
#       - Some rooms may have items to collect
#       - There is at least one win condition and one lose condition
#       - Use nested if statements or loops as appropriate
#       - Game continues until win/lose or player quits

print("6: Text Adventure Game")
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

Exercise 1: Conditional Statements
[ ] 1.1: Grade Classifier
[ ] 1.2: Leap Year Checker
[ ] 1.3: Number Analyzer
[ ] 1.4: Rock, Paper, Scissors Game

Exercise 2: For Loops
[ ] 2.1: Number Summation
[ ] 2.2: Factorial Calculator
[ ] 2.3: Pattern Printer
[ ] 2.4: FizzBuzz

Exercise 3: While Loops
[ ] 3.1: Countdown
[ ] 3.2: Password Attempt Limiter
[ ] 3.3: Number Guessing Game
[ ] 3.4: Input Validator

Exercise 4: Loop Control Statements
[ ] 4.1: Find First Prime
[ ] 4.2: Skip Multiples
[ ] 4.3: Sum Until Threshold
[ ] 4.4: Process Positive Numbers

Exercise 5: Nested Loops
[ ] 5.1: Multiplication Table
[ ] 5.2: Coordinate Grid
[ ] 5.3: Pattern Pyramid

Exercise 6: Mini Project
[ ] Text Adventure Game

Progress: [_____] 0% complete
""")