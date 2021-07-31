import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd


def write():

	
		st.markdown("<p style='padding:30px;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:26px;border-radius:10px;'>Predict Sale</p>", unsafe_allow_html=True)
    
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if st.button("Process"):
			if data_file is not None:
				file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
				st.write(file_details)

				df = pd.read_csv(data_file)
				st.dataframe(df)



