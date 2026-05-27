#aedric
#robotguess
#robot he guess

import random
secret=random.randint(1,100)

def robot():
    attempts = 0
    for guess in range(1,101):
        attempts = attempts+1
        if guess == secret:
            print(f"Secret number was: {secret}")
            print(f"Attempts {attempts}")

def binaryrobot():
    attempts=0
    low=1
    high=100
    found=False
    while found == False:
        mid = (low + high) // 2
        if mid > secret:
            high = mid -1
            attempts = attempts+1
        if mid < secret:
            low = mid + 1
            attempts = attempts+1
        else:
            attempts = attempts+1
            print(f"Secret number was: {secret}")
            print(f"Attempts {attempts}")
            found=True

binaryrobot()
