# apply_discount

## Signature
`apply_discount(price: float, discount_percent: float) -> float`

## Contract
Returns the final price after applying the given discount percentage,
rounded to 2 decimal places.

Raises `ValueError` for any invalid input: None, non-numeric type, negative price,
or discount_percent outside `[0, 100]`.

## Rules
- Final price = `price - price * (discount_percent / 100.0)`.
- Result is rounded to 2 decimal places via `round(..., 2)`.
- A discount of 0 returns the original price (rounded).
- A discount of 100 returns 0.0.

## Important: rounding
Computation: `final = price - price * (discount_percent / 100.0)`, then `round(final, 2)`.
Be careful with banker's rounding edge cases. Compute expected values precisely; do not approximate.
- `apply_discount(1.99, 50)` → `0.995` rounds to `0.99` (not 1.00, banker's rounding)
- `apply_discount(100.555, 10)` → `90.4995` rounds to `90.5`

## Edge cases
- `apply_discount(100, 25)` → 75.0
- `apply_discount(99.99, 10)` → 89.99
- `apply_discount(0, 50)` → 0.0
- `apply_discount(100, 0)` → 100.0
- `apply_discount(100, 100)` → 0.0
- `apply_discount(100, 101)` raises `ValueError`
- `apply_discount(-1, 10)` raises `ValueError`
- `apply_discount(None, 10)` raises `ValueError`
- `apply_discount("100", 10)` raises `ValueError`