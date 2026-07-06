def ask_for_age():
    age = int(input("What is your age? "))
    return age
def can_they_vote(age):
    if age >= 18:
        print("You can vote")      # your "can vote" message
    else:
        print("You cannot vote")      # your "too young" message


age = ask_for_age()
can_they_vote(age)
