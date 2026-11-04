# Question 5: Derive grade using a function based on UoP scale[cite: 1]

def get_grade(marks):
    if marks >= 93.33:
        return 'A'
    elif marks >= 90:
        return 'A-'
    elif marks >= 86.67:
        return 'B+'
    elif marks >= 83.33:
        return 'B'
    elif marks >= 80:
        return 'B-'
    elif marks >= 76.67:
        return 'C+'
    elif marks >= 73.33:
        return 'C'
    elif marks >= 70:
        return 'C-'
    elif marks >= 66.67:
        return 'D+'
    elif marks >= 63.33:
        return 'D'
    elif marks >= 60:
        return 'D-'
    else:
        return 'F'

# Test scenarios[cite: 1]
test_marks = [54, 72, 98, 23.5]
for mark in test_marks:
    print(f"Marks: {mark} -> Grade: {get_grade(mark)}")

# User input[cite: 1]
user_mark = float(input("\nEnter your marks: "))
print(f"Your Grade: {get_grade(user_mark)}")