for i in range(20):
    result = 7*i
    multiple_3 = result % 3
    if (0 == result % 3):
        print(f"{result}*", end=" ")
    else:
        print(f"{result}", end=" ")