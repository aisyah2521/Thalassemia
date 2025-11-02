import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Objective 1")
st.header("Objective 1", divider="gray")

# The raw GitHub URL for the CSV file
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/thalassemia_qol_data%20(1).csv"

"""
*Thalassemia* — This dataset presents comprehensive health-related quality of life (HRQoL) metrics 
collected from thalassemia patients in Bangladesh using the validated SF-36 (Short Form Health Survey) questionnaire.
"""

# 💾 Load and Cache Data
@st.cache_data
def load_data(url):
    """Loads the CSV data from a URL into a Pandas DataFrame."""
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Call the function to load the data
df = load_data(DATA_URL)

# 📊 Streamlit App Layout
st.title("🩸 Thalassemia Quality of Life Data")
st.subheader("Data Loaded from GitHub")

if not df.empty:
    st.success(f"✅ Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    st.dataframe(df)

    # --- BASIC DATA INFO ---
    st.markdown("---")
    st.subheader("Quick Data Information")
    st.write("Column Names and Data Types:")
    st.write(df.dtypes)

    # --- FIGURE 1: Age Histogram ---
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Age_of_Participants'], bins=20, edgecolor='black')
    ax.set_title('Distribution of Age of Participants')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    st.markdown("""
    *Figure 1* — A **histogram** showing the distribution of participants’ ages, illustrating 
    how the study population is spread across different age groups.
    """)

    # --- FIGURE 2: Gender Pie Chart ---
    gender_counts = df['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
           startangle=90, colors=['skyblue', 'lightcoral'])
    ax.set_title('Distribution of Gender')
    ax.axis('equal')
    st.pyplot(fig)

    st.markdown("""
    *Figure 2* — A **pie chart** titled "Distribution of Gender," showing 
    the proportion of male and female participants in the dataset.
    """)

    # --- FIGURE 3: Blood Transfusion Bar Chart ---
    fig, ax = plt.subplots(figsize=(10, 6))
    df['Frequency_of_Blood_Transfusion'].value_counts().plot(kind='bar', edgecolor='black', ax=ax)
    ax.set_title('Distribution of Frequency of Blood Transfusion')
    ax.set_xlabel('Frequency of Blood Transfusion')
    ax.set_ylabel('Count')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("""
    *Figure 3* — A **bar chart** titled "Distribution of Frequency of Blood Transfusion." 
    It compares the number of participants (count) across different transfusion frequency categories.
    """)

else:
    st.error("❌ The DataFrame is empty. Please check the URL or file format.")
