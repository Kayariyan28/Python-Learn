# Python Functions Cheatsheet

This cheatsheet provides a quick reference for Python's functions covered in Module 1 of Python Journey.

## Function Basics

### Defining a Function
```python
def function_name(parameter1, parameter2):
    """
    Docstring: Explains what the function does.
    
    Args:
        parameter1: Description of the first parameter
        parameter2: Description of the second parameter
        
    Returns:
        Description of what the function returns
    """
    # Function body
    # Code to execute
    
    return result  # Optional return statement
```

### Calling a Function
```python
# Call a function without parameters
result = function_name()

# Call a function with parameters
result = function_name(value1, value2)

# Call a function and ignore its return value
function_name(value1, value2)
```

## Function Parameters

### Required Parameters
```python
def greet(name):
    return f"Hello, {name}!"

# Must provide the required parameter
greeting = greet("Alice")  # Works
# greeting = greet()  # Error - missing required parameter
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Default parameter can be omitted
greeting1 = greet("Bob")  # Uses default greeting: "Hello, Bob!"
greeting2 = greet("Bob", "Hi")  # Overrides default: "Hi, Bob!"
```

### Positional vs. Keyword Arguments
```python
def describe_pet(animal_type, pet_name):
    return f"I have a {animal_type} named {pet_name}."

# Positional arguments (order matters)
description1 = describe_pet("hamster", "Harry")

# Keyword arguments (order doesn't matter)
description2 = describe_pet(pet_name="Harry", animal_type="hamster")

# Mix of positional and keyword arguments
# Positional arguments must come first
description3 = describe_pet("hamster", pet_name="Harry")
```

### Variable Number of Arguments (*args)
```python
def sum_all(*numbers):
    """Accept any number of positional arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

# Call with different numbers of arguments
result1 = sum_all(1, 2)  # 3
result2 = sum_all(1, 2, 3, 4, 5)  # 15
result3 = sum_all()  # 0
```

### Variable Number of Keyword Arguments (**kwargs)
```python
def build_profile(**user_info):
    """Accept any number of keyword arguments"""
    return user_info

# Call with different keyword arguments
profile1 = build_profile(name="Alice", age=30, occupation="Engineer")
profile2 = build_profile(name="Bob", is_active=True)
```

### Mixed Parameter Types
```python
def mixed_function(pos1, pos2, *args, default1="default", **kwargs):
    # pos1, pos2: required positional parameters
    # *args: variable positional arguments
    # default1: default parameter
    # **kwargs: variable keyword arguments
    pass

# Call with mixed arguments
mixed_function(1, 2, 3, 4, 5, default1="custom", key1="value1", key2="value2")
```

## Return Values

### Returning a Single Value
```python
def square(number):
    return number ** 2

result = square(5)  # 25
```

### Returning Multiple Values
```python
def get_dimensions(radius):
    diameter = radius * 2
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius ** 2
    return diameter, circumference, area

# Return values can be assigned to multiple variables
d, c, a = get_dimensions(5)

# Or captured as a tuple
dimensions = get_dimensions(5)
diameter = dimensions[0]
```

### Returning Different Values Based on Conditions
```python
def get_grade(score):
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

grade = get_grade(85)  # "B"
```

### Returning None
```python
def greet_user(name):
    print(f"Hello, {name}!")
    # No return statement, implicitly returns None

result = greet_user("Alice")  # result will be None
```

## Variable Scope

### Local Variables
```python
def my_function():
    # x is a local variable
    x = 10
    print(f"Inside function: x = {x}")

my_function()
# print(x)  # Error: x is not defined outside the function
```

### Global Variables
```python
# y is a global variable
y = 20

def my_function():
    # Accessing a global variable
    print(f"Inside function: y = {y}")

my_function()
print(f"Outside function: y = {y}")
```

### Modifying Global Variables
```python
counter = 0

def increment():
    # Using the global keyword to modify the global variable
    global counter
    counter += 1
    print(f"Counter is now {counter}")

increment()  # Counter is now 1
increment()  # Counter is now 2
```

### Variable Shadowing
```python
x = "global"

def test():
    # This creates a new local variable, not modifying the global one
    x = "local"
    print(f"Inside function: x = {x}")

test()  # Inside function: x = local
print(f"Outside function: x = {x}")  # Outside function: x = global
```

## Advanced Function Concepts

