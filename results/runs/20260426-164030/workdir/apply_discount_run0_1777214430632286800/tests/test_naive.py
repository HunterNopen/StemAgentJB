import pytest
from source import apply_discount

def test_apply_discount_valid_cases():
    assert apply_discount(100, 25) == 75.0
    assert apply_discount(99.99, 10) == 89.99
    assert apply_discount(0, 50) == 0.0
    assert apply_discount(100, 0) == 100.0
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_invalid_discount_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 101)
    with pytest.raises(ValueError):
        apply_discount(100, -1)

def test_apply_discount_invalid_price():
    with pytest.raises(ValueError):
        apply_discount(-1, 10)

def test_apply_discount_none_values():
    with pytest.raises(ValueError):
        apply_discount(None, None)
    with pytest.raises(ValueError):
        apply_discount(None, 10)
    with pytest.raises(ValueError):
        apply_discount(100, None)

def test_apply_discount_invalid_types():
    with pytest.raises(TypeError):
        apply_discount("100", 10)
    with pytest.raises(TypeError):
        apply_discount(100, "10")
    with pytest.raises(TypeError):
        apply_discount("100", "10")

def test_apply_discount_edge_cases():
    assert apply_discount(100.00, 0) == 100.00
    assert apply_discount(100.00, 100) == 0.00
    assert apply_discount(50.50, 50) == 25.25
    assert apply_discount(200.00, 25) == 150.00
    assert apply_discount(150.75, 33.33) == 100.00

def test_apply_discount_rounded_cases():
    assert apply_discount(100.555, 10) == 90.50
    assert apply_discount(99.999, 10) == 89.99
    assert apply_discount(123.456, 50) == 61.73