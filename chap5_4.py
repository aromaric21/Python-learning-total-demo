capital = 100
taux = 0.043

print("Année | Capital")
print("-----------------------")

for annee in range(1, 21):
    capital += capital * (1 + taux)
    print(f"{annee:5d} | {capital:.2f} €")
print("###########################################")
print(f"Capital accumulé : {capital:.2f} €")
print("###########################################")