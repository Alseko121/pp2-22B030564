import re

pattern = r'[a-z]+_[a-z]+'

string = input("Enter a string to search for sequences of lowercase letters joined with an underscore: ")

matches = re.findall(pattern, string)

if matches:
    print(f" lowecase '{string}':")
    for match in matches:
        print(match)
else:
    print(f"No lowercase '{string}'.")