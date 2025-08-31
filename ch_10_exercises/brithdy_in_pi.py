import re
from pathlib import Path

def format_number(number):
    last_digit = number % 10 # To get the 1's place digit
    formatted = str(number)
    if last_digit == 1:
        formatted += "st"
    elif last_digit == 2:
        formatted += "nd"
    elif last_digit == 3:
        formatted += "rd"
    else:
        formatted += "th"
    return formatted
# Read in a file with a lot digits of pi
path = Path('pi_digits_longer.txt')

# Process the file into on line by replacing the whitespace
contents = path.read_text().strip()

# Ask for birthday in 3/3/2004 format
birthday = input("Please enter your birthday in the format dd/mm or dd/mm/yy.\nPlease do not enter any leading zeroes unless it is for the year. ex. 3/3 or 10/7/09: ")

# Clear the '/' and then search for it
birthday = re.sub(r"/", "", birthday)
#print(f"Input birthday: {birthday}")

result = re.search(birthday, contents)
#print(result)
if (result):
    digit_start = format_number(result.start())
    print(f"There was a match! Your birthday starts at the {digit_start} digit of pi! Printing from there...")
    print(contents[result.start() : result.end() + 5])
else:
    print("It doesn't seem like your birthday is in this part of pi :(")