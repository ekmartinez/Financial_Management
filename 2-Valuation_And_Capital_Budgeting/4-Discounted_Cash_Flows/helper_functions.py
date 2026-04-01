def present_value_amount(amount, rate, periods):
    """Returns the present value of $1"""
    pv_fact = 1 / (1 + rate)**(periods)
    
    return pv_fact * amount

def annuityPVFactor(payment, rate, periods):
    """Return the Present Value Factor of an Ordinary Annuity"""
    
    annPVFactor = (1 - (1/(1 + rate)**periods)) / rate
    
    return annPVFactor * payment

def future_value_simple(amount, rate, periods):
    """Returns future value with simple interest"""
    
    return f'{amount + (amount * rate) * periods:,.2f}'

def future_value_compounded(amount, rate, periods):
    """Returns future value with compounding interest"""
    
    return f'{amount * (1 + rate) ** periods:,.2f}'

def perpetuity(pmt, rate):
    """Return the value of a constant perpetuity"""
    
    return pmt / rate

def continuousFV(present_value, rate, years):
    """Returns the Future Value using continuous compounding"""
    
    e = 2.718
    contFV = present_value * (e ** (rate * years))
    
    return contFV

def higher_pv(x, y):
    """Evaluates which investment is higher"""
    
    if x > y:
        return "X"
    else:
        return "Y"
        
def effectiveRate(APR, Compounding):
    return (1 + APR / Compounding) ** Compounding - 1