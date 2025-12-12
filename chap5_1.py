import math


def dms_to_radians(degrees, minutes, seconds):

    # Conversion DMS → degrés décimaux
    decimal_degrees = degrees + minutes / 60 + seconds / 3600

    # Conversion degrés → radians
    radians = decimal_degrees * math.pi / 180
    return radians


# PP
d= int(input("Degrés: "))
m = int(input("Minutes: "))
s= int(input("Secondes: "))

resultat = dms_to_radians(d, m, s)
print(f"{d}° {m}' {s}\" = {resultat} radians")