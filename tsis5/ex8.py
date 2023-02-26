import re

string = input()

split_string = re.findall(r'[A-Z][^A-Z]*', string)

print(f" {split_string}")