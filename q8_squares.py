# Question 8: Filter numbers from 1 to 50[cite: 2]

result = []
for i in range(1, 51):
    square = i ** 2
    if square % 4 == 0 and square % 3 != 0:
        result.append(i)

print("Numbers whose squares are divisible by 4 but not by 3:")
print(result)