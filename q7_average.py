# Question 7: Average of integers 1 to N[cite: 2]

def compute_average(N):
    total_sum = N * (N + 1) // 2  # Mathematical sum formula for efficiency
    avg = total_sum / N
    return avg

n_values = [9, 999, 1000000]
for n in n_values:
    print(f"Average for N = {n:,} is {compute_average(n)}")