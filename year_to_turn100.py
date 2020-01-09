"""A simple little program I wrote that tells the user what year they will turn 100 based on their input.
This is not a perfect program but my main goal was to use classes and methods as I work to get in the habit of doing that at all times.



===== RESTART: C:\Users\ssciere\Desktop\practice python\year_to_turn100.py =====
What is your name? Steve
What year were you born? 1979
Hi Steve, you will turn 100 in the year 2079.
What is your name? Fred
What year were you born? 1988
Hi Fred, you will turn 100 in the year 2088.
>>>

"""

class User:

    def __init__(self, name, yearBorn):
        self.name = name
        self.yearBorn = yearBorn

    #class method to calculate and give results
    def giveResults(name, yearBorn):
        yearsToTurn100 = str(yearBorn + 100)
        print("Hi " + name + ", you will turn 100 in the year " + yearsToTurn100 + ".")

    #static method to get user info
    @staticmethod
    def getUserData():
        userName = input("What is your name? ")
        userYearBorn = int(input("What year were you born? "))
        userInfo = {"name":userName, "yearBorn":userYearBorn}
        return userInfo


userInfo = User.getUserData() #call static method
user1 = User(userInfo["name"], userInfo["yearBorn"])
User.giveResults(user1.name,user1.yearBorn)

# Let's go through procerss again for a second user

userInfo = User.getUserData()
user2 = User(userInfo["name"], userInfo["yearBorn"])
User.giveResults(user2.name,user2.yearBorn)







    



