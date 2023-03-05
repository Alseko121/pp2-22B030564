#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def plndrm(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
#reverse and lower case
a = input("")

if plndrm(a):
    print("Yes")
else:
    print("No")