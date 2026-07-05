def conversion_rate(conversions:int, 
                    visitors:int)->float:
    """Returns the coverion rate of a group."""
    return conversions/visitors

def absolute_lift(treatment_rate:float, 
                  control_rate:float)->float:
    """Returns the absolute lift given the conversion rate of treatment and control group."""
    return treatment_rate-control_rate

def relative_lift(treatment_rate:float, 
                  control_rate:float)->float:
    """Returns the relative lift given the conversion rate of treatment and control group."""
    return (treatment_rate-control_rate)/control_rate