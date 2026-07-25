# The break and continue statements
import time

# break - example
print("The break instruction:")
for i in range(1, 6):
    time.sleep(1)
    if i == 3:
        time.sleep(2)
        break
    print("Inside the loop.", i)

print("Outside the loop")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    time.sleep(1)
    if i == 3:
        time.sleep(2)
        continue
    print("Inside the loop.", i)

print("Outside the loop.")