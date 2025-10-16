animals = ["cat", "dog", "duck", "hippo", "zebra", "tiger"]
animals.sort()
# for i in range(len(animals)):
#     print(f"The animal at index {str(i)} is the {animals[i]}")

for index, item in enumerate(animals):
    print(f"The animal at index {str(index)} is the {item}")
