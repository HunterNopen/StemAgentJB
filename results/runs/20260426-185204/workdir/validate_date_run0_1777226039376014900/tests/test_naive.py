import pytest
from source import validate_date

def test_valid_dates():
    assert validate_date('2024-02-29') == True
    assert validate_date('2023-01-01') == True
    assert validate_date('2023-12-31') == True
    assert validate_date('2000-02-29') == True
    assert validate_date('1900-02-28') == True
    assert validate_date('2024-04-30') == True
    assert validate_date('2024-06-30') == True
    assert validate_date('2024-09-30') == True
    assert validate_date('2024-11-30') == True
    assert validate_date('9999-12-31') == True

def test_type_errors():
    with pytest.raises(TypeError):
        validate_date(2024)
    with pytest.raises(TypeError):
        validate_date(2024.0)
    with pytest.raises(TypeError):
        validate_date([])