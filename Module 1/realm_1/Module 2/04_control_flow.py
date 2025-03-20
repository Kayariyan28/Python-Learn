# ========================================================
# Python Journey: Module 2 - Control Flow
# ========================================================
# This file covers how to control the flow of your program
# using conditional statements and loops.
# ========================================================

print("=" * 50)
print("Python Control Flow: Conditionals and Loops")
print("=" * 50)

# ------------------------------------------------------
# CONDITIONAL STATEMENTS (IF, ELIF, ELSE)
# ------------------------------------------------------
# Conditional statements allow your program to make decisions
# based on certain conditions. They execute different code blocks
# depending on whether conditions evaluate to True or False.
# ------------------------------------------------------

print("\nCONDITIONAL STATEMENTS:")

# Basic if statement
print("\n--- Basic if statement ---")
age = 20

if age >= 18:
    print("You are an adult.")
    
# Note: The indented code block runs only if the condition is True

# If-else statement
print("\n--- If-else statement ---")
temperature = 15

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's not very hot today.")

# If-elif-else (multiple conditions)
print("\n--- If-elif-else statement ---")
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
print("\n--- Nested if statements ---")
is_weekend = True
weather = "sunny"

if is_weekend:
    if weather == "sunny":
        print("Perfect day for outdoor activities!")
    else:
        print("Maybe watch a movie at home?")
else:
    print("It's a work/school day.")

# Combining conditions with logical operators
print("\n--- Combining conditions ---")

has_ticket = True
has_id = False

# Using 'and' - both conditions must be True
if has_ticket and has_id:
    print("You can enter the venue.")
else:
    print("You cannot enter the venue.")
    if not has_ticket:
        print("You need a ticket.")
    if not has_id:
        print("You need an ID.")

# Using 'or' - at least one condition must be True
is_student = True
is_senior = False

if is_student or is_senior:
    print("You get a discount.")
else:
    print("You pay full price.")

# ------------------------------------------------------
# FOR LOOPS
# ------------------------------------------------------
# For loops are used to iterate over a sequence (like a list,
# tuple, dictionary, set, or string) and execute a block of
# code for each item in the sequence.
# ------------------------------------------------------

print("\nFOR LOOPS:")

# Looping through a range of numbers
print("\n--- Looping through a range ---")
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(1, 6) generates 1, 2, 3, 4, 5
    print(f"Number: {i}")

# Looping through a string
print("\n--- Looping through a string ---")
word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(letter)

# Looping through a list
print("\n--- Looping through a list ---")
fruits = ["apple", "banana", "cherry", "date"]
print("Fruit list:")
for fruit in fruits:
    print(f"- {fruit}")

# Using enumerate to get index and value
print("\n--- Using enumerate ---")
print("Fruits with indexes:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Using range with step
print("\n--- Range with step ---")
print("Even numbers from 2 to 10:")
for num in range(2, 11, 2):  # Start at 2, end before 11, step by 2
    print(num)

# ------------------------------------------------------
# WHILE LOOPS
# ------------------------------------------------------
# While loops execute a block of code as long as a condition
# is True. They're useful when you don't know in advance how
# many times the loop should run.
# ------------------------------------------------------

print("\nWHILE LOOPS:")

# Basic while loop
print("\n--- Basic while loop ---")
count = 1
print("Counting from 1 to 5 using while:")
while count <= 5:
    print(count)
    count += 1  # Don't forget to update the condition variable!

# While loop with break
print("\n--- While loop with break ---")
print("Counting until we hit 4:")
count = 1
while True:  # Infinite loop - needs a break statement
    print(count)
    if count == 4:
        print("Reached 4, stopping the loop")
        break  # Exit the loop immediately
    count += 1

# While loop with continue
print("\n--- While loop with continue ---")
print("Printing only odd numbers:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # If count is even
        continue  # Skip the rest of this iteration
    print(count)

# ------------------------------------------------------
# LOOP CONTROL STATEMENTS
# ------------------------------------------------------
# Python provides statements to control loop execution:
# - break: Exits the loop completely
# - continue: Skips the current iteration and moves to the next
# - pass: Does nothing, acts as a placeholder
# ------------------------------------------------------

print("\nLOOP CONTROL STATEMENTS:")

# Break example
print("\n--- Break example ---")
print("Looking for 'cherry' in the fruit list:")
for fruit in fruits:
    print(f"Checking {fruit}...")
    if fruit == "cherry":
        print(f"Found {fruit}! Stopping search.")
        break

# Continue example
print("\n--- Continue example ---")
print("Printing numbers from 1 to 5, skipping 3:")
for i in range(1, 6):
    if i == 3:
        print(f"Skipping {i}")
        continue
    print(f"Number: {i}")

# Pass example
print("\n--- Pass example ---")
print("Demonstrating pass as a placeholder:")
for i in range(1, 4):
    if i == 2:
        # pass does nothing, but it's a valid statement
        # useful when you need a placeholder for future code
        pass
    else:
        print(f"Processing number: {i}")

# ------------------------------------------------------
# EXERCISE: CONTROL FLOW CHALLENGES
# ------------------------------------------------------
# Let's practice conditional statements and loops with some
# fun challenges.
#
# Instructions:
# 1. Uncomment each challenge and complete it
# 2. Run the file to see your results
# ------------------------------------------------------

print("\n--- EXERCISE: CONTROL FLOW CHALLENGES ---")

# # Challenge 1: FizzBuzz
# # Print numbers from 1 to 20, but:
# # - For multiples of 3, print "Fizz" instead of the number
# # - For multiples of 5, print "Buzz" instead of the number
# # - For multiples of both 3 and 5, print "FizzBuzz"
# print("\nChallenge 1: FizzBuzz")
# for num in range(1, 21):
#     # Add your code here
#     # Hint: use if, elif, and else with the modulo operator (%)
#     pass  # Replace this with your code

# # Challenge 2: Password Validator
# # Check if a password meets these criteria:
# # - At least 8 characters long
# # - Contains at least one uppercase letter
# # - Contains at least one digit
# print("\nChallenge 2: Password Validator")
# password = input("Enter a password to validate: ")
# 
# # Add your code here
# # Hint: Use len() to check length and loops or string methods to check characters
# # Example: any(char.isupper() for char in password) checks for uppercase

# # Challenge 3: Sum of Even Numbers
# # Calculate the sum of all even numbers from 1 to N
# print("\nChallenge 3: Sum of Even Numbers")
# try:
#     n = int(input("Enter a positive number N: "))
#     # Add your code here
#     # Hint: Use a loop with a condition to check for even numbers
# except ValueError:
#     print("That's not a valid number!")

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: FLOW CONTROLLER 🏆")
print("You've mastered conditional statements and loops!")
print("=" * 50)

print("\nWhat's next? Continue to 05_lists_and_operations.py")