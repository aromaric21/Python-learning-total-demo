t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []
t4 = []
for i in range(len(t2)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)

for i in range(len(t1)):
    t4.append(t1[i])
    t4.append(t2[i])

print(t4)