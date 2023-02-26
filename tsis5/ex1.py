import re

pattern = r'a(b*)'

string = input("Enter a string to check for the pattern 'a(b*)': ")

match = re.match(pattern, string)
if match:
    print(f"'{string}' matches the pattern 'a(b*)'")
else:
    print(f"'{string}' does not match the pattern 'a(b*)'")