# ========================================================
# Python Journey: Module 1 - Integration Challenge
# ========================================================
# This challenge combines all concepts from Module 1 into a
# comprehensive project that tests your Python skills.
# ========================================================

print("=" * 60)
print("Python Journey: Module 1 - Integration Challenge")
print("=" * 60)

# ------------------------------------------------------
# STUDENT DATA MANAGEMENT SYSTEM
# ------------------------------------------------------
# In this challenge, you'll create a Student Data Management System 
# that allows you to track and analyze student information and grades.
# This project integrates all Module 1 concepts:
# - Variables and Data Types
# - User Input and Output
# - Conditional Statements
# - Loops
# - Lists and List Operations
# - Functions
# ------------------------------------------------------

print("""
Welcome to the Student Data Management System
=============================================

In this project, you'll create a program that allows teachers to:
1. Add new students to the system
2. Record grades for assignments
3. Calculate statistics (averages, highest/lowest grades)
4. Generate reports
5. Search and filter student data

This project will test your understanding of all Module 1 concepts!
""")

# ------------------------------------------------------
# PART 1: DATA SETUP
# ------------------------------------------------------
# Create the basic data structures to store student information
# ------------------------------------------------------

print("\nPART 1: DATA SETUP")
print("-" * 40)

# TODO: Create data structures to store:
#       - Student information (name, ID, age, grade level)
#       - Assignment grades for each student
#       - Subjects or courses

# Hint: Consider using lists of dictionaries, or nested dictionaries
# Example structure:
# students = [
#     {
#         "id": 1,
#         "name": "John Smith",
#         "age": 15,
#         "grade_level": 10,
#         "grades": {
#             "math": [85, 90, 92],
#             "science": [76, 88, 90],
#             "history": [92, 95, 88]
#         }
#     },
#     ...
# ]

# Your code here for creating initial data structures
# Start with at least 3 example students with some grades


# ------------------------------------------------------
# PART 2: HELPER FUNCTIONS
# ------------------------------------------------------
# Create functions for common operations in the system
# ------------------------------------------------------

print("\nPART 2: HELPER FUNCTIONS")
print("-" * 40)

# TODO: Create the following functions:

# 1. add_student(students, name, age, grade_level)
#    Adds a new student to the system with a unique ID
#    Returns the updated student list


# 2. add_grade(students, student_id, subject, grade)
#    Adds a grade for a specific student and subject
#    Returns True if successful, False if student or subject not found


# 3. get_student_by_id(students, student_id)
#    Returns the student dictionary for the given ID, or None if not found


# 4. calculate_subject_average(students, student_id, subject)
#    Calculates the average grade for a specific student in a subject
#    Returns the average or None if student or subject not found


# 5. calculate_overall_average(students, student_id)
#    Calculates the overall grade average across all subjects for a student
#    Returns the average or None if student not found


# 6. get_class_average(students, subject)
#    Calculates the average grade for all students in a specific subject
#    Returns the average


# 7. find_highest_grade(students, subject)
#    Finds the highest grade and the student who earned it in a subject
#    Returns a tuple (student_name, highest_grade)


# 8. get_failing_students(students, subject, passing_grade=60)
#    Returns a list of students who are failing the subject
#    (average below passing_grade)


# Your code here for all helper functions


# ------------------------------------------------------
# PART 3: USER INTERFACE
# ------------------------------------------------------
# Create the main menu and user interaction functions
# ------------------------------------------------------

print("\nPART 3: USER INTERFACE")
print("-" * 40)

# TODO: Create the following functions for the user interface:

# 1. display_menu()
#    Displays the main menu options and returns the user's choice


# 2. add_student_ui(students)
#    Handles user input for adding a student
#    Calls the add_student function and displays confirmation


# 3. add_grade_ui(students)
#    Handles user input for adding a grade
#    Calls the add_grade function and displays confirmation


# 4. view_student_ui(students)
#    Handles user input for viewing a specific student's information
#    Displays student details including grades and averages


# 5. view_class_statistics_ui(students)
#    Displays various statistics about the class:
#    - Average grade by subject
#    - Highest and lowest performing students
#    - Number of passing/failing students


# 6. generate_report_ui(students)
#    Generates a formatted report of all students and their grades
#    Has options for sorting and filtering data


# Your code here for all UI functions


# ------------------------------------------------------
# PART 4: MAIN PROGRAM
# ------------------------------------------------------
# Put everything together into a functioning program
# ------------------------------------------------------

print("\nPART 4: MAIN PROGRAM")
print("-" * 40)

# TODO: Create the main function that:
#       1. Initializes the student data
#       2. Displays the menu
#       3. Handles user input
#       4. Calls the appropriate functions
#       5. Loops until the user chooses to exit


def main():
    """Main function to run the Student Data Management System."""
    # Your code here
    pass


# ------------------------------------------------------
# PART 5: EXTENSIONS AND IMPROVEMENTS
# ------------------------------------------------------
# If you complete the basic functionality, try these enhancements
# ------------------------------------------------------

print("\nPART 5: EXTENSIONS AND IMPROVEMENTS")
print("-" * 40)

# TODO: Consider adding these features to enhance your system:

# 1. Data Persistence
#    Save and load student data to/from a file

# 2. Grade Weighting
#    Allow different assignments to have different weights

# 3. GPA Calculation
#    Convert numerical grades to letter grades and calculate GPA

# 4. Student Ranking
#    Rank students based on their performance

# 5. Attendance Tracking
#    Add functionality to track student attendance

# 6. Data Visualization
#    Create text-based graphs or charts to visualize student performance

# 7. Course Management
#    Add ability to create, modify, or delete courses/subjects

# 8. Search Functionality
#    Allow searching for students by name, grade level, or performance

# These are optional challenges if you finish the main project!


# ------------------------------------------------------
# Run the program
# ------------------------------------------------------

# Uncomment this to run your program
# if __name__ == "__main__":
#     main()


# ------------------------------------------------------
# Achievement Tracker
# ------------------------------------------------------
# Track your progress by checking off completed parts
# ------------------------------------------------------

print("\n" + "=" * 60)
print("Achievement Tracker")
print("=" * 60)
print("""
Check off each part as you complete it:

Part 1: Data Setup
[ ] Created student data structure
[ ] Implemented example student data

Part 2: Helper Functions
[ ] add_student function
[ ] add_grade function
[ ] get_student_by_id function
[ ] calculate_subject_average function
[ ] calculate_overall_average function
[ ] get_class_average function
[ ] find_highest_grade function
[ ] get_failing_students function

Part 3: User Interface
[ ] display_menu function
[ ] add_student_ui function
[ ] add_grade_ui function
[ ] view_student_ui function
[ ] view_class_statistics_ui function
[ ] generate_report_ui function

Part 4: Main Program
[ ] Implemented main function
[ ] Program runs without errors
[ ] All features work as expected

Part 5: Extensions (Optional)
[ ] Added at least one extension feature

Progress: [_____] 0% complete
""")