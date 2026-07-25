def addition(*args):
    total = 0
    for arg in args:
        total += arg
    print(f"Les somme est {total}")


addition(1,5,8,11)