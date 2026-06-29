# Quest 18: The Loop of Riddles
# A while loop that keeps asking for input until the user is correct
# This is how games work — keep looping until something specific happens

secret_number = 13  # the answer the user needs to guess

guess = 0  # start with a wrong guess so the loop begins

while guess != secret_number:  # keep looping until they get it right
    guess = int(input("Guess the secret number: "))  # int() converts the typed text to a number
    if guess != secret_number:
        print("Wrong! Try again.")

print("Correct! You solved the riddle!")
