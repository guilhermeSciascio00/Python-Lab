#This program reads your sentence, and print it uppercase, lower case.
#The number of words in the sentence(space included)
#The number of characters in the sentence(space excluded)
#And it will also print the sentence in reverse

print("Welcome to the sentence reader, in this program we will:")
print("""Read your sentence, transform it in upper/lower case
Count how many words and characters it has and reverse the sentence\n""")

print("Write a sentence: ")
sentence = input(">").strip()
sentence_list = sentence.split()
joined_sentence = "".join(sentence_list)
reversed_list = sentence.split()

#"how it works" underneath the hood, because u can just do[::-1]
list_lenght = len(reversed_list)
for i in range(list_lenght // 2):
    temp_word = reversed_list[-i -1]
    reversed_list[-i -1] = reversed_list[i]
    reversed_list[i] = temp_word

print(f"Lower: {sentence.lower()}")
print(f"Upper: {sentence.upper()}")
print(f"Total sentence lenght(with spaces): {len(sentence)}")
print(f"Total sentence lenght(without spaces): {len(joined_sentence)}")
print(f"The reversed sentence is: {" ".join(reversed_list)}")
print(f"The reversed letters: {" ".join(sentence_list)[::-1]}")
