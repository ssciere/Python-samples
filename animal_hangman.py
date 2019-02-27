"""Animal Hangman Game...This is my solution to problem #32 on practicepython.org (Create a hangman game)  The problem suggests drawing from a list of all words but
I decided to only use names of common animals to make winning a little easier. :)  I added some validation of the user's guesses and tried to use functions wherever possible.
I'm sure this could have been done with less code, but I'm still relatively new to Python...I'd like to stop back and update this as I learn to be more efficient!

To play, you'll need to grab the wordlist_for_hangman_game.txt file from this same repository and place it in the same folder as this program.

"""

from random import sample        #used in generate_word function
from pprint import pprint as pp  #used in generate_word function
import sys #used to end program when player is finished

def opening_info(): #provided instructions at start of game
    print ("Welcome to the hangman game. You'll try to guess a word that is the name of an animal. ")
    print ("Each time you guess a letter that is not in the word, another body part is added to the hangman.")
    print ("To win, you must guess the word before you have a full hangman. \n")
    print ("A full hangman looks like this:")
    print ("  0")
    print ("-/-")
    print ("/\\")  #first slash turns the second one into a normal character
    print()
    print ("Good luck!")
    print()


def generate_word(): # Imports a random word from list in a text file
    with open("wordlist_for_hangman_game.txt") as f:
        word = str(sample(f.read().split(), 1))
        to_remove = "[]'"
        for char in to_remove:
            word = word.replace(char,"")
        return(word)

def main_game(): #main processing portion of the game
    word = str(generate_word())
    word_len = len(word)
    wrong_guesses = 0
    list_of_guesses = []
    guessed_or_not = {} #dict to keep track of which letters have been guessed
    for i in range(word_len):
        guessed_or_not[i] =  "n" #sets all values to no initially
    correct_letters = 0
    while wrong_guesses < 6:
        show_hangman(wrong_guesses)
        print("ANIMAL:")
        for i in range(word_len):
            if guessed_or_not[i] == "n": print ("__ ", end ="")  #prints a blank if letter is unguessed
            else: print (word[i]," ", end ="") #prints letter if guessed
        print()
        users_guess = input("Guess a letter and press <enter> ") #user_guesses
        users_guess = validate(users_guess, list_of_guesses) #converts guess to lower case and checks for repeats or bad data
        list_of_guesses.append(users_guess)
        did_you_get_one = "n"
        for i in range(word_len):
            if users_guess == word[i]:
                guessed_or_not[i]="y"
                correct_letters += 1
                did_you_get_one = "y"
        if did_you_get_one == "n":
            wrong_guesses = wrong_guesses + 1
        if correct_letters == word_len:
            print("Yes - the word was",word)
            print("WINNER!!!!")
            play_again()
    show_hangman(6)
    print ("You Lost.  The word was " + word + ".")
    play_again()

def validate(guess, guesses): #validation function for user guesses
    guess = guess.lower()
    while guess.isalpha() == False: #check for non-letters
        print("Invalid Entry - Please enter letters only!")
        guess = input("Guess a letter and press <enter> ")  #prompt user to guess again so they can enter a letter
        guess = guess.lower()
        
    while guess in guesses: #check for duplicate guesses
        print("You already guessed",guess,"!")
        guess = input("Guess a new letter and press <enter> ")  #prompt user to guess again so they can enter a new letter
        guess = guess.lower()

    while len(guess) > 1: #check for multiple character guesses
        print("Invalid Entry - Please enter only one letter!")
        guess = input("Guess a letter and press <enter> ")  #prompt user to guess again so they can enter only one letter
        guess = guess.lower()
    return(guess)

def show_hangman(missed): #prints out the hangman after each guess
    print("CURRENT HANGMAN:")
    if missed == 0: print("None")
    if missed > 0: print("  0")
    if missed == 2: print(" /")
    if missed == 3: print("-/")
    if missed >= 4: print("-/-")
    if missed == 5: print("/")
    if missed == 6: print("/\\")
    print()

                     
def play_again():
    play_again = input("Play again (y/n)? ")
    play_again = play_again.lower()
    if play_again == "y": main_game()
    else: game_ends()

def game_ends():
    print("Thanks for playing!")
    sys.exit(0)
    
opening_info()
main_game()

    
