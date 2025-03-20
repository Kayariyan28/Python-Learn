# ========================================================
# Python Journey: Realm 1, Module 2 - Basic Error Handling
# ========================================================
# This file covers how to handle errors and exceptions in Python,
# a crucial skill for writing robust and reliable programs.
# ========================================================

print("=" * 60)
print("Python Journey: Basic Error Handling")
print("=" * 60)

# ------------------------------------------------------
# WHAT ARE ERRORS AND EXCEPTIONS?
# ------------------------------------------------------
# In Python, errors are problems that occur in your program that prevent it
# from running or cause it to stop unexpectedly. There are two main types:
#
# 1. Syntax Errors: Errors in the structure of your code that prevent
#    the program from running at all.
#
# 2. Exceptions: Errors that occur during execution (runtime) when 
#    something unexpected happens.
#
# Handling exceptions allows your program to continue running even when 
# things go wrong, making your programs more robust and user-friendly.
# ------------------------------------------------------

print("\nUNDERSTANDING ERRORS AND EXCEPTIONS")
print("-" * 40)

# Let's deliberately cause some common errors to see what they look like

# Uncomment the line below to see a SyntaxError
# print("This will cause a syntax error because there's no closing parenthesis

print("Example 1: Common exceptions you might encounter:")

# Trying to divide by zero - causes ZeroDivisionError
try:
    result = 10 / 0
    print(result)  # This line never executes
except ZeroDivisionError:
    print("• ZeroDivisionError: Division by zero is not allowed in mathematics")

# Trying to access a non-existent index - causes IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])  # Index 10 doesn't exist
except IndexError:
    print("• IndexError: Trying to access an index that doesn't exist")

# Trying to access a non-existent key - causes KeyError
try:
    my_dict = {"name": "Alice", "age": 30}
    print(my_dict["address"])  # Key 'address' doesn't exist
except KeyError:
    print("• KeyError: Trying to access a dictionary key that doesn't exist")

# Trying to convert an invalid string to a number - causes ValueError
try:
    number = int("hello")  # 'hello' can't be converted to an integer
except ValueError:
    print("• ValueError: Can't convert a non-numeric string to a number")

# Trying to use a name that hasn't been defined - causes NameError
try:
    print(undefined_variable)  # This variable doesn't exist
except NameError:
    print("• NameError: Using a variable or function name that wasn't defined")

# Trying to use a module that isn't imported - causes ModuleNotFoundError
try:
    import non_existent_module
except ModuleNotFoundError:
    print("• ModuleNotFoundError: Trying to import a module that doesn't exist")

print("\nWithout error handling, any of these exceptions would crash your program!")

# ------------------------------------------------------
# BASIC ERROR HANDLING WITH TRY-EXCEPT
# ------------------------------------------------------
# The try-except block allows you to "try" to execute code that might cause
# an exception, and "except" (catch) any exceptions that occur.
#
# Basic structure:
# try:
#     # Code that might cause an exception
# except:
#     # Code that executes if an exception occurs
# ------------------------------------------------------

print("\nBASIC ERROR HANDLING WITH TRY-EXCEPT")
print("-" * 40)

print("Example 2: Handling a potential division by zero:")

# Without error handling
print("\nWithout error handling:")
def divide_without_handling(a, b):
    """Attempt to divide a by b without error handling."""
    return a / b

# Let's try with valid inputs first
print("10 / 2 =", divide_without_handling(10, 2))  # Works fine

# Let's uncomment this to see what happens with invalid input
# print("10 / 0 =", divide_without_handling(10, 0))  # This would crash the program

