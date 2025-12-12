import os
from math import sqrt

# Saisie des longueurs
nombre = float(input("Saissisez un nombre : "))

# Racine carrée de ce nombre
if nombre >= 0:
    rc_nbre = sqrt(nombre)
    print(f"La racine carrée de ce nombre est : {rc_nbre}.")

else:
    print("la racine carrée de ce nombre ne peut être calculée.")

os.system("pause")

