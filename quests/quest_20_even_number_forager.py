# Quest 20: The Even Number Forager
# Combining a for loop with an if statement
# For each number, we check a condition and only act if it's true

for number in range(1, 21):  # loop through 1 to 20
    if number % 2 == 0:  # % gives the remainder — if remainder is 0, it's even
        print(f"{number} is an even number")
