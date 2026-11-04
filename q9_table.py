# Question 9: Multiplication table using while loop[cite: 2]

num = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))

i = 1
print(f"\nMultiplication Table for {num} up to {limit}:")
while i <= limit:
    print(f"{num} x {i} = {num * i}")
    i += 1