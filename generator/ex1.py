def square_generator(N):
    for i in range(N):
        yield i**2
N = int(input())

squares = square_generator(N)

for square in squares:
    print(square)
#squares