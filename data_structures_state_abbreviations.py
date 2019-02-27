"""
Data structure problem from the "#100DaysofCode in Python" program from the "Talk
Python to Me" Podcast

To use this program, you will also need to load the states_data.py file from this same repo in the same folder as the program

Instructions for problem:
Create a script that imports the US States data structures contained in the following script file in our Repo: https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/07-09-data-structures/code/data.py

Perform the following tasks on the list and dict. The less you look at them, the better this exercise will be. Remember: Dicts are unsorted.

Print out the 10th item in each.

Print out the 45th key in the dictionary.

Print out the 27th value in the dictionary."""



import collections
from states_data import *




us_state_abbrev = collections.OrderedDict(us_state_abbrev) #converted dict to Ordered Dict so it can be indexed

#Prints out the 10th item in each
def Print10thAll(us_state_abbrev=us_state_abbrev, states_list=states_list):
    print (list(us_state_abbrev.items())[9])
    print (states_list[9])

#Print out the 45th key in the dictionary
def Print45thKey(us_state_abbrev=us_state_abbrev):
    print (list(us_state_abbrev.keys())[44])

#Prints out the 27th value in the dictionary
def Print27thValue(us_state_abbrev=us_state_abbrev):
    print (list(us_state_abbrev.values())[26])

#run the functions
Print10thAll(us_state_abbrev, states_list)
Print45thKey (us_state_abbrev)
Print27thValue(us_state_abbrev)
