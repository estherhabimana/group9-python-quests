"""Quest 14: The Logical Gatekeeper.

Demonstrates the 'and' operator.
"""

age = int(input("How old are you? "))
gold = int(input("How many gold coins do you carry? "))

if age >= 18 and gold >= 20:
    print("Welcome to the club. Enjoy your night.")
else:
    print("Sorry, you cannot enter.")
