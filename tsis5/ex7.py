snake_case_string = input()

words = snake_case_string.split("_")

camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

print(f"The camel case string is: {camel_case}")