# With error handling
print("\nWith error handling:")
def divide_with_handling(a, b):
    """Attempt to divide a by b with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Now let's try both valid and invalid inputs
print("10 / 2 =", divide_with_handling(10, 2))  # Still works fine
print("10 / 0 =", divide_with_handling(10, 0))  # Now handles the error gracefully

# Practice: Write your own function that handles a potential error
print("\nPractice: Try to handle a potential IndexError when accessing a list:")

# TODO: Uncomment and complete this function
# def get_element(lst, index):
#     """Return the element at the given index, or a message if the index is invalid."""
#     try:
#         # Your code here to get the element
#     except IndexError:
#         # Your code here to handle the error
#
# my_list = ["apple", "banana", "cherry"]
# print(get_element(my_list, 1))  # Should print: banana
# print(get_element(my_list, 5))  # Should print an error message instead of crashing

# Solution to the practice exercise
def get_element(lst, index):
    """Return the element at the given index, or a message if the index is invalid."""
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range for a list of length {len(lst)}"

my_list = ["apple", "banana", "cherry"]
print(get_element(my_list, 1))  # Should print: banana
print(get_element(my_list, 5))  # Should print an error message

# ------------------------------------------------------
# HANDLING MULTIPLE EXCEPTIONS
# ------------------------------------------------------
# You can catch different types of exceptions and handle them differently
# by using multiple except blocks or by catching multiple exception types
# in a single except block.
# ------------------------------------------------------

print("\nHANDLING MULTIPLE EXCEPTIONS")
print("-" * 40)

print("Example 3: Handling different types of exceptions separately:")

def process_data(data, index, divisor):
    """Process data by accessing an element and dividing it by a divisor."""
    try:
        value = data[index]  # Might cause IndexError
        result = value / divisor  # Might cause ZeroDivisionError or TypeError
        return result
    except IndexError:
        return f"Error: Index {index} is out of range"
    except ZeroDivisionError:
        return f"Error: Cannot divide {value} by zero"
    except TypeError:
        return f"Error: Cannot divide {value} by {divisor} (invalid types)"

# Test the function with different scenarios
data = [10, 20, 30, 40]

print("Valid case:", process_data(data, 2, 2))  # Should work fine
print("Invalid index:", process_data(data, 10, 2))  # Should catch IndexError
print("Zero division:", process_data(data, 1, 0))  # Should catch ZeroDivisionError
print("Type error:", process_data(data, 1, "2"))  # Should catch TypeError

print("\nExample 4: Catching multiple exception types in a single except block:")

def safe_operation(a, b):
    """Perform a division operation safely."""
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError) as error:
        # The 'as error' part captures the exception object for inspection
        return f"Operation failed: {type(error).__name__} - {error}"

print("Valid operation:", safe_operation(10, 2))
print("Division by zero:", safe_operation(10, 0))
print("Type error:", safe_operation(10, "2"))

# ------------------------------------------------------
# USING ELSE AND FINALLY WITH TRY-EXCEPT
# ------------------------------------------------------
# The try-except block can be extended with two additional clauses:
#
# 1. else: Code that executes if no exceptions occur
# 2. finally: Code that always executes, regardless of whether an exception occurred
#
# Full structure:
# try:
#     # Code that might cause an exception
# except ExceptionType:
#     # Code that executes if an exception occurs
# else:
#     # Code that executes if no exception occurs
# finally:
#     # Code that always executes, with or without exceptions
# ------------------------------------------------------

print("\nUSING ELSE AND FINALLY WITH TRY-EXCEPT")
print("-" * 40)

print("Example 5: Using 'else' clause:")

def read_number_from_string(string):
    """Convert a string to a number if possible."""
    try:
        number = float(string)
    except ValueError:
        print(f"'{string}' cannot be converted to a number.")
        return None
    else:
        # This only runs if no exception was raised in the try block
        print(f"Successfully converted '{string}' to {number}.")
        return number

print(read_number_from_string("123.45"))  # Should succeed
print(read_number_from_string("hello"))   # Should fail

print("\nExample 6: Using 'finally' clause:")

def open_and_read_file(filename):
    """Open a file and read its contents safely."""
    try:
        print(f"Trying to open {filename}...")
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    finally:
        # This always runs, whether an exception occurred or not
        print(f"File operation attempt completed for {filename}.")
        # We should also close the file here if it was opened
        # but that would require additional checks

print(open_and_read_file("existing_file.txt"))  # This will fail since the file doesn't exist
print(open_and_read_file("non_existent_file.txt"))  # This will also fail

print("\nExample 7: Complete try-except-else-finally structure:")

def divide_numbers_complete(a, b):
    """Demonstrate a complete try-except-else-finally structure."""
    print(f"Attempting to divide {a} by {b}...")
    
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Division operation completed, successful or not.")

print(divide_numbers_complete(10, 2))  # Should succeed
print(divide_numbers_complete(10, 0))  # Should fail

# ------------------------------------------------------
# RAISING EXCEPTIONS
# ------------------------------------------------------
# Sometimes you want to deliberately raise an exception when a certain
# condition is met. This is done using the 'raise' statement.
# ------------------------------------------------------

print("\nRAISING EXCEPTIONS")
print("-" * 40)

print("Example 8: Raising exceptions deliberately:")

def calculate_square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        # Deliberately raise an exception for negative numbers
        raise ValueError("Cannot calculate square root of a negative number")
    
    return number ** 0.5

try:
    print("Square root of 16:", calculate_square_root(16))
    print("Square root of -4:", calculate_square_root(-4))  # This will raise an exception
except ValueError as e:
    print(f"Caught an error: {e}")

print("\nExample 9: Re-raising exceptions after handling them:")

def process_age(age):
    """Process a person's age, but only if it's valid."""
    try:
        # Convert the age to an integer
        age = int(age)
        
        # Age must be positive
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        # Age must be reasonable
        if age > 150:
            raise ValueError("Age is unreasonably high")
            
    except ValueError as e:
        # If it's our custom error message, handle it specially
        if "Age cannot be negative" in str(e) or "Age is unreasonably high" in str(e):
            print(f"Invalid age provided: {e}")
            return None
        else:
            # Re-raise the original exception for other ValueError cases
            print("Caught a different ValueError, re-raising it...")
            raise
    
    # If we got here, the age is valid
    return f"Processing age: {age}"

# Test with various inputs
try:
    print(process_age(25))      # Valid age
    print(process_age(-5))      # Negative age
    print(process_age(200))     # Unreasonably high age
    print(process_age("abc"))   # Non-numeric input
except ValueError as e:
    print(f"Main program caught: {e}")

# ------------------------------------------------------
# CREATING CUSTOM EXCEPTIONS
# ------------------------------------------------------
# Python allows you to define your own exception types by creating
# classes that inherit from the built-in Exception class or one of
# its subclasses.
# ------------------------------------------------------

print("\nCREATING CUSTOM EXCEPTIONS")
print("-" * 40)

print("Example 10: Creating and using a custom exception:")

# Define a custom exception
class InvalidAgeError(Exception):
    """Exception raised for invalid age values."""
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        # Call the base class constructor with the parameters it needs
        super().__init__(f"{message}: {age}")

def validate_age(age):
    """Validate a person's age using a custom exception."""
    try:
        age = int(age)
    except ValueError:
        raise InvalidAgeError(age, "Age must be a number")
    
    if age < 0:
        raise InvalidAgeError(age, "Age cannot be negative")
    
    if age > 150:
        raise InvalidAgeError(age, "Age is unreasonably high")
    
    return f"Age {age} is valid"

