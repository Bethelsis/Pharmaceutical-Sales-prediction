''' This script loads and displays the raw data to the webpage'''

# Libraries
import streamlit as st
import pandas as pd 



def write():
    with st.spinner("Loading Data ..."):
        st.title('Data description')
         
        st.write("""      The data contains historical sales data for 1,115 Rossmann stores. """)

        train = pd.read_csv('Scripts/pages/train.csv')
        store = pd.read_csv('Scripts/pages/store.csv')
        merged_train = pd.merge(left = train, right = store, how = 'inner', left_on = 'Store', right_on = 'Store')
        merged_train = merged_train.set_index('Store')
        st.write(merged_train.sample(20))
        
