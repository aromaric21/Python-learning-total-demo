# Saisie des longueurs
a = float(input("longueur a du triangle: "))
b = float(input("longueur b du triangle: "))
c = float(input("longueur c du triangle: "))

# Vérification de l'existence du triangle
if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle")

    est_rectangle = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
    est_equilateral = (a == b == c)
    est_isocele = (a == b) or (a == c) or (b == c)

    # Determination du type de triangle
    if est_equilateral:
         print("Triangle équilatéral")
    elif est_rectangle and est_isocele:
         print("Triangle rectangle et isocèle")
    elif est_rectangle:
         print("Triangle rectangle")
    elif est_isocele:
         print("Triangle isocèle")
    else:
         print("Triangle quelconque")

else:
    print("Il est impossible de construire un triangle avec ces longueurs.")

