from atkludosana_dzeramnauda import cena_uz_float, procenti_uz_float

def test_cena_uz_float():
    assert cena_uz_float("10") == 10
    assert cena_uz_float("10€") == 10



test_cena_uz_float()


