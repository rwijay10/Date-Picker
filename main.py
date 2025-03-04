import os
import random


#User can select one of the date ideas and it will also show if its expensive or not
date_ideas = {
        "At home" : ["DIY Wine & Paint Night", "Indoor Picnic", "Coof-Off Challenge", "Home Spa Night", 
        "Board Game Marathon", "Build A Blanket Fort", "Karaoke Night", "DIY Pizza Night", "Stargazing Indoors"],

        "Indoor" : ["Escape Room", "Museum or Art Gallery", "Bowling", "Indoor Rock Climbing", "Comedy Show", "Arcade or Barcade", 
        "Theater", "Indoor Trampoline Park", "Mini Golf"],

        "Outdoor" : ["Hiking Adventures", "Beach Day", "Drive-in Movie", "Farmers' Market", "Kayaking or Canoeing", 
        "Botanical Garden Visit", "Sunset Picnic", "Outdoor Sports", "Zoo or Aquarium", "Camping Trip"]
    }


#user inputs date type
i = input("What kind of date would you like to do? (At home, indoor, or outdoor): ")


if i.casefold() == "at home":
    random_at_home = random.choice(date_ideas["At home"])
    print(random_at_home)
elif i.casefold() == "indoor":
    random_indoor = random.choice(date_ideas["Indoor"])
    print(random_indoor)
elif i.casefold() == "outdoor":
    random_outdoor = random.choice(date_ideas["Indoor"])
    print(random_outdoor)
else:
    print("Please choose a valid option")
    input("What kind of date would you like to do? (At home, indoor, or outdoor): ")