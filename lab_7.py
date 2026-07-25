blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
height=0
used=0
next_layer=1

while used + next_layer <= blocks:
    used += next_layer
    height += 1
    next_layer += 1

print("The height of the pyramid:", height)