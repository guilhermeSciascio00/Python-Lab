#This program will count how many times a letter has appeared in a given sentence.

message = "I couldn't remember everything they said in the meeting, however I noticed that Jeff was not paying attetion, instead he was playing with a pencil the whole meeting."

wordCount = {}

for character in message:
    wordCount.setdefault(character, 0)
    wordCount[character] += 1

print(wordCount)
