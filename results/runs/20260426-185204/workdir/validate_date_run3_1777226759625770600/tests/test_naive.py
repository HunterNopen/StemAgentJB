import pytest
from source import validate_date

def test_valid_dates():
    assert validate_date('2024-02-29') == True
    assert validate_date('2023-01-01') == True
    assert validate_date('2023-12-31') == True
    assert validate_date('2000-02-29') == True
    assert validate_date('1900-02-28') == True
    assert validate_date('1996-02-29') == True
    assert validate_date('2024-04-30') == True
    assert validate_date('2024-06-30') == True
    assert validate_date('2024-09-30') == True
    assert validate_date('2024-11-30') == True

def test_edge_cases():
    assert validate_date('2024-02-28') == True
    assert validate_date('2023-02-28') == True
    assert validate_date('2024-02-29') == True
    assert validate_date('2023-02-29') == False
    assert validate_date('2024-04-30') == True
    assert validate_date('2024-06-30') == True
    assert validate_date('2024-09-30') == True
    assert validate_date('2024-11-30') == True
    assert validate_date('2024-12-31') == True
    assert validate_date('2024-01-01') == True

def test_non_string_input():
    with pytest.raises(TypeError):
        validate_date(2024)
    with pytest.raises(TypeError):
        validate_date(2024.0)
    with pytest.raises(TypeError):
        validate_date([])
    with pytest.raises(TypeError):
        validate_date({})
    with pytest.raises(TypeError):
        validate_date(set())
    with pytest.raises(TypeError):
        validate_date(True)
    with pytest.raises(TypeError):
        validate_date(False)