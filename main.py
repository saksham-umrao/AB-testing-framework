# import metrics
# import hypothesis_testings
# import confidence_intervals
# import power_analysis

# rate = metrics.conversion_rate(100,1000)

# result_hypo_test = hypothesis_testings.two_proportion_z_test(120,1000,100,1000)
# result_ci = confidence_intervals.confidence_interval_difference_in_proportions(120,1000,100,1000)

# reuslt_sample_size = power_analysis.required_sample_size_proportions(baseline_conversion_rate=0.10,
#                                                       minimum_detectable_effect=0.02)

# print(rate)
# print(result_hypo_test)
# print(result_ci)
# print(reuslt_sample_size)

#-------------------------------------------------------------------------------------------------------------

# from experiment import Experiment

# experiment = Experiment(
#     treatment_conversions=120,
#     treatment_size=1000,
#     control_conversions=100,
#     control_size=1000
# )

# print(experiment.treatment_conversion_rate())
# print(experiment.control_conversion_rate())
# print(experiment.absolute_lift())
# print(experiment.relative_lift())

# print(experiment.two_proportion_z_test(0.95))
# print(experiment.confidence_interval(0.95))

# print(experiment.required_sample_size(
#     minimum_detectable_effect=0.02, alpha=0.05, power=0.80
# ))

#------------------------------------------------------------------------------------------------------

# from experiment import Experiment
# import visualization
# import math

# experiment = Experiment(
#     treatment_conversions=120,
#     treatment_size=1000,
#     control_conversions=100,
#     control_size=1000
# )

# print(experiment.generate_report())

# print("*"*100)

# print(experiment)

# #visualization.plot_conversion_rates(experiment.control_conversion_rate(), experiment.treatment_conversion_rate())

# p_t = experiment.treatment_conversion_rate()
# p_c = experiment.control_conversion_rate()

# se = math.sqrt((p_t*(1-p_t)/experiment.treatment_size) + (p_c*(1-p_c)/experiment.control_size))

# visualization.plot_confidence_interval_visualizations(experiment.confidence_interval()[0],
#                                                       experiment.absolute_lift(), 
#                                                       experiment.confidence_interval()[1],
#                                                       standard_error=se)

#--------------------------------------------------------------------------------------------------------------------------------

# from simulation import simulate_ab_test

# experiment = simulate_ab_test(
#     control_rate=0.10,
#     treatment_rate=0.12,
#     sample_size_per_group=1000
# )

# print(experiment)

#----------------------------------------------------------------------------------------------------------------------------------

# # testing estimate_power function
# from simulation import estimate_power

# power = estimate_power(
#     control_rate=0.10,
#     treatment_rate=0.12,
#     sample_size_per_group=3839,
#     num_simulations=10000
# )

# print(power)

#--------------------------------------------------------------------------------------------------------------------------

# # testing the plot_power_curve function

# from visualization import plot_power_curve

# plot_power_curve(
#     control_rate=0.10,
#     treatment_rate=0.12
# )

#------------------------------------------------------------------------------------------------------------------------------

# final main.py

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