# ========================================================
# Python Journey: Module 1 - Solutions
# ========================================================
# This file contains solutions to the practice exercises.
# Use these as a reference after attempting the exercises.
# ========================================================

# ------------------------------------------------------
# EXERCISE 1: VARIABLE PRACTICE - SOLUTION
# ------------------------------------------------------

def exercise_1_solution():
    """Solution for variable practice exercise."""
    print("\n--- EXERCISE 1: VARIABLE PRACTICE (SOLUTION) ---")
    
    # 1. Create variables of different types
    age = 25
    name = "Alex"
    height = 1.75
    is_student = True
    
    # 2. Print all variables with their types
    print(f"name: {name} (type: {type(name)})")
    print(f"age: {age} (type: {type(age)})")
    print(f"height: {height} (type: {type(height)})")
    print(f"is_student: {is_student} (type: {type(is_student)})")
    
    # 3. Perform arithmetic operations
    age_in_months = age * 12
    height_in_feet = height * 3.28084
    
    print(f"Age in months: {age_in_months}")
    print(f"Height in feet: {height_in_feet:.2f}")
    
    # 4. Combine strings
    greeting = f"Hello! My name is {name} and I am {age} years old."
    print(greeting)
    
    print("Exercise 1 solution complete!\n")

# ------------------------------------------------------
# EXERCISE 2: CONDITIONAL LOGIC - SOLUTION
# ------------------------------------------------------

def exercise_2_solution():
    """Solution for conditional logic exercise."""
    print("\n--- EXERCISE 2: CONDITIONAL LOGIC (SOLUTION) ---")
    
    # 1. Age classifier
    def classify_age(age):
        """Classify a person's age into a category."""
        if age < 0:
            return "Invalid age"
        elif age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 64:
            return "Adult"
        else:
            return "Senior"
    
    # Test age classifier
    test_ages = [5, 15, 25, 70]
    for age in test_ages:
        category = classify_age(age)
        print(f"Age {age} is classified as: {category}")
    
    # 2. Grade calculator
    def calculate_grade(score):
        """Convert a numerical score to a letter grade."""
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    # Test grade calculator
    test_scores = [95, 85, 75, 65, 55]
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score {score} gets grade: {grade}")
    
    print("Exercise 2 solution complete!\n")

# ------------------------------------------------------
# EXERCISE 3: LOOPS - SOLUTION
# ------------------------------------------------------

