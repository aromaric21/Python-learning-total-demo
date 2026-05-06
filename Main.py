from Dvd_manager import DVDManager
from Dvd import DVD


manager = DVDManager()

def afficher_list():
    manager.lister_dvd()
    print("")
    
def ajouter_dvd():
    print("")
    titre = input("Titre : ")
    annee = input("Annee : ")
    realisateur = input("Realisateur : ")
    dvd = DVD(titre, realisateur, annee)
    manager.ajouter_dvd(dvd)
    
def supprimer_dvd():
    id = input("ID du DVD à supprimer ?")
    manager.supprimer_dvd(id)
     
while True:
    print("Gestion des DVD")
    print("1. Afficher la liste des DVD")
    print("2. Ajouter un DVD")
    print("3. Supprimer un DVD")
    print("4. Quitter le programme")
    print("")
    response = input("Votre choix :")
    print("")
    
    if response=="1":
        afficher_list()
    elif response=="2":
        ajouter_dvd()
    elif response=="3":
        supprimer_dvd()
    elif response=="4":
        manager.fermer_connexion()
        break
    else:
        print("Reponse invalide. Veiller réessayer")