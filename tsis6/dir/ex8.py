import os
file= "C:\Users\murat\Tsis\TSIS1\tsis6\dir and files\a.txt"

if os.path.exists(file):
    if os.access(file, os.R_OK) and os.access(file, os.W_OK):
        os.remove(file)
        print(f" {file} deleted.")
    else:
        print(f"You do not have access {file}.")
else:
    print(f" {file} does not exist.")