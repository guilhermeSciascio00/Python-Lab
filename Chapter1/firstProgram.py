#This program says hello and ask for the user's name and age.

print("hello world")
print("What's is your name? ")
myName = input(">")
print("It's good to meet you, " + myName)
print("The lenght of your name is,  " + str(len(myName)))
print("What's is your age? ")
myAge = input(">")
print(myName + " ,you'll be " + str(int(myAge) + 1) + " years old next year")
