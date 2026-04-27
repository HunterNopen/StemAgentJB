import pytest
from your_module import apply_discount  # Replace 'your_module' with the actual module name

def test_apply_discount_valid_cases():
    assert apply_discount(100, 25) == 75.0
    assert apply_discount(99.99, 10) == 89.99
    assert apply_discount(0, 50) == 0.0
    assert apply_discount(100, 0) == 100.0
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_invalid_cases():
    with pytest.raises(ValueError):
        apply_discount(100, 101)
    with pytest.raises(ValueError):
        apply_discount(-1, 10)
    with pytest.raises(ValueError):
        apply_discount(None, 10)
    with pytest.raises(TypeError):
        apply_discount("100", 10)
    with pytest.raises(TypeError):
        apply_discount(100, "10")
    with pytest.raises(TypeError):
        apply_discount(None, None)

def test_apply_discount_edge_cases():
    assert apply_discount(100.00, 50) == 50.0
    assert apply_discount(50.50, 50) == 25.25
    assert apply_discount(200, 0) == 200.0
    assert apply_discount(200, 100) == 0.0
    assert apply_discount(123.456, 33.33) == round(123.456 - 123.456 * (33.33 / 100.0), 2)