#This program takes any string and formats it.. removing white spaces and putting the first letter as capitalized

print("Insert a string that isn't formated, and we will deal with it for you")
msg = input(">")

separated_msg = msg.split()
    
for index, word in enumerate(separated_msg):
    separated_msg[index] = word.lower()
    
new_msg = " ".join(separated_msg)
new_msg = new_msg.capitalize()
print(new_msg)
