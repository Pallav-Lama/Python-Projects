import random
import string
from tkinter import Y

WORDLIST_FILENAME = "words.txt"
RESPONSES = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]

def load_word():
    print ("Loading word list from file...")
    inFile = open (WORDLIST_FILENAME) 
    line = inFile.readline( ) 
    wordlist = line.split()
    print (" ", len(wordlist), "words loaded.") 
    inFile.close()
    return wordlist

def choose_random_word(all_words):
    word = random.choice(all_words)
    return word

def is_word_guessed(word, lives):    
    if lives == 0:
        print(RESPONSES[3].format(word))
    else:
        print(RESPONSES[1], RESPONSES[2].format(lives))

def get_guessed_word(word):
    lives = 5
    word_letters = set(word)
    alphabet =  set(string.ascii_lowercase)
    used_letters = set()
    while len(word_letters)>0 and lives>0:  
        print("Used letters: ", ' '.join(used_letters))
        print(RESPONSES[4].format(lives))
        
        given_word = [letter if letter in used_letters else '-' for letter in word]
        print('The word: ', ' '.join(given_word))

        user_letter = input("Guess a letter: ").lower()
        print("------------------------------")
        if user_letter in alphabet - used_letters:           
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print(RESPONSES[6].format(user_letter))
                word_letters.remove(user_letter)
            else:
                print(RESPONSES[7].format(user_letter))
                lives=lives-1
        elif user_letter in used_letters:
            print(RESPONSES[8].format(user_letter))
        else:
            print ("Invalid Character!!!")
    is_word_guessed(word, lives)

def hangman():
    print("Welcome to Hangman Ultimate Edition")
    try:          
        word = choose_random_word(load_word())     
        # print(word) #To check
        print(RESPONSES[0].format(len(word)))
        print("---------------")
        get_guessed_word(word)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    hangman()


