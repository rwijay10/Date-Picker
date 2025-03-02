import os
import random


#User can select one of the date ideas and it will also show if its expensive or not
date_ideas = [
    {
        "At home" : 
        {"DIY Wine & Paint Night" : "Inexpensive", 
        "Indoor Picnic" : "Inexpensive", 
        "Coof-Off Challenge" : "Inexpensive", 
        "Home Spa Night" : "Inexpensive", 
        "Board Game Marathon" : "Expensive",
        "Build A Blanket Fort" : "Inexpensive", 
        "Karaoke Night" : "Inexpensive", 
        "DIY Pizza Night" : "Inexpensive", 
        "Stargazing Indoors" : "Inexpensive"}
    },
    {
        "Indoor" : 
        {"Escape Room" : "Expensive", 
        "Museum or Art Gallery" : "Expensive", 
        "Bowling" : "Expensive", 
        "Indoor Rock Climbing" : "Expensive", 
        "Comedy Show" : "Inexpensive", 
        "Arcade or Barcade" : "Inexpensive", 
        "Theater" : "Expensive", 
        "Indoor Trampoline Park" : "Expensive", 
        "Mini Golf" : "Expensive"}
    },
    {
        "Outdoor" : 
        {"Hiking Adventures" : "Expensive", 
        "Beach Day" : "Inexpensive", 
        "Drive-in Movie" : "Expensive", 
        "Farmers' Market" : "Inexpensive", 
        "Kayaking or Canoeing" : "Expensive", 
        "Botanical Garden Visit" : "Inexpensive", 
        "Sunset Picnic" : "Inexpensive", 
        "Outdoor Sports" : "Inexpensive", 
        "Zoo or Aquarium" : "Expensive", 
        "Camping Trip" : "Inexpensive"}
    }
]

#user inputs date type
i = input("What kind of date would you like to do? (At home, indoor, or outdoor): ")


if i.casefold() == "at home":
    print(random.choice(list(date_ideas.values())))