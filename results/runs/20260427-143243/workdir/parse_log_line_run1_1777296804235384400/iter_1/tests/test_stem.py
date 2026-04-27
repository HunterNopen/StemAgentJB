import pytest
from source import parse_log_line

def test_malformed_log_lines():
    assert parse_log_line('') is None
    assert parse_log_line('malformed') is None
    assert parse_log_line('2024-01-05 12:10 INFO') is None
    assert parse_log_line('2024-01-05 25:10:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:61:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:10:61 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:10:05,123 INFO') is None

def test_invalid_input_types():
    with pytest.raises(ValueError):
        parse_log_line(None)
    with pytest.raises(TypeError):
        parse_log_line(123)
    with pytest.raises(TypeError):
        parse_log_line([])

def test_edge_cases():
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05,999 ERROR Critical failure') == {'datetime': '2024-01-05 12:10:05,999', 'level': 'ERROR', 'message': 'Critical failure'}
    assert parse_log_line('2024-01-05 12:10:05,000 WARNING Low disk space') == {'datetime': '2024-01-05 12:10:05,000', 'level': 'WARNING', 'message': 'Low disk space'}
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot complete with extra info') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot complete with extra info'}

def test_edge_case_hours():
    assert parse_log_line('2024-01-05 00:00:00 INFO Start of day') == {'datetime': '2024-01-05 00:00:00', 'level': 'INFO', 'message': 'Start of day'}
    assert parse_log_line('2024-01-05 23:59:59 INFO End of day') == {'datetime': '2024-01-05 23:59:59', 'level': 'INFO', 'message': 'End of day'}
    assert parse_log_line('2024-01-05 24:00:00 INFO Invalid hour') is None

def test_edge_case_minutes():
    assert parse_log_line('2024-01-05 12:00:00 INFO Valid minute') == {'datetime': '2024-01-05 12:00:00', 'level': 'INFO', 'message': 'Valid minute'}
    assert parse_log_line('2024-01-05 12:59:59 INFO Last minute') == {'datetime': '2024-01-05 12:59:59', 'level': 'INFO', 'message': 'Last minute'}
    assert parse_log_line('2024-01-05 12:60:00 INFO Invalid minute') is None

def test_edge_case_seconds():
    assert parse_log_line('2024-01-05 12:10:00 INFO Valid second') == {'datetime': '2024-01-05 12:10:00', 'level': 'INFO', 'message': 'Valid second'}
    assert parse_log_line('2024-01-05 12:10:59 INFO Last second') == {'datetime': '2024-01-05 12:10:59', 'level': 'INFO', 'message': 'Last second'}
    assert parse_log_line('2024-01-05 12:10:60 INFO Invalid second') is None