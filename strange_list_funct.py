def strange_fun(n):

    strange_list = []

    for i in range(n):
        strange_list.insert(0, i)
    return strange_list

print(strange_fun(5))