"""Quest 12: The Two-Path Cave.

Demonstrates if-else: one path when the condition is true, a default
path for every other case. NB the correct password is Iamking
"""

PASSW = "Iamking"

guess = input("Speak the password to enter the cave: ")

if guess == PASSW:
    print("Access Granted.")
else:
    print("Access Denied.")
