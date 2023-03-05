# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.
#C:\Users\murat\PycharmProjects\ to check
import os

path = input("path: ")

if os.path.exists(path):
    print("Path exists")
    directory, file = os.path.split(path)
    print(f"Directory: {directory}")
    print(f"Filename: {file}")
else:
    print("Path doesnt exist")