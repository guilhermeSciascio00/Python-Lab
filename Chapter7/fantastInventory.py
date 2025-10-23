#fantasy inventory, just to practice dictionaries

# inventory = {"torch" : 42, "coins": 278, "rope": 4, "Mana Potion": 7, "Health Potion" : 3, "Arrows": 15, "Gold Sword" : 1}

print("Inventory items")
def displayInventory(inventory : dict):
    for item, quantity in inventory.items():
        print(f"{item}: {str(quantity)}")

def addItemsToInventory(inventory : dict, addedItems : list):
    if addedItems == []:
        return None
    else:
        for item in addedItems:
            if item in inventory.keys():
                inventory[item] += 1
            else:
                inventory.setdefault(item, 1)
        
inventory = {"Gold Coins": 4}
zombieLoot = ["Gold Coins", "Broken Wood Sword", "Gold Coins"]
cowLoot = ["Raw Beef", "Raw Beef", "Leather", "Gold Coins", "Gold Coins"]

displayInventory(inventory)
addItemsToInventory(inventory, zombieLoot)
print("Inventory after killing the zombie")
print("Press enter to continue: ")
temp = input()
displayInventory(inventory)
print("Inventory after killing the cow")
print("Press enter to continue: ")
temp = input()
addItemsToInventory(inventory, cowLoot)
displayInventory(inventory)

