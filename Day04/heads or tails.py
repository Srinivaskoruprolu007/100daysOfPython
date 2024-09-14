import random

# Generate a random integer between 0 and 1 (inclusive).
random_side = random.randint(0, 1)

# Determine the outcome based on the generated random number.
if random_side == 1:
    # If the number is 1, print "tails".
    print("tails")
else:
    # If the number is 0, print "heads".
    print("heads")