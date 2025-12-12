def fahrenheit_to_celsius(tf):
    return (tf - 32) / 1.8

def celsius_to_fahrenheit(tc):
    return tc * 1.8 + 32

def afficher_menu_principal():
    print("\n======= MENU PRINCIPAL =======")
    print("1 - Menu des conversions")
    print("2 - Aide")
    print("3 - Quitter")

def afficher_menu_conversion():
    print("\n----- MENU DES CONVERSIONS -----")
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    print("3 - Retour au menu principal")

while True:
   afficher_menu_principal()
   choix = input("Choisissez une option entre (1 - 2) :")

   if choix == "1":
       # Menu des conversions
       while True:
           afficher_menu_conversion()
           sous_choix = input("choississez une conversion : ")

           if sous_choix == "1":
               try:
                   tc = float(input("Entrez la température en °C : "))
                   tf = celsius_to_fahrenheit(tc)
                   print(f"Résultat : {tc} °C = {tf:.2f} °F")
               except ValueError:
                   print("Erreur :  veuillez entrez un nombre valide !")

           elif sous_choix == "2":
               try:
                   tf = float(input("Entrez la température en °F : "))
                   tc = fahrenheit_to_celsius(tf)
                   print(f"Résultat : {tf} °F = {tc:.2f} °C")
               except ValueError:
                   print("Erreur:  veuillez entrez un nombre valide !")
           elif sous_choix == "3":
               print("Retour au menu principal")
               break
           else:
               print("Option invalde, veuillez réessayer.")

   elif choix == "2":
       print("\n===== AIDE =====")
       print("Ce programme permet :")
       print("- de convertir Celsius ↔ Fahrenheit")
       print("- d’utiliser un menu avancé")
       print("- de revenir en arrière à tout moment")
       print("Formules :")
       print("  TF = TC × 1.8 + 32")
       print("  TC = (TF - 32) / 1.8")

   elif choix == "3":
       print("Fermeture du programme. À bientôt !")
       break

   else:
        print("Option inconnue, merci de choisir 1, 2 ou 3.")