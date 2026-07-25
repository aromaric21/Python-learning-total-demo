for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")


for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)