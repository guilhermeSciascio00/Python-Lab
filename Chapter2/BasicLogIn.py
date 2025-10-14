#This program will ask to the user its nickname and password, if it's the same as the singed up one then he will access the system.

print("Hello, I see it's your first time here, what's your username? ")
username = input(">")
print("Password: ")
password = input(">")

print("User created, now you can login")
print("Username")
validUsername = input(">")
print("Password")
validPassword = input(">")
if(validUsername == username and validPassword == password):
    print("Welcome! " + validUsername + " have a nice day :D")
else:
    print("Username/Password is incorrect")
