#Practicing List comprehension

prime_numbers = [i for i in range(20) if i % 3 == 0]
print(prime_numbers)

words = ["HELLO", "WORLD", "Python", "is", "FUN"]
words3_longer = {word for word in words if len(word) > 3}
words_lower_case = []
for word in words3_longer:
    words_lower_case.append(word.lower())
    
print(words_lower_case)
    

    
