print("Suite de Fibonacci")

a,b,c=1,1,1               # a et b servent au calcul des termes successifs
                          # c est un simple compteur

print(b)                  # affichage du prémier terme
while c < 15:             # nous afficherons 15 termes au total
    a,b,c = b, a+b, c+1
    print(b)