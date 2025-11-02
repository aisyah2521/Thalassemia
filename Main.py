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
ax.hist(df['Age_of_Participants'], bins=20, edgecolor='black')
ax.set_title('Distribution of Age of Participants')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig)

"""
  **Figure 1** This graph is a **histogram** that shows the Distribution of Age Of Participants. 
  """

gender_counts = df['Gender'].value_counts()

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['skyblue', 'lightcoral']
)
ax.set_title('Distribution of Gender')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)

"""
  **Figure 2** This graph is a **pie chart** title "Distribution Of Gender."
  """


fig, ax = plt.subplots(figsize=(10, 6))
df['Frequency_of_Blood_Transfusion'].value_counts().plot(
    kind='bar', edgecolor='black', ax=ax
)
ax.set_title('Distribution of Frequency of Blood Transfusion')
ax.set_xlabel('Frequency of Blood Transfusion')
ax.set_ylabel('Count')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

"""
  **Figure 3** This graph is a **bar chart** title "Distribution Of Frequency Of Blood Transfusion.It compares
  the number of participants (count) falling into three diffrent categories of transfusion frequency.
  """
