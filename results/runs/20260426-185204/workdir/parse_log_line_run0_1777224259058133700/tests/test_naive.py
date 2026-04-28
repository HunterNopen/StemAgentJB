import pytest
from source import parse_log_line

def test_parse_log_line_malformed():
    assert parse_log_line('malformed') is None
    assert parse_log_line('') is None
    assert parse_log_line('2024-01-05 12:10 INFO') is None
    assert parse_log_line('2024-01-05 25:10:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:61:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:10:61 INFO Boot') is None

def test_parse_log_line_none():
    with pytest.raises(ValueError):
        parse_log_line(None)

def test_parse_log_line_non_string():
    with pytest.raises(TypeError):
        parse_log_line(123)
    with pytest.raises(TypeError):
        parse_log_line(12.34)
    with pytest.raises(TypeError):
        parse_log_line([])