"""This is a set of problems from the "#100DaysOfCode in Python" program (purchased from the "Talk Python to Me" Podcast)

Problems: Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
"""

import collections

#This is the dictionary provided in the problem
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

#returns a list of all Jeeps
def get_all_jeeps(cars=cars):
    jeep_list = str([cars.get('Jeep')])
    jeep_list = jeep_list.replace("'", "") #next three lines just remove unwanted characters for output
    jeep_list = jeep_list.replace("[", "")
    jeep_list = jeep_list.replace("]", "")
    print("The models of Jeeps are as follows: " + jeep_list + ".")
    



#returns a list the first model (value) associated with each make (key)
#finds the number of keys, loops through each pair and grabs the first value for each
    
def get_first_model_each_manufacturer(cars=cars):
    cars = collections.OrderedDict(cars)
    i = 0
    first_values = []
    while i < len(cars):
        temp_item = list(cars.values())[i] #picks out first model/value
        first_values.append(temp_item[0]) # adds first model/value to a list
        i += 1
    print("The first models of each make are as follows: " + ", ".join(first_values) + ".")

#return an alphabetized list of models(values) that contain the string "Trail"
def get_all_matching_models(cars=cars, grep='Trail'):
    cars = collections.OrderedDict(cars)
    all_models = []
    i = 0
    while i < len(cars):  #nested loop reads through each key, then each value for each key.  
        temp_list = list(cars.values())[i]
        j = 0
        while j < len(temp_list):
            if grep in str((temp_list[j])):
                all_models.append((temp_list[j]))  #Any value containing "Trail" is added to list named "all_models"
            j = j + 1
        i += 1
    all_models.sort()  #just putting in alphabetical order here
    
    print("The models that contain the word 'trail' are as follows: " + ", ".join(all_models) + ".")
    
    
#return all car models sorted alphabetically
def sort_car_models(cars=cars):
    cars = collections.OrderedDict(cars)
    all_models = []
    i = 0
    while i < len(cars):  #nested loop reads through each key, then each value for each key.  
        temp_list = list(cars.values())[i]
        j = 0
        while j < len(temp_list):
            all_models.append((temp_list[j])) #adds individual item to list
            
            j = j + 1
        i += 1
    all_models.sort()  #just putting in alphabetical order here
    
    print("The full list of models in alphabetical order is as follows: " + ", ".join(all_models) + ".")

get_all_jeeps(cars)
print()
get_first_model_each_manufacturer(cars)
print()
get_all_matching_models(cars)
print()
sort_car_models(cars)


"""BELOW IS THE OUTPUT FROM RUNNNING THE CODE ABOVE

 RESTART: C:/Users/Steve/Desktop/100 days/practice_problems_data_structures.py 
The models of Jeeps are as follows: Grand Cherokee, Cherokee, Trailhawk, Trackhawk.

The first models of each make are as follows: Falcon, Commodore, Maxima, Civic, Grand Cherokee.

The models that contain the word 'trail' are as follows: Trailblazer, Trailhawk.

The full list of models in alphabetical order is as follows: 350Z, Accord, Barina, Captiva, Cherokee, Civic, Commodore, Fairlane, Falcon, Festiva, Focus, Grand Cherokee, Jazz, Maxima, Navara, Odyssey, Pulsar, Trackhawk, Trailblazer, Trailhawk.
>>>

"""

