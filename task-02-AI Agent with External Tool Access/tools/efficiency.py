def calculate_efficiency(units_produced: int, target_units: int) -> str:
    """
    Calculate production efficiency as (produced ÷ target) × 100.

    Args:
        units_produced (int): Number of units actually produced.
        target_units (int): Planned or target units.

    Returns:
        str: Efficiency percentage in a formatted string.
    """
    if target_units <= 0:
        return "Error: Target units must be greater than zero."

    efficiency = (units_produced / target_units) * 100
    return f"Efficiency is {efficiency:.2f}% (Produced: {units_produced}, Target: {target_units})"
