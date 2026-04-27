import pytest
from source import parse_log_line

def test_malformed_log_lines():
    assert parse_log_line('') is None
    assert parse_log_line('malformed') is None
    assert parse_log_line('2024-01-05 12:10 INFO') is None
    assert parse_log_line('2024-01-05 25:10:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:61:00 INFO Boot') is None
    assert parse_log_line('2024-01-05 12:10:61 INFO Boot') is None

def test_invalid_input_types():
    with pytest.raises(ValueError):
        parse_log_line(None)
    with pytest.raises(TypeError):
        parse_log_line(123)
    with pytest.raises(TypeError):
        parse_log_line([])

def test_valid_log_lines():
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05,123 ERROR Disk space low') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'ERROR', 'message': 'Disk space low'}

def test_edge_cases():
    assert parse_log_line('2024-01-05 12:10:05,123 INFO') is None
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot complete'}

def test_invalid_time_format():
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05,123 INFO') is None

def test_time_boundary_cases():
    assert parse_log_line('2024-01-05 00:00:00 INFO Start') == {'datetime': '2024-01-05 00:00:00', 'level': 'INFO', 'message': 'Start'}
    assert parse_log_line('2024-01-05 23:59:59 INFO End') == {'datetime': '2024-01-05 23:59:59', 'level': 'INFO', 'message': 'End'}
    assert parse_log_line('2024-01-05 23:59:60 INFO Invalid') is None
    assert parse_log_line('2024-01-05 24:00:00 INFO Invalid') is None
    assert parse_log_line('2024-01-05 12:60:00 INFO Invalid') is None

def test_invalid_level():
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05 DEBUG Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'DEBUG', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05 WARNING Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'WARNING', 'message': 'Boot complete'}