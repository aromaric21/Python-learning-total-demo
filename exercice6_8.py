a, b = 0, 50
somme = 0

for nombre in range(a, b):
    if (nombre % 3 == 0) & (nombre % 5 == 0):
        somme += nombre

print(somme)