def exercise_3_solution():
    """Solution for loops exercise."""
    print("\n--- EXERCISE 3: LOOPS (SOLUTION) ---")
    
    # 1. Counting with a for loop
    print("Counting from 1 to 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print()  # New line
    
    # 2. Sum of numbers
    sum_result = 0
    for i in range(1, 101):
        sum_result += i
    print(f"Sum of numbers from 1 to 100: {sum_result}")
    
    # 3. Multiplication table
    number = 7
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")
    
    # 4. Countdown with a while loop
    print("\nCountdown:")
    countdown = 10
    while countdown > 0:
        print(countdown, end=" ")
        countdown -= 1
    print("Blast off!")
    
    # 5. Break and continue
    print("\nNumbers from 1 to 20 (skipping multiples of 3, stopping at 15):")
    for i in range(1, 21):
        if i == 15:
            print("Reached 15, stopping!")
            break
        if i % 3 == 0:
            continue
        print(i, end=" ")
    print()  # New line
    
    print("Exercise 3 solution complete!\n")

# ------------------------------------------------------
# EXERCISE 4: LISTS - SOLUTION
# ------------------------------------------------------

def exercise_4_solution():
    """Solution for lists exercise."""
    print("\n--- EXERCISE 4: LISTS (SOLUTION) ---")
    
    # 1. Create and modify a list
    favorite_foods = ["pizza", "sushi", "tacos", "ice cream"]
    print(f"Original favorite foods: {favorite_foods}")
    
    favorite_foods.append("chocolate")
    print(f"After adding chocolate: {favorite_foods}")
    
    favorite_foods.insert(0, "pasta")
    print(f"After inserting pasta at the beginning: {favorite_foods}")
    
    favorite_foods.remove("tacos")
    print(f"After removing tacos: {favorite_foods}")
    
    favorite_foods.sort()
    print(f"After sorting alphabetically: {favorite_foods}")
    
    # 2. List operations
    numbers = list(range(1, 11))
    print(f"\nNumbers: {numbers}")
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    squared_numbers = [num ** 2 for num in numbers]
    print(f"Squared numbers: {squared_numbers}")
    
    numbers_sum = sum(numbers)
    numbers_min = min(numbers)
    numbers_max = max(numbers)
    numbers_avg = numbers_sum / len(numbers)
    
    print(f"Sum: {numbers_sum}")
    print(f"Minimum: {numbers_min}")
    print(f"Maximum: {numbers_max}")
    print(f"Average: {numbers_avg}")
    
    # 3. Nested lists
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\nMatrix:")
    for row in matrix:
        print(row)
    
    print("\nSum of each row:")
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        print(f"Row {i + 1}: {row_sum}")
    
    print("Exercise 4 solution complete!\n")

# ------------------------------------------------------
# EXERCISE 5: FUNCTIONS - SOLUTION
# ------------------------------------------------------

def exercise_5_solution():
    """Solution for functions exercise."""
    print("\n--- EXERCISE 5: FUNCTIONS (SOLUTION) ---")
    
    # 1. Basic function
    def is_even(number):
        """Return True if number is even, False otherwise."""
        return number % 2 == 0
    
    # Test is_even
    test_numbers = [4, 7, 10, 15]
    for num in test_numbers:
        result = is_even(num)
        print(f"{num} is even: {result}")
    
    # 2. Function with multiple parameters
    def area_of_rectangle(width, height):
        """Calculate the area of a rectangle."""
        return width * height
    
    # Test area_of_rectangle
    print(f"\nArea of rectangle (3x5): {area_of_rectangle(3, 5)}")
    print(f"Area of rectangle (2.5x6.7): {area_of_rectangle(2.5, 6.7):.2f}")
    
    # 3. Function with default parameters
    def greet(name, greeting="Hello"):
        """Greet someone with a customizable greeting."""
        return f"{greeting}, {name}!"
    
    # Test greet
    print(f"\n{greet('Alice')}")
    print(f"{greet('Bob', 'Hi there')}")
    
    # 4. Function that returns multiple values
    def statistics(numbers):
        """Calculate statistics for a list of numbers."""
        if not numbers:
            return None, None, 0, None
        
        min_val = min(numbers)
        max_val = max(numbers)
        total = sum(numbers)
        avg = total / len(numbers)
        
        return min_val, max_val, total, avg
    
    # Test statistics
    test_data = [10, 5, 7, 22, 13, 8]
    min_val, max_val, total, avg = statistics(test_data)
    print(f"\nStatistics for {test_data}:")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Sum: {total}")
    print(f"Average: {avg:.2f}")
    
    # 5. Recursive function
    def factorial(n):
        """Calculate the factorial of n recursively."""
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    # Test factorial
    for i in range(6):
        print(f"\n{i}! = {factorial(i)}")
    
    print("Exercise 5 solution complete!\n")

# ------------------------------------------------------
# EXERCISE 6: INTEGRATION CHALLENGE - SOLUTION
# ------------------------------------------------------

def exercise_6_solution():
    """Solution for integration challenge."""
    print("\n--- EXERCISE 6: INTEGRATION CHALLENGE (SOLUTION) ---")
    
    def run_quiz():
        """Run a simple Python quiz game."""
        questions = [
            {
                "question": "What symbol is used for comments in Python?",
                "answer": "#"
            },
            {
                "question": "What function is used to get the length of a list?",
                "answer": "len"
            },
            {
                "question": "What data type would you use to store a sequence of items that should never change?",
                "answer": "tuple"
            },
            {
                "question": "What loop keyword is used to skip the current iteration?",
                "answer": "continue"
            },
            {
                "question": "What is the correct way to create a function in Python?",
                "answer": "def"
            }
        ]
        
        score = 0
        
        print("Welcome to the Python Quiz Game!")
        print(f"You will be asked {len(questions)} questions about Python.")
        print("Type your answer and press Enter.\n")
        
        for i, q in enumerate(questions, 1):
            print(f"Question {i}: {q['question']}")
            user_answer = input("Your answer: ").strip().lower()
            
            if user_answer == q['answer'].lower():
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Incorrect. The answer is: {q['answer']}")
            
            print()  # Add a blank line between questions
        
        # Calculate percentage and grade
        percentage = (score / len(questions)) * 100
        
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        # Display final results
        print("=" * 30)
        print("QUIZ COMPLETE!")
        print("=" * 30)
        print(f"You scored {score} out of {len(questions)}")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Grade: {grade}")
        
        if grade in ["A", "B"]:
            print("Great job! You know your Python basics well!")
        elif grade in ["C", "D"]:
            print("Not bad! With a bit more practice, you'll master these concepts.")
        else:
            print("Keep studying! Python takes practice to learn.")
    
    # Run the quiz
    run_quiz()
    
    print("Exercise 6 solution complete!\n")

# Run solution demonstrations when this file is executed
if __name__ == "__main__":
    print("Python Journey: Module 1 - Solutions")
    print("=" * 50)
    print("These are solutions to the module exercises.")
    print("It's best to try solving the exercises yourself first!")
    
    # Uncomment these to see the solutions
    # exercise_1_solution()
    # exercise_2_solution()
    # exercise_3_solution()
    # exercise_4_solution()
    # exercise_5_solution()
    # exercise_6_solution()
    
    print("\nRefer to these solutions after attempting the exercises on your own.")