
""""possible_destinations" is a dictionary that contains keys that are various placed in Durham, and values that are tuples that contain ratings (1-10) for each
of the questions in the list named "possible_destinations".  This data is for use with the durham_fun_finder.py file in this same directory

FYI - I chose tuples since the chance of the dictionary growing is greater than the chance the program will ever need to alter the data
If additional questions need to be added, the data can just be changed without updating the program as long as the locations all have the same number
of "ratings" as there are questions asked of the user."""

possible_destinations = {"Sarah P Duke Gardens":(10,3,2,10,2),"Bennett Place Historic Site": (8,3,2,10,1),"American Tobacco Historic District":(8,6,6,9,3),
"Duke Homestead":(6,1,1,2,1), "Historic Durham Athletic Park":(10,5,5,2,2),"Eno River State Park":(10,1,1,2,1),"Streets at Southpoint":(3,8,3,2,4),
"Bull City Ciderworks":(4,4,8,3,6),"Brightleaf Square":(4,4,8,3,4),"Fullsteam Brewery":(4,5,8,3,5),"Durham Distillery":(1,4,8,3,6),
"Honeygirl Meadery":(1,4,8,3,7),"Al Buehler Hiking Trails":(10,1,2,10,3),"Hi-Wire Brewing":(4,5,8,3,10),"James Joyce Irish Pub":(7,6,9,5,4),
"Boxcar Barcade":(2,5,8,2,10),"Quater Horse Barcade":(1,3,8,4,9), "Parts and Labor":(8,8,10,5,4),"106 Main":(1,2,9,6,5)}


question_list = ["How important is it that this activy is outside? ", "How important is it that food is available? ",
                 "How important is it that adult beverages are available? ","How important is it that the activity is low budget? ",
                 "How important is it that the location is new to Durham? "]
