
def govmnt_taxes(hand:int, reduced: bool) -> float:
    iva = 0.1
    if reduced:
        ajd = 0.003
        if hand == 1:
            return ajd + iva
        else:
            itp = 0.035
            return ajd + itp
    else:
        ajd = 0.012
        if hand == 1:
            return ajd + iva
        else:
            itp = 0.06
            return ajd + itp

def get_amortization(principal: float, years: int, apr: float):
    """
    Calculate compound interest.

    Args:
    principal (float): The initial amount of money. 240000 loan amount
    apr (float): The annual percentage rate (in percentage). 0.05 loan interest rate
    term (int): The time the money is invested for (in years). 30 * 12 loan term in months

    Returns:
    float: The total amount after compound interest.
    """

    monthly_rate = apr / 12
    term = years * 12 
    payment = (monthly_rate * principal) / (1-(1+monthly_rate)**(-term))
    
    return payment