message = "Hello, world!"
for char in message:
    print(char.upper(), end=" ")
    
print()
onlyHello = message[0:5]
print(onlyHello.lower())

if("hello" in message.lower()):
    print("He have hello in the message XD")
else:
    print("Nah, we didn't even get a hello")
