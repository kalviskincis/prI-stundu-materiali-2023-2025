import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("4/8") == 50
    assert convert("10/10") == 100
    assert convert("1/1000") == 0

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(100) == "F"

def test_dalit_ar_nulli():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

test_dalit_ar_nulli()