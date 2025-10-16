#Asks the user a number, an given number will be turned into one
import sys

def collatzy_function(number=2):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print("Welcome to the collatz function program")
print("Any given number will be turned into one")

try:
    enteredNumber = int(input(">"))
    if(enteredNumber < 0):
        enteredNumber = abs(enteredNumber)
except ValueError:
    print("Please, enter a valid value, exiting the program")
    sys.exit()

while True:
    print(enteredNumber, end=" ")
    
    if(enteredNumber != 1):
        enteredNumber = collatzy_function(enteredNumber)
    else:
        break

