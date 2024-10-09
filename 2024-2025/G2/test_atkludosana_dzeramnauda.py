from atkludosana_dzeramnauda import cena_uz_float, procenti_uz_float

def test_cena_uz_float():
    assert cena_uz_float("10") == 10
    assert cena_uz_float("10€") == 10

def test_procenti_uz_float():
    assert procenti_uz_float("15") == 0.15
    assert procenti_uz_float("15%") == 0.15

test_cena_uz_float()
test_procenti_uz_float()