# Question 3: Reverse a string and check for Palindrome[cite: 1]

text = input("Enter a string or number: ")

# Reverse string[cite: 1]
reversed_text = text[::-1]
print(f"Reversed text: {reversed_text}")

# Check palindrome[cite: 1]
if text.lower() == reversed_text.lower():
    print("It is a Palindrome!")
else:
    print("It is NOT a Palindrome!")