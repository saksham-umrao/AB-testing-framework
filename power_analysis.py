import math
from statistics import NormalDist

def required_sample_size_proportions(baseline_conversion_rate:float,
                                     minimum_detectable_effect:float,
                                     alpha=0.05,
                                     power=0.80)->int:
    """Performs power analysis and returns the required sample size per group for a two proportion z test to reach a certain power."""
    
    if baseline_conversion_rate<0 or baseline_conversion_rate>1:
        raise ValueError(f"Invalid value of baseline_conversion_rate={baseline_conversion_rate}, Expected a value in the interval [{0},{1}]")
    if minimum_detectable_effect<=0:
        raise ValueError(f"Invalid value of minimum_detectable_effect={minimum_detectable_effect}, Expected a positive value")
    if alpha<=0 or alpha>=1:
        raise ValueError(f"Invalid value of alpha={alpha}, Expected value in the interval ({0},{1})")
    if power<=0 or power>=1:
        raise ValueError(f"Invalid value of power={power}, Expected value in the interval ({0},{1})")
    if baseline_conversion_rate + minimum_detectable_effect > 1:
        raise ValueError("baseline_conversion_rate + minimum_detectable_effect must be <= 1")
    
    z_alpha_by_2 = NormalDist().inv_cdf(1-alpha/2)
    z_power = NormalDist().inv_cdf(power)

    p = baseline_conversion_rate
    delta = minimum_detectable_effect

    n = (((z_alpha_by_2 + z_power)/delta)**2)*((p+delta)*(1-p-delta) + p*(1-p))

    return math.ceil(n)