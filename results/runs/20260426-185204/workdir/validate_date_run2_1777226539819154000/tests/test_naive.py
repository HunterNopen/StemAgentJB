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
    assert validate_date('2024-01-31') == True
    assert validate_date('9999-12-31') == True

def test_edge_cases():
    assert validate_date('2024-02-28') == True
    assert validate_date('2024-02-29') == True
    assert validate_date('2023-02-28') == True
    assert validate_date('2023-02-29') == False
    assert validate_date('2024-04-30') == True
    assert validate_date('2024-06-30') == True
    assert validate_date('2024-09-30') == True
    assert validate_date('2024-11-30') == True
    assert validate_date('2024-01-31') == True
    assert validate_date('2024-02-30') == False
    assert validate_date('2024-02-29') == True
    assert validate_date('2024-02-28') == True
    assert validate_date('2024-02-29') == True
    assert validate_date('2024-02-30') == False
    assert validate_date('2024-02-31') == False
    assert validate_date('2024-03-31') == True
    assert validate_date('2024-04-31') == False
    assert validate_date('2024-05-31') == True
    assert validate_date('2024-06-31') == False
    assert validate_date('2024-07-31') == True
    assert validate_date('2024-08-31') == True
    assert validate_date('2024-09-31') == False
    assert validate_date('2024-10-31') == True
    assert validate_date('2024-11-31') == False
    assert validate_date('2024-12-31') == True