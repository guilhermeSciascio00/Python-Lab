#return a random number between 0 and n

import random

def random_number(maxNumber):
    return random.randint(0, maxNumber)

print(f"Your random number is {random_number(100)}")
