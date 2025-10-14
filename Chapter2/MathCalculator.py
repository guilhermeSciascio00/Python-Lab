#This program will ask the user which basic operation he wants to do, and then ask for two number to do them.

print("Welcome to the basic math calculator")
print("Which operation do you want to do? ")
print("Add[0], Subtract[1], Multiplication[2], Division[3]")
option = int(input(">"))
if(option == 0):
    print("Which numbers do you want to add? ")
    num1 = input(">")
    num2 = input(">")
    print("The result of, " + num1 + " + " + num2 + " is " + str(int(num1) + int(num2)))
elif(option == 1):
    print("Which numbers do you want to subtract? ")
    num1 = input(">")
    num2 = input(">")
    print("The result of, " + num1 + " - " + num2 + " is " + str(int(num1) - int(num2)))
elif(option == 2):
    print("Which numbers do you want to multiply? ")
    num1 = input(">")
    num2 = input(">")
    print("The result of, " + num1 + " * " + num2 + " is " + str(int(num1) * int(num2)))
elif(option == 3):
    print("Which numbers do you want to multiply? ")
    num1 = input(">")
    num2 = input(">")
    print("The result of, " + num1 + " / " + num2 + " is " + str(float(num1) / float(num2)))
else:
    print("Wrong option.. Please enter a valid option next time.")
