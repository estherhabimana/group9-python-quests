# Quest 17: The Endless Staircase
# A while loop keeps running AS LONG AS a condition is true
# Unlike a for loop, it doesn't count steps — it just checks the condition each time

step = 0  # we start at step 0

while step < 5:  # keep going while step is less than 5
    print(f"Climbing step {step + 1}...")
    step += 1  # add 1 to step each time, otherwise the loop runs forever!

print("You reached the top of the staircase!")
