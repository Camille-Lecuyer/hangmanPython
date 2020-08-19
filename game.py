import random
from words import word_list

def getWord():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False

def letterList(word):
    letters = []
    for letter in word:
        if letter not in letters:
            letters += letter
    return letters

print(letterList(getWord()))