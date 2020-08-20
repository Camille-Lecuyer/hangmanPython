import random
from words import word_list

def getWord():
    word = random.choice(word_list)
    return word.upper()

def play(word):
   wordCompletion = "_" * len(word)
   guessed = False
   guessedLetters = []
   guessedWords = []
   tries = 6
   print("Let's play Hangman!")
   print(display_hangman(tries))
   print(wordCompletion)
   print("\n")
   while not guessed and tries > 0:
      guess = input("Please guess a letter or word:  ").upper()
      if len(guess)==1 and guess.isalpha():
         if guess in guessedLetters:
               print("You already guessed the letter ", guess)
         elif guess not in word:
               print(guess, " is not in the word.")
               tries -= 1
               guessedLetters.append(guess)
         else:
            print("Good job, ", guess, " is in the word!")
            guessedLetters.append(guessedLetters)
            wordAsList = list(wordCompletion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               wordAsList[index] = guess
            wordCompletion = "".join(wordAsList)
            if "_" not in wordCompletion:
               guessed = true
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessedWords:
            print("You already guess the word", guess) 
         elif guess != word:
            print(guess, "is not the word")
            tries -= 1
            guessedWords.append(guess)
         else:
            guessed= true
            wordCompletion = word
      print(display_hangman(tries))
      print(wordCompletion)
      print("\n")
   if guessed:
      print("Congratulation, you guessed", word)
   else:
      print("sorry you ran out of tries, the word was", word)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
   word = getWord()
   play(word)
   while input("Play again? (Y/N)").upper() == "Y":
      word = getWord()
      play(word)

if __name__ == "__main__":
   main()