def parse_user_id_from_string(input_str):
    """Extract integer user ID from various formats, or return None if not found."""
    if input_str is None:
        raise ValueError("input_str cannot be None")
    if not isinstance(input_str, str):
        raise TypeError("input_str must be a string")
    if input_str == "":
        return None
    
    # Pattern 1: "USER:12345"
    if input_str.startswith("USER:"):
        rest = input_str[5:]
        if rest.isdigit():
            return int(rest)
        return None
    
    # Pattern 2: "ID=67890"
    if input_str.startswith("ID="):
        rest = input_str[3:]
        if rest.isdigit():
            return int(rest)
        return None
    
    # Pattern 3: "user_abc123" - extract trailing digits
    if "_" in input_str:
        parts = input_str.split('_')
        last_part = parts[-1]
        if last_part.isdigit():
            return int(last_part)
    
    # Pattern 4: just digits
    if input_str.isdigit():
        return int(input_str)
    
    # Fallback: collect all digits
    digits = ''.join(ch for ch in input_str if ch.isdigit())
    if digits:
        return int(digits)
    return None