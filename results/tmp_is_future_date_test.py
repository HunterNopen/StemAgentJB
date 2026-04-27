import pytest
from source import is_future_date

def test_valid_future_dates():
    assert is_future_date("2026-01-02", "2026-01-01") is True
    assert is_future_date("2026-01-01", "2025-12-31") is True
    assert is_future_date("2026-02-01", "2026-01-31") is True

def test_equal_dates():
    assert is_future_date("2026-01-01", "2026-01-01") is False
    assert is_future_date("2025-12-31", "2025-12-31") is False

def test_valid_past_dates():
    assert is_future_date("2025-12-31", "2026-01-01") is False
    assert is_future_date("2025-01-01", "2025-01-02") is False

def test_invalid_dates():
    assert is_future_date("2021-02-30", "2021-01-01") is False  # Invalid day
    assert is_future_date("2021-04-31", "2021-01-01") is False  # Invalid day
    assert is_future_date("2021-13-01", "2021-01-01") is False  # Invalid month
    assert is_future_date("2021-01-01", "2021-02-30") is False  # Invalid day in current date

def test_none_inputs():
    with pytest.raises(ValueError):
        is_future_date(None, "2026-01-01")
    with pytest.raises(ValueError):
        is_future_date("2026-01-01", None)

def test_non_string_inputs():
    with pytest.raises(TypeError):
        is_future_date(2026, "2026-01-01")
    with pytest.raises(TypeError):
        is_future_date("2026-01-01", 2026)
    with pytest.raises(TypeError):
        is_future_date([], "2026-01-01")
    with pytest.raises(TypeError):
        is_future_date("2026-01-01", {})

def test_edge_cases():
    assert is_future_date("0001-01-01", "0001-01-01") is False  # Earliest valid date
    assert is_future_date("9999-12-31", "9999-12-30") is True  # Latest valid date
    assert is_future_date("2023-01-01", "2023-01-02") is False  # Same year, next day
    assert is_future_date("2023-01-01", "2022-12-31") is True  # Year difference

def test_malformed_strings():
    assert is_future_date("2026-01-0A", "2026-01-01") is False  # Non-numeric day
    assert is_future_date("2026-01-01", "2026-01-0B") is False  # Non-numeric day in current date
    assert is_future_date("2026-01-01", "2026-01") is False  # Incomplete current date
    assert is_future_date("2026-01", "2026-01-01") is False  # Incomplete target date

def test_leap_years():
    assert is_future_date("2024-02-29", "2024-02-28") is True  # Leap year
    assert is_future_date("2023-02-29", "2023-02-28") is False  # Non-leap year
    assert is_future_date("2020-02-29", "2020-02-28") is True  # Leap year
    assert is_future_date("2020-02-28", "2020-02-29") is False  # Leap year comparison

def test_boundary_dates():
    assert is_future_date("2023-01-01", "2022-12-31") is True  # New Year boundary
    assert is_future_date("2023-01-01", "2023-01-01") is False  # Same day boundary
    assert is_future_date("2023-01-02", "2023-01-01") is True  # Next day boundary
    assert is_future_date("2023-01-01", "2023-01-02") is False  # Previous day boundary