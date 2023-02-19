def div(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

nums = div(n)
for num in nums:
    print(num)
#divisible 3 and 4