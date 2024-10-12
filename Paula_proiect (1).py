import re

def afisare_indiciu(cuvant_secret, indicii):
    rezultat = ''
    for idx in range(min(len(cuvant_secret), len(indicii))):
        if indicii[idx] != '*':
            rezultat += indicii[idx]
        else:
            rezultat += '*'
    return rezultat

def actualizeaza_indiciul(cuvant_secret, indicii, litera):
    indicii_noi = list(indicii)
    for idx, char in enumerate(cuvant_secret):
        if char == litera:
            indicii_noi[idx] = litera
    return ''.join(indicii_noi)

def citeste_cuvinte_din_fisier(fisier):
    cuvinte = []
    with open(fisier, 'r', encoding='utf-8') as f:
        for linie in f:
            parti = linie.split(';')
            if len(parti) == 3:
                indiciu, cuvant_corect = parti[1].strip(), parti[2].strip()
                cuvinte.append((indiciu, cuvant_corect))
    return cuvinte

def spanzuratoarea(fisier_cuvinte):
    cuvinte_de_verificat = citeste_cuvinte_din_fisier(fisier_cuvinte)

    # Variabile pentru a ține evidența rezultatelor
    cuvinte_ghicite = 0
    cuvinte_pierdute = 0
    total_incercari = 0  # Variabilă pentru a număra toate încercările

    for indiciu_initial, cuvant_secret in cuvinte_de_verificat:
        indicii = indiciu_initial
        numar_incercari = 400
        incercari_pentru_acest_cuvant = 0  # Contor pentru fiecare cuvânt
        litere_incercate = set()

        print("\nBine ai venit la jocul Spânzurătoarea!")
        print("Cuvântul de ghicit are indiciul inițial:", afisare_indiciu(cuvant_secret, indicii))

        while numar_incercari > 0 and "*" in indicii:
            for litera in cuvant_secret:  # Ghicește automat literele din cuvântul secret.
                litera = litera.upper()

                if litera in litere_incercate:
                    continue

                litere_incercate.add(litera)
                incercari_pentru_acest_cuvant += 1  # Incrementăm încercările pentru fiecare literă încercată

                if litera in cuvant_secret:
                    indicii = actualizeaza_indiciul(cuvant_secret, indicii, litera)
                    print(f"Litera {litera} a fost ghicită.")
                else:
                    numar_incercari -= 6
                    print(f"Litera {litera} nu este în cuvânt. Îți mai rămân {numar_incercari} încercări.")

                print("Indiciul actualizat:", afisare_indiciu(cuvant_secret, indicii))

            break

        # Totalizăm încercările pentru acest cuvânt
        total_incercari += incercari_pentru_acest_cuvant

        if "*" not in indicii:
            print("Felicitări! Ai ghicit cuvântul complet:", cuvant_secret)
            cuvinte_ghicite += 1  # Incrementăm pentru cuvânt ghicit
        else:
            print("Ai pierdut! Cuvântul era:", cuvant_secret)
            cuvinte_pierdute += 1  # Incrementăm pentru cuvânt pierdut

    # Afișarea rezultatului final
    print("\nRezultatul final:")
    print(f"Cuvinte ghicite: {cuvinte_ghicite}")
    print(f"Cuvinte pierdute: {cuvinte_pierdute}")
    print(f"Suma totală de încercări reușite: {cuvinte_ghicite} din {len(cuvinte_de_verificat)} cuvinte.")
    print(f"Au fost efectuate {total_incercari} încercări în total.")

# Citirea și rularea jocului folosind cuvintele din fișierul 'cuvinte_de_verificat.txt'
fisier_cuvinte = 'cuvinte_de_verificat.txt'
spanzuratoarea(fisier_cuvinte)
