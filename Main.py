import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(
  page_title="Objective 1"
)
st.header("Objective 1", divider="gray")


# The raw GitHub URL for the CSV file
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv"

"""
  **Scientific Visualization** is a multidisciplinary field that focuses on transforming complex
scientific data into visual forms that are easier to understand, interpret, and communicate.
  Through the use of computational techniques, visualization helps researchers explore datasets,
identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
  """

## 💾 Load and Cache Data
# Use st.cache_data to load the data only once.
# This improves performance by avoiding re-downloading the file on every interaction.
@st.cache_data
def load_data(url):
    """Loads the CSV data from a URL into a Pandas DataFrame."""
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

# Call the function to load the data
df = load_data(DATA_URL)

## 📊 Streamlit App Layout
st.title("🩸 Thalassemia Quality of Life Data")
st.subheader("Data Loaded from GitHub")

if not df.empty:
    st.write(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    
    # Display the DataFrame in an interactive table
    st.dataframe(df)

    # Display some basic information
    st.markdown("---")
    st.subheader("Quick Data Information")
    st.text(f"Column Names and Data Types:")
    st.write(df.dtypes)
else:
    st.error("The DataFrame is empty. Please check the URL or file format.")

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['Age_of_Participants'], bins=20, edgecolor='black')
ax.set_title('Distribution of Age of Participants')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig)

"""
  **Scientific Visualization** is a multidisciplinary field that focuses on transforming complex
scientific data into visual forms that are easier to understand, interpret, and communicate.
  Through the use of computational techniques, visualization helps researchers explore datasets,
identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
  """

