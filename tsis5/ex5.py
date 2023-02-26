import re

pattern = r'a.+b$'

string = input("Enter a string to search for strings that match the pattern 'a.+b$': ")

matches = re.findall(pattern, string)

if matches:
    print(f"string '{string}':")
    for match in matches:
        print(match)
else:
    print(f"No strings '{string}'.")