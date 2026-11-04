# Question 4: Pizza Pricing Logic[cite: 1]

size = input("Enter the size of the pizza (small/medium/large): ").strip().lower()

if size == "small":
    print("The price is $3.00")
elif size == "medium":
    print("The price is $4.00")
elif size == "large":
    print("The price is $5.50")
else:
    print("Invalid size")