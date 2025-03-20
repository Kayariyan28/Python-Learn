# ========================================================
# Python Journey: Module 1 - Control Flow Solutions
# ========================================================
# Solutions for the exercises on conditionals and loops
# ========================================================

print("=" * 60)
print("Python Journey: Control Flow - Solutions")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Conditional Statements (if, elif, else)
# ------------------------------------------------------

print("\nExercise 1: Conditional Statements")
print("-" * 40)

# 1.1: Grade Classifier
print("1.1: Grade Classifier")

def classify_grade():
    """Classify a numerical grade into a letter grade."""
    try:
        # In a real program, we would use input() to get the grade
        # For this solution file, we'll test with different values
        for test_grade in [95, 85, 75, 65, 55, 105, -10]:
            grade = test_grade
            
            # Check if the grade is valid
            if grade < 0 or grade > 100:
                print(f"Grade {grade} is invalid. Please enter a number between 0 and 100.")
            else:
                # Determine the letter grade
                if grade >= 90:
                    letter = "A"
                elif grade >= 80:
                    letter = "B"
                elif grade >= 70:
                    letter = "C"
                elif grade >= 60:
                    letter = "D"
                else:
                    letter = "F"
                
                print(f"A grade of {grade} is a letter grade of {letter}.")
    except ValueError:
        print("Invalid input. Please enter a numerical grade.")

classify_grade()

# 1.2: Leap Year Checker
print("\n1.2: Leap Year Checker")

def check_leap_year():
    """Check if a given year is a leap year."""
    test_years = [1900, 2000, 2020, 2023, 2024]
    
    for year in test_years:
        # A leap year is divisible by 4
        # But not by 100 unless it's also divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

check_leap_year()

# 1.3: Number Analyzer
print("\n1.3: Number Analyzer")

def analyze_number():
    """Analyze a number for several properties."""
    # Test with various numbers
    test_numbers = [0, 7, 10, 15, -8, 17, 20]
    
    for num in test_numbers:
        print(f"\nAnalyzing {num}:")
        
        # Check if positive, negative, or zero
        if num > 0:
            print(f"- {num} is positive")
        elif num < 0:
            print(f"- {num} is negative")
        else:
            print(f"- {num} is zero")
        
        # Check if even or odd (zero is considered even)
        if num % 2 == 0:
            print(f"- {num} is even")
        else:
            print(f"- {num} is odd")
        
        # Check if multiple of 5
        if num % 5 == 0:
            print(f"- {num} is a multiple of 5")
        else:
            print(f"- {num} is not a multiple of 5")
        
        # Check if prime
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"- {num} is a prime number")
            else:
                print(f"- {num} is not a prime number")
        elif num == 0 or num == 1:
            print(f"- {num} is neither prime nor composite")
        else:  # num < 0
            print(f"- {num} is negative (prime numbers are positive by definition)")

analyze_number()

# 1.4: Rock, Paper, Scissors Game
print("\n1.4: Rock, Paper, Scissors Game")

def rock_paper_scissors():
    """Simple rock-paper-scissors game."""
    # For this solution, we'll simulate user input
    # Normally, we would use: player_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # We'll test with different player choices
    player_choices = ["rock", "paper", "scissors", "invalid"]
    
    # Computer's choice (hardcoded for this solution)
    computer_choice = "paper"
    print(f"Computer has chosen: {computer_choice}")
    
    for player_choice in player_choices:
        print(f"\nPlayer chooses: {player_choice}")
        
        # Validate player choice
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

rock_paper_scissors()

# ------------------------------------------------------
# Exercise 2: For Loops
# ------------------------------------------------------

print("\nExercise 2: For Loops")
print("-" * 40)

# 2.1: Number Summation
print("2.1: Number Summation")

def sum_to_n():
    """Calculate the sum of numbers from 1 to n."""
    # Test with different values of n
    test_values = [5, 10, 100]
    
    for n in test_values:
        # Calculate the sum using a for loop
        total = 0
        for i in range(1, n + 1):
            total += i
        
        print(f"Sum of numbers from 1 to {n}: {total}")
        
        # Alternative method using the formula: sum = n * (n + 1) / 2
        formula_result = n * (n + 1) // 2
        print(f"Using formula: {formula_result}")

sum_to_n()

# 2.2: Factorial Calculator
print("\n2.2: Factorial Calculator")

def calculate_factorial():
    """Calculate the factorial of a number."""
    # Test with different values
    test_values = [0, 1, 5, 10]
    
    for n in test_values:
        # Calculate factorial using a for loop
        factorial = 1
        
        # Special case for 0!
        if n == 0:
            print(f"{n}! = {factorial}")
            continue
        
        for i in range(1, n + 1):
            factorial *= i
        
        print(f"{n}! = {factorial}")

calculate_factorial()

