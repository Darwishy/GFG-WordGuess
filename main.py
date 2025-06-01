# Get users name / wish good luck and explain the rules / tries.
# make a list of random words and a random.choice word variable
# Let the User Guess
# check if user guess is in the random word
# -= 1 tries per try.

import random

user_Name = input("Hello, what is your name?: ")
print(f"Welcome to the word guessing game {user_Name}, you get 12 tries to guess the word.")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print(word)
guess = ""
tries = 12

while tries > 0:
    user_Guess = input("Guess a letter: ").lower()
    if user_Guess in word:
        tries -= 1
        guess += user_Guess
        print(f"{user_Guess} is in the word. {tries}/12 tries left. you've guessed {len(guess)} letters out of {len(word)}")
    elif user_Guess not in word:
        tries -= 1
        print(f"{user_Guess} is NOT in the word. {tries}/12 tries left. you've guessed {len(guess)} letters out of {len(word)}")
    if tries == 0:
        print(f"You ran out of tries. The word was : {word}. Good luck next time !")


    if len(guess) == len(word): 
        print(f"You guessed the word. It was {word}") 
        break
