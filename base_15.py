# Exemple 1
word = "Python"

for letter in word:
    print(letter, end="*")



# Exemple 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)



text = "OpenEDG Python Institute"
for letter in text:
    if letter == "p":
        break
    print(letter, end="")


