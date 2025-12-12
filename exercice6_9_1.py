# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non
import os

annee = input("Saississsez une année : ")
annee = int(annee)

bissextile = False   # On crée un booléen qui vaut vrai ou faux

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bisextile.")
else:
    print("L'année saisie n'est pas bisextile.")


os.system("pause")