# Test with various inputs
for test_age in [25, -5, 200, "abc"]:
    try:
        print(validate_age(test_age))
    except InvalidAgeError as e:
        print(f"Caught custom exception: {e}")

# ------------------------------------------------------
# PRACTICAL ERROR HANDLING PATTERNS
# ------------------------------------------------------
# Here are some common patterns and best practices for error handling in Python.
# ------------------------------------------------------

print("\nPRACTICAL ERROR HANDLING PATTERNS")
print("-" * 40)

print("Example 11: Catching all exceptions (use with caution):")

def risky_operation(value):
    """A function that could fail in multiple ways."""
    try:
        result = 100 / value
        result += int("abc")  # This will always fail
        return result
    except Exception as e:
        # This will catch ALL exceptions - use with caution!
        # It's generally better to catch specific exceptions
        print(f"Operation failed: {type(e).__name__} - {e}")
        return None

print(risky_operation(5))  # Will fail with ValueError from int("abc")
print(risky_operation(0))  # Will fail with ZeroDivisionError

print("\nExample 12: Logging exceptions:")

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_with_logging(a, b):
    """Divide two numbers with error logging."""
    try:
        result = a / b
        logging.info(f"Successfully divided {a} by {b} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Failed to divide {a} by {b}: Division by zero")
        return None
    except Exception as e:
        logging.error(f"Unexpected error dividing {a} by {b}: {type(e).__name__} - {e}")
        return None

