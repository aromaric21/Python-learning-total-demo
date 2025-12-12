# Demander la vitesse en miles par heure
vitesse_mph = float(input("Enter la vitesse en miles par heure (mph): "))

# Conversions
# 1 mile = 1609 mètres
vitesse_m_s = (vitesse_mph * 1609) / 3600
vitesse_m_h = vitesse_mph * 1.609


# Affichage des résultats
print(f"Vitesse en miles/secondes (m/s) : {vitesse_m_s:.2f} m/s")
print(f"Vitesse en miles/heures (m/h) : {vitesse_m_h:.2f} km/h")