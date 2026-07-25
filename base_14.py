counter = 5
while True:
    print("Stuck in an infinite loop")
    counter -= 1
    if counter == 0:
        break


# Exemple 2
counter1 = 5
while counter1 > 2:
    print(counter1)
    counter1 -= 1