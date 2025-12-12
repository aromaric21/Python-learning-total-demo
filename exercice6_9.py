# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non
import os

annee = input("Saississsez une année : ")
annee = int(annee)

bissextile = False   # On crée un booléen qui vaut vrai ou faux

if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print("L'année saisie est bisextile.")
else:
    print("L'année saisie n'est pas bisextile.")

os.system('pause')