# Write a Python program to count the number of lines in a text file.
#1.txt file name
a = input("file name ")
count = 0
with open(a, 'r') as f:
    for line in f:
        count += 1
print(count)