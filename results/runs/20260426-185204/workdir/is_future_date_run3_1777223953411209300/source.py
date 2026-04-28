def is_future_date(date_str, current_date_str):
    """Return True if date_str is strictly after current_date_str (both YYYY-MM-DD)."""
    if date_str is None or current_date_str is None:
        raise ValueError("date_str and current_date_str cannot be None")
    if not isinstance(date_str, str) or not isinstance(current_date_str, str):
        raise TypeError("date strings must be strings")
    
    # validate returns False for invalid dates (business rule)
    if not validate_date(date_str) or not validate_date(current_date_str):
        return False  # cannot compare invalid dates
    
    target_parts = date_str.split('-')
    current_parts = current_date_str.split('-')
    target_num = int(target_parts[0]) * 10000 + int(target_parts[1]) * 100 + int(target_parts[2])
    current_num = int(current_parts[0]) * 10000 + int(current_parts[1]) * 100 + int(current_parts[2])
    return target_num > current_num