from source import validate_date

def test_validate_date_accepts_leap_day():
    assert validate_date("2024-02-29") is True