'''This writes the insights gained from the EDA.'''

import streamlit as st


def write():
    with st.spinner("Loading Data ..."):
       
        st.markdown("<p style='padding:30px;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:26px;border-radius:10px;'>Insights from the data</p>", unsafe_allow_html=True)
    
        st.markdown("""
        The data has a lot of useful features that can provide insights into the stores sales. Based on the exploratory data analysis conducted, the following conclusions can be made: 
        * The number of customers is directly related to the volume of sales.
        
        """)
      
