# Task 1: Create a Dictionary of Student Marks

# Step 1: Create a dictionary of student marks
student_marks = {
    "Riya": 85,
    "Samiran": 92,
    "Arjun": 78,
    "Priya": 88,
    "Rahul": 95
}

# Step 2: Ask user for a student name
name = input("Enter the student's name: ")

# Step 3: Retrieve and display marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Sorry, no record found for student named '{name}'.")