### Docstrings
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access the docstring
help(calculate_area)
# or
print(calculate_area.__doc__)
```

### Lambda Functions (Anonymous Functions)
```python
# Basic lambda function
square = lambda x: x ** 2
result = square(5)  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
result = add(3, 4)  # 7

# Lambda with if-else (conditional expression)
is_even = lambda x: True if x % 2 == 0 else False
result = is_even(4)  # True
```

### Higher-Order Functions
```python
# Function that takes a function as an argument
def apply_function(func, value):
    return func(value)

# Use with different functions
result1 = apply_function(lambda x: x ** 2, 5)  # 25 (square)
result2 = apply_function(lambda x: x + 10, 5)  # 15 (add 10)

# Function that returns a function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Create and use specialized functions
double = create_multiplier(2)
triple = create_multiplier(3)
result1 = double(5)  # 10
result2 = triple(5)  # 15
```

### Built-in Higher-Order Functions

#### map()
```python
# Apply a function to each item in an iterable
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
# Convert result to list to display
squared_list = list(squared)  # [1, 4, 9, 16, 25]
```

#### filter()
```python
# Filter items based on a function that returns boolean
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_list = list(even_numbers)  # [2, 4, 6, 8, 10]
```

#### sorted() with key function
```python
# Sort an iterable based on values returned by a key function
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
# Sort by age (second element in tuple)
sorted_by_age = sorted(people, key=lambda person: person[1])
# [("Charlie", 20), ("Alice", 25), ("Bob", 30)]
```

## Recursive Functions

### Basic Recursion
```python
def factorial(n):
    """Calculate the factorial of n using recursion."""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

result = factorial(5)  # 5 * 4 * 3 * 2 * 1 = 120
```

### Recursive Function Components
1. **Base Case**: The condition where the function stops calling itself
2. **Recursive Case**: The function calls itself with a modified argument

```python
def countdown(n):
    # Base case
    if n <= 0:
        print("Blastoff!")
        return
    # Recursive case
    else:
        print(n)
        countdown(n-1)  # Call with a smaller argument

countdown(5)  # Prints: 5, 4, 3, 2, 1, Blastoff!
```

## Best Practices

1. **Use descriptive function names**: Choose names that reflect what the function does
   ```python
   # Good
   def calculate_area(length, width):
       return length * width
   
   # Less clear
   def calc(l, w):
       return l * w
   ```

2. **Write clear docstrings**: Document what the function does, its parameters, and return values
   ```python
   def get_full_name(first_name, last_name):
       """
       Combine first and last name into a properly formatted full name.
       
       Args:
           first_name (str): The person's first name
           last_name (str): The person's last name
           
       Returns:
           str: The formatted full name (First Last)
       """
       return f"{first_name} {last_name}"
   ```

3. **Follow the Single Responsibility Principle**: Each function should do one thing well
   ```python
   # Better: Two functions with clear responsibilities
   def read_data(file_path):
       # Code to read data
       
   def process_data(data):
       # Code to process data
   
   # Less clear: One function doing multiple things
   def read_and_process(file_path):
       # Code to read and process data
   ```

4. **Use default values appropriately**: Make the most common use case the simplest
   ```python
   # Default parameters make the common case simpler
   def connect_to_database(host="localhost", port=3306, user="admin"):
       # Connection code
   
   # Most common use case is now simplest
   connect_to_database()  # Uses all defaults
   connect_to_database(port=5000)  # Customize just one parameter
   ```

5. **Return results instead of printing**: Functions should usually return values, not print them
   ```python
   # Better - returns a value that can be used elsewhere
   def calculate_area(radius):
       return 3.14159 * radius ** 2
   
   # Less flexible - only prints the result
   def print_area(radius):
       print(3.14159 * radius ** 2)
   ```

6. **Be consistent with return values**: Return similar types for all function exit points
   ```python
   # Consistent return types
   def find_user(user_id):
       if user_exists(user_id):
           return get_user_data(user_id)  # Returns user data
       else:
           return None  # Still returns a value (None)
   
   # Inconsistent return types (harder to use)
   def find_user_bad(user_id):
       if user_exists(user_id):
           return get_user_data(user_id)  # Returns user data
       else:
           print("User not found")  # Returns None implicitly
   ```

Remember that functions are a key building block for modular, maintainable code. Well-designed functions make your code more readable, reusable, and easier to test.