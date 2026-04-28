def validate_date(date_str):
    """Return True if date_str is a valid date in YYYY-MM-DD format, else False."""
    if date_str is None:
        raise ValueError("date_str cannot be None")
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")
    
    parts = date_str.split('-')
    if len(parts) != 3:
        return False
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return False
    
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_days[1] = 29
    if day < 1 or day > month_days[month - 1]:
        return False
    
    return True