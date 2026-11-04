# Question 01: Check if a number is divisible by 3

number = int(input("Enter a number: "))

if number % 3 == 0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is NOT divisible by 3")