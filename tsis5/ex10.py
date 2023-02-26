import re

string = input("Enter a camel case string: ")

snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

print(f"The resulting snake case string is: {snake_case_string}")