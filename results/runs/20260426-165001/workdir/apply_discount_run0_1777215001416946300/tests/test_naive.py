import pytest
from source import apply_discount

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
    
    with pytest.raises(ValueError):
        apply_discount(100, None)
    
    with pytest.raises(ValueError):
        apply_discount("100", 10)
    
    with pytest.raises(ValueError):
        apply_discount(100, "10")
    
    with pytest.raises(ValueError):
        apply_discount([100], 10)
    
    with pytest.raises(ValueError):
        apply_discount(100, [10])

def test_apply_discount_edge_cases():
    assert apply_discount(50, 0) == 50.0
    assert apply_discount(50, 100) == 0.0
    assert apply_discount(1.99, 50) == 0.995
    assert apply_discount(100.00, 50.00) == 50.0
    assert apply_discount(200, 25) == 150.0

def test_apply_discount_rounded_cases():
    assert apply_discount(100.555, 10) == 90.50
    assert apply_discount(99.999, 10) == 89.99
    assert apply_discount(100.001, 10) == 90.00

if __name__ == "__main__":
    pytest.main()