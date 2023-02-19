import math

num = int(input("number of sides: "))
length = int(input("length of a side: "))

area = (num * length ** 2) // (4 * math.tan(math.pi / num))

print(f"The area of the polygon is: {area}")