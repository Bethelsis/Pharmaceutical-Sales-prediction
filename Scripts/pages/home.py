''' This is the home page'''

# Libraries
import streamlit as st

def write():
    with st.spinner("Loading Home ..."):
        st.title('Rossmann Pharmaceuticals')
        st.write(
            """
            Dirk Rossmann GmbH (usual: Rossmann) is one of the largest drug store chains in Europe with around 56,200 employees and more than 4000 stores across Europe.
                """
        )
        st.image('Scripts/pages/home.jpg', use_column_width=True)
        st.write("""
        
         This app is an end-to-end solution that allows the Rosemann pharmaceutical company to see sales forecasts for its stores six weeks in advance, as well as expected trends.
         """)
