my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
uniq_elt_list = []

for i in my_list:
    if i not in uniq_elt_list:
        uniq_elt_list.append(i)
    continue
#
print("The list with unique elements only:")
print(uniq_elt_list)