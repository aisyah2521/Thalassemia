import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

st.set_page_config(
  page_title="Objective 2"
)
st.header("Objective 2", divider="gray")


# The raw GitHub URL for the CSV file
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv"

"""
  **Thalassemia** This dataset presents comprehensive health-related quality of life (HRQoL) metrics collected from thalassemia patients in Bangladesh using 
  the validated SF-36 (Short Form Health Survey) questionnaire.
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


diagnosis_counts = df['Diagnosis'].value_counts()

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    diagnosis_counts,
    labels=diagnosis_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.3}
)
ax.set_title('Distribution of Diagnosis', pad=20.0)
ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle

st.pyplot(fig)

"""
  **Thalassemia** This dataset presents comprehensive health-related quality of life (HRQoL) metrics collected from thalassemia patients in Bangladesh using 
  the validated SF-36 (Short Form Health Survey) questionnaire.
  """
