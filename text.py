import re

text = "Hello, world! Hello there!"
pattern = r"hello"
matches = re.findall(pattern,text,re.IGNORECASE)
print(matches) 