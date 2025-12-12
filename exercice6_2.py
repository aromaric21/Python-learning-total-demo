# Saisie ses côtés
import math

a = float(input("Enter le premier côté a : "))
b = float(input("Enter le deuxième côté b : "))
c = float(input("Enter le troisième côté c : "))

# Périmètre : P = a + b + c
# Demi-périmètre : d = (a + b + c) / 2
# Aire (formule de Héron) : S = sqrt(d(d-a)(d-b)(d-c))

# Calcul du périmètre
perimetre = a + b + c

# Calcul du demi-périmètre
d = perimetre / 2

# Calcul de l'aire (formule de Héron)
aire = math.sqrt(d* (d - a) * (d - b) * (d - c))


# Affichage des résultats
print(f"Perimètre du triangle : {perimetre:.2f}")
print(f"Aire du triangle : {aire:.2f}")