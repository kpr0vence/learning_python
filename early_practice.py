# 2-7 Stripping Names (Strings) - Use a variable to represent a name and add some whitespace characters
#  throghout the name. Show the whitesoace and then show the ability to strip it.

name = "\t\nMr.Oange     " 
print(f"The name before stripping: \"{name}\"")
name_cleaned = name.strip();    
print(f"The name after stripping: \"{name_cleaned}\"")

# Leanred: Basic print and string statements. string.strip() only cleans the back and end. Not the middle.
    # Ex. name = "Mr.\nOrange" the new line in the middle wouldn't've been stripped