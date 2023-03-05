#Write a Python program with builtin function that accepts a string and
# calculate the number of upper case letters and lower case letters
import string

def cnt(s):
    up = sum(1 for char in s if char in string.ascii_uppercase)
    low = sum(1 for char in s if char in string.ascii_lowercase)
    return (up, low)

a = input("")
upper, lower = cnt(a)

print("uppercase", upper)
print("lowercase", lower)