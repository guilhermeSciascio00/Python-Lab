#This programm will ask for the user which type of fuel he wants to fill the vehicle, how many liters he wants and its final price.
#Prices based on brazil's average price

gasolinePrice = 6.20
dieselPrice = 6.06
ethanolPrice = 4.30

print("Welcome to the br-0056 fuel stop, here are our prices for today")

print("Price's table: ")
print("[0] Gasoline: R$" + str(gasolinePrice))
print("[1] Diesel: R$" + str(dieselPrice))
print("[2] Ethanol: R$" + str(ethanolPrice))

litersAmount = 0.0
totalPrice = 0.0
option = 0

while True:
    print("What type of fuel do you want to buy? ")
    option = int(input(">"))
    if(option >= 3 or option < 0):
        continue
    else:
        print("How many liters would you like to fill up? ")
        litersAmount = input(">")
        if(option == 0):
            totalPrice = int(litersAmount) * gasolinePrice
        elif(option == 1):
            totalPrice = int(litersAmount) * dieselPrice
        elif(option == 2):
            totalPrice = int(litersAmount) * ethanolPrice
        break

totalPrice = round(totalPrice, 2)
if(option == 0):
    print("You bought " + str(litersAmount) + "L of gasoline and the total price is: R$" + str(totalPrice))
elif(option == 1):
    print("You bought " + str(litersAmount) + "L of diesel and the total price is: R$" + str(totalPrice))
elif(option == 2):
    print("You bought " + str(litersAmount) + "L of ethanol and the total price is: R$" + str(totalPrice))
 


