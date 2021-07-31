'''This writes the insights gained from the EDA.'''

import streamlit as st


def write():
    with st.spinner("Loading Data ..."):
        st.title('INSIGHTS FROM THE DATA')
        st.markdown("""
        The data has a lot of useful features that can provide insights into the stores sales. Based on the exploratory data analysis conducted, the following conclusions can be made: 
        * The number of customers is directly related to the volume of sales.
        
        """)
      
