def check_reorder(daily_demand: int, lead_time: int, safety_stock: int, current_stock: int) -> str:
    """
    Decide whether to reorder inventory based on demand, lead time, and safety stock.

    Args:
        daily_demand (int): Units consumed per day.
        lead_time (int): Number of days it takes for a new order to arrive.
        safety_stock (int): Buffer stock to prevent shortages.
        current_stock (int): Current inventory level.

    Returns:
        str: Recommendation string (Reorder needed / Stock sufficient).
    """
    if daily_demand < 0 or lead_time < 0 or safety_stock < 0 or current_stock < 0:
        return "Error: All inputs must be non-negative."

    reorder_point = (daily_demand * lead_time) + safety_stock

    if current_stock <= reorder_point:
        return f"Reorder needed. Current stock ({current_stock}) ≤ Reorder point ({reorder_point})."
    else:
        return f"Stock sufficient. Current stock ({current_stock}) > Reorder point ({reorder_point})."
