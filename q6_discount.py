# Question 6: One line if-else statement for discount eligibility[cite: 2]

age = int(input("Enter your age: "))
has_id = input("Do you have a student ID? (Yes/No): ").strip().lower() == "yes"

# One line condition[cite: 2]
message = "You are eligible for a discount!" if (age < 18 or has_id or age >= 65) else "Sorry, no discount available."
print(message)