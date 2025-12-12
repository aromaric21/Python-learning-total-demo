# Constante gravitationnelle
G = 6.67e-11

# Masses (kg)
m1 = 10000
m2 = 10000

# Distance initiale (m)
d = 0.05

# Nombre de calculs
nb_valeurs = 4

print("Force de gravitation entre deux masses de 10 000 kg :\n")
for i in range(nb_valeurs):
    force = G * (m1 * m2) / (d ** 2)
    print(f"d = {d:.2f} m : la force vaut {force:.4f} N")
    d *= 2   # progression géométrique de raison 2

