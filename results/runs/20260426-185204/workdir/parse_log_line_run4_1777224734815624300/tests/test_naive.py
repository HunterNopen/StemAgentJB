import pytest
from source import parse_log_line

def test_parse_log_line_malformed():
    assert parse_log_line('malformed') is None
    assert parse_log_line('') is None
    assert parse_log_line('2024-01-05 12:10 INFO') is None
    assert parse_log_line('2024-01-05 25:10:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:61:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:10:61 INFO Boot') is None

def test_parse_log_line_invalid_type():
    with pytest.raises(ValueError):
        parse_log_line(None)
    with pytest.raises(TypeError):
        parse_log_line(123)
    with pytest.raises(TypeError):
        parse_log_line([])

def test_parse_log_line_edge_cases():
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot'}
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}