#This program will execute a factorial function
#Factorial - 5! = 5 * 4 * 3 * 2 * 1 = 120 n *= (n - 1)
def factorial(number):
    total = 0
    if number <= 1:
        return 1
    else:
        total += number * factorial(number - 1)
        
    return total



myNumber = 1
print(f"The factorial of {myNumber} is {factorial(myNumber)}")

