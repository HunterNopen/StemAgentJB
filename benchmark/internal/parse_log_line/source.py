def parse_log_line(line):
    """Return dict with keys 'datetime', 'level', 'message' or None if malformed log."""
    if line is None:
        raise ValueError("log line cannot be None")
    if not isinstance(line, str):
        raise TypeError("log line must be a string")
    if line == "":
        return None  # empty line is not an error but yields no data
    
    parts = line.split(' ')
    if len(parts) < 4:
        return None  # insufficient parts -> cannot parse
    
    date_str = parts[0]
    time_str = parts[1]
    level = parts[2]
    message = ' '.join(parts[3:])
    
    # Validate time format strictly
    time_parts = time_str.split(':')
    if len(time_parts) != 3:
        return None
    try:
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        sec_part = time_parts[2]
        if ',' in sec_part:
            second = int(sec_part.split(',')[0])
        else:
            second = int(sec_part)
    except ValueError:
        return None
    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
        return None
    
    return {
        'datetime': f"{date_str} {time_str}",
        'level': level,
        'message': message
    }