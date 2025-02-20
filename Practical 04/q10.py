import random

# Generate a random number between 1 and 9
secret_number = random.randint(1, 9)

while True:
    guess = input("Guess a number between 1 and 9 (or type 'exit' to quit): ")

    if guess.lower() == 'exit':
        print("Thanks for playing! The number was", secret_number)
        break

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess < 1 or guess > 9:
        print("Out of range! Guess a number between 1 and 9.")
    elif guess == secret_number:
        print("Congratulations! You guessed the right number!")
        break
    else:
        print("Wrong guess! Try again.")
