import math as m
import pytest
import pytest_1 as e

def test_pos_int_diff():
    assert e.equalize(1,2) == 5.1962

def test_negative_numbers():
    assert e.equalize(2, -1) == 0.3333

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert e.equalize(2, 2) in str(er.value)

def test_positive_numbers():
    assert e.equalize(0.2, 0.1) == 1.6432

def test_negative_root():
    assert e.equalize(1, -2) == "can't sqrt negative"

def test_error_input():
    assert e.equalize("asdsa", 0) == "this is not number"
    assert e.equalize("", 0) == "this is not number"
    assert e.equalize("10**-9", 0) == "this is not number"