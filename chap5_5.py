# Programme pour afficher les grains de riz du problème du jeu d'échecs
print("Case\tGrains (entier)\t\tNotation scientifique")

for i in range(1, 65):   # 64 cases
    grains = 2 ** (i - 1)  # Nombre exact
    grains_scientifique = f"{grains:.5e}"  # Notation scientifique

    print(f"{i}    \t{grains}              \t\t{grains_scientifique}")