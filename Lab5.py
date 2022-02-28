"""
Lab 5
"""
#3.1
alien_color = "green"
if alien_color == "green":
    print("You have earned 5 points!")
#3.2
alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points!")
    
else:
    print("You have earned 10 points!")
#3.3
favorite_fruits = ["strawberries", "bananas", "grapes"]

if "dates" in favorite_fruits:
    print("You really like dates!")
    
if "raspberries" in favorite_fruits:
    print("You really like raspberries!")
    
if "strawberries" in favorite_fruits:
    print("You really like strawberries!")
#3.4
my_brother = 29

if my_brother<10:
    print("You are a child!")
    
elif my_brother>=10 and my_brother<20:
    print("You are a teenager!")
    
else:
    print("You are an adult!")