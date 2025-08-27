# Work with tuples - lists where you can't overwrite or add a 
# single element, but you can overwrite what the tuple variable points to 

artists = ("NewDad", "The Crane Wives", "Destroy Boys", "Crystal Castles", "CIEL")
for artist in artists:
    print(f"I really like the band, {artist}")

# Try to modify one and verify that it crashes
# artists[3] = "Panic! At the Disco"    # Verified, neither worked
# artists.append("Bastille")

# Overwrite the tuple
print()
artists = ("Bastille", "Shayfer James", "Cosmo Sheldrake", "Jann", "The Hoosiers")
for artist in artists:
    print(f"I also like the band, {artist}")