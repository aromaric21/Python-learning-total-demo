# Conversion d'un nombre total de secondes en années, mois, jours, heures, minutes et secondes

total_seconds = int(input("Entrez un nombre de secondes : "))

# Définition des durées
seconds_per_minute = 60
seconds_per_hour = 60 * 60
seconds_per_day = 24 * 3600
seconds_per_month = 30 * seconds_per_day     # approximation (1 mois = 30 jours)
seconds_per_year = 12 * seconds_per_month    # approximation (1 an = 12 mois)


# Calculs
years = total_seconds // seconds_per_year
remaining_seconds = total_seconds % seconds_per_year

months = remaining_seconds // seconds_per_month
remaining_seconds %= seconds_per_month

days = remaining_seconds // seconds_per_day
remaining_seconds %= seconds_per_day

hours = remaining_seconds // seconds_per_hour
remaining_seconds %= seconds_per_hour

minutes = remaining_seconds // seconds_per_minute
seconds = remaining_seconds % seconds_per_minute

# Résultat
print("\nConversion :")
print("Années   :", years)
print("Mois     :", months)
print("Jours    :", days)
print("Heures   :", hours)
print("Minutes  :", minutes)
print("Secondes :", seconds)