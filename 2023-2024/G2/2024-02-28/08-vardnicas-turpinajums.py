# Vārdnīca vingrinājumiem
visiSkaitli = {'četri': 'four', 'divi': 'two', 'trīs': 'three', 'viens': 'one'}

if 'pieci' in visiSkaitli:
    print(f'ir, {visiSkaitli['pieci']}')
else:
    print('Nav, tūlīt būs.')
    visiSkaitli['pieci'] = 'five'

print(visiSkaitli)


# Noņem komentāru zīmes nakamajām 5 rindām


# Vingrinājumi:
# 1) Izveido pārbaudi, vai vārdnīcā visiSkaitli ir atslēga 'septiņi'. Ja nav, tad pievieno atbilstošu atslēgas—vērtības pāri
"""
if 'septiņi' in visiSkaitli:
    print(f'ir, {visiSkaitli['septiņi']}')
else:
    print('Nav, tūlīt būs.')
    visiSkaitli['septiņi'] = 'seven'

print(visiSkaitli)
"""
# 2) Ja iepriekšējais izdevās, maini kodu, lai varētu pāraudīt jebkadu lietotāja ievadītu atslēgu un, ja tādas nav tad pievienot atbilstošu atslēgas-vērtības pāri, pirms tam noskaidrojot vēlamo vērtību.
koMeklet = input('Kādu atslēgu pārbaudīt?')
if koMeklet in visiSkaitli:
    print(f'Atrasts: {visiSkaitli[koMeklet]}')
else:
    print('Nav atrasts.')
    vertiba = input(f'Kāda būs vērtība atslēgai {koMeklet}')
    visiSkaitli[koMeklet] = vertiba
    print(visiSkaitli)
