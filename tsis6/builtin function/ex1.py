#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)
list = [2, 4, 6]
a = multiply_list(list)
print(a)