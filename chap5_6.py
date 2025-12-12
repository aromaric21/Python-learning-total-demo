chaine = "La programmation Python"
i=0
for c in chaine:
    if c=="e":
        i +=1
if i:
    print(f"La chaine contient {i} 'e'")
else:
    print(f"Aucun 'e' trouvé")