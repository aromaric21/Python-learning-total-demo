import os

note = float(input("Saissisez votre note obtenue : "))
total_point = float(input("Saissisez le total des points : "))

note = float(note)
total_point = float(total_point)

#appreciation = ""
pourcentage = (note / total_point) * 100

if pourcentage >= 80:
    appreciation = "A"

elif pourcentage >= 60:
    appreciation = "B"
elif pourcentage >= 50:
    appreciation = "C"
elif pourcentage >= 40:
    appreciation = "D"
elif pourcentage < 40:
    appreciation = "E"
else:
    appreciation = "E"

print(f"Pourcentage : {pourcentage:.2f}%")
print(f"Appréciation : {appreciation}")
os.system("pause")

