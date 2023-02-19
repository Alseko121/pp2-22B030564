def cnt(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
x = cnt(n)
for i in x:
    print(i)
#from n to 0