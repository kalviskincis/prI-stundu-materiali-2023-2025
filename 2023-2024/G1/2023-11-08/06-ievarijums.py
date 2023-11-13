def ievarijums(abolu_daudzums, cena_cukurs):
    recepte_aboli = 3
    recepte_cukurs = 1.5

    izmaksas_receptei = recepte_cukurs * cena_cukurs
    izmaksas_1kg = izmaksas_receptei / recepte_aboli

    izmaksas = abolu_daudzums * izmaksas_1kg
    print(f"Ievārījumam no {abolu_daudzums} kg ābolu nepieciešams cukurs {izmaksas} vērtībā.")

cik_aboli = int(input("Cik āboli jāsavāra ievārījumā?"))
cukura_cena = float(input("Cik maksā cukurs 1 kg?"))
ievarijums(cik_aboli, cukura_cena)


