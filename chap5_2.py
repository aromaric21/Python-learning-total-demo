import math

# Demander la valeur en radians
radians = float(input("Entrez l'angle en radians: "))

# Convertion en dégrées
degres = math.degrees(radians)

print("*************** Convertion en dégrées ***********************************")
print(degres)
print("***********************************************************")

# Extraire degrés, minutes, secondes
d=int(degres)
print("********************** Extrait Degrés ****************************")
print(d)
print("***********************************************************")

reste = abs(degres-d)
print("********************** Extrait reste ****************************")
print(reste)
print("***********************************************************")

m= int(reste * 60)
print("********************** Extrait minutes ****************************")
print(m)
print("***********************************************************")
s= (reste*60 - m) * 60
print("********************** Extrait secondes ****************************")
print(s)
print("***********************************************************")

print(f"{radians} rad= {d}° {m}' {s:.2f}''")