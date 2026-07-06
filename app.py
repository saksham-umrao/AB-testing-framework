import streamlit as st
from experiment import Experiment
import visualization
import math

st.title("📊 A/B Testing Dashboard")

st.write("Enter experiment parameters below:")

col1, col2 = st.columns([1,1])
with col1:
    control_conversions = st.number_input("Control Conversions", value=100)
    treatment_conversions = st.number_input("Treatment Conversions", value=120)
with col2:
    control_size = st.number_input("Control Size", value=1000)
    treatment_size = st.number_input("Treatment Size", value=1000)

st.space()

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    confidence_level = st.number_input("Confidence Level", min_value=0.01, max_value=0.99, value=0.95, step=0.01, format="%.2f")
with col2:
    minimum_detectable_effect = st.number_input("Minimum Detectable Effect", min_value=0.001, value=0.020, step=0.001, format="%.3f")
with col3:    
    alpha = st.number_input("Alpha", min_value=0.01, max_value=0.99, value=0.05, step=0.01, format="%.2f")
with col4:
    power = st.number_input("Power", min_value=0.01, max_value=0.99, value=0.80, step=0.01, format="%.2f")

exp = Experiment(treatment_conversions=treatment_conversions,
                 treatment_size=treatment_size,
                 control_conversions=control_conversions,
                 control_size=control_size)

if st.button("Run Experiment"):
    st.session_state.show_report = True
if st.session_state.get("show_report", False):
    st.subheader("Results")
    st.code(exp.print_report(confidence_level, minimum_detectable_effect, alpha, power), language=None)

st.subheader("Visualizations:")
st.write("Please select the plots that you want to see:")
conversion_rate_plot = st.checkbox("Conversion Rate Comparison")
confidence_interval_plot = st.checkbox("Confidence Interval Visualization")
power_curve_plot = st.checkbox("Power Curve")
if st.button("Generate Plots"):
    if conversion_rate_plot:
        fig1 = visualization.plot_conversion_rates(exp.control_conversion_rate(),
                                                exp.treatment_conversion_rate(),
                                                show=False)
        st.pyplot(fig1)

    if confidence_interval_plot:
        p_t = exp.treatment_conversion_rate()
        p_c = exp.control_conversion_rate()

        se = math.sqrt((p_t*(1-p_t)/exp.treatment_size) + (p_c*(1-p_c)/exp.control_size))
        ci = exp.confidence_interval(confidence_level)
        fig2 = visualization.plot_confidence_interval_visualizations(lower_bound=ci[0],
                                                                    estimate=exp.absolute_lift(),
                                                                    upper_bound=ci[1],
                                                                    standard_error=se,
                                                                    show=False)
        st.pyplot(fig2)

    if power_curve_plot:
        fig3 = visualization.plot_power_curve(exp.control_conversion_rate(),
                                            exp.treatment_conversion_rate(),
                                            num_simulations=10000,
                                            show=False)
        st.pyplot(fig3)