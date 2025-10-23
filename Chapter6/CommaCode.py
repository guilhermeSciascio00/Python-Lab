fruits = ["banana", "cherry", "watermelon", "strawberry", "raspberry", "blackberry", "blueberry"]

def PrintListAsText(listToConvert:list) -> None:
    if not listToConvert:
        print("The list is empty")
    else:
        for i in range(len(listToConvert)):
            if(listToConvert[i] == listToConvert[-2]):
                print(listToConvert[i], end=" and ")
            elif(listToConvert[i] == listToConvert[-1]):
                print(listToConvert[i])
            else:
                print(listToConvert[i], end=", ")

PrintListAsText(fruits)
