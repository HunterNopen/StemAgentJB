import pytest
from source import parse_log_line

def test_malformed_log_lines():
    assert parse_log_line('malformed') is None
    assert parse_log_line('') is None
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

def test_large_log_line():
    long_message = ' '.join(['message'] * 1000)
    log_line = f'2024-01-05 12:10:05 INFO {long_message}'
    result = parse_log_line(log_line)
    assert result['datetime'] == '2024-01-05 12:10:05'
    assert result['level'] == 'INFO'
    assert result['message'] == long_message

def test_edge_cases():
    assert parse_log_line('2024-01-05 12:10:05,123 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05,123', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05 INFO Boot complete') == {'datetime': '2024-01-05 12:10:05', 'level': 'INFO', 'message': 'Boot complete'}
    assert parse_log_line('2024-01-05 12:10:05,999 WARNING Low disk space') == {'datetime': '2024-01-05 12:10:05,999', 'level': 'WARNING', 'message': 'Low disk space'}