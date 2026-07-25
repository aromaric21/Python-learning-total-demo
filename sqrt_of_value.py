# Initialisation

x = 1

precision= 0.001

# Iteractif loop
while abs(x**2 - 2) > precision:
    x = (x + 2/x) / 2


print(x)