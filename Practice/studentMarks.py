# Get input from the user
student_name = input("Enter student name: ")

subject_names = ['Marathi', 'English', 'Physics', 'Chemistry', 'Math', 'Bio']
subject_marks = [float(input(f"Enter marks for {subject_names}: ")) for subject_names in subject_names]


average_marks = sum(subject_marks) / len(subject_marks)


if all(mark >= 40 for mark in subject_marks):
    if average_marks >= 70:
        result = 'Pass with First Class'
    elif average_marks >= 60:
        result = 'Pass with Second Class'
    else:
        result = 'Pass'
else:
    result = 'Fail'

print("\nStudent Name:", student_name)
print("Subject-wise marks:")
for i, mark in enumerate(subject_marks):
    print(f"{subject_names[i]}: {mark}")

print(f"\nAverage Marks: {average_marks}")
print(f"Result: {result}")
