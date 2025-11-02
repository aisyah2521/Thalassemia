import streamlit as st
import pandas as pd
st.set_page_config(
  page_title="Objective 1"
)
st.header("Objective 1", divider="gray")

import streamlit as st
import pandas as pd

# The raw GitHub URL for your CSV file
DATA_URL = 'https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv'

## 🚀 Load Data Function
@st.cache_data
def load_data(url):
    """
    Loads data from the specified URL and caches it for performance.
    """
    try:
        # Read the CSV directly from the URL
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

---

## 📊 Streamlit Application
st.title('Thalassemia QoL Data Viewer')
st.markdown(f"Loading data from: **{DATA_URL}**")

# Load the data
df = load_data(DATA_URL)

if not df.empty:
    st.subheader('Raw Data')
    # Display the data as an interactive table
    st.dataframe(df)

    # Optional: Display some basic info
    st.subheader('Data Information')
    st.write(f"Number of rows: **{len(df)}**")
    st.write(f"Number of columns: **{len(df.columns)}**")

else:
    st.warning("The DataFrame is empty. Please check the URL and file content.")
