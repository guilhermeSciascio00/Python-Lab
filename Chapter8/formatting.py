name = "Alice"
age = 2000

message1 = "Alice is " + str(age) + " years old"
message2 = f"Alice is {age} years old"
message3 = "My name is %s and I'm %s years old" % (name, age)
message4 = "My name is {0} and I'm {1} years old. {0} doesn't know how to read books, but {0} excels at reading people minds".format(name, age)
print(message4)
