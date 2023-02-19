def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input("a:"))
b = int(input("b: "))

for sqr in squares(a, b):
    print(sqr)
#squares of all numbers from a to b