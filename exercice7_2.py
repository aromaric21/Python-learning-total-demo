def ligneCar(n, ca):
    if not isinstance(n, int):
        raise TypeError('n doit être un entier')

    if n < 0:
        raise ValueError('n doit être positif ou nul')

    return ca *n

# PP
print(ligneCar(5, '*'))
print(ligneCar(3, 'x'))
print(ligneCar(0, 'a'))

print(ligneCar(4, 'ab'))
print(ligneCar(2, 7))

print(ligneCar(-2, 7))
print(ligneCar("c", 7))
