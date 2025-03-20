# ========================================================
# Python Journey: Module 1 - Variables and User Input Solutions
# ========================================================
# Solutions for the exercises on variables and user interaction
# ========================================================

print("=" * 60)
print("Python Journey: Variables and User Input - Solutions")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Variable Creation and Naming
# ------------------------------------------------------

print("\nExercise 1: Variable Creation and Naming")
print("-" * 40)

# 1.1: Create variables for a person's profile
print("1.1: Create variables for a person's profile")
full_name = "Alex Johnson"
age = 28
height = 1.75  # in meters
is_student = False

print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Is student? {is_student}")

# 1.2: Create variables for a car's specifications
print("\n1.2: Create variables for a car's specifications")
make = "Toyota"
model = "Corolla"
year = 2022
engine_size = 1.8  # in liters
is_electric = False
fuel_efficiency = 32.5  # miles per gallon

print(f"Car: {year} {make} {model}")
print(f"Engine size: {engine_size}L")
print(f"Electric: {is_electric}")
print(f"Fuel efficiency: {fuel_efficiency} mpg")

# 1.3: Create variables related to a circle
print("\n1.3: Create variables related to a circle")
radius = 5
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2

print(f"Circle with radius: {radius}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")

# 1.4: Fix the invalid variable names
print("\n1.4: Fix invalid variable names")
# Original: 1st_place = "Gold"
first_place = "Gold"

# Original: user-name = "JohnDoe"
user_name = "JohnDoe"

# Original: class = "Python 101"
course_class = "Python 101"  # or python_class

# Original: average$ = 75.5
average_dollars = 75.5

# Original: for = "loop keyword"
for_keyword = "loop keyword"

print(f"First place: {first_place}")
print(f"Username: {user_name}")
print(f"Class: {course_class}")
print(f"Average ($): {average_dollars}")
print(f"For keyword: {for_keyword}")

# ------------------------------------------------------
# Exercise 2: Variable Operations and Updates
# ------------------------------------------------------

print("\nExercise 2: Variable Operations and Updates")
print("-" * 40)

# 2.1: Score calculation
print("2.1: Score calculation")
# Starting score
score = 0
print(f"Initial score: {score}")

# Add 10 points
score += 10
print(f"After adding 10 points: {score}")

# Add 5 more points
score += 5
print(f"After adding 5 more points: {score}")

# Double the score
score *= 2
print(f"After doubling: {score}")

# Subtract 7 points
score -= 7
print(f"After subtracting 7 points: {score}")

# 2.2: Shopping cart
print("\n2.2: Shopping cart calculation")
item_price = 29.99
quantity = 3
discount_percentage = 10
tax_rate = 7.5

# Calculate subtotal (price * quantity)
subtotal = item_price * quantity
print(f"Subtotal: ${subtotal:.2f}")

# Apply discount
discount_amount = subtotal * (discount_percentage / 100)
after_discount = subtotal - discount_amount
print(f"After {discount_percentage}% discount: ${after_discount:.2f}")

# Apply tax
tax_amount = after_discount * (tax_rate / 100)
final_price = after_discount + tax_amount
print(f"Tax ({tax_rate}%): ${tax_amount:.2f}")
print(f"Final price: ${final_price:.2f}")

# 2.3: Swapping variables
print("\n2.3: Swapping variables")
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Swap without a temporary variable
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 2.4: Create a "mad libs" sentence
print("\n2.4: Mad libs sentence")
noun = "python"
verb = "codes"
adjective = "brilliant"
adverb = "quickly"

# Create a sentence using the variables
mad_libs_sentence = f"The {adjective} {noun} {verb} {adverb} through the program."
print(mad_libs_sentence)

# ------------------------------------------------------
# Exercise 3: Getting User Input
# ------------------------------------------------------

print("\nExercise 3: Getting User Input")
print("-" * 40)

# For the purpose of this solution file, we'll simulate user input
# In a real exercise, you would use input() and users would type their responses

# 3.1: Basic information collector
print("3.1: Basic information collector")
# Simulating input instead of: name = input("What is your name? ")
name = "Maria"
age = 24  # Simulating: age = int(input("How old are you? "))
favorite_color = "Blue"  # Simulating: favorite_color = input("What is your favorite color? ")

# Print a summary
print("\nSummary of Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Color: {favorite_color}")
print(f"Thank you, {name}! I also like {favorite_color.lower()}.")

# 3.2: Calculator
print("\n3.2: Simple calculator")
# Simulating input
num1 = 15  # Simulating: num1 = float(input("Enter first number: "))
num2 = 7   # Simulating: num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print(f"You entered: {num1} and {num2}")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} × {num2} = {multiplication}")
print(f"Division: {num1} ÷ {num2} = {division}")

# 3.3: Temperature converter
print("\n3.3: Temperature converter")
# Simulating input
fahrenheit = 98.6  # Simulating: fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5/9

# Display the result
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# 3.4: Age calculator
print("\n3.4: Age calculator")
# Simulating input
import datetime
current_year = datetime.datetime.now().year

# Simulating: birth_year_input = input("Enter your birth year: ")
birth_year_input = "1995"

try:
    birth_year = int(birth_year_input)
    
    # Check if the year is valid (not in the future)
    if birth_year > current_year:
        print("Error: Birth year cannot be in the future!")
    else:
        approximate_age = current_year - birth_year
        print(f"You are approximately {approximate_age} years old in {current_year}.")
except ValueError:
    print("Error: Please enter a valid year as a number.")

# ------------------------------------------------------
# Exercise 4: String Formatting
# ------------------------------------------------------

print("\nExercise 4: String Formatting")
print("-" * 40)

# 4.1: Format a greeting using variables and f-strings
print("4.1: Formatted greeting")
name = "Sarah"
time_of_day = "morning"  # Could be "morning", "afternoon", or "evening"

# Create a greeting that varies based on the time of day
if time_of_day == "morning":
    greeting = f"Good morning, {name}! Have a wonderful day ahead."
elif time_of_day == "afternoon":
    greeting = f"Good afternoon, {name}! Hope you're having a productive day."
else:  # evening
    greeting = f"Good evening, {name}! Hope you had a great day."

print(greeting)

# 4.2: Format a receipt
print("\n4.2: Formatted receipt")
store_name = "Python Grocery"
item = "Organic Apples"
quantity = 5
price = 2.99

# Format a receipt with aligned columns
print(f"{store_name}")
print(f"{'=' * 30}")
print(f"{'Item':<15} {'Quantity':>5} {'Price':>10}")
print(f"{'-' * 30}")
print(f"{item:<15} {quantity:>5} ${price:>9.2f}")
print(f"{'-' * 30}")
total = quantity * price
print(f"{'Total':<15} {'':<5} ${total:>9.2f}")
print(f"{'=' * 30}")
print(f"Thank you for shopping at {store_name}!")

# 4.3: Format a progress display
print("\n4.3: Formatted progress bar")
task_name = "Downloading"
progress_percentage = 40

# Create a progress bar
bar_length = 10
filled_length = int(progress_percentage / 100 * bar_length)
bar = '#' * filled_length + ' ' * (bar_length - filled_length)

progress_bar = f"{task_name}: [{bar}] {progress_percentage}%"
print(progress_bar)

# ------------------------------------------------------
# Exercise 5: Mini Project - Personal Data Form
# ------------------------------------------------------

print("\nExercise 5: Mini Project - Personal Data Form")
print("-" * 40)

# For this solution, we'll simulate user input
print("5: Personal data form")

# Simulating user input collection
full_name = "John Smith"
try:
    age = 35
    height_cm = 180
    weight_kg = 75
    occupation = "Software Developer"
    
    # Calculate derived information
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)  # BMI formula: weight(kg) / height(m)²
    
    import datetime
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    retirement_age = 65
    retirement_year = birth_year + retirement_age
    
    # Display the collected and calculated information
    print("\n" + "=" * 40)
    print("PERSONAL DATA SUMMARY")
    print("=" * 40)
    
    print(f"\nPersonal Information:")
    print(f"  Full Name: {full_name}")
    print(f"  Age: {age} years")
    print(f"  Height: {height_cm} cm ({height_m:.2f} m)")
    print(f"  Weight: {weight_kg} kg")
    print(f"  Occupation: {occupation}")
    
    print(f"\nCalculated Information:")
    print(f"  BMI: {bmi:.2f}")
    print(f"  Birth Year (approx.): {birth_year}")
    print(f"  Retirement Year (at age 65): {retirement_year}")
    
    # BMI Category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"
    
    print(f"  BMI Category: {bmi_category}")
    
    print("\n" + "=" * 40)
    print("Thank you for using the Personal Data Form!")
    print("=" * 40)
    
except ValueError:
    print("Error: Please enter valid numerical values for age, height, and weight.")
except ZeroDivisionError:
    print("Error: Height cannot be zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each exercise as you complete it:

Exercise 1: Variable Creation and Naming
[✓] 1.1: Person's profile variables
[✓] 1.2: Car specification variables
[✓] 1.3: Circle-related variables
[✓] 1.4: Fix invalid variable names

Exercise 2: Variable Operations and Updates
[✓] 2.1: Score calculation
[✓] 2.2: Shopping cart calculation
[✓] 2.3: Swapping variables
[✓] 2.4: Mad libs sentence

Exercise 3: Getting User Input
[✓] 3.1: Basic information collector
[✓] 3.2: Simple calculator
[✓] 3.3: Temperature converter
[✓] 3.4: Age calculator

Exercise 4: String Formatting
[✓] 4.1: Formatted greeting
[✓] 4.2: Formatted receipt
[✓] 4.3: Formatted progress bar

Exercise 5: Mini Project
[✓] Personal data form

Progress: [█████] 100% complete
""")