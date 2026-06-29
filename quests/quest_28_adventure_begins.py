

def start():
    print("\nYou stand at the entrance to a dark forest.")
    print("A narrow path splits ahead of you.")
    choice = input("Do you go LEFT or RIGHT? ").lower()

    if choice == "left":
        cave()
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

def ending_treasure():
    print("\nThe chest bursts open — gold coins pour out everywhere!")
    print("You are rich! You win!")

def ending_dragon():
    print("\nYou sneak past the dragon and find a secret exit.")
    print("You escape the forest with your life. You win!")

def ending_wizard():
    print("\nThe wizard gifts you a magic map to hidden treasure.")
    print("You find it and live happily ever after. You win!")

start()
