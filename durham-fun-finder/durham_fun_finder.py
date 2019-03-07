"""This program helps the user choose an activity/place to go in Durham.  The user is asked a series of questions about the perfect acvity they can envision.  The
programc ompares the user input to a ratings for various locations in Durham and creates a "compatibility rating" for each location.   The location with the highest
rating is presented to the user as the place they should go!

The data needed for this program is in the durham_location_data.py file, located in this same directory.  (It must be placed in the same directory as this file if you
wish to run this program locally.) FYI - If additional questions need to be added, the data can just be changed without updating this program, as long as the locations
all have the same number of "ratings" as there are questions asked of the user"""

import random
from durham_location_data import possible_destinations, question_list #gets data from another file in the same directory

def main():
    opening_banner()
    find_best_match()
    end_message()

def opening_banner():
    print("********Welcome to the Durham Fun Finder*********")
    print(" a great tool to help you figure out what to do!")
    print()

def gather_user_preferences(): #This is where the user answers the questions about their perfect activity
    print("Please tell us about the most perfect activity you can envision!")
    print()
    preferences = [] #this will store the users preferences (AKA answers to the questions)
    x = 0
    while x < len(question_list): #loops throuh as many times as there are questions in the question list
        preferences.append (input(question_list[x]))        
        valid_entries = ['1','2','3','4','5','6','7','8','9','10']  
        while (preferences[x]) not in valid_entries:  #loop gives warning message and asks for input again until a repsonse of 1-10 is given
            del preferences[x] #gets rid of a bad entry if given
            print("Please choose an entry that is a number 1-10") #warning message
            preferences.append(input(question_list[x])) #adds response to the preference list once determined to be valid
        x += 1
    return(preferences)

def find_best_match(): #loops through all the locations compares their category ratings to the user input to create compatibility rating
    preferences = gather_user_preferences()
    best_rating = 0  #best_rating,best_location are changed each time a new most compatable location is found while comparing locations to user preferences
    best_location = ""
    for location, ratings in possible_destinations.items():
        x = 0
        compatibility_rating = (len(preferences)) * 10 #compatibility_rating for each location starts as 10 X the number of questions (since each question has a max compatibility of 10)
        while x < len(preferences): #loops through the number of times that there are questions in the list of questions
            compatibility_rating = compatibility_rating - (abs(int(preferences[x]) - ratings[x]))
            x = x + 1
               
        if compatibility_rating > best_rating: #if the location being examined has a higher rating than the best rating thus far, the best rating is replaced with the current rating
            best_rating = compatibility_rating
            best_location = location   #best location thus far is also updated if we have a new highest rating
        elif compatibility_rating == best_rating:   #if there is a tie, a random number is used to determine which location to make the best thus far
            ran_number = int(random.randint(1, 2))
            if ran_number == 1:   #if ran_number is 1 the best location and rating get changed, if 2 they do not.  this breaks the tie!
                best_rating = compatibility_rating
                best_location = location

        
    print()
    print("The best location for you to visit is " + best_location) #feedback provided now to the user
    print()
    choose_again_inquiry()
            
def choose_again_inquiry():
    
    again = input("Do you want to choose another (y/n)?")
    if again.lower() != 'y' and again.lower() != 'n': choose_again_inquiry() #validates input is y or n as requested by restarting function if invalid response given
    if again.lower() == "y":    
        print()
        find_best_match()   #runs main function again if user wants another turn
        
def end_message():
    print()
    print("Thanks for using the Durham Fun Finder!")


if __name__ == '__main__':
    main()







							            		 
                                                                
