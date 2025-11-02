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
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/thalassemia_qol_data%20(1).csv"

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

fig, ax = plt.subplots(figsize=(8, 6))
sns.kdeplot(df['Physical_Health_Summary'].dropna(), fill=True, ax=ax)
ax.set_title('Density Plot of Physical Health Summary')
ax.set_xlabel('Physical Health Summary Score')
ax.set_ylabel('Density')

st.pyplot(fig)

"""
  **Figure 1** This graph is a **Density Plot** also knows as a Kernel Density Estimate or KDE plot
  illustrating the distribution of the Physical Health Summary Score.
  """


# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
sns.violinplot(x='Occupational_Status', y='Social_Functioning', data=df, ax=ax)
ax.set_title('Distribution of Social Functioning by Occupational Status')
ax.set_xlabel('Occupational Status')
ax.set_ylabel('Social Functioning Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)


"""
  **Figure 2** This graph is a **Violin Plot** titled "Distribution of Total SF by Type of Family (Nuclear).
  "It compares the distribution of the Total SF Score (likely a summary function ore health score) 
  for two groups: participants who are not in a nuclear family (False) and those who are in a nuclear family(True).
  """ 

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Diagnosis', y='Mental_Health_Summary', data=df, ax=ax)
ax.set_title('Distribution of Mental Health Summary by Diagnosis')
ax.set_xlabel('Diagnosis')
ax.set_ylabel('Mental Health Summary')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

"""
  **Figure 3** This graph is a **Box Plot** title "Distribution of Mental Health Summary by Diagnosis."it
  compares the spread and central tendency of a Mental Health Summary Score across four different diagnostic groups.
  """
