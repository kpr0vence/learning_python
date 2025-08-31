from pathlib import Path
from datetime import date
contents = f"Diary Entery for {date.today()}\n------------------\n"
contents += input("How as your day today? ")
contents += "\n"
contents += input("Is there anything upcomming that you're excited or nervous for? ")
contents += "\n"

file_name = str(date.today()).replace("-", "_")
file_name = f"diary_entry_{file_name}"
path = Path(file_name)
path.write_text(contents)

print(f"\nYour diary entry has been saved in the file '{file_name}' in this directory")