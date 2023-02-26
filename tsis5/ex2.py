import re

pattern = r'a(bb|bbb)'

string = input()

match = re.match(pattern, string)
if match:
    print(f"'{string}' have the 'a(bb|bbb)'")
else:
    print(f"'{string}' does not have the 'a(bb|bbb)'")
