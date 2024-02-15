
def govmnt_taxes(hand:int, reduced: bool) -> float:
    iva = 0.1
    if reduced:
        if hand == 1:
            ajd = 0.003
            return ajd + iva
        else:
            itp = 0.035
            return itp
    else:
        if hand == 1:
            ajd = 0.01
            return ajd + iva
        else:
            itp = 0.06
            return itp

def interest_simple(principal: float, time: int, rate):
    """
    Calculate compound interest.

    Args:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in percentage).
    time (int): The time the money is invested for (in years).

    Returns:
    float: The total amount after compound interest.
    """
    
    if rate > 1:
        rate = rate / 100
    amount = principal * (1 + rate_decimal)**time
    
    return amount