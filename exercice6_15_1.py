notes = []

while True:
    try:
        note = float(input("Entrez une note (valeur négative pour arrêter) : "))

        # Condition d'arrêt
        if note < 0:
            print("\n⛔ Saisie terminée.")
            break

        # Ajout de la note à la liste
        notes.append(note)

        # Calculs statistiques
        nombre_notes = len(notes)
        note_max = max(notes)
        note_min = min(notes)
        moyenne = sum(notes) / nombre_notes

        # Affichage des résultats
        print("\n📊 Statistiques actuelles :")
        print(f"Nombre de notes : {nombre_notes}")
        print(f"Note la plus élevée : {note_max}")
        print(f"Note la plus basse : {note_min}")
        print(f"Moyenne des notes : {moyenne:.2f}\n")

    except ValueError:
        print("❌ Veuillez entrer un nombre valide.\n")
