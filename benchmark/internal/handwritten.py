# ------------------- 1. Date Validation -------------------
def validate_date(date_str):
    """Return True if date_str is a valid date in YYYY-MM-DD format, else False."""
    if date_str is None:
        raise ValueError("date_str cannot be None")
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")
    
    parts = date_str.split('-')
    if len(parts) != 3:
        return False  # wrong format -> business rule violation, not exception
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return False  # non-numeric components -> invalid date
    
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


# ------------------- 2. Permission Check -------------------
def check_permission(user_role, action_required):
    """Return True if user_role is allowed to perform action_required, else False."""
    if user_role is None or action_required is None:
        raise ValueError("user_role and action_required cannot be None")
    if not isinstance(user_role, str) or not isinstance(action_required, str):
        raise TypeError("user_role and action_required must be strings")
    
    valid_roles = ['admin', 'manager', 'user', 'guest']
    if user_role not in valid_roles:
        return False  # unknown role is business disallowed, not error
    
    if user_role == 'admin':
        return True
    elif user_role == 'manager':
        return action_required in ('approve', 'view', 'edit')
    elif user_role == 'user':
        return action_required == 'view'
    elif user_role == 'guest':
        return action_required == 'view_public'
    return False


# ------------------- 3. Parsing Log Line -------------------
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
    
    # Validate date (business rule)
    if not validate_date(date_str):
        return None
    
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


# ------------------- 4. State Transition (Order) -------------------
def transition_order_status(current_status, action):
    """Return new status based on allowed transitions, or current status if action invalid."""
    if current_status is None or action is None:
        raise ValueError("current_status and action cannot be None")
    if not isinstance(current_status, str) or not isinstance(action, str):
        raise TypeError("current_status and action must be strings")
    
    valid_statuses = ['draft', 'submitted', 'approved', 'shipped', 'delivered', 'cancelled']
    if current_status not in valid_statuses:
        return current_status  # unknown status, no change
    
    # Business logic transitions (domain rules)
    if current_status == 'draft':
        if action == 'submit':
            return 'submitted'
        elif action == 'cancel':
            return 'cancelled'
        else:
            return current_status
    elif current_status == 'submitted':
        if action == 'approve':
            return 'approved'
        elif action == 'cancel':
            return 'cancelled'
        else:
            return current_status
    elif current_status == 'approved':
        if action == 'ship':
            return 'shipped'
        else:
            return current_status  # cannot cancel after approval
    elif current_status == 'shipped':
        if action == 'deliver':
            return 'delivered'
        else:
            return current_status
    elif current_status == 'delivered':
        return current_status  # no valid actions from delivered
    elif current_status == 'cancelled':
        return current_status  # immutable
    return current_status


# ------------------- 5. Numerical Edge Cases (Discount) -------------------
def apply_discount(price, discount_percent):
    """Return discounted price rounded to 2 decimals. Raises on invalid inputs."""
    if price is None or discount_percent is None:
        raise ValueError("price and discount_percent required")
    if not isinstance(price, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("price and discount_percent must be numeric")
    if price < 0:
        raise ValueError(f"price must be non-negative, got {price}")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"discount_percent must be in [0, 100], got {discount_percent}")
    
    final_price = price - price * (discount_percent / 100.0)
    return round(final_price, 2)


# ------------------- 6. Future Date Check (with business rule) -------------------
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


# ------------------- 7. Permission Check with Groups -------------------
def can_access_resource(user, resource):
    """Return True if user can access resource based on role, ownership, groups."""
    if user is None or resource is None:
        raise ValueError("user and resource cannot be None")
    if not isinstance(user, dict) or not isinstance(resource, dict):
        raise TypeError("user and resource must be dictionaries")
    
    # Required keys; raise if missing critical fields
    if 'active' not in user:
        raise KeyError("user dict must have 'active' key")
    if 'role' not in user:
        raise KeyError("user dict must have 'role' key")
    if 'id' not in user:
        raise KeyError("user dict must have 'id' key")
    if 'owner_id' not in resource:
        raise KeyError("resource dict must have 'owner_id' key")
    
    # Business logic (returns False for disallowed cases)
    if not user['active']:
        return False
    if resource.get('public', False):
        return True
    if user.get('role') == 'admin':
        return True
    if user.get('id') == resource.get('owner_id'):
        return True
    
    user_groups = user.get('groups', [])
    resource_groups = resource.get('allowed_groups', [])
    if not resource_groups:
        return False
    for ug in user_groups:
        if ug in resource_groups:
            return True
    if 'everyone' in resource_groups:
        return True
    return False


# ------------------- 8. Parsing User ID from String -------------------
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


# ------------------- 9. State Transition for User Account -------------------
def transition_account_state(current_state, action, failed_login_count=0):
    """Return new account state based on state machine rules."""
    if current_state is None or action is None:
        raise ValueError("current_state and action cannot be None")
    if not isinstance(current_state, str) or not isinstance(action, str):
        raise TypeError("current_state and action must be strings")
    if not isinstance(failed_login_count, int):
        raise TypeError("failed_login_count must be an integer")
    
    valid_states = ['active', 'suspended', 'locked', 'deleted']
    if current_state not in valid_states:
        return current_state  # unknown state, unchanged
    
    # Normalize failed_login_count (negative -> 0, but this is a business rule, not exception)
    if failed_login_count < 0:
        failed_login_count = 0
    
    # Automatic transition due to too many failures (business rule)
    if current_state == 'active' and failed_login_count >= 5:
        return 'locked'
    
    # Manual actions (business rules)
    if action == 'delete':
        if current_state != 'deleted':
            return 'deleted'
        return current_state
    elif action == 'suspend':
        if current_state == 'active':
            return 'suspended'
        return current_state
    elif action == 'unsuspend':
        if current_state == 'suspended':
            return 'active'
        return current_state
    elif action == 'unlock':
        if current_state == 'locked':
            return 'active'
        return current_state
    else:
        return current_state  # unknown action, no change