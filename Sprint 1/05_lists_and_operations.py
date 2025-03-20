# ========================================================
# Python Journey: Module 1 - Lists and Operations
# ========================================================
# This file covers how to work with lists in Python, including
# creating lists, accessing elements, and performing common operations.
# ========================================================

print("=" * 50)
print("Python Lists and Operations")
print("=" * 50)

# ------------------------------------------------------
# INTRODUCTION TO LISTS
# ------------------------------------------------------
# Lists are ordered collections of items that can store different
# data types. They are mutable (can be changed after creation)
# and are one of Python's most versatile data structures.
# ------------------------------------------------------

print("\nINTRODUCTION TO LISTS:")

# Creating lists
fruits = ["apple", "banana", "cherry", "date"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

# Printing lists
print(f"Fruits list: {fruits}")
print(f"Numbers list: {numbers}")
print(f"Mixed data types list: {mixed}")
print(f"Empty list: {empty_list}")

# List length
print(f"Number of fruits: {len(fruits)}")

# ------------------------------------------------------
# ACCESSING LIST ELEMENTS
# ------------------------------------------------------
# You can access individual elements in a list using indexing,
# and you can extract portions of a list using slicing.
# ------------------------------------------------------

print("\nACCESSING LIST ELEMENTS:")

# Indexing (accessing individual elements)
# Remember: Python uses zero-based indexing (the first element is at index 0)
print("\n--- Indexing ---")
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing starts from the end
print(f"Second-to-last fruit: {fruits[-2]}")

# Slicing (accessing a range of elements)
print("\n--- Slicing ---")
print(f"First two fruits: {fruits[0:2]}")  # From index 0 up to (but not including) index 2
print(f"All fruits except the first one: {fruits[1:]}")  # From index 1 to the end
print(f"All fruits up to the last one: {fruits[:-1]}")  # From start up to (not including) the last item
print(f"All fruits: {fruits[:]}") # From start to end (creates a copy)

# Slicing with step
print(f"Every other fruit: {fruits[::2]}")  # Start:end:step
print(f"Fruits in reverse order: {fruits[::-1]}")  # Negative step reverses the order

# ------------------------------------------------------
# MODIFYING LISTS
# ------------------------------------------------------
# Lists are mutable, meaning you can change their content
# after creation by adding, removing, or modifying elements.
# ------------------------------------------------------

print("\nMODIFYING LISTS:")

# Changing an element
colors = ["red", "green", "blue", "yellow"]
print(f"Original colors: {colors}")

colors[1] = "purple"  # Change the second element
print(f"After changing 'green' to 'purple': {colors}")

# Adding elements
print("\n--- Adding elements ---")
print(f"Original colors: {colors}")

colors.append("orange")  # Add to the end of the list
print(f"After append('orange'): {colors}")

colors.insert(2, "pink")  # Insert at specific position (index 2)
print(f"After insert(2, 'pink'): {colors}")

more_colors = ["brown", "gray"]
colors.extend(more_colors)  # Add all elements from another list
print(f"After extend({more_colors}): {colors}")

# Removing elements
print("\n--- Removing elements ---")
print(f"Current colors: {colors}")

removed_color = colors.pop()  # Remove and return the last element
print(f"Removed color (pop): {removed_color}")
print(f"After pop(): {colors}")

removed_color = colors.pop(1)  # Remove and return element at index 1
print(f"Removed color (pop(1)): {removed_color}")
print(f"After pop(1): {colors}")

colors.remove("pink")  # Remove first occurrence of a specific value
print(f"After remove('pink'): {colors}")

# Be careful with remove() - it raises an error if the value isn't found
# Example: colors.remove("black") would raise a ValueError

# Clear a list
numbers_copy = numbers.copy()  # Make a copy so we don't modify the original
print(f"Numbers copy before clear: {numbers_copy}")
numbers_copy.clear()  # Remove all elements
print(f"Numbers copy after clear: {numbers_copy}")

# ------------------------------------------------------
# COMMON LIST OPERATIONS
# ------------------------------------------------------
# Python provides many useful operations and methods for
# working with lists efficiently.
# ------------------------------------------------------

print("\nCOMMON LIST OPERATIONS:")

# Concatenating lists
print("\n--- Concatenating lists ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"{list1} + {list2} = {combined}")

# Repeating lists
print("\n--- Repeating lists ---")
repeated = list1 * 3
print(f"{list1} * 3 = {repeated}")

# Finding elements
print("\n--- Finding elements ---")
scores = [85, 92, 78, 90, 92, 85, 70]
print(f"Scores: {scores}")
print(f"First occurrence of 92 is at index: {scores.index(92)}")
print(f"Count of 85 in the list: {scores.count(85)}")

# Checking if an element exists
print("\n--- Checking membership ---")
print(f"Is 90 in scores? {'yes' if 90 in scores else 'no'}")
print(f"Is 100 in scores? {'yes' if 100 in scores else 'no'}")

# Sorting
print("\n--- Sorting ---")
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Unsorted list: {unsorted}")

# Sort the list in-place (modifies the original list)
unsorted.sort()
print(f"After sort(): {unsorted}")

# Sort in descending order
unsorted.sort(reverse=True)
print(f"After sort(reverse=True): {unsorted}")

# sorted() function (returns a new sorted list, doesn't modify the original)
names = ["Charlie", "Alice", "Bob", "David"]
print(f"Original names: {names}")
sorted_names = sorted(names)
print(f"sorted(names): {sorted_names}")
print(f"Original names (unchanged): {names}")

# Reversing a list
print("\n--- Reversing ---")
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")
numbers.reverse()  # In-place reversal
print(f"After reverse(): {numbers}")

# ------------------------------------------------------
# LIST COMPREHENSIONS
# ------------------------------------------------------
# List comprehensions provide a concise way to create lists
# based on existing lists or other iterables.
# ------------------------------------------------------

print("\nLIST COMPREHENSIONS:")

# Basic list comprehension
print("\n--- Basic list comprehension ---")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares using comprehension: {squares}")

# Equivalent using a for loop
squares_loop = []
for x in numbers:
    squares_loop.append(x**2)
print(f"Squares using loop: {squares_loop}")

# List comprehension with condition
print("\n--- List comprehension with condition ---")
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# More complex example
print("\n--- More complex example ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
long_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print(f"Original fruits: {fruits}")
print(f"Long fruits (uppercased): {long_fruits}")

# ------------------------------------------------------
# NESTED LISTS (2D LISTS)
# ------------------------------------------------------
# Lists can contain other lists, creating multi-dimensional
# data structures useful for representing grids, matrices, etc.
# ------------------------------------------------------

print("\nNESTED LISTS (2D LISTS):")

# Creating a 2D list (a list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix (2D list): {matrix}")

# Accessing elements in a 2D list
print(f"Element at row 0, column 1: {matrix[0][1]}")  # Should be 2
print(f"Element at row 2, column 2: {matrix[2][2]}")  # Should be 9

# Traversing a 2D list
print("\nTraversing a matrix:")
for row in matrix:
    for item in row:
        print(item, end=" ")  # Print items in the row
    print()  # Move to next line after each row

# ------------------------------------------------------
# EXERCISE: LIST MANIPULATOR
# ------------------------------------------------------
# Practice working with lists by implementing various operations
# on a sample list.
#
# Instructions:
# 1. Uncomment the code below
# 2. Implement the requested operations
# 3. Run the file to see your results
# ------------------------------------------------------

print("\n--- EXERCISE: LIST MANIPULATOR ---")

# # Create a list of your favorite hobbies
# hobbies = []  # Add at least 3 hobbies
#
# # Print the list and its length
# print(f"My hobbies: {hobbies}")
# print(f"I have {len(hobbies)} hobbies")
#
# # Add a new hobby to the end of the list
# # Your code here
#
# # Insert a hobby at the beginning of the list
# # Your code here
#
# # Remove one hobby from the list
# # Your code here
#
# # Print the updated list
# print(f"Updated hobbies: {hobbies}")
#
# # Create a new list containing only hobbies with more than 5 letters
# # Hint: Use a list comprehension
# # Your code here
#
# # Create a list of tuples where each tuple contains:
# # (hobby, length_of_hobby)
# # Hint: Use a list comprehension
# # Your code here

print("\n" + "=" * 50)
print("🏆 ACHIEVEMENT UNLOCKED: LIST MASTER 🏆")
print("You've learned how to work with Python lists!")
print("=" * 50)

print("\nWhat's next? Continue to 06_functions.py")