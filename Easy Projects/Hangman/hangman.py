import random
from words import words 
import string

def gett_valid_word (words):
    word = random.choice(words) # randomly chooses something from de list
    while '-' in word or ' ' in word: 
        word = random.choice(words)
    return word

def hangman ():
    word = gett_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print ('You have used these letters: ', ' '.join(used_letters))

        # what the current word is ( is W - R D)  # lambda?
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ('Current word: ', ' '.join(word_list))    

        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print('You have already used that letter. Choose another one')
        else:
            print('Invalid character')

    # gets here whehn len(word_letters) == 0
