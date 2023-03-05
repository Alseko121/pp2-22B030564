with open('a.txt', 'r') as a, open('b.txt', 'b') as b:
    for line in a:
        b.write(line)