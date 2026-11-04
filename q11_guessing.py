# Question 11: Secret number guessing game

secret_number = 7  # Can be any secret number between 1 and 10

while True:
    guess = int(input("Guess the secret number (1-10): "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")