# quest_30_reflective_scribe.py
# This script revisits Quest 27 (FizzBuzz), Quest 28 (Adventure Game),
# and Quest 29 (Code Breaker) with detailed comments explaining each part.

# ─────────────────────────────────────────
# QUEST 27 — FizzBuzz
# ─────────────────────────────────────────

# range(1, 101) generates numbers 1 to 100.
# The stop value (101) is exclusive, so we use 101 to include 100.
for number in range(1, 101):

    # We check the combined condition FIRST (divisible by both 3 and 5).
    # If we checked % 3 first, the number 15 would print "Fizz" and never
    # reach the FizzBuzz branch — so order here is critical.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # % is the modulo operator — it gives the remainder after division.
    # If number % 3 == 0, there is no remainder, meaning it divides evenly.
    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    # If none of the above conditions matched, just print the number itself.
    else:
        print(number)


# ─────────────────────────────────────────
# QUEST 28 — Choose Your Own Adventure
# ─────────────────────────────────────────

# Each location in the game is its own function.
# This keeps the code organised — instead of one huge block,
# each scene is a self-contained, readable chunk.

def start():
    print("\nYou stand at the entrance to a dark forest.")
    print("A narrow path splits ahead of you.")

    # .lower() converts whatever the user types to lowercase,
    # so "LEFT", "left", and "Left" all behave the same way.
    choice = input("Do you go LEFT or RIGHT? ").lower()

    if choice == "left":
        cave()      # calling another function moves the player to a new scene
    elif choice == "right":
        meadow()
    else:
        print("You hesitate too long and a wolf chases you home. Game over.")

def cave():
    print("\nYou enter a damp cave. You hear dripping water.")
    print("There is a glowing chest and a sleeping dragon.")
    choice = input("Do you open the CHEST or sneak PAST the dragon? ").lower()

    if choice == "chest":
        ending_treasure()
    elif choice == "past":
        ending_dragon()
    else:
        print("You stand frozen. The dragon wakes up. Game over.")

def meadow():
    print("\nYou walk into a sunny meadow. A friendly wizard waves at you.")
    choice = input("Do you GREET the wizard or IGNORE them? ").lower()

    if choice == "greet":
        ending_wizard()
    elif choice == "ignore":
        print("The wizard turns you into a frog. Game over.")
    else:
        print("The wizard looks confused and walks away.")

# Each ending is its own function — this makes it easy to add
# new endings later without rewriting the whole game.
def ending_treasure():
    print("\nThe chest bursts open — gold coins pour out everywhere!")
    print("You are rich! You win!")

def ending_dragon():
    print("\nYou sneak past the dragon and find a secret exit.")
    print("You escape the forest with your life. You win!")

def ending_wizard():
    print("\nThe wizard gifts you a magic map to hidden treasure.")
    print("You find it and live happily ever after. You win!")

# start() must be called outside and after all the function definitions.
# Python reads the file top to bottom — if we called start() before
# defining cave() or meadow(), Python wouldn't know what those are yet.
start()


# ─────────────────────────────────────────
# QUEST 29 — The Code Breaker
# ─────────────────────────────────────────

secret_code = 42

# This flag starts as False. We only set it to True if the user
# guesses correctly. After the loop, we check it to decide
# what message to print.
solved = False

# range(1, 4) gives exactly 3 attempts: 1, 2, 3.
# A for loop is used here instead of while because we know
# the exact number of attempts allowed.
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3 — Enter the secret code: "))

    if guess == secret_code:
        print("Correct! Access granted.")
        solved = True
        # break exits the loop immediately — no more attempts are offered
        # once the correct code is entered.
        break
    else:
        remaining = 3 - attempt
        if remaining > 0:
            print(f"Wrong code. You have {remaining} attempt(s) left.")
        else:
            print("Wrong code.")

# This runs after the loop finishes (either via break or all 3 attempts used).
# "not solved" is True only if the user never guessed correctly.
if not solved:
    print(f"Access denied. The secret code was {secret_code}.")
