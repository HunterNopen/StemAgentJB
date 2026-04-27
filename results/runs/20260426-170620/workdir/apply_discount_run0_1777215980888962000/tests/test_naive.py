import pytest
from source import apply_discount

def test_apply_discount_valid_cases():
    assert apply_discount(100, 25) == 75.0
    assert apply_discount(99.99, 10) == 89.99
    assert apply_discount(1.99, 50) == 0.99
    assert apply_discount(100.555, 10) == 90.5
    assert apply_discount(0, 50) == 0.0
    assert apply_discount(100, 0) == 100.0
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_edge_cases():
    assert apply_discount(100, 50) == 50.0
    assert apply_discount(50, 50) == 25.0
    assert apply_discount(200, 25) == 150.0

def test_apply_discount_invalid_cases():
    with pytest.raises(ValueError):
        apply_discount(100, 101)
    with pytest.raises(ValueError):
        apply_discount(-1, 10)
    with pytest.raises(ValueError):
        apply_discount(None, 10)
    with pytest.raises(ValueError):
        apply_discount(100, None)
    with pytest.raises(ValueError):
        apply_discount("100", 10)
    with pytest.raises(ValueError):
        apply_discount(100, "10")
    with pytest.raises(ValueError):
        apply_discount("100", "10")

def test_apply_discount_zero_discount():
    assert apply_discount(50, 0) == 50.0
    assert apply_discount(0, 0) == 0.0

def test_apply_discount_full_discount():
    assert apply_discount(50, 100) == 0.0
    assert apply_discount(0, 100) == 0.0

def test_apply_discount_non_numeric_price():
    with pytest.raises(ValueError):
        apply_discount([], 10)
    with pytest.raises(ValueError):
        apply_discount({}, 10)
    with pytest.raises(ValueError):
        apply_discount(set(), 10)

def test_apply_discount_non_numeric_discount():
    with pytest.raises(ValueError):
        apply_discount(100, [])
    with pytest.raises(ValueError):
        apply_discount(100, {})
    with pytest.raises(ValueError):
        apply_discount(100, set())