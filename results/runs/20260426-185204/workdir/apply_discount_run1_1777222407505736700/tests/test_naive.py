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

def test_apply_discount_non_numeric_price():
    with pytest.raises(ValueError):
        apply_discount('100', 10)
    with pytest.raises(ValueError):
        apply_discount([100], 10)
    with pytest.raises(ValueError):
        apply_discount({100}, 10)
    with pytest.raises(ValueError):
        apply_discount((100,), 10)

def test_apply_discount_non_numeric_discount():
    with pytest.raises(ValueError):
        apply_discount(100, '10')
    with pytest.raises(ValueError):
        apply_discount(100, [10])
    with pytest.raises(ValueError):
        apply_discount(100, {10})
    with pytest.raises(ValueError):
        apply_discount(100, (10,))

def test_apply_discount_negative_price():
    with pytest.raises(ValueError):
        apply_discount(-10, 10)

def test_apply_discount_discount_out_of_bounds():
    with pytest.raises(ValueError):
        apply_discount(100, -1)
    with pytest.raises(ValueError):
        apply_discount(100, 101)