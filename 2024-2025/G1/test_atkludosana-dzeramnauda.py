from atkludosana_dzeramnauda import cena_uz_float, procenti_uz_float

def test_cena_uz_float():
    assert cena_uz_float("10") == 10
    assert cena_uz_float("10€") == 10

def test_procenti_uz_float():
    assert procenti_uz_float("5") == 0.05
    assert procenti_uz_float("5%") == 0.05

# test_cena_uz_float()
test_procenti_uz_float()

