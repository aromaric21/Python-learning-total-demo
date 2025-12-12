liste_de_mots = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']

moins_de_6 = []
six_ou_plus = []

for mot in liste_de_mots:
    if len(mot) < 6 :
        moins_de_6.append(mot)
    else:
        six_ou_plus.append(mot)

print("Mots avec moins de six caractères : ", moins_de_6)
print("Mots avec moins de six ou plus : ", six_ou_plus)