print(divide_with_logging(10, 2))  # Should succeed and log success
print(divide_with_logging(10, 0))  # Should fail and log error

print("\nExample 13: Handling expected vs. unexpected exceptions:")

def process_user_input(input_string):
    """Process user input, handling expected errors explicitly."""
    try:
        # Convert to number - might cause ValueError
        number = float(input_string)
        
        # Do further processing - might cause other exceptions
        result = 100 / number  # Might cause ZeroDivisionError
        
        return f"Processed result: {result}"
        
    except ValueError:
        # Expected error - handle specifically
        return "Error: Please enter a valid number"
    except ZeroDivisionError:
        # Another expected error - handle specifically
        return "Error: Cannot process zero values"
    except Exception as e:
        # Unexpected error - log and provide a generic message
        logging.error(f"Unexpected error processing '{input_string}': {type(e).__name__} - {e}")
        return "An unexpected error occurred. Please try again."

# Test with various inputs
test_inputs = ["42", "abc", "0", "0.5"]
for input_string in test_inputs:
    print(f"Input: '{input_string}' -> {process_user_input(input_string)}")

# ------------------------------------------------------
# EXERCISE: ERROR HANDLING CHALLENGE
# ------------------------------------------------------
# Practice your error handling skills with a more complex example.
# ------------------------------------------------------

print("\nEXERCISE: ERROR HANDLING CHALLENGE")
print("-" * 40)

print("Create a function called 'safe_calculator' that can perform basic operations:")
print("- The function should accept three parameters: a, operation, b")
print("- Valid operations are: +, -, *, /, ** (power)")
print("- Handle all potential errors gracefully")
print("- Return the result of the operation or an appropriate error message")

# TODO: Implement the safe_calculator function here
def safe_calculator(a, operation, b):
    """
    Perform basic arithmetic operations safely.
    
    Args:
        a: First operand
        operation: String representing the operation (+, -, *, /, **)
        b: Second operand
    
    Returns:
        Result of the operation or an error message
    """
    # First, try to convert the operands to numbers if they're not already
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Error: Operands must be numbers"
    
    # Check if the operation is valid
    valid_operations = ['+', '-', '*', '/', '**']
    if operation not in valid_operations:
        return f"Error: '{operation}' is not a valid operation. Use one of: {', '.join(valid_operations)}"
    
    # Perform the operation
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                return "Error: Division by zero"
            return a / b
        elif operation == '**':
            # Check if we might get a complex result
            if a < 0 and not b.is_integer():
                return "Error: Cannot raise negative number to a fractional power (would result in a complex number)"
            return a ** b
    except Exception as e:
        return f"Error: Operation failed - {type(e).__name__} - {e}"

# Test cases
test_cases = [
    (10, '+', 5),      # Basic addition
    (10, '-', 5),      # Basic subtraction
    (10, '*', 5),      # Basic multiplication
    (10, '/', 5),      # Basic division
    (10, '**', 2),     # Power operation
    (10, '/', 0),      # Division by zero
    (10, '%', 5),      # Invalid operation
    ('abc', '+', 5),   # Non-numeric first operand
    (10, '+', 'xyz'),  # Non-numeric second operand
    (-2, '**', 0.5)    # Negative number raised to fractional power
]

print("\nTesting the safe_calculator function:")
for a, op, b in test_cases:
    result = safe_calculator(a, op, b)
    print(f"{a} {op} {b} = {result}")

# ------------------------------------------------------
# REAL-WORLD APPLICATION: FILE PROCESSING
# ------------------------------------------------------
# Let's apply error handling to a real-world scenario: reading and
# processing a file that might not exist or might have invalid content.
# ------------------------------------------------------

print("\nREAL-WORLD APPLICATION: FILE PROCESSING")
print("-" * 40)

def calculate_average_from_file(filename):
    """
    Read numbers from a file and calculate their average.
    
    Args:
        filename: The name of the file to read
    
    Returns:
        The average of the numbers in the file, or an error message
    """
    try:
        # Try to open the file
        with open(filename, 'r') as file:
            # Read all lines
            lines = file.readlines()
            
            # Check if the file is empty
            if not lines:
                return "File is empty"
            
            # Try to convert each line to a number
            total = 0
            count = 0
            
            for i, line in enumerate(lines, 1):
                try:
                    # Strip whitespace and convert to float
                    number = float(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    # Skip lines that are not valid numbers
                    print(f"Warning: Line {i} ('{line.strip()}') is not a valid number. Skipping.")
            
            # Check if we found any valid numbers
            if count == 0:
                return "No valid numbers found in the file"
            
            # Calculate and return the average
            return total / count
            
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read file '{filename}'"
    except Exception as e:
        return f"Error: {type(e).__name__} - {e}"

# Test the function with various scenarios
print("Testing calculate_average_from_file function:")

# Create a test file with valid numbers
with open("valid_numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n50")

# Create a test file with some invalid entries
with open("mixed_numbers.txt", "w") as file:
    file.write("10\n20\nNot a number\n40\n50")

# Test cases
print(f"Valid file: {calculate_average_from_file('valid_numbers.txt')}")
print(f"Mixed file: {calculate_average_from_file('mixed_numbers.txt')}")
print(f"Non-existent file: {calculate_average_from_file('does_not_exist.txt')}")

# ------------------------------------------------------
# SUMMARY AND BEST PRACTICES
# ------------------------------------------------------
# Here's a summary of error handling concepts and best practices.
# ------------------------------------------------------

print("\nSUMMARY AND BEST PRACTICES")
print("-" * 40)

print("""
Key Error Handling Concepts:
1. Use try-except blocks to handle potential exceptions
2. Catch specific exceptions rather than using bare except
3. Use else for code that should only run if no exceptions occur
4. Use finally for code that should always run
5. Raise exceptions when invalid conditions are detected
6. Create custom exceptions for your specific error cases
7. Log exceptions for debugging and monitoring

Best Practices:
1. Never use bare 'except:' without specifying the exception type
2. Keep your try blocks as small as possible
3. Don't suppress exceptions without handling them appropriately
4. Use custom exceptions to provide more meaningful error information
5. Use logging instead of print statements for errors in production code
6. Avoid catching Exception for specific errors (catch specific exceptions)
7. Document the exceptions your functions might raise
8. Handle exceptions at the appropriate level in your code

Remember: Good error handling makes your code more robust and user-friendly!
""")

# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each concept as you understand it:

Basic Concepts
[ ] Understanding different types of errors
[ ] Using try-except blocks
[ ] Handling specific exceptions
[ ] Using else and finally clauses
[ ] Raising exceptions
[ ] Creating custom exceptions

Advanced Concepts
[ ] Re-raising exceptions
[ ] Catching multiple exception types
[ ] Logging exceptions
[ ] Handling expected vs. unexpected exceptions
[ ] Using exceptions in real-world scenarios

Progress: [_____] 0% complete
""")

print("\nWhat's next? Continue learning about functions and more advanced Python concepts!")