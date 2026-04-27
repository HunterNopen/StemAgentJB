from source import is_future_date
import pytest

def test_valid_future_date():
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2026-02-01', '2026-01-31') is True

def test_valid_equal_date():
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_valid_past_date():
    assert is_future_date('2025-12-31', '2026-01-01') is False
    assert is_future_date('2025-01-01', '2025-01-02') is False

def test_invalid_dates():
    assert is_future_date('2021-02-30', '2021-01-01') is False
    assert is_future_date('2021-04-31', '2021-01-01') is False
    assert is_future_date('2021-13-01', '2021-01-01') is False
    assert is_future_date('2021-01-01', '2021-02-30') is False
    assert is_future_date('2021-01-01', '2021-04-31') is False
    assert is_future_date('2021-01-01', '2021-13-01') is False

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
    with pytest.raises(TypeError):
        is_future_date([], '2026-01-01')
    with pytest.raises(TypeError):
        is_future_date('2026-01-01', {})

def test_edge_cases():
    assert is_future_date('0001-01-01', '0001-01-01') is False
    assert is_future_date('9999-12-31', '9999-12-30') is True
    assert is_future_date('9999-12-31', '9999-12-31') is False
    assert is_future_date('2023-01-01', '2023-01-02') is False
    assert is_future_date('2023-01-02', '2023-01-01') is True

def test_invalid_format():
    assert is_future_date('2026/01/01', '2026-01-01') is False
    assert is_future_date('01-01-2026', '2026-01-01') is False
    assert is_future_date('2026-01-01', '01-01-2026') is False
    assert is_future_date('2026-01-01', '2026-01-01T00:00:00') is False

def test_boundary_dates():
    assert is_future_date('2026-01-01', '2026-01-02') is False
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2025-12-31', '2026-01-01') is False
    assert is_future_date('2026-01-01', '2026-01-01') is False

def test_leap_years():
    assert is_future_date('2024-02-29', '2024-02-28') is True
    assert is_future_date('2024-02-28', '2024-02-29') is False
    assert is_future_date('2020-02-29', '2020-02-28') is True
    assert is_future_date('2020-02-28', '2020-02-29') is False

def test_month_end_dates():
    assert is_future_date('2021-03-31', '2021-03-30') is True
    assert is_future_date('2021-03-30', '2021-03-31') is False
    assert is_future_date('2021-04-30', '2021-04-29') is True
    assert is_future_date('2021-04-29', '2021-04-30') is False

def test_edge_case_years():
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2025-12-31', '2026-01-01') is False

def test_boundary_years():
    assert is_future_date('9999-12-31', '9999-12-30') is True
    assert is_future_date('9999-12-30', '9999-12-31') is False

def test_comparison_edge_cases():
    assert is_future_date('2026-01-01', '2026-01-01') is False
    assert is_future_date('2026-01-02', '2026-01-01') is True
    assert is_future_date('2026-01-01', '2026-01-02') is False
    assert is_future_date('2026-01-01', '2025-12-31') is True
    assert is_future_date('2025-12-31', '2026-01-01') is False