#This program will create a pre-defined number of how much L of soda and how much KG of food you will need for a party. 

kgOfFoodPerPerson = 0.3
literOfSodaPerPerson = 0.4

print("Welcome to the fictional party calculator, what's you name? ")
name = ''
while not name: #While the name is empty(false)
    name = input(">")

if name:#Only works if name is true bool(name)
    peopleQuantity = 0
    print(name + " How many people will come to the party? ")
    
    while not peopleQuantity:#While the people quantiy is equal to zero
        peopleQuantity = int(input(">"))
       
    totalFoodAmount = round(peopleQuantity * kgOfFoodPerPerson, 2)
    totalSodaAmount = round(peopleQuantity * literOfSodaPerPerson, 2)
    
    print(name + " you will need around " + str(totalFoodAmount) + " kg of food", end=" ")
    print("and " + str(totalSodaAmount) + "L of soda")
