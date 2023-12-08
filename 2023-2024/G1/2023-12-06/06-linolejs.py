import math

def gridas_izmaksas(cena, linoleja_platums, telpas_platums, telpas_garums):
    loksnes = math.ceil(telpas_platums / linoleja_platums)
    linoleja_laukums = loksnes * telpas_garums * linoleja_platums
    izmaksas = linoleja_laukums * cena
    return izmaksas

print(gridas_izmaksas(8, 4, 9, 5))