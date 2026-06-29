"""Quest 13: The maze of Many choices.
"""
score = int(input("Enter the score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
