import pytest
from source import validate_date

def test_valid_dates():
    assert validate_date('2024-02-29') is True
    assert validate_date('2023-01-01') is True
    assert validate_date('2023-12-31') is True
    assert validate_date('2024-04-30') is True
    assert validate_date('2024-06-30') is True
    assert validate_date('2024-11-30') is True
    assert validate_date('2024-01-31') is True

def test_invalid_dates():
    assert validate_date('2023-02-29') is False
    assert validate_date('2024-13-01') is False
    assert validate_date('2024-02-30') is False
    assert validate_date('2024-04-31') is False
    assert validate_date('2024-06-31') is False
    assert validate_date('2024-11-31') is False
    assert validate_date('2024-02-28') is True
    assert validate_date('2024-02-29') is True
    assert validate_date('2024-02-27') is True
    assert validate_date('2024-02-01') is True

def test_boundary_years():
    assert validate_date('0000-01-01') is False
    assert validate_date('0001-01-01') is True
    assert validate_date('9999-12-31') is True
    assert validate_date('10000-01-01') is False

def test_edge_cases():
    assert validate_date('2024-02-29') is True
    assert validate_date('2023-02-29') is False
    assert validate_date('2024-04-31') is False
    assert validate_date('2024-06-31') is False
    assert validate_date('2024-11-31') is False
    assert validate_date('2024-01-01') is True
    assert validate_date('2024-12-31') is True

def test_leap_years():
    assert validate_date('2000-02-29') is True
    assert validate_date('1900-02-29') is False
    assert validate_date('2024-02-29') is True
    assert validate_date('2023-02-29') is False

def test_month_boundaries():
    assert validate_date('2024-01-01') is True
    assert validate_date('2024-01-31') is True
    assert validate_date('2024-02-01') is True
    assert validate_date('2024-02-28') is True
    assert validate_date('2024-02-29') is True
    assert validate_date('2024-03-01') is True
    assert validate_date('2024-03-31') is True
    assert validate_date('2024-04-30') is True
    assert validate_date('2024-05-31') is True
    assert validate_date('2024-06-30') is True
    assert validate_date('2024-07-31') is True
    assert validate_date('2024-08-31') is True
    assert validate_date('2024-09-30') is True
    assert validate_date('2024-10-31') is True
    assert validate_date('2024-11-30') is True
    assert validate_date('2024-12-31') is True