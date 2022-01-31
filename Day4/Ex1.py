# Heads or tails
import random

end = 1000
result = random.randint(1,end)
if result < end / 2:
    print("Result of the coin toss is: HEADS")
else:
    print("Result of the coin toss is: TAILS")
