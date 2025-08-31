from pathlib import Path

def print_contents(contents):
    print(contents, end="")
    print(" <-- End of contents variable")

path = Path("pi_digits.txt")
contents = path.read_text()     # Reads the contents from the file into a string, 
print_contents(contents)        # respecting the new lines,

# Use split lines to turn a string with new line chars into an array
lines = contents.splitlines()

for i, line in enumerate(lines):
    print(f"Line {i}: {line}")