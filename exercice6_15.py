from statistics import mean

note_eleve = float(input("Saissisez une note : "))


listes_de_note = []

while note_eleve > 0 :
    note_eleve = float(input("Saissisez une note : "))
    listes_de_note.append(note_eleve)

print(f"Nombre total de note : {listes_de_note}")
print(f"La note la plus élévée est : {max(listes_de_note)}")
print(f"La note la plus basse est : {min(listes_de_note)}")
print(f"La moyenne de toutes les notes est : {mean(listes_de_note)}")
