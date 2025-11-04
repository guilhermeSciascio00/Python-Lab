#This program creates a list with x random numbers
#Returns which number is higher and lower
#Returns the sum of all numbers

import random

list_start_lenght = 20
random_number_list = [0] * list_start_lenght
random_num_list_even = []
random_num_list_odd = []

for i in range(len(random_number_list)):
    random_number_list[i] = random.randint(1,100)
    
for i in range(len(random_number_list)):
    if random_number_list[i] % 2 == 0:
        random_num_list_even.append(random_number_list[i])
    else:
        random_num_list_odd.append(random_number_list[i])

print(f"Even Numbers in the list: {random_num_list_even}")
print(f"Odd Numbers in the list: {random_num_list_odd}")

print(f"The highest number in the list is: {max(random_number_list)}")
print(f"The lowest number in the list is: {min(random_number_list)}")
print(f"The sum of all number in the list is: {sum(random_number_list)}")

print("Please, enter a number: ")
number = int(input(">"))

if number in random_number_list:
    print(f"The number {number} is in the list!!")
else:
    print(f"No, the number {number} isn't in the list")
