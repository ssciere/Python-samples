"""This is a simple little rock, paper, scissors game I wrote for an exercise on the "100 Days of Coding in Python" program I'm working on.  The main purpose
of the exercise was to learn to use classes."""

import random

class Weapon:
    def __init__(self, name, beats):
        self.name = name
        self.beats = beats #"beats" is best thought of as "the choice the computer choice 'beats'"
  

def maingame():
    print_header()
    game_loop()
    thanks()

def print_header():
    print("ROCK PAPER SCISSIORS GAME")

def game_loop():
    win_or_lose = "win" 
    possible_choices = [
        Weapon("r","s"),
        Weapon("p","r"),
        Weapon("s","p"),
    ]
    
    player_choice = ""  #ask player for their choice of rock, paper, or scissors
    while player_choice != "r" and player_choice != "p" and player_choice != "s":
        player_choice = input("Enter <r>ock, <p>aper or <s>cissors and press <enter>")
        
            
    computer_choice = random.choice(possible_choices)
    print("Computer chooses " + computer_choice.name)
    if computer_choice.beats == player_choice: #winner is decided here.  (If the choice the computers choice can beat matches the players, player loses)
        win_or_lose = "lose"
    if computer_choice.name == player_choice:  #added this incase the computer's choice is the same as the player's choice
        win_or_lose = "tied"
    print("You " + win_or_lose)
    print()
    play_again = ""   #ask player if they want to play again
    while play_again != "y" and play_again != "n":
        play_again = input("Play again (y/n + enter)")
        if play_again == "y":
            game_loop()

   

def thanks():
    print("Thanks for playing")


maingame()

