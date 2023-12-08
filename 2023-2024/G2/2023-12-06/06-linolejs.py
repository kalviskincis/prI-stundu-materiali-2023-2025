import math

def gridas_izmaksas(cena, linoleja_platums, telpas_platums, telpas_garums):
    loksnes = math.ceil(telpas_platums / linoleja_platums)
    izmaksas = loksnes * linoleja_platums * telpas_garums * cena
    return izmaksas

print(gridas_izmaksas(8, 2, 10, 10))