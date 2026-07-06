import metrics
import confidence_intervals
import hypothesis_testings
import power_analysis

class Experiment:
    """Represents an A/B test experiment and provides methods for computing conversion metrics, hypothesis tests, 
    confidence intervals, power analysis, and experiment reports."""
    def __init__(self,
                 treatment_conversions:int,
                 treatment_size:int,
                 control_conversions:int,
                 control_size:int):
        self.treatment_conversions = treatment_conversions
        self.treatment_size = treatment_size
        self.control_conversions = control_conversions
        self.control_size = control_size

    def treatment_conversion_rate(self):
        return metrics.conversion_rate(self.treatment_conversions, self.treatment_size)
    
    def control_conversion_rate(self):
        return metrics.conversion_rate(self.control_conversions, self.control_size)
    
    def absolute_lift(self):
        return metrics.absolute_lift(self.treatment_conversion_rate(), self.control_conversion_rate())
    
    def relative_lift(self):
        return metrics.relative_lift(self.treatment_conversion_rate(), self.control_conversion_rate())
    
    def confidence_interval(self, confidence_level=0.95):
        return confidence_intervals.confidence_interval_difference_in_proportions(self.treatment_conversions,
                                                                                  self.treatment_size,
                                                                                  self.control_conversions,
                                                                                  self.control_size,
                                                                                  confidence_level)
    
    def two_proportion_z_test(self, confidence_level=0.95):
        return hypothesis_testings.two_proportion_z_test(self.treatment_conversions,
                                                         self.treatment_size,
                                                         self.control_conversions,
                                                         self.control_size,
                                                         confidence_level)
    
    def required_sample_size(self, minimum_detectable_effect=0.02, alpha=0.05, power=0.80):
        """Returns the required sample size per group for a desired power and minimum detectable effect."""
        return power_analysis.required_sample_size_proportions(self.control_conversion_rate(),
                                                               minimum_detectable_effect,
                                                               alpha,
                                                               power)
    
    def generate_report(self, confidence_level=0.95, minimum_detectable_effect=0.02, alpha=0.05, power=0.80):
        """Generates and returns a dictionary containing the complete A/B test analysis."""
        test_results = self.two_proportion_z_test(confidence_level)

        report = {'control_conversion_rate': self.control_conversion_rate(),
             'treatment_conversion_rate': self.treatment_conversion_rate(),
             'absolute_lift': self.absolute_lift(),
             'relative_lift': self.relative_lift(),
             'required_sample_size': self.required_sample_size(minimum_detectable_effect, alpha, power),
             'z_statistic': test_results['z_statistic'],
             'z_critical': test_results['z_critical'],
             'p_value': test_results['p_value'],
             'reject_null': test_results['reject_null'],
             'confidence_interval': self.confidence_interval(confidence_level)}
        
        return report
    
    def __str__(self):
        """Returns a formatted string summary of the A/B test results."""
        report = self.generate_report()

        return (
            f"A/B Test Summary\n"
            f"-----------------\n"
            f"Control Conversion Rate   : {report['control_conversion_rate']:.4f}\n"
            f"Treatment Conversion Rate : {report['treatment_conversion_rate']:.4f}\n"
            f"Absolute Lift             : {report['absolute_lift']:.4f}\n"
            f"Relative Lift             : {report['relative_lift']:.2%}\n"
            f"Required Sample Size      : {report['required_sample_size']}\n"
            f"Z Statistic               : {report['z_statistic']:.4f}\n"
            f"Z Critical                : {report['z_critical']:.4f}\n"
            f"P Value                   : {report['p_value']:.4f}\n"
            f"Reject Null               : {report['reject_null']}\n"
            f"Confidence Interval       : "
            f"({report['confidence_interval'][0]:.4f}, "
            f"{report['confidence_interval'][1]:.4f})"
        )
    
    def print_report(self, confidence_level=0.95, minimum_detectable_effect=0.02, alpha=0.05, power=0.80):
        """Returns a formatted A/B test summary using custom analysis parameters."""
        report = self.generate_report(confidence_level, minimum_detectable_effect, alpha, power)

        return (
            f"A/B Test Summary\n"
            f"-----------------\n"
            f"Control Conversion Rate   : {report['control_conversion_rate']:.4f}\n"
            f"Treatment Conversion Rate : {report['treatment_conversion_rate']:.4f}\n"
            f"Absolute Lift             : {report['absolute_lift']:.4f}\n"
            f"Relative Lift             : {report['relative_lift']:.2%}\n"
            f"Required Sample Size      : {report['required_sample_size']}\n"
            f"Z Statistic               : {report['z_statistic']:.4f}\n"
            f"Z Critical                : {report['z_critical']:.4f}\n"
            f"P Value                   : {report['p_value']:.4f}\n"
            f"Reject Null               : {report['reject_null']}\n"
            f"Confidence Interval       : "
            f"({report['confidence_interval'][0]:.4f}, "
            f"{report['confidence_interval'][1]:.4f})"
        )