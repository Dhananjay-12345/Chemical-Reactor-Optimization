import streamlit as st

def show_reactor_info(reactor_type):

    st.subheader("ℹ️ Reactor Information")

    if reactor_type == "CSTR":

        st.info("""
        **CSTR (Continuous Stirred Tank Reactor)**

        ✔ Perfect Mixing

        ✔ Uniform Concentration

        ✔ Easy Temperature Control

        ✔ Lower Conversion than PFR

        ✔ Widely used in liquid-phase reactions
        """)

    elif reactor_type == "PFR":

        st.success("""
        **PFR (Plug Flow Reactor)**

        ✔ No Back Mixing

        ✔ Higher Conversion

        ✔ Better Volume Efficiency

        ✔ Smaller Reactor Size for Same Conversion

        ✔ Common in tubular industrial reactors
        """)

    else:

        col1, col2 = st.columns(2)

        with col1:

            st.info("""
            **CSTR**

            ✔ Perfect Mixing

            ✔ Uniform Concentration

            ✔ Easy Temperature Control

            ✔ Lower Conversion
            """)

        with col2:

            st.success("""
            **PFR**

            ✔ No Back Mixing

            ✔ Higher Conversion

            ✔ Better Volume Efficiency

            ✔ Smaller Volume Requirement
            """)