#This is a game where you need to guess the word before the guesses run out
import random


possible_words = ["Spoon", "Apple", "Orange", "Strawberry", "Chair", "Table", "Pineapple", "Keyboard", "Mouse", "House", "Fork", "Knife", "Banana", "Cherry"]

guess_word = possible_words[random.randint(0, len(possible_words - 1))]
guess_word_list = list(guess_word.lower())
guessed_letters = []
guesses_amount = 6

empty_list = guess_word_list.copy()
for i in range(len(guess_word_list)):
    empty_list[i] = "_"
    
print("The word has the following lenght: ")
print(empty_list)

print("Let's begin")
print(f"You have in total {guesses_amount} guesses")

while True:
    print(f"Word: {empty_list}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Guesses left {guesses_amount}")
    print("Guess a letter: ")
    
    guessed_letter = input(">").lower()
    guesses_amount -= 1
    guessed_letters.append(guessed_letter)
    
    if guessed_letter in guess_word_list:
        for i in range(len(guess_word_list)):
            if guess_word_list[i] == guessed_letter:
                empty_list[i] = guessed_letter
    
        if "_" not in empty_list:
            print("You won!!")
            print(f"Left guesses: {guesses_amount}")
            print(f"The correct word is: {guess_word}")
            break
    
        if guesses_amount <= 0:
            print("You lose!")
            print(f"The correct word was: {str(guess_word)}")
            break
        
    else:
        continue
