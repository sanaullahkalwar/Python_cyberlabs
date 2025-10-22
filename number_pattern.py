#importing regex module
import re

#actual text from the will search the pattern
text = "Contect: 123-456-7890 or +1-555-0123-4567"

#actual regex pattern
pattern = r"\d{3}[-.]?\d{3}[-.]?\d{4}"

phones = re.findall(pattern,text)

print(f"Found Pattern : {phones}")
print(f"Total matches: {len(phones)}")


