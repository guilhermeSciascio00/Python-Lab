fruitPricing = {"Banana 12x": "$4.75", "Tomato 1KG" : "$2.75"}

while True:
    print("\n*** Product List ***")
    for key in fruitPricing.keys():
        print(key)
    print("Which product do you want to see the price?(Press enter to quit)")
    product = input(">")
    if(product == ""):
        break
    else:
        if product in fruitPricing.keys():
            print(f"The price of the: {product} is {fruitPricing[product]}")
            print("Press enter to continue: ")
            temp = input()
        else:
            print("Hmm, this product isn't in the list")
            print("Could you tell me the name of the product again? ")
            productName = input(">")
            print("Now, it's price: ")
            productPrice = input(">")
            fruitPricing[productName] = "$" + productPrice
            print("Database updated!")
