from experiment import Experiment
import visualization
import math

experiment = Experiment(
    treatment_conversions=120,
    treatment_size=1000,
    control_conversions=100,
    control_size=1000
)

print(experiment)

visualization.plot_conversion_rates(control_rate= experiment.control_conversion_rate(), 
                                    treatment_rate=experiment.treatment_conversion_rate())

p_t = experiment.treatment_conversion_rate()
p_c = experiment.control_conversion_rate()

se = math.sqrt((p_t*(1-p_t)/experiment.treatment_size) + (p_c*(1-p_c)/experiment.control_size))
ci = experiment.confidence_interval()

visualization.plot_confidence_interval_visualizations(lower_bound=ci[0],
                                                      estimate=experiment.absolute_lift(),
                                                      upper_bound=ci[1],
                                                      standard_error=se)

visualization.plot_power_curve(control_rate=experiment.control_conversion_rate(),
                               treatment_rate=experiment.treatment_conversion_rate(),
                               num_simulations=10000)
