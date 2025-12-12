notes = []
coeffs = []

while True:
    # ----- Saisie de la note avec contrôle -----
    while True:
        note = float(input("Entrez une note (entre 0 et 20) : "))
        if 0 <= note <= 20:
            break
        else:
            print("❌ Erreur : la note doit être comprise entre 0 et 20.")

    # ----- Saisie du coefficient avec contrôle -----
    while True:
        coeff = float(input("Entrez le coefficient (> 0) : "))
        if coeff > 0:
            break
        else:
            print("❌ Erreur : le coefficient doit être strictement positif.")

    # Ajout dans les listes
    notes.append(note)
    coeffs.append(coeff)

    # ----- Calculs -----
    nombre_notes = len(notes)
    note_max = max(notes)
    note_min = min(notes)

    somme_ponderee = 0
    somme_coeffs = 0

    for i in range(nombre_notes):
        somme_ponderee += notes[i] * coeffs[i]
        somme_coeffs += coeffs[i]

    moyenne = somme_ponderee / somme_coeffs

    # ----- Affichage -----
    print("\n📊 Statistiques après saisie")
    print("Nombre de notes :", nombre_notes)
    print("Note la plus élevée :", note_max)
    print("Note la plus basse :", note_min)
    print("Moyenne pondérée :", round(moyenne, 2))

    # Continuer ou arrêter
    continuer = input("\nAjouter une autre note ? (o/n) : ")
    if continuer.lower() != 'o':
        break
