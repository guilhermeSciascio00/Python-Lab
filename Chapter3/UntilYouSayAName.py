#This code will ask you for the name you registred, however if you don't say it the programm will keep looping until you say it

print("Welcome to UntilYouSayAName")
print("First you need to register a name, here")
targetName = input(">")
print("Nice, now let's start")
name = ''
while name != targetName:
    print("What's the name?")
    name = input(">")

print("Well done " + targetName)
