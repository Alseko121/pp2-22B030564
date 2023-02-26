import re
string = input()

new_string = re.sub(r'(?<!\s)[A-Z]', lambda x: f" {x.group(0)}", string).strip()

print(f" {new_string}")