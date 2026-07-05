import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist
from simulation import estimate_power

def plot_conversion_rates(control_rate:float, 
                          treatment_rate:float):
    """Plots bar plot to visualize and compare the conversion rate of control and treatment population"""
    if control_rate<0 or control_rate>1:
        raise ValueError(f"Invalid value of control_rate={control_rate}, Expected value in the interval [{0},{1}].")
    if treatment_rate<0 or treatment_rate>1:
        raise ValueError(f"Invalid value of treatment_conversion_rate={treatment_rate}, Expected value in the interval [{0},{1}].")
    
    plt.bar(x=['Control Group', 'Treatment Group'], height=[control_rate, treatment_rate])

    plt.title("Conversion Rate Comparison")
    plt.ylabel("Conversion Rate")
    plt.show()

def plot_confidence_interval_visualizations(lower_bound:float, 
                                            estimate:float, 
                                            upper_bound:float, 
                                            standard_error:float):
    """Visualizes confidence interval using error plot and sampling distribution curve."""
    if not (lower_bound <= estimate and estimate <= upper_bound):
        raise ValueError(f"Expected relation between the values: lower_bound<=estimate<=upper_bound.")
    if standard_error<=0:
        raise ValueError(f"Invalid value of standard_error={standard_error}, Expected a positive value.")
    
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(6,6))

    fig.suptitle("Confidence Interval Visualizations")

    # Plot1: Error-bar plot

    lower_error = estimate-lower_bound
    upper_error = upper_bound-estimate

    ax1.errorbar(x=0, y=estimate, yerr=[[lower_error], [upper_error]], fmt='o')

    ax1.axhline(y=0, linestyle='--')
    ax1.set_xticks([0])
    ax1.set_xticklabels(['Lift'])
    ax1.set_ylabel("Difference in Conversion Rates")
    ax1.set_title("Estimate with Confidence Interval")

    # Plot2: Sampling Distribution

    x=np.linspace(start=-4.5*standard_error,
                  stop=4.5*standard_error,
                  num=1000)
    
    distribution = NormalDist(mu=estimate, sigma=standard_error)

    y = [distribution.pdf(val) for val in x]

    ax2.plot(x,y)

    ax2.axvline(lower_bound, linestyle=':', label='Lower bound')
    ax2.axvline(estimate, label='Estimate')
    ax2.axvline(upper_bound, linestyle='--', label='Upper bound')
    ax2.legend()

    ax2.set_title("Sampling Distribution")
    ax2.set_xlabel("Lift")
    ax2.set_ylabel("Density")

    plt.tight_layout()
    plt.show()

def plot_power_curve(control_rate:float, 
                     treatment_rate:float, 
                     num_simulations=10000):
    """Plots the power curve (curve of estimated power of the test against the sample size)."""
    if control_rate<0 or control_rate>1:
        raise ValueError(f"Invalid value of control_rate={control_rate}, Expected value in the interval [{0},{1}].")
    if treatment_rate<0 or treatment_rate>1:
        raise ValueError(f"Invalid value of treatment_conversion_rate={treatment_rate}, Expected value in the interval [{0},{1}].")
    if num_simulations<=0:
        raise ValueError(f"Invalid value of num_simulations={num_simulations}, Expected a positive value.")
    
    estimated_power_array = []
    sample_size_array = []
    
    for sample_size_per_group in range(500, 15500, 500):
        estimated_power_array.append(estimate_power(control_rate, treatment_rate, sample_size_per_group, num_simulations))
        sample_size_array.append(sample_size_per_group)
                
    plt.plot(sample_size_array, estimated_power_array)
    plt.xlabel('Sample Size')
    plt.ylabel('Estimated Power')
    plt.title('Power Curve')
    plt.show()        