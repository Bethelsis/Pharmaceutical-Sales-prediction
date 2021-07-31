import streamlit as st
import awesome_streamlit as ast
import home
import data 
import predicted
import insights
import predict

# create the pages
PAGES = {
    "Home": home,
    "Data":data,
    "Insights": insights,
    "Predicted sales ": predicted,
    "predict": predict
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