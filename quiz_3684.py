list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
print(list_3)

print("####################################################")
del list_1[0]
print(f" Liste 1 : {list_1}")
print(f" Liste 3 : {list_3}")
print("####################################################")
del list_2[0]
print(f" Liste 2 = {list_2}")
print(f" Liste 3 : {list_3}")
print("######################################################")
print(f" Liste 3 = {list_3}")

