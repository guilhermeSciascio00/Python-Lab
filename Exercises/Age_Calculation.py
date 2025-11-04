#This program will ask the user their name, age of birth and calcs their age
import time


current_year = int(time.localtime().tm_year)

print("Welcome to guessing your age!")
print("What's your name? ")
name = input(">")

print(f"Hello, {name}. What was the year you have born?")
birth_year = int(input(">"))

print(f"{name}. What's your favorite color? ")
fav_color = input(">")

if birth_year > current_year:
    print("Pretty funny, your futuristic mind")
else:
    age = current_year - birth_year
    print(f"{name} you are {age} years old and your favorite color is {fav_color}")

