#It's a program that asks ther user its age and name and tells the user date of birth
from datetime import datetime

currentTime = datetime.today()
currentYear = currentTime.year


print("Ready to discover the year you've borned? ")
print("What's your name? ")
myName = input(">")
print("It's a pleasure to have you here, " + myName)
print(myName + " what's your age? ")
myAge = input(">")
print(myName + " you've borned in the year", str(currentYear - int(myAge)))
