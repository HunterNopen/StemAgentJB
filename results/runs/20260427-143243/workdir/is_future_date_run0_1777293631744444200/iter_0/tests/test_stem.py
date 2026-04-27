import pytest
from source import is_future_date

def test_valid_future_date():
    assert is_future_date('2026-01-02', '2026-01-01') is True

def test_valid_equal_date():
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_valid_past_date():
    assert is_future_date('2025-12-31', '2026-01-01') is False

def test_invalid_date_string():
    assert is_future_date('invalid-date', '2026-01-01') is False
    assert is_future_date('2026-01-01', 'invalid-date') is False

def test_none_inputs():
    with pytest.raises(ValueError):
        is_future_date(None, '2026-01-01')
    with pytest.raises(ValueError):
        is_future_date('2026-01-01', None)

def test_non_string_inputs():
    with pytest.raises(TypeError):
        is_future_date(2026, '2026-01-01')
    with pytest.raises(TypeError):
        is_future_date('2026-01-01', 2026)

def test_edge_case_years():
    assert is_future_date('9999-12-31', '9999-12-30') is True
    assert is_future_date('10000-01-01', '9999-12-31') is False
    assert is_future_date('0001-01-01', '0001-01-01') is False

def test_edge_case_days():
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2026-01-02') is False

def test_invalid_years():
    assert is_future_date('2026-01-01', '2026-01-32') is False
    assert is_future_date('2026-01-01', '2026-00-01') is False
    assert is_future_date('2026-01-01', '2026-13-01') is False

def test_invalid_months():
    assert is_future_date('2026-01-01', '2026-02-30') is False
    assert is_future_date('2026-01-01', '2026-02-29') is False

def test_valid_dates_with_leap_years():
    assert is_future_date('2024-02-29', '2023-02-28') is True
    assert is_future_date('2023-02-28', '2024-02-29') is False

def test_valid_dates_with_different_years():
    assert is_future_date('2027-01-01', '2026-12-31') is True
    assert is_future_date('2025-01-01', '2026-01-01') is False

def test_valid_dates_with_different_months():
    assert is_future_date('2026-02-01', '2026-01-31') is True
    assert is_future_date('2026-01-31', '2026-02-01') is False

def test_valid_dates_with_different_days():
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2026-01-02') is False

def test_edge_case_invalid_dates():
    assert is_future_date('2023-02-29', '2023-02-28') is False
    assert is_future_date('2023-04-31', '2023-04-30') is False

def test_edge_case_empty_strings():
    assert is_future_date('', '2026-01-01') is False
    assert is_future_date('2026-01-01', '') is False
    assert is_future_date('', '') is False

def test_edge_case_whitespace_strings():
    assert is_future_date('   ', '2026-01-01') is False
    assert is_future_date('2026-01-01', '   ') is False
    assert is_future_date('   ', '   ') is False