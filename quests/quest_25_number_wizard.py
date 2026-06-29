# quest_25_number_wizard.py

secret_number = 42
guess = int(input("Guess the secret number (1-100): "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    guess = int(input("Guess again: "))

print("You got it! The number was", secret_number)
