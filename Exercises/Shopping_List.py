# A program that will server as a shopping list manager to the user
#You will be able to see the items in there, add, and remove
#It will also use persistent data
from pathlib import Path
import json

current_directoy = Path.cwd() / "Exercises"
current_data_file = current_directoy / "shoppingList.json"
shopping_list = []
option = 0

def check_option(option):
    if option == 1:
        print("What item do you want to add? ")
        add_item = input(">").strip().capitalize()
        shopping_list.append(add_item)
        print(f"{add_item} added to the list")
    elif option == 2:
        print("What item do you want to remove? ")
        remove_item = input(">").strip().capitalize()
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"{remove_item} removed from the list")
        else:
            print("It wasn't possible to find the given item, did you type it correctly?")
    elif option == 3:
        if len(shopping_list) == 0:
            print("Enter an item in the list first")
        else:
           for item in shopping_list:
                print(item) 
    
    input("Press any key to continue...")

if(current_data_file.exists()):
    with open(current_data_file, "r", encoding="UTF-8") as json_data:
        shopping_list = json.load(json_data)

print("Welcome to the Shopping List Manager")
while option != 4:
    print("Choose an option: ")
    while True:
        print("1. Add an item\n2. Remove an item\n3. View the list\n4. Quit")
        #Check if the given value is a digit
        while True:
            option = input(">")
            if(option.isdigit()):
                option = int(option)
                break
            else:
                print("Please enter only number")
            
        if(option > 4 or option < 1):
            print("Please enter a valid option")
        else:
            break
    
    if option != 4:   
        check_option(option)
        
print("The program has ended")
with open(current_data_file,"w", encoding="UTF-8") as json_data:
    json.dump(shopping_list, json_data)
