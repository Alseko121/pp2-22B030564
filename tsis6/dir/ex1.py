#Write a Python program to list only directories, files and all directories, files in a specified path
#C:\Users\murat\PycharmProjects\ to check
import os
path = input("")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

print("\n")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

print("\nDirectories and Files:")
for item in os.listdir(path):
    print(item)