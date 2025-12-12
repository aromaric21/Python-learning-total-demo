import os

nom = input("Saississsez votre nom : ")
sexe = input("Saississsez votre sexe (M ou F): ")

if sexe == "M":
    print(f"Cher Monsieur {nom}")
elif sexe == "F":
    print(f"Cher Mademoiselle {nom}")

else:
    print(f"Cher {nom}")

os.system("pause")

