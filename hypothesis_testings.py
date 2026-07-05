import math
from statistics import NormalDist

def two_proportion_z_test(treatment_conversions:int,
                          treatment_size:int,
                          control_conversions:int,
                          control_size:int,
                          confidence_level=0.95)->dict:
    """Performs a two-proportion z-test and returns the z-statistic, critical value, p-value, and decision of the test."""
    if treatment_size<=0:
        raise ValueError(f"Invalid value of treatment_size={treatment_size}, Expected a positive sized sample")
    if control_size<=0:
        raise ValueError(f"Invalid value of control_size={control_size}, Expected a positive sized sample")
    if treatment_conversions<0 or treatment_conversions>treatment_size:
        raise ValueError(f"Invalid value of treatment_conversions={treatment_conversions}, Expected a value between {0} and {treatment_size}")
    if control_conversions<0 or control_conversions>control_size:
        raise ValueError(f"Invalid value of control_conversions={control_conversions}, Expected a value between {0} and {control_size}")
    if confidence_level<=0 or confidence_level>=1:
        raise ValueError(f"Invalid value of confidence_level={confidence_level}, Expected a value in the interval ({0},{1})")
    
    p_t_estimate = treatment_conversions/treatment_size
    p_c_estimate = control_conversions/control_size

    pooled_proportion = (treatment_conversions+control_conversions)/(treatment_size+control_size)
    standard_error = math.sqrt(pooled_proportion*(1-pooled_proportion)*(1/treatment_size + 1/control_size))

    z_statistic = (p_t_estimate-p_c_estimate)/standard_error

    alpha = 1-confidence_level
    z_critical = NormalDist().inv_cdf(1-alpha/2)
    p_value = 2*(1-NormalDist().cdf(abs(z_statistic)))

    return {'z_statistic': z_statistic,
            'z_critical': z_critical,
            'p_value': p_value,
            'reject_null': abs(z_statistic)>abs(z_critical)}