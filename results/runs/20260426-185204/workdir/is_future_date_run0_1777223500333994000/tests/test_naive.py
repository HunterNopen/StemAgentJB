import pytest
from source import is_future_date

def test_is_future_date_none_inputs():
    with pytest.raises(ValueError):
        is_future_date(None, '2021-01-01')
    with pytest.raises(ValueError):
        is_future_date('2021-01-01', None)

def test_is_future_date_non_string_inputs():
    with pytest.raises(TypeError):
        is_future_date(2021, '2021-01-01')
    with pytest.raises(TypeError):
        is_future_date('2021-01-01', 2021)
    with pytest.raises(TypeError):
        is_future_date(['2021-01-01'], '2021-01-01')
    with pytest.raises(TypeError):
        is_future_date('2021-01-01', ['2021-01-01'])