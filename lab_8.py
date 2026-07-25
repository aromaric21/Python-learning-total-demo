# Program of Collatz
c0 = int(input("Enter a natural number(non nul): "))

steps = 0

while c0 != 1:
    print(c0)   # Display currently value
    if c0 % 2 == 0: # if pair
        c0 = c0 // 2

    else:             # if impair
        c0 = 3 * c0 + 1

    steps += 1

print(c0) # Display the last 1
print("Steps = ",steps)