import streamlit as st
import awesome_streamlit as ast
import Scripts.home
import Scripts.data 
import Scripts.predicted
import Scripts.insights
import Scripts.predict

# create the pages
PAGES = {
    "Home": Scripts.home,
    "Data":Scripts.data,
    "Insights": Scripts.insights,
    "Predicted sales ":Scripts.predicted,
    "predict": Scripts.predict
}


# render the pages
def main():




    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
  
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()