def estimate_downtime_cost(hours: float, cost_per_hour: float) -> str:
    """
    Estimate financial loss due to downtime.

    Args:
        hours (float): Number of downtime hours.
        cost_per_hour (float): Cost per hour of downtime.

    Returns:
        str: Total cost in a formatted string.
    """
    if hours < 0 or cost_per_hour < 0:
        return "Error: Hours and cost per hour must be non-negative."

    total_cost = hours * cost_per_hour
    return f"Downtime cost is estimated at ${total_cost:,.2f} (Hours: {hours}, Rate: ${cost_per_hour}/hr)"
