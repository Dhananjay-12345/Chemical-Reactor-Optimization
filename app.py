import streamlit as st
import matplotlib.pyplot as plt
from reaction import reaction
from reactor import CSTR_REACTOR
from reactor import PFR_REACTOR
from economics import *
from graphs import *
from reactor_info import show_reactor_info

def reactor_recommendation(X_cstr, X_pfr):

    if X_pfr > X_cstr:

        recommendation = "PFR"

        reason = f"""
        ✓ Higher Conversion ({X_pfr:.3f} vs {X_cstr:.3f})

        ✓ Better Volume Utilization

        ✓ Suitable for maximizing conversion
        """

    elif X_cstr > X_pfr:

        recommendation = "CSTR"

        reason = f"""
        ✓ Higher Conversion ({X_cstr:.3f} vs {X_pfr:.3f})

        ✓ Better performance under current conditions
        """

    else:

        recommendation = "Either"

        reason = "Both reactors provide nearly identical conversion."

    return recommendation, reason

st.set_page_config(
    page_title="Chemical Reactor Design Suite",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚛️ Chemical Reactor Design & Optimization Suite")

st.markdown(
    """
    Design • Analyze • Optimize • Compare Chemical Reactors
    """
)


st.sidebar.title("⚙️ Simulation")

simulation_type = st.sidebar.selectbox(
"Simulation Type",
[
    "Single Temperature",
    "Temperature Comparison",
    "Volume Comparison",
    "Design Reactor"
]
)
st.sidebar.header("Reaction Parameters")

if simulation_type == "Single Temperature":

    
    frequency_factor = st.sidebar.number_input("Frequency Factor (A)", min_value = 0.0, value=1e7)

    activation_energy = st.sidebar.number_input("Activation Energy (J/mol)", value=60000.0)

    temperature = st.sidebar.number_input("Temperature (K)",min_value = 100.0 , max_value = 2000.0, value=380.0)

    order = st.sidebar.number_input("Reaction Order",min_value=0.0 , value=1.0)

    st.sidebar.header("Reactor Parameters")

    reactor_type = st.selectbox("select reactor" , ["CSTR","PFR","BOTH"])

    volume = st.sidebar.number_input("Volume (m³) ",min_value = 0.0001, value=100.0)

    flowrate = st.sidebar.number_input("Flowrate (m³/s)",min_value=0.001 , value=10.0)

    concentration = st.sidebar.number_input("Initial Concentration (mole/m³)", min_value = 0.001 , value=3.0)

    st.sidebar.header("Economic Parameters")

    reactant_price = st.sidebar.number_input("Feed Cost (₹/mol)" , min_value = 0.0)
    product_price = st.sidebar.number_input("Product Price (₹/mol)" , min_value = 0.0)
    operating_hours = st.sidebar.number_input("Operating Hours(hr)" , min_value = 0.0)
    st.sidebar.header("Capital Cost Analysis")

    reactor_cost_per_m3 = st.sidebar.number_input("Reactor Cost (₹/m³)",min_value=0.0,value=100000.0)
    
elif simulation_type == "Temperature Comparison":
    frequency_factor = st.sidebar.number_input("Frequency Factor (A)", min_value = 0.0, value=1e7)

    activation_energy = st.sidebar.number_input("Activation Energy (J/mol)", value=60000.0)

    start_temp = st.sidebar.number_input("Start Temperature",value=300.0)

    end_temp = st.sidebar.number_input("End Temperature",value=500.0)

    step = st.sidebar.number_input("Temperature Step",min_value=1.0,value=10.0)

    order = st.sidebar.number_input("Reaction Order",min_value=0.0 , value=1.0)

    st.sidebar.header("Reactor Parameters")

    reactor_type = st.selectbox("select reactor" , ["CSTR","PFR","BOTH"])

    volume = st.sidebar.number_input("Volume (m³) ",min_value = 0.0001, value=100.0)

    flowrate = st.sidebar.number_input("Flowrate (m³/s)",min_value=0.001 , value=10.0)

    concentration = st.sidebar.number_input("Initial Concentration (mole/m³)", min_value = 0.001 , value=3.0)
elif simulation_type == "Volume Comparison":
    frequency_factor = st.sidebar.number_input("Frequency Factor (A)", min_value = 0.0, value=1e7)

    activation_energy = st.sidebar.number_input("Activation Energy (J/mol)", value=60000.0)

    temperature = st.sidebar.number_input("Temperature (K)",min_value = 100.0 , max_value = 2000.0, value=380.0)

    order = st.sidebar.number_input("Reaction Order",min_value=0.0 , value=1.0)

    st.sidebar.header("Reactor Parameters")

    reactor_type = st.selectbox("select reactor" , ["CSTR","PFR","BOTH"])

    start_volume = st.sidebar.number_input("Start Volume (m³)",min_value=0.01,value=0.01)

    end_volume = st.sidebar.number_input("End Volume (m³)",min_value=0.02,value=500.0)

    step_volume = st.sidebar.number_input("Volume Step",min_value=0.01,value=10.0)

    flowrate = st.sidebar.number_input("Flowrate (m³/s)",min_value=0.001 , value=10.0)

    concentration = st.sidebar.number_input("Initial Concentration (mole/m³)", min_value = 0.001 , value=3.0)


elif simulation_type == "Design Reactor":
    designx = st.selectbox("find :",["Required Temperature","Required Volume","Required Flowrate"])
    frequency_factor = st.sidebar.number_input("Frequency Factor (A)", min_value = 0.0, value=1e7)

    activation_energy = st.sidebar.number_input("Activation Energy (J/mol)", value=60000.0)
    if designx != "Required Temperature":
        temperature = st.sidebar.number_input("Temperature (K)",min_value = 100.0 , max_value = 2000.0, value=380.0)


    conversion = st.sidebar.number_input("CONVERSION",min_value = 0.01 , max_value = 1.000, value=0.01)

    order = st.sidebar.number_input("Reaction Order",min_value=0.0 , value=1.0)

    st.sidebar.header("Reactor Parameters")

    reactor_type = st.selectbox("select reactor" , ["CSTR","PFR","BOTH"])
    if designx != "Required Volume":
        volume = st.sidebar.number_input("Volume(m³)",min_value = 0.0001, value=100.0)
    if designx != "Required Flowrate":
        flowrate = st.sidebar.number_input("Flowrate (m³/s)",min_value=0.001 , value=10.0)

    concentration = st.sidebar.number_input("Initial Concentration (mole/m³)", min_value = 0.001 , value=3.0)


if st.button("Run Simulation"):
    st.success("Simulation Started")

    react1 = reaction(frequency_factor, activation_energy)
 

    if simulation_type == "Single Temperature":
        cstr = CSTR_REACTOR(
        volume,
        flowrate,
        concentration,
        order
        )

        pfr = PFR_REACTOR(
        volume,
        flowrate,
        concentration,
        order
        )
        
        k = react1.rateconstant(temperature)
      
        X_cstr = cstr.conversion(k)
        X_pfr = pfr.conversion(k)
        recommendation, reason = reactor_recommendation(
        X_cstr,
        X_pfr
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🌡 Temperature", f"{temperature:.2f} K")

        with col2:
            st.metric("⚡ Rate Constant", f"{k:.5e}")

        with col3:
            if reactor_type == "CSTR":
                st.metric("⚗ Conversion", f"{X_cstr*100:.2f}%")
            elif reactor_type == "PFR":
                st.metric("⚗ Conversion", f"{X_pfr*100:.2f}%")
            else:
                st.metric(
                    "⚗ Best Conversion",
                    f"{max(X_cstr, X_pfr)*100:.2f}%"
                )

        with col4:
            st.metric("🛢 Volume", f"{volume:.2f} m³")

            if reactor_type == "BOTH" :
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("CSTR Conversion", f"{X_cstr:.6f}")

                with col2:
                    st.metric("PFR Conversion", f"{X_pfr:6f}")
            elif reactor_type=="CSTR":
                st.metric("CSTR Conversion", f"{X_cstr:.6f}")
            else:
                st.metric("PFR Conversion", f"{X_pfr:.6f}")

        st.divider()

        col1, col2 = st.columns([1,2])

        with col1:

            st.metric(
            "Recommended Reactor",
            recommendation
            )

        with col2:

            st.info(reason)
       
        with st.expander("💰 Economic Analysis"):
            if reactor_type != "BOTH":
                if reactor_type == "CSTR":

                    conversion = X_cstr
                else:
                    conversion = X_pfr

                (revenue_per_sec,profit_per_sec,annual_profit,capital_cost,payback_period) = single_reactor_economics(
                flowrate,concentration,conversion,product_price,reactant_price,operating_hours,volume,reactor_cost_per_m3)

                col1, col2, col3, col4, col5 = st.columns(5)

                with col1:
                    st.metric(
                    "Revenue (₹/s)",
                    f"{revenue_per_sec:.2f}"
                    )

                with col2:
                    st.metric(
                    "Revenue (₹/hr)",
                    f"{revenue_per_sec*3600:.2f}"
                    )

                with col3:
                    st.metric(
                    "Profit (₹/s)",
                    f"{profit_per_sec:.2f}"
                    )

                with col4:
                    st.metric(
                    "Profit (₹/hr)",
                    f"{profit_per_sec*3600:.2f}"
                    )

                with col5:
                    st.metric(
                    "Annual Profit (₹/year)",
                    f"{annual_profit:,.0f}"
                    )
                              
                col6, col7 = st.columns(2)

                with col6:
                    st.metric(
                    "Capital Cost",
                    f"₹{capital_cost:,.0f}"
                    )

                with col7:

                    if payback_period is not None:
                        st.metric(
                        "Payback Period",
                        f"{payback_period:.2f} years"
                        )
                    else:
                        st.metric(
                        "Payback Period",
                        "Not Profitable"
                        )
                
            else:
                profit_cstr, profit_pfr = compare_reactors_economics(flowrate,concentration,X_cstr,X_pfr,product_price,reactant_price)
                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                    "CSTR Profit (₹/s)",
                    f"{profit_cstr:.2f}"
                    )

                with col2:
                    st.metric(
                    "PFR Profit (₹/s)",
                    f"{profit_pfr:.2f}"
                    )
                if profit_pfr > profit_cstr:

                    st.success(
                    f"""
                    🏆 Economic Recommendation

                    PFR

                    Additional Profit:
                    ₹{profit_pfr-profit_cstr:.2f}/s
                    """
                    )

                else:

                    st.success(
                    f"""
                    🏆 Economic Recommendation

                    CSTR

                    Additional Profit:
                    ₹{profit_cstr-profit_pfr:.2f}/s
                    """
                    )
        if reactor_type != "BOTH":
            report = f"""
            CHEMICAL REACTOR SIMULATOR REPORT

            ----------------------------------------

            Reaction Parameters

            Frequency Factor : {frequency_factor:.2e}

            Activation Energy : {activation_energy:.2f} J/mol

            Reaction Order : {order}

            ----------------------------------------

            Reactor Parameters

            Temperature : {temperature:.2f} K

            Volume : {volume:.2f} m³

            Flowrate : {flowrate:.2f}

            Initial Concentration : {concentration:.2f}

            ----------------------------------------

            Results

            CSTR Conversion : {X_cstr:.4f}

            PFR Conversion : {X_pfr:.4f}

            Rate Constant : {k:.5e}

            Recommended Reactor : {recommendation}

            Reason : {reason}

            ----------------------------------------

            Economic Analysis

            Revenue per second : ₹{revenue_per_sec:.2f}

            Profit per second : ₹{profit_per_sec:.2f}

            Annual Profit : ₹{annual_profit:,.0f}

            ----------------------------------------
            Generated by Chemical Reactor Simulator
            """
            st.download_button(
            label="📄 Download Report",
            data=report,
            file_name=f"reactor_report_{reactor_type}.txt",
            mime="text/plain"
        )

        show_reactor_info(reactor_type)

    elif simulation_type =="Temperature Comparison":
      
        cstr = CSTR_REACTOR(
        volume,
        flowrate,
        concentration,
        order
        )

        pfr = PFR_REACTOR(
        volume,
        flowrate,
        concentration,
        order
        )
        temperature=[]
        C_conversion = []
        P_conversion = []
        temp = start_temp

        while (temp<=end_temp):
            k=react1.rateconstant(temp)

            X_cstr = cstr.conversion(k)
            X_pfr = pfr.conversion(k)

            temperature.append(temp)
            C_conversion.append(X_cstr)
            P_conversion.append(X_pfr)

            temp+=step

        fig = temperature_graph(temperature,C_conversion,P_conversion,reactor_type)

        st.plotly_chart(
        fig,
        use_container_width=True
        )

        st.subheader("Recommendation")

        if reactor_type == "CSTR":

            max_conv = max(C_conversion)

            best_temp = temperature[
            C_conversion.index(max_conv)
            ]

            st.success(
            f"""
        Best Temperature for CSTR

        Maximum Conversion = {max_conv:.4f}

        Temperature = {best_temp:.2f} K
        """
        )

        elif reactor_type == "PFR":

            max_conv = max(P_conversion)

            best_temp = temperature[
            P_conversion.index(max_conv)
            ]

            st.success(
            f"""
        Best Temperature for PFR

        Maximum Conversion = {max_conv:.4f}

        Temperature = {best_temp:.2f} K
        """
        )

        else:

            max_cstr = max(C_conversion)
            max_pfr = max(P_conversion)

            best_temp_cstr = temperature[
            C_conversion.index(max_cstr)
            ]

            best_temp_pfr = temperature[
            P_conversion.index(max_pfr)
            ]

            if max_pfr > max_cstr:

                st.success(
                f"""
                Recommended Reactor : PFR

                Best Conversion = {max_pfr:.4f}

                Best Temperature = {best_temp_pfr:.2f} K

                CSTR Best Conversion = {max_cstr:.4f}

                Reason:
                Higher maximum conversion
                """
                )

            else:

                st.success(
                f"""
                Recommended Reactor : CSTR

                Best Conversion = {max_cstr:.4f}

                Best Temperature = {best_temp_cstr:.2f} K

                PFR Best Conversion = {max_pfr:.4f}

                Reason:
                Higher maximum conversion
                """
                )

        show_reactor_info(reactor_type)

    elif simulation_type == "Volume Comparison":
        k = react1.rateconstant(temperature)
        volume_list = []
        C_conversion = []
        P_conversion = []
        vol = start_volume

        while vol <= end_volume:
            cstr = CSTR_REACTOR(
            vol,
            flowrate,
            concentration,
            order
            )
            X_cstr = cstr.conversion(k)
            C_conversion.append(X_cstr)
            pfr = PFR_REACTOR(
            vol,
            flowrate,
            concentration,
            order
            )

            X_pfr = pfr.conversion(k)

            P_conversion.append(X_pfr)
            volume_list.append(vol)
            vol += step_volume

       
        fig = temperature_graph(volume_list,C_conversion,P_conversion,reactor_type)

        st.plotly_chart(
        fig,
        use_container_width=True
        )

        st.subheader(" Recommendation")

        if reactor_type == "CSTR":

            max_conv = max(C_conversion)

            best_volume = volume_list[
            C_conversion.index(max_conv)
            ]

            st.success(
            f"""
        Best Volume for CSTR

        Maximum Conversion = {max_conv:.4f}

        Volume = {best_volume:.2f}
        """
        )

        elif reactor_type == "PFR":

            max_conv = max(P_conversion)

            best_volume = volume_list[
            P_conversion.index(max_conv)
            ]

            st.success(
            f"""
        Best Volume for PFR

        Maximum Conversion = {max_conv:.4f}

        Volume = {best_volume:.2f}
        """
        )

        else:

            max_cstr = max(C_conversion)
            max_pfr = max(P_conversion)

            best_vol_cstr = volume_list[
            C_conversion.index(max_cstr)
            ]

            best_vol_pfr = volume_list[
            P_conversion.index(max_pfr)
            ]

            if max_pfr > max_cstr:

                st.success(
                f"""
                Recommended Reactor : PFR

                Best Conversion = {max_pfr:.4f}

                Best Volume = {best_vol_pfr:.2f}

                CSTR Best Conversion = {max_cstr:.4f}

                Reason:
                Higher maximum conversion
                """
                )

            else:

                st.success(
                f"""
                Recommended Reactor : CSTR

                Best Conversion = {max_cstr:.4f}

                Best Volume = {best_vol_cstr:.2f}

                PFR Best Conversion = {max_pfr:.4f}

                Reason:
                Higher maximum conversion
                """
                )

        show_reactor_info(reactor_type)
        

    else:
        if designx == "Required Temperature":
            cstr = CSTR_REACTOR(
            volume,
            flowrate,
            concentration,
            order
            )

            pfr = PFR_REACTOR(
            volume,
            flowrate,
            concentration,
            order
            )

            if reactor_type == "CSTR":
                if conversion != 1:
                    req_temp = cstr.TFGC(conversion,activation_energy,frequency_factor)
                if conversion != 1:
                    st.metric("REQUIRED TEMPERATURE", f"{req_temp:.2f}")
                else:
                    st.metric("REQUIRED TEMPERATURE", f"{"very large"}")
            elif reactor_type == "PFR":
                if conversion != 1:
                    req_temp = pfr.TFGC(conversion,frequency_factor,activation_energy)
                if conversion != 1:
                    st.metric("REQUIRED TEMPERATURE", f"{req_temp:.2f}")
                else:
                    st.metric("REQUIRED TEMPERATURE", f"{"very large"}")
            elif reactor_type == "BOTH" :
                if conversion != 1:
                    req_temp1 = cstr.TFGC(conversion,activation_energy,frequency_factor)
                    req_temp2 = pfr.TFGC(conversion,frequency_factor,activation_energy)
                col1, col2 = st.columns(2)

                with col1:
                    if conversion != 1:
                        st.metric("REQUIRED TEMPERATURE", f"{req_temp1:.2f}")
                    else:
                        st.metric("REQUIRED TEMPERATURE", f"{"very large"}")
                with col2:
                    if conversion != 1:
                        st.metric("REQUIRED TEMPERATURE", f"{req_temp2:.2f}")
                    else:
                        st.metric("REQUIRED TEMPERATURE", f"{"very large"}")

                    
        elif designx == "Required Volume":
            k = react1.rateconstant(temperature)
            cstr = CSTR_REACTOR(
            50,
            flowrate,
            concentration,
            order
            )
            pfr = PFR_REACTOR(
            50,
            flowrate,
            concentration,
            order
            )
            if reactor_type == "CSTR":
                req_volume = cstr.VFGC(conversion,k)
                if conversion != 1:
                    st.metric("REQUIRED VOLUME",f"{req_volume:.2f}")
                else:
                    st.metric("REQUIRED VOLUME","very large")
            elif reactor_type == "PFR":
                req_volume = pfr.VFGC(conversion,k)
                if conversion != 1:
                    st.metric("REQUIRED VOLUME",f"{req_volume:.2f}")
                else:
                    st.metric("REQUIRED VOLUME","very large")
            elif reactor_type == "BOTH" :
                if conversion != 1:
                    req_volume1 = cstr.VFGC(conversion,k)
                    req_volume2 = pfr.VFGC(conversion,k)

                col1, col2 = st.columns(2)

                with col1:
                    if conversion != 1:
                        st.metric("REQUIRED VOLUME", f"{req_volume1:.2f}")
                    else :
                        st.metric("REQUIRED VOLUME", f"{"very large"}")
                with col2:
                    if conversion != 1:
                        st.metric("REQUIRED VOLUME", f"{req_volume2:.2f}")
                    else :
                        st.metric("REQUIRED VOLUME", f"{"very large"}")


        show_reactor_info(reactor_type)

        