def table(base):
    n = 1
    while n <= 11:
        print(n * base, end=' ')
        n = n + 1
a = 1
while a < 29:
    table(a)
    print()
    a += 1
