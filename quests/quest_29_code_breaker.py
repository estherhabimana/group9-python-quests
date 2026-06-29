secret_code = 42
solved = False

for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3 — Enter the secret code: "))

    if guess == secret_code:
        print("Correct! Access granted.")
        solved = True
        break
    else:
        remaining = 3 - attempt
        if remaining > 0:
            print(f"Wrong code. You have {remaining} attempt(s) left.")
        else:
            print("Wrong code.")

if not solved:
    print(f"Access denied. The secret code was {secret_code}.")
