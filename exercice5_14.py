liste = [32, 5, 12, 8, 3, 75, 2, 15, 120, 125, 100]
impairs = []
pairs = []

for i in liste:
    if i % 2 == 0:
        pairs.append(i)
    else:
        impairs.append(i)

print(pairs)
print(impairs)



