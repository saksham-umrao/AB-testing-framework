import math
from statistics import NormalDist

def confidence_interval_difference_in_proportions(treatment_conversions:int,
                                                  treatment_size:int,
                                                  control_conversions:int,
                                                  control_size:int,
                                                  confidence_level=0.95)->list[float, float]:
    """Contructs and returns the confidence interval for the difference in proportions based on the given confidence level"""
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

    standard_error = math.sqrt((p_t_estimate*(1-p_t_estimate)/treatment_size) + (p_c_estimate*(1-p_c_estimate)/control_size))

    alpha = 1-confidence_level
    z_critical = NormalDist().inv_cdf(1-alpha/2)

    lower_bound = (p_t_estimate-p_c_estimate)-z_critical*standard_error
    upper_bound = (p_t_estimate-p_c_estimate)+z_critical*standard_error
    
    return [lower_bound, upper_bound]