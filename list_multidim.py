temps = [[0.0 for h in range(24)] for d in range(31)]

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon :", average)

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]


