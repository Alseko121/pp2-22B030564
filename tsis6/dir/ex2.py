#C:\Users\murat\PycharmProjects\ to check
import os

path = input()

if os.path.exists(path):
    access = "exists"
    if os.access(path, os.R_OK):
        access += ", readable"
    if os.access(path, os.W_OK):
        access += ", writable"
    if os.access(path, os.X_OK):
        access += ", executable"
    print(f"{path} {access}")
else:
    print(f"{path} does not exist")