# Python Journey: Realm 1, Module 3
# Scope, Namespaces, and Modules

# =============================================================================
# Part 1: Understanding Scope and Namespaces
# =============================================================================

"""
# 🔍 SCOPE AND NAMESPACES

In Python, understanding scope and namespaces is crucial for writing effective code.
Let's explore what these concepts mean and how they work.

## What is a Namespace?

A namespace is like a container that holds a set of identifiers (variable names, 
function names, etc.) and their corresponding objects. Think of it as a dictionary 
where the keys are the names and the values are the objects themselves.

## What is Scope?

Scope determines where in your program a particular name is visible and can be accessed.
The scope defines the portion of code where a name can be unambiguously referenced.

## 🧩 Types of Scopes in Python

Python has four main types of scopes:
1. Local scope: Names inside the current function
2. Enclosing scope: Names in the local scope of any enclosing functions
3. Global scope: Names at the top level of the module
4. Built-in scope: Names in the built-in modules (like print, len)

Let's explore these through examples:
"""

# -------- EXAMPLE 1: LOCAL AND GLOBAL SCOPE --------

# This is in the global scope
message = "Hello from global scope!"

def greet():
    # This is in the local scope of the greet function
    message = "Hello from local scope!"
    print(message)  # This will access the local message

print("Example 1: Local vs Global Scope")
print(message)  # Accesses the global message
greet()         # Calls the function, which accesses its local message
print(message)  # Still accesses the global message (unchanged)
print()

"""
Notice how the local `message` inside the function is separate from the global `message`.
Each scope maintains its own separate namespace.
"""

# -------- EXAMPLE 2: ACCESSING GLOBAL VARIABLES FROM LOCAL SCOPE --------

count = 0  # Global variable

def increment():
    global count  # This tells Python to use the global variable
    count += 1    # Now we're modifying the global variable
    print(f"Count inside function: {count}")

print("Example 2: Accessing Global Variables")
print(f"Count before: {count}")
increment()
print(f"Count after: {count}")  # The global variable was modified
print()

"""
The `global` keyword allows a function to access and modify a variable in the global scope.
Without it, Python would create a new local variable instead.
"""

# -------- EXAMPLE 3: ENCLOSING SCOPE (NESTED FUNCTIONS) --------

def outer_function():
    outer_var = "I'm in the outer function"
    
    def inner_function():
        inner_var = "I'm in the inner function"
        print(inner_var)
        print(outer_var)  # Can access variable from the enclosing scope
    
    inner_function()
    # print(inner_var)  # This would cause an error - inner_var is not accessible here

print("Example 3: Enclosing Scope")
outer_function()
print()

"""
The inner function can access variables from its enclosing function, but not vice versa.
"""

# -------- EXAMPLE 4: NONLOCAL VARIABLES --------

def counter_function():
    count = 0
    
    def increment():
        nonlocal count  # This tells Python to use the variable from the enclosing scope
        count += 1
        return count
    
    return increment  # Returns the inner function

print("Example 4: Nonlocal Variables")
counter = counter_function()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
print()

"""
The `nonlocal` keyword is similar to `global`, but it's used to access variables in the 
enclosing function scope rather than the global scope. This example also demonstrates a 
closure - the inner function "remembers" the environment in which it was created.
"""

# -------- EXAMPLE 5: NAME LOOKUP RULES --------

x = "global x"

def test():
    y = "local y"
    print(x)  # Python looks for x in the local scope, then in the global scope
    print(y)  # Python finds y in the local scope

print("Example 5: Name Lookup Rules")
test()
# print(y)  # This would cause an error - y is not in the global scope
print()

"""
Python follows the LEGB rule for name lookups:
1. Local scope (current function)
2. Enclosing scope (any enclosing functions)
3. Global scope (top-level of module)
4. Built-in scope (Python's built-in names)

If a name is not found in any of these scopes, Python raises a NameError.
"""

# -------- PRACTICE EXERCISE 1 --------
"""
🧠 PRACTICE TIME!

Predict what will be printed by the following code, then run it to check your answer.
Can you explain why?
"""

def scope_test():
    def local_function():
        value = "local"
    
    def nonlocal_function():
        nonlocal value
        value = "nonlocal"
    
    def global_function():
        global value
        value = "global"
    
    value = "test"
    local_function()
    print(f"After local assignment: {value}")
    nonlocal_function()
    print(f"After nonlocal assignment: {value}")
    global_function()
    print(f"After global assignment: {value}")

print("Practice Exercise 1")
scope_test()
print(f"Global value: {value}")
print()

"""
Explanation:
- `local_function()` creates a new local variable that doesn't affect the enclosing scope.
- `nonlocal_function()` modifies the variable in the enclosing scope.
- `global_function()` modifies the global variable, not the one in the enclosing scope.
- After the function exits, we can see the global value was set.
"""

# =============================================================================
# Part 2: Importing and Using Modules
# =============================================================================

"""
# 📦 MODULES IN PYTHON

Modules are files containing Python code that can be imported and used in other Python files.
They help organize code into reusable, logical units.

## Types of Modules

1. **Built-in modules**: Come with Python (like `math`, `random`, `datetime`)
2. **Third-party modules**: Installed via pip (like `requests`, `pandas`, `numpy`)
3. **Custom modules**: Created by you or your team

## Ways to Import Modules
"""

# -------- EXAMPLE 6: BASIC IMPORTS --------

# Import the entire module
import math

# Now we can use functions from the math module with dot notation
print("Example 6: Basic Imports")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print()

# -------- EXAMPLE 7: IMPORTING SPECIFIC ITEMS --------

# Import only specific items from a module
from random import randint, choice

print("Example 7: Importing Specific Items")
print(f"Random number between 1 and 10: {randint(1, 10)}")
print(f"Random choice from a list: {choice(['apple', 'banana', 'cherry'])}")
print()

"""
Notice the difference:
- With `import math`, we use `math.sqrt()`
- With `from random import randint`, we use just `randint()`
"""

# -------- EXAMPLE 8: IMPORT WITH ALIAS --------

# Import a module with an alias
import datetime as dt

print("Example 8: Import with Alias")
print(f"Current date and time: {dt.datetime.now()}")
print()

"""
Using aliases can make your code more concise, especially with modules that have long names.
"""

# -------- EXAMPLE 9: IMPORTING EVERYTHING (USE WITH CAUTION) --------

# Import all names from a module (not recommended in most cases)
from math import *

print("Example 9: Importing Everything")
print(f"Cosine of 0: {cos(0)}")  # Notice we don't need math.cos
print()

"""
⚠️ CAUTION: Using `from module import *` is generally not recommended as it 
can lead to name conflicts and makes it unclear where functions are coming from.
"""

# -------- EXAMPLE 10: CREATING AND IMPORTING CUSTOM MODULES --------

"""
To create your own module:
1. Create a new .py file (e.g., my_module.py)
2. Write functions, classes, variables, etc.
3. Import it in other files

Let's imagine we have a file called "calculator.py" with these contents:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

PI = 3.14159
```

We could import and use it like this:

```python
import calculator

print(calculator.add(5, 3))       # 8
print(calculator.subtract(10, 4)) # 6
print(calculator.PI)              # 3.14159
```

Or:

```python
from calculator import add, subtract

print(add(5, 3))       # 8
print(subtract(10, 4)) # 6
```
"""

# -------- EXAMPLE 11: MODULE SEARCH PATH --------

import sys

print("Example 11: Module Search Path")
print("Python looks for modules in these locations:")
for path in sys.path:
    print(f"- {path}")
print()

"""
When you import a module, Python searches for it in the directories listed in `sys.path`.
This includes:
1. The directory of the script being run
2. The Python standard library directories
3. The site-packages directory (where third-party packages are installed)
"""

# -------- EXAMPLE 12: THE dir() FUNCTION --------

print("Example 12: The dir() Function")
print("Names in the math module:")
import math
for name in dir(math)[:10]:  # Print just the first 10 for brevity
    print(f"- {name}")
print("... (and more)")
print()

"""
The `dir()` function returns a list of names in a module. It's a great way to explore
what's available in a module.
"""

# -------- PRACTICE EXERCISE 2 --------
"""
🧠 PRACTICE TIME!

1. Import the 'time' module and use it to make your program pause for 2 seconds.
2. Import only the 'randrange' function from the random module and use it to 
   generate a random number between 0 and 100.
"""

print("Practice Exercise 2")
# Your solution here
import time
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done waiting!")

from random import randrange
random_number = randrange(101)  # 0 to 100
print(f"Random number between 0 and 100: {random_number}")
print()

# -------- CHALLENGE PROJECT: CREATING A SIMPLE MODULE SYSTEM --------
"""
🏆 CHALLENGE PROJECT: Module Explorer

Create a simple program that helps the user explore Python's built-in modules.
The program should:
1. Allow the user to enter the name of a built-in module
2. Display basic information about the module
3. List some of the functions or variables available in that module
"""

def module_explorer():
    print("="*50)
    print("MODULE EXPLORER")
    print("="*50)
    print("Discover what's inside Python's built-in modules!")
    print()
    
    while True:
        module_name = input("Enter a module name (or 'quit' to exit): ").strip()
        
        if module_name.lower() == 'quit':
            break
        
        try:
            # Dynamically import the module
            module = __import__(module_name)
            
            print(f"\nModule: {module_name}")
            
            # Get the module's docstring
            doc = module.__doc__
            if doc:
                print(f"\nDescription: {doc.split('.')[0]}.")  # Just the first sentence
            
            # List some attributes and functions
            print("\nSome available names in this module:")
            names = dir(module)
            
            # Filter out private names (those starting with _)
            public_names = [name for name in names if not name.startswith('_')]
            
            # Display up to 10 names
            for name in sorted(public_names)[:10]:
                try:
                    attr = getattr(module, name)
                    if callable(attr):
                        print(f"- {name}() (function)")
                    else:
                        print(f"- {name} (variable)")
                except:
                    print(f"- {name}")
            
            if len(public_names) > 10:
                print(f"... and {len(public_names) - 10} more")
                
        except ImportError:
            print(f"Module '{module_name}' not found. Try another name.")
        except Exception as e:
            print(f"Error exploring module: {e}")
        
        print("\n" + "-"*50 + "\n")

# Uncomment to run the module explorer:
# module_explorer()

# =============================================================================
# Summary and Key Takeaways
# =============================================================================
"""
🎯 KEY TAKEAWAYS

1. **Scope and Namespaces**
   - Python has local, enclosing, global, and built-in scopes
   - Use `global` to access global variables from functions
   - Use `nonlocal` to access variables from enclosing functions
   - Python uses the LEGB rule for name lookups

2. **Importing and Using Modules**
   - Modules help organize and reuse code
   - Various ways to import: `import module`, `from module import item`, etc.
   - Create your own modules by making .py files
   - Use `dir()` to explore module contents

🚀 NEXT STEPS

Now that you understand scope, namespaces, and modules, you're ready to:
- Create your own custom modules to organize your code
- Use Python's rich ecosystem of built-in and third-party modules
- Understand more complex code that uses different scopes and imports

Remember: Good code organization through proper use of scope and modules will make
your programs more maintainable, reusable, and easier to understand!
"""