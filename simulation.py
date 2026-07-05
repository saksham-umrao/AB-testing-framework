import numpy as np
from experiment import Experiment

def simulate_ab_test(control_rate:float, 
                     treatment_rate:float, 
                     sample_size_per_group:int)->Experiment:
    """Simulates the control group and the treatment group and returns an Experiment object with the randomly simulated conversions."""
    if control_rate<0 or control_rate>1:
        raise ValueError(f"Invalid value of control_rate={control_rate}, Expected a value in the interval [{0},{1}].")
    if treatment_rate<0 or treatment_rate>1:
        raise ValueError(f"Invalid value of treatment_rate={treatment_rate}, Expected a value in the interval [{0},{1}].")
    if sample_size_per_group<=0:
        raise ValueError(f"Invalid value of sample_size_per_group={sample_size_per_group}, Expected a positive value.")
    control_conversions = np.random.binomial(sample_size_per_group, control_rate)
    treatment_conversions = np.random.binomial(sample_size_per_group, treatment_rate)
    
    return Experiment(treatment_conversions=treatment_conversions,
                            treatment_size=sample_size_per_group,
                            control_conversions=control_conversions,
                            control_size=sample_size_per_group)

def estimate_power(control_rate:float, 
                   treatment_rate:float,
                   sample_size_per_group:int,
                   num_simulations=10000)->float:
    """Estimates and returns the power of a two proportion z test using monte carlo simulation."""
    if control_rate<0 or control_rate>1:
        raise ValueError(f"Invalid value of control_rate={control_rate}, Expected a value in the interval [{0},{1}].")
    if treatment_rate<0 or treatment_rate>1:
        raise ValueError(f"Invalid value of treatment_rate={treatment_rate}, Expected a value in the interval [{0},{1}].")
    if sample_size_per_group<=0:
        raise ValueError(f"Invalid value of sample_size_per_group={sample_size_per_group}, Expected a positive value.")
    if num_simulations<=0:
        raise ValueError(f"Invalid value of num_simulations={num_simulations}, Expected a positive value.")
    count=0
    for _ in range(num_simulations):
        exp = simulate_ab_test(control_rate, treatment_rate, sample_size_per_group)
        if exp.two_proportion_z_test()['reject_null']:
            count+=1
    
    estimated_power = count/num_simulations

    return estimated_power