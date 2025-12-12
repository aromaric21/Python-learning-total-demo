liste = [32, 5, 12, 8, 3, 75, 2, 15, 125]

# for i in liste:
#       print(i, end=" ")
print(" ".join(str(x) for x in liste))
print(f"Le plus grand élément de cette liste est la valeur : {max(liste)}")



