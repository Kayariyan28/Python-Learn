# ========================================================
# Python Journey: Module 1 - Basic Syntax and Data Types Solutions
# ========================================================
# Solutions for the exercises on Python syntax and data types
# ========================================================

print("=" * 60)
print("Python Journey: Basic Syntax and Data Types - Solutions")
print("=" * 60)

# ------------------------------------------------------
# Exercise 1: Working with Integers and Floats
# ------------------------------------------------------

print("\nExercise 1: Working with Integers and Floats")
print("-" * 40)

# 1.1: Calculate the area of a rectangle with length 7.5 and width 3.2
print("1.1: Area of rectangle with length 7.5 and width 3.2")
length = 7.5
width = 3.2
area = length * width
print(f"The area of the rectangle is {area} square units")

# 1.2: Convert temperature from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
print("\n1.2: Convert 27 degrees Celsius to Fahrenheit")
celsius = 27
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# 1.3: Calculate how many whole slices can be obtained from 3 pizzas if each pizza 
# has 8 slices and 5 people want to have an equal number of slices
print("\n1.3: Pizza slicing problem")
pizzas = 3
slices_per_pizza = 8
total_slices = pizzas * slices_per_pizza
people = 5
slices_per_person = total_slices // people  # Integer division for whole slices
remaining_slices = total_slices % people    # Modulo for remainder
print(f"Total slices: {total_slices}")
print(f"Each person gets {slices_per_person} slices")
print(f"Remaining slices: {remaining_slices}")

# 1.4: Use the modulo operator to check if a number is odd or even
print("\n1.4: Check if numbers are odd or even")
# Check if 42 is odd or even
num1 = 42
if num1 % 2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

# Check if 97 is odd or even
num2 = 97
if num2 % 2 == 0:
    print(f"{num2} is even")
else:
    print(f"{num2} is odd")

# ------------------------------------------------------
# Exercise 2: String Operations
# ------------------------------------------------------

print("\nExercise 2: String Operations")
print("-" * 40)

# 2.1: Create a string containing your first and last name, then extract and 
# print your initials
print("2.1: Extract initials from your name")
full_name = "John Doe"
# Split the name and get first letter of each part
name_parts = full_name.split()
first_initial = name_parts[0][0]
last_initial = name_parts[1][0]
initials = first_initial + last_initial
print(f"Full name: {full_name}")
print(f"Initials: {initials}")

# 2.2: Take the sentence and print it with all letters in different cases
original_sentence = "Python programming is fun and powerful."
print("\n2.2: Change case of sentence")
print(f"Original: {original_sentence}")
print(f"ALL CAPS: {original_sentence.upper()}")
print(f"lowercase: {original_sentence.lower()}")
print(f"Title Case: {original_sentence.title()}")

# 2.3: Create a string containing a 10-digit phone number (no spaces/dashes)
# Then use string slicing to print it in the format: (XXX) XXX-XXXX
print("\n2.3: Format a phone number")
phone_number = "5551234567"
formatted_number = f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}"
print(f"Original: {phone_number}")
print(f"Formatted: {formatted_number}")

# 2.4: Fix the typos in the following sentence using string replacement
typo_sentence = "Pythom is a populer progamming lnguage for begimners."
print("\n2.4: Fix the typos")
print(f"With typos: {typo_sentence}")
fixed_sentence = typo_sentence.replace("Pythom", "Python")
fixed_sentence = fixed_sentence.replace("populer", "popular")
fixed_sentence = fixed_sentence.replace("progamming", "programming")
fixed_sentence = fixed_sentence.replace("lnguage", "language")
fixed_sentence = fixed_sentence.replace("begimners", "beginners")
print(f"Fixed: {fixed_sentence}")

# ------------------------------------------------------
# Exercise 3: Boolean Logic and Comparison
# ------------------------------------------------------

print("\nExercise 3: Boolean Logic and Comparison")
print("-" * 40)

# 3.1: Create two boolean variables and demonstrate the AND, OR, and NOT operations
print("3.1: Boolean operations")
is_sunny = True
is_weekend = False

print(f"is_sunny: {is_sunny}")
print(f"is_weekend: {is_weekend}")

# AND operation
print(f"is_sunny AND is_weekend: {is_sunny and is_weekend}")

# OR operation
print(f"is_sunny OR is_weekend: {is_sunny or is_weekend}")

# NOT operation
print(f"NOT is_sunny: {not is_sunny}")
print(f"NOT is_weekend: {not is_weekend}")

# 3.2: Write expressions to check if a number is between 10 and 20 (inclusive)
# and if a number is either less than 0 or greater than 100
print("\n3.2: Comparison operations")
num = 15
is_between_10_and_20 = 10 <= num <= 20
print(f"Is {num} between 10 and 20? {is_between_10_and_20}")

num = 5
is_between_10_and_20 = 10 <= num <= 20
print(f"Is {num} between 10 and 20? {is_between_10_and_20}")

num = 150
is_outside_0_to_100 = num < 0 or num > 100
print(f"Is {num} less than 0 or greater than 100? {is_outside_0_to_100}")

num = 50
is_outside_0_to_100 = num < 0 or num > 100
print(f"Is {num} less than 0 or greater than 100? {is_outside_0_to_100}")

# 3.3: Create a complex boolean expression
print("\n3.3: Complex boolean expression")
# Check if a number is divisible by 2 OR (divisible by 3 AND greater than 10)
num = 12
result = (num % 2 == 0) or ((num % 3 == 0) and (num > 10))
print(f"Is {num} divisible by 2 OR (divisible by 3 AND greater than 10)? {result}")

num = 9
result = (num % 2 == 0) or ((num % 3 == 0) and (num > 10))
print(f"Is {num} divisible by 2 OR (divisible by 3 AND greater than 10)? {result}")

num = 15
result = (num % 2 == 0) or ((num % 3 == 0) and (num > 10))
print(f"Is {num} divisible by 2 OR (divisible by 3 AND greater than 10)? {result}")

# ------------------------------------------------------
# Exercise 4: Type Conversion
# ------------------------------------------------------

print("\nExercise 4: Type Conversion")
print("-" * 40)

# 4.1: Convert the following strings to integers and perform a calculation
num_string1 = "42"
num_string2 = "73"
print("4.1: Convert strings to integers")
num1 = int(num_string1)
num2 = int(num_string2)
sum_result = num1 + num2
print(f"{num_string1} + {num_string2} = {sum_result}")

# 4.2: Convert the following strings to floats and perform a calculation
float_string1 = "3.14159"
float_string2 = "2.71828"
print("\n4.2: Convert strings to floats")
float1 = float(float_string1)
float2 = float(float_string2)
product = float1 * float2
print(f"{float_string1} * {float_string2} = {product}")

# 4.3: Convert the following float to an integer in two ways
pi_value = 3.14159
print("\n4.3: Convert float to integer")
# a) By simple type conversion (which truncates the decimal part)
truncated = int(pi_value)
print(f"Truncated {pi_value} to {truncated}")

# b) By rounding to the nearest integer
rounded = round(pi_value)
print(f"Rounded {pi_value} to {rounded}")

# 4.4: Convert various data types to boolean values
print("\n4.4: Convert to boolean values")
# Integers to boolean
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool(-10) = {bool(-10)}")

# Strings to boolean
print(f"bool('') = {bool('')}")  # Empty string
print(f"bool('hello') = {bool('hello')}")

# None to boolean
print(f"bool(None) = {bool(None)}")

# 4.5: Safely convert user input to numbers
test_input1 = "42"  # Should work
test_input2 = "3.14159"  # Should work
test_input3 = "hello"  # Should detect and handle this error
print("\n4.5: Safely convert to numbers")

# Function to safely convert to a number
def safe_convert_to_number(input_string):
    try:
        # Try as integer first
        return int(input_string)
    except ValueError:
        try:
            # If not integer, try as float
            return float(input_string)
        except ValueError:
            # If not a number at all, return None
            return None

# Test the function with different inputs
result1 = safe_convert_to_number(test_input1)
result2 = safe_convert_to_number(test_input2)
result3 = safe_convert_to_number(test_input3)

print(f"Converting '{test_input1}': {result1}")
print(f"Converting '{test_input2}': {result2}")
print(f"Converting '{test_input3}': {result3 if result3 is not None else 'Not a number'}")

# ------------------------------------------------------
# Bonus Challenge: String Formatting
# ------------------------------------------------------

print("\nBonus Challenge: String Formatting")
print("-" * 40)

# Create formatted output that displays product data in a nice table
product1_name = "Laptop"
product1_price = 1299.99
product1_quantity = 5

product2_name = "Phone"
product2_price = 799.50
product2_quantity = 12

product3_name = "Headphones"
product3_price = 49.99
product3_quantity = 25

# Print a formatted table with headers and alignment
print("Bonus: Format product table")
print(f"{'Product':<12} {'Price':>10} {'Quantity':>10} {'Total':>12}")
print("-" * 46)

product1_total = product1_price * product1_quantity
print(f"{product1_name:<12} ${product1_price:>9.2f} {product1_quantity:>10} ${product1_total:>11.2f}")

product2_total = product2_price * product2_quantity
print(f"{product2_name:<12} ${product2_price:>9.2f} {product2_quantity:>10} ${product2_total:>11.2f}")

product3_total = product3_price * product3_quantity
print(f"{product3_name:<12} ${product3_price:>9.2f} {product3_quantity:>10} ${product3_total:>11.2f}")

print("-" * 46)
grand_total = product1_total + product2_total + product3_total
print(f"{'TOTAL':<12} {'':<10} {'':<10} ${grand_total:>11.2f}")

# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each exercise as you complete it:

Exercise 1: Working with Integers and Floats
[✓] 1.1: Calculate rectangle area
[✓] 1.2: Convert Celsius to Fahrenheit
[✓] 1.3: Pizza slicing problem
[✓] 1.4: Check odd or even numbers

Exercise 2: String Operations
[✓] 2.1: Extract initials
[✓] 2.2: Change string case
[✓] 2.3: Format phone number
[✓] 2.4: Fix typos in a sentence

Exercise 3: Boolean Logic and Comparison
[✓] 3.1: Basic boolean operations
[✓] 3.2: Comparison expressions
[✓] 3.3: Complex boolean expression

Exercise 4: Type Conversion
[✓] 4.1: Convert strings to integers
[✓] 4.2: Convert strings to floats
[✓] 4.3: Convert float to integer (two ways)
[✓] 4.4: Convert to boolean values
[✓] 4.5: Safely convert user input

Bonus Challenge:
[✓] String formatting table

Progress: [█████] 100% complete
""")