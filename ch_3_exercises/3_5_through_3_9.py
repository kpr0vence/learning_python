# Make a list of guests, print they're names, then change one of the guests, and reprint the guest list
guests = ["dracula", "Frankenstein's Monster", "CHESHIRE CAT", "dr. doom", "One of the beatles"]
canceler = 4
second_option = "One of the other beatles"

for guest in guests:
    print(f"{guest.title()}, you are invited to my Murder Mystery Dinner Party!")

print(f"\nOh no, {guests[canceler].title()} can't make it! Guess I'll have to invite {second_option.title()}...")
guests[canceler] = second_option

print("\nOkay the new guest list is as follows: ", end="")
end = len(guests)
for i in range(end):
    print(guests[i].title(), end="")
    if i == end - 2:
        print(", and ", end="")
    elif i != end - 1: 
        print(", ", end="") 
    else: 
        print();    # get the new line in there

# Add some guests to the beginning, middle, and end of the list
guests.append("All of the Teenage Mutant Ninja Turtles")   # Add to back
guests.insert(0, "Twilight Sparkle")    # Add to front
mid_index = round((len(guests))/ 2)      # Was converting to float point beacuse the result was 3.5, round to 4
guests.insert(mid_index, "Batman")

print("\nWe have an updated guests list: ")
for guest in guests:
    print(guest.title())

# Showcase some sorting techniques
print("\nOriginal list:")
print(guests)
print("Here is all of my guests sorted alphabetically:")
print(sorted(guests))      # Temp sorting
sorted_guests = guests[:]   # Make a non-aliased copy
sorted_guests.sort();
print("Here is all of my guests sorted alphabetically again:")
print(sorted_guests)
print("Here's proof the original was unaffected")
print(guests)
print("Here is all of my guests sorted in reverse alphabetical order:")
sorted_guests.sort(reverse=True) 
print(sorted_guests)
print("Here is the original list reversed:")
reverse_guests = guests[:]
reverse_guests.reverse();
print(reverse_guests)


# Remove people from the list until there's only 2
print(f"\nOh no, my building's firecode says I can only have 2 guests over. I'm so sorry, but I'm going to have to uninvite some of you all because I currently have {len(guests)} guests.")

while len(guests) > 2:  # We want to go while the length is strictly more than 2. Once we only have indexes 0, 1 (len = 2) we want to stop
    print(f"Goodby, {guests.pop()}, maybe next time...")

print(f"\nNow it's just {guests[0]}, {guests[1]}, and I :(")

# Remove the rest of the dinner guests, and reprint to verify empty list
del guests[0]
del guests[0]   # The original index 0 has been removed, placing the old guests[1] at guests[0]
print(guests)