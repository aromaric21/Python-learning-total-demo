import math

l = float(input("Enter la longueur du pendule: "))
g = float(input("Enter l'accélérateur de la pesanteur : "))

# Période T = 2 * pi * sqrt(l / g)
periode = 2 * math.pi * math.sqrt(l / g)

# Affichage des résultats
print(f" La période du pendule simple est : {periode:.2f}")
