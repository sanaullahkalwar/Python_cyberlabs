import re

#write the word you want to search
pattern = r"hello"

#open and read the file
with open("test.txt","r") as file:
    text=file.read()


#find all case insensitive matches
matches = re.findall(pattern,text,re.IGNORECASE)

print(f"Matches found: {matches}")
print(f"Total matches: {len(matches)}")