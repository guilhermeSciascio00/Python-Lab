from animal import Animal
        
tiger = Animal("Tiger", "Siberian", False)
owl = Animal("Owl", "Barn", False)
brown_bear = Animal("Bear", "Brown", False)
panda = Animal("Panda", "Giant", False)

print(f"We have a total of {Animal.current_animals} animals")
print(f"Here are the animals we have in our {Animal.live_at}")
for animal in Animal.animal_list:
    animal.ShortDescription()
