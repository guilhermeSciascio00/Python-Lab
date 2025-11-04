class Animal:
    """An Animal Class"""
    
    live_at = "Florest"
    current_animals = 0
    animal_list = []
    
    def __init__(self, name, type, is_domestic):
        self.name = name
        self.type = type
        self.is_domestic = is_domestic
        Animal.current_animals += 1
        Animal.animal_list.append(self)
    
    def LookAt(self):
        """ Print the animal you are looking at"""
        print(f"You are looking at the {self.type} {self.name}")

    def Move(self):
        """ The animal is moving"""
        print(f"The {self.type} {self.name} is moving towards you!!")

    def Describe(self):
        """ Describe the current animal"""
        print(f"It's a {self.name} of type {self.type}, is it domestic you might ask? {self.is_domestic}")

    def ShortDescription(self):
        """ A Short description of the animal, containing only the name and type"""
        print(f"{self.type} {self.name}")