# 2.3: Pattern Printer
print("\n2.3: Pattern Printer")

def print_pattern():
    """Print a triangle pattern of asterisks."""
    # Number of rows in the pattern
    rows = 5
    
    print("Pattern:")
    
    # Outer loop for rows
    for i in range(1, rows + 1):
        # Print i asterisks in each row
        print("*" * i)
    
    # Alternative approach using nested loops
    print("\nSame pattern using nested loops:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()  # New line after each row

print_pattern()

# 2.4: FizzBuzz
print("\n2.4: FizzBuzz")

def fizzbuzz():
    """Implement the FizzBuzz game."""
    print("FizzBuzz from 1 to 30:")
    
    for num in range(1, 31):
        # Check conditions in specific order (both divisible by 3 and 5 first)
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()

# ------------------------------------------------------
# Exercise 3: While Loops
# ------------------------------------------------------

print("\nExercise 3: While Loops")
print("-" * 40)

# 3.1: Countdown
print("3.1: Countdown")

def countdown():
    """Count down from 10 to 1, then print 'Blast off!'"""
    count = 10
    
    while count > 0:
        print(count)
        count -= 1
    
    print("Blast off!")

countdown()

# 3.2: Password Attempt Limiter
print("\n3.2: Password Attempt Limiter")

def password_checker():
    """Check if the user entered the correct password within 3 attempts."""
    correct_password = "python123"
    max_attempts = 3
    attempts = 0
    
    # For this solution, we'll simulate user input
    # In a real program, we would use: password = input("Enter the password: ")
    test_passwords = ["wrong1", "wrong2", "python123"]
    
    while attempts < max_attempts:
        # Simulate user input
        password = test_passwords[attempts]
        attempts += 1
        
        print(f"Attempt {attempts}: Entering '{password}'")
        
        if password == correct_password:
            print("Correct password! Access granted.")
            break
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect password. {remaining} attempts remaining.")
            else:
                print("Incorrect password. No attempts remaining.")
    
    if attempts == max_attempts and password != correct_password:
        print("Access denied. Too many failed attempts.")

password_checker()

# 3.3: Number Guessing Game
print("\n3.3: Number Guessing Game")

def guessing_game():
    """Play a number guessing game."""
    import random
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    print(f"(The secret number is {secret_number})")  # In a real game, this would be hidden
    
    # For this solution, we'll simulate user guesses
    # In a real program, we would use: guess = int(input("Enter your guess: "))
    
    # Simulate a series of guesses that eventually find the number
    # For demonstration, we'll use a simple strategy to find the number
    lower_bound = 1
    upper_bound = 100
    
    while True:
        # Simple bisection algorithm to find the number
        guess = (lower_bound + upper_bound) // 2
        attempts += 1
        
        print(f"Guess #{attempts}: {guess}")
        
        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
            lower_bound = guess + 1
        else:
            print("Too high! Try a lower number.")
            upper_bound = guess - 1

guessing_game()

# 3.4: Input Validator
print("\n3.4: Input Validator")

def validate_input():
    """Keep asking for a number between 1 and 10 until a valid input is provided."""
    
    # For this solution, we'll simulate user input
    # In a real program, we would use: user_input = input("Enter a number between 1 and 10: ")
    test_inputs = ["hello", "-5", "15", "7"]
    attempt = 0
    
    valid_input = False
    while not valid_input:
        # Simulate user input
        if attempt < len(test_inputs):
            user_input = test_inputs[attempt]
        else:
            user_input = "7"  # Default to valid input if we run out of test cases
        
        attempt += 1
        print(f"Attempt {attempt}: Entering '{user_input}'")
        
        try:
            number = int(user_input)
            if 1 <= number <= 10:
                print(f"Valid input! You entered {number}.")
                valid_input = True
            else:
                print("Invalid range. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

validate_input()

# ------------------------------------------------------
# Exercise 4: Loop Control Statements
# ------------------------------------------------------

print("\nExercise 4: Loop Control Statements")
print("-" * 40)

# 4.1: Find First Prime
print("4.1: Find First Prime")

def find_first_prime_after():
    """Find the first prime number after a given number."""
    # Test with different starting points
    test_starts = [10, 20, 100]
    
    for start in test_starts:
        print(f"Finding first prime after {start}:")
        num = start + 1  # Start checking from the next number
        
        while True:
            # Check if num is prime
            is_prime = True
            if num <= 1:
                is_prime = False
            else:
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
            
            if is_prime:
                print(f"The first prime number after {start} is {num}")
                break
            
            num += 1

find_first_prime_after()

# 4.2: Skip Multiples
print("\n4.2: Skip Multiples")

def skip_multiples():
    """Print numbers from 1 to 20, but skip multiples of 3."""
    print("Numbers from 1 to 20, skipping multiples of 3:")
    
    for i in range(1, 21):
        if i % 3 == 0:
            continue  # Skip this iteration
        print(i, end=" ")
    print()  # New line after all numbers

skip_multiples()

# 4.3: Sum Until Threshold
print("\n4.3: Sum Until Threshold")

def sum_until_threshold():
    """Calculate the sum of integers from 1 upward until the sum exceeds 100."""
    threshold = 100
    current_sum = 0
    num = 0
    
    while current_sum <= threshold:
        num += 1
        current_sum += num
        print(f"Adding {num}: Sum = {current_sum}")
    
    print(f"The sum first exceeded {threshold} after adding {num}")
    print(f"Final sum: {current_sum}")
    print(f"Last number added: {num}")

sum_until_threshold()

# 4.4: Process Positive Numbers
print("\n4.4: Process Positive Numbers")

def process_positive_numbers():
    """
    Process positive numbers (print their square),
    skip negative numbers, and exit when 0 is entered.
    """
    # For this solution, we'll simulate user input
    # In a real program, we would use: num = input("Enter a number (0 to exit): ")
    test_inputs = [5, -3, 7, -2, 0]
    
    for test_input in test_inputs:
        num = test_input
        print(f"Processing input: {num}")
        
        if num == 0:
            print("Exiting as requested.")
            break
        elif num < 0:
            print("Negative number. Skipping.")
            continue
        else:
            square = num ** 2
            print(f"The square of {num} is {square}")

process_positive_numbers()

# ------------------------------------------------------
# Exercise 5: Nested Loops
# ------------------------------------------------------

print("\nExercise 5: Nested Loops")
print("-" * 40)

# 5.1: Multiplication Table
print("5.1: Multiplication Table")

def multiplication_table():
    """Generate and display a multiplication table for numbers 1 through 10."""
    # Define the size of the table
    size = 10
    
    # Print header row
    print("   |", end="")
    for i in range(1, size + 1):
        print(f"{i:3}", end="")
    print("\n" + "-" * 44)
    
    # Print each row
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        # Print each column in the current row
        for j in range(1, size + 1):
            print(f"{i*j:3}", end="")
        print()  # New line after each row

multiplication_table()

# 5.2: Coordinate Grid
print("\n5.2: Coordinate Grid")

def coordinate_grid():
    """Print all coordinate pairs (x,y) where x and y both range from 1 to 5."""
    print("Coordinate pairs (x,y) from 1 to 5:")
    
    for x in range(1, 6):
        for y in range(1, 6):
            print(f"({x},{y})", end=" ")
        print()  # New line after each x value

coordinate_grid()

# 5.3: Pattern Pyramid
print("\n5.3: Pattern Pyramid")

def pattern_pyramid():
    """Print a number pyramid pattern."""
    rows = 5
    
    print("Number Pyramid:")
    
    for i in range(1, rows + 1):
        # Print the current number i, repeated i times
        for j in range(1, i + 1):
            print(i, end="")
        print()  # New line after each row

pattern_pyramid()

# ------------------------------------------------------
# Exercise 6: Mini Project - Adventure Game
# ------------------------------------------------------

print("\nExercise 6: Mini Project - Adventure Game")
print("-" * 40)

def adventure_game():
    """Simple text-based adventure game using control flow."""
    print("=== THE PYTHON DUNGEON ===")
    print("You find yourself in a mysterious dungeon with multiple paths ahead.")
    
    # Keep track of inventory and game state
    inventory = []
    has_key = False
    has_sword = False
    game_over = False
    
    # Starting room
    current_room = "entrance"
    
    # Game loop
    while not game_over:
        # Display current inventory
        print(f"\nInventory: {', '.join(inventory) if inventory else 'Empty'}")
        
        # Handle each room
        if current_room == "entrance":
            print("\nYou are at the entrance of the dungeon.")
            print("There are three paths ahead:")
            print("1. A dark corridor to the north")
            print("2. A dimly lit room to the east")
            print("3. A stairway leading down to the west")
            
            # Simulate choice
            choice = input("\nWhich way do you go? (north/east/west/quit): ").lower()
            
            if choice == "north":
                current_room = "corridor"
            elif choice == "east":
                current_room = "dim_room"
            elif choice == "west":
                current_room = "stairway"
            elif choice == "quit":
                print("You decide to leave the dungeon. Game over!")
                game_over = True
            else:
                print("Invalid choice. Try again.")
        
        elif current_room == "corridor":
            print("\nYou enter a long, dark corridor.")
            if "torch" not in inventory:
                print("It's too dark to see anything. You need a light source.")
                print("You return to the entrance.")
                current_room = "entrance"
            else:
                print("Your torch illuminates the corridor, revealing a sword on the wall.")
                if "sword" not in inventory:
                    take_sword = input("Take the sword? (yes/no): ").lower()
                    if take_sword == "yes":
                        inventory.append("sword")
                        has_sword = True
                        print("You take the sword. It might be useful later.")
                    else:
                        print("You leave the sword on the wall.")
                
                print("\nAt the end of the corridor is a door.")
                print("You can go through the door or return to the entrance.")
                choice = input("What do you do? (door/return): ").lower()
                
                if choice == "door":
                    current_room = "monster_room"
                elif choice == "return":
                    current_room = "entrance"
                else:
                    print("Invalid choice. You stay in the corridor.")
        
        elif current_room == "dim_room":
            print("\nYou enter a dimly lit room with ancient artifacts.")
            if "torch" not in inventory:
                print("You find a torch on the wall and take it.")
                inventory.append("torch")
            
            print("You notice a small key on a table.")
            if "key" not in inventory and not has_key:
                take_key = input("Take the key? (yes/no): ").lower()
                if take_key == "yes":
                    inventory.append("key")
                    has_key = True
                    print("You take the key. It might unlock something important.")
                else:
                    print("You leave the key on the table.")
            
            print("\nThere's nothing else of interest here.")
            print("You return to the entrance.")
            current_room = "entrance"
        
        elif current_room == "stairway":
            print("\nYou descend the stairway and find a locked chest at the bottom.")
            if "key" in inventory:
                open_chest = input("Use the key to open the chest? (yes/no): ").lower()
                if open_chest == "yes":
                    print("\nYou unlock the chest and find a map of the dungeon!")
                    print("The map reveals a secret exit behind the treasure room.")
                    inventory.append("map")
                    print("\nYou return to the entrance with your new treasure map.")
                    current_room = "entrance"
                else:
                    print("You decide not to open the chest.")
                    print("You return to the entrance.")
                    current_room = "entrance"
            else:
                print("The chest is locked. You need a key to open it.")
                print("You return to the entrance.")
                current_room = "entrance"
        
        elif current_room == "monster_room":
            print("\nYou enter a large chamber and find yourself face to face with a dragon!")
            if has_sword:
                print("The dragon attacks, but you defend yourself with your sword.")
                fight_choice = input("Do you fight the dragon or run? (fight/run): ").lower()
                
                if fight_choice == "fight":
                    print("\nYou bravely fight the dragon and defeat it!")
                    print("Behind the dragon, you discover a room filled with treasure.")
                    current_room = "treasure_room"
                else:
                    print("You run back to the entrance, narrowly escaping the dragon.")
                    current_room = "entrance"
            else:
                print("The dragon attacks! Without a weapon, you're defenseless.")
                print("You run back to the entrance, narrowly escaping with your life.")
                current_room = "entrance"
        
        elif current_room == "treasure_room":
            print("\nYou enter a magnificent treasure room filled with gold and jewels!")
            if "map" in inventory:
                print("Using your map, you locate the secret exit behind a tapestry.")
                secret_exit = input("Take the secret exit with the treasure? (yes/no): ").lower()
                
                if secret_exit == "yes":
                    print("\nCongratulations! You successfully escaped the dungeon with the treasure!")
                    print("YOU WIN!")
                    game_over = True
                else:
                    print("You decide to explore more before leaving.")
                    print("You return to the entrance.")
                    current_room = "entrance"
            else:
                print("You gather as much treasure as you can carry.")
                print("With no clear way out, you return to the entrance to find an exit.")
                inventory.append("treasure")
                current_room = "entrance"

# For this solution file, we don't run the game automatically
# Uncomment the line below to play the game
# adventure_game()

print("Text Adventure Game solution is ready to run.")
print("Uncomment the 'adventure_game()' call to play the game.")

# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each exercise as you complete it:

Exercise 1: Conditional Statements
[✓] 1.1: Grade Classifier
[✓] 1.2: Leap Year Checker
[✓] 1.3: Number Analyzer
[✓] 1.4: Rock, Paper, Scissors Game

Exercise 2: For Loops
[✓] 2.1: Number Summation
[✓] 2.2: Factorial Calculator
[✓] 2.3: Pattern Printer
[✓] 2.4: FizzBuzz

Exercise 3: While Loops
[✓] 3.1: Countdown
[✓] 3.2: Password Attempt Limiter
[✓] 3.3: Number Guessing Game
[✓] 3.4: Input Validator

Exercise 4: Loop Control Statements
[✓] 4.1: Find First Prime
[✓] 4.2: Skip Multiples
[✓] 4.3: Sum Until Threshold
[✓] 4.4: Process Positive Numbers

Exercise 5: Nested Loops
[✓] 5.1: Multiplication Table
[✓] 5.2: Coordinate Grid
[✓] 5.3: Pattern Pyramid

Exercise 6: Mini Project
[✓] Text Adventure Game

Progress: [█████] 100% complete
""")