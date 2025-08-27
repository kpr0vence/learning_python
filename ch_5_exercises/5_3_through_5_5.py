# Give a variable the value green, yellow, or red. Give a player 5 points if its green
alien_color = "YELLOW"
points = "XXX"
if (alien_color.lower() == "green"):
    points = "5"
else:
    points = "An unknow amount of"

print(f"You just shot down a {alien_color} alien. You get {points} point!")

# Redo this, assigning a different amount of points for each color
num_points = 0

if (alien_color.lower() == "green"):
    num_points = 5
elif (alien_color.lower() == "yellow"):
    num_points = 10
elif (alien_color.lower() == "red"):
    num_points = 15
else:  # Must've been a shiny alien...
    num_points = 1000000;

print(f"\nYou just shot down a {alien_color} alien. You get {num_points} points!")