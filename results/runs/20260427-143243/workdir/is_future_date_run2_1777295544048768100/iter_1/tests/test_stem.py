from source import is_future_date
import pytest

def test_is_future_date_valid_cases():
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2026-02-01', '2026-01-31') is True
    assert is_future_date('2026-01-01', '2025-12-31') is True

def test_is_future_date_equal_dates():
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_is_future_date_none_input():
    with pytest.raises(ValueError):
        is_future_date(None, '2026-01-01')
    with pytest.raises(ValueError):
        is_future_date('2026-01-01', None)

def test_is_future_date_non_string_input():
    with pytest.raises(TypeError):
        is_future_date(2026, '2026-01-01')
    with pytest.raises(TypeError):
        is_future_date('2026-01-01', 2026)
    with pytest.raises(TypeError):
        is_future_date([], '2026-01-01')
    with pytest.raises(TypeError):
        is_future_date('2026-01-01', {})

def test_is_future_date_boundary_cases():
    assert is_future_date('0001-01-01', '0001-01-01') is False
    assert is_future_date('9999-12-31', '9999-12-30') is True
    assert is_future_date('9999-12-31', '10000-01-01') is False

def test_is_future_date_edge_cases():
    assert is_future_date('2026-01-01', '2026-01-02') is False
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_is_future_date_invalid_format():
    assert is_future_date('2026/01/01', '2026-01-01') is False
    assert is_future_date('01-01-2026', '2026-01-01') is False
    assert is_future_date('2026-01-01T00:00:00', '2026-01-01') is False

def test_is_future_date_leap_year():
    assert is_future_date('2024-02-29', '2024-02-28') is True
    assert is_future_date('2023-02-29', '2023-02-28') is False

def test_is_future_date_edge_case_years():
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2025-12-31', '2026-01-01') is False

def test_is_future_date_invalid_day():
    assert is_future_date('2026-04-31', '2026-04-30') is False
    assert is_future_date('2026-02-30', '2026-02-29') is False

def test_is_future_date_invalid_month():
    assert is_future_date('2026-13-01', '2026-12-31') is False
    assert is_future_date('2026-00-01', '2026-01-01') is False

def test_is_future_date_invalid_year():
    assert is_future_date('10000-01-01', '9999-12-31') is False
    assert is_future_date('0000-01-01', '0001-01-01') is False

def test_is_future_date_future_date_with_leap_year():
    assert is_future_date('2024-02-29', '2024-02-28') is True
    assert is_future_date('2024-03-01', '2024-02-29') is True

def test_is_future_date_invalid_date_format():
    assert is_future_date('2026-01-32', '2026-01-01') is False
    assert is_future_date('2026-01-01', '2026-01-32') is False

def test_is_future_date_edge_case_comparisons():
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2025-12-31', '2026-01-01') is False
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_is_future_date_boundary_years():
    assert is_future_date('9999-12-31', '9999-12-30') is True
    assert is_future_date('0001-01-01', '0001-01-01') is False

def test_is_future_date_invalid_string_input():
    assert is_future_date('not-a-date', '2026-01-01') is False
    assert is_future_date('2026-01-01', 'not-a-date') is False