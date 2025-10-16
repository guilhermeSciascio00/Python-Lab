#a simple program that you can create a list of things you need to buy on the supermarket

print("Welcome to your market list, list everything you will need to buy!!")
buy_list = []

print("What do you will buy?")
print("Just press enter if you want to end the list")
user_input = ""

while True:
    print(f"Item {len(buy_list) + 1}: ")
    user_input = input(">")
    buy_list.append(user_input)
    if(user_input == ""):
        break
    
print("Here is your full list: ")
for item in buy_list:
    print(item)
