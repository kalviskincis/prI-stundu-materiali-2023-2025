from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_dala_ar_nulli():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

test_dala_ar_nulli()

