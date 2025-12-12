def fahrenheit_to_celsius(tf):
    return (tf - 32) / 1.8

def celsius_to_fahrenheit(tc):
    return tc * 1.8 + 32

while True:
    print("=== Convertisseur Celsius / Fahrenheit ===")
    print("1 - Convertir Celsius vers Fahrenheit")
    print("2 - Convertir Fahrenheit vers Celsius")
    choix = input("Choisissez une option (1 ou 2) : ")

    if choix == "1":
        tc = float(input("Entrez la température en °C : "))
        tf = celsius_to_fahrenheit(tc)
        print(f"{tc} °C = {tf:.2f} °F")

    elif choix == "2":
        tf = float(input("Entrez la température en °F : "))
        tc = fahrenheit_to_celsius(tf)
        print(f"{tf} °F = {tc:.2f} °C")

    else:
        print("Option invalide. Veuillez entrer 1 ou 2.")

    # Option pour continuer
    continuer = input("\nVoulez-vous continuer ? (o/n) : ").lower()
    if continuer != "o":
        print("Programme terminé. Au revoir !")
        break