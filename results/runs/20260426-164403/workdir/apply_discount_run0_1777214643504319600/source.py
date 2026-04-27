def apply_discount(price, discount_percent):
    """Return discounted price rounded to 2 decimals. Raises on invalid inputs."""
    if not isinstance(price, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("price and discount_percent must be numeric")
    if price is None or discount_percent is None:
        raise TypeError("price and discount_percent must be numeric")
    if price < 0:
        raise ValueError(f"price must be non-negative, got {price}")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"discount_percent must be in [0, 100], got {discount_percent}")
    
    final_price = price - price * (discount_percent / 100.0)
    return round(final_price, 2)