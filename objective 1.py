import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Objective 1", layout="wide")
st.header("Objective 1", divider="gray")

# =========================
# LOAD DATA
# =========================
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/thalassemia_qol_data%20(1).csv"

st.markdown("""
*Thalassemia* — This dataset presents comprehensive health-related quality of life (HRQoL) metrics collected from thalassemia patients in Bangladesh using 
the validated SF-36 (Short Form Health Survey) questionnaire.
""")

@st.cache_data
def load_data(url):
    """Loads CSV data from GitHub."""
    try:
        data = pd.read_csv(url)
        data.columns = data.columns.str.strip()  # Clean column names
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data(DATA_URL)

# =========================
# DATA OVERVIEW
# =========================
st.title("🩸 Thalassemia Quality of Life Data")
st.subheader("Data Loaded from GitHub")

if not df.empty:
    st.success(f"✅ Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    
    st.dataframe(df, use_container_width=True)
  
    st.markdown("---")
    st.subheader("Quick Data Information")
    st.text("Column Names and Data Types:")
    st.write(df.dtypes)
    
    # =========================
    # 📊 DYNAMIC METRICS SECTION
    # =========================
    st.markdown("---")
    st.subheader("📈 Dynamic Dataset Metrics")

    # Compute key metrics
    total_participants = len(df)
    avg_age = df['Age_of_Participants'].mean() if 'Age_of_Participants' in df.columns else np.nan

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        dominant_gender = gender_counts.idxmax()
        dominant_gender_percent = (gender_counts.max() / total_participants) * 100
    else:
        dominant_gender = "N/A"
        dominant_gender_percent = 0

    if 'Frequency_of_Blood_Transfusion' in df.columns:
        most_common_transfusion = df['Frequency_of_Blood_Transfusion'].mode()[0]
    else:
        most_common_transfusion = "N/A"

    # Display metrics side by side
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Participants", f"{total_participants}")
    col2.metric("🎂 Average Age", f"{avg_age:.1f} years" if not np.isnan(avg_age) else "N/A")
    col3.metric("🚻 Dominant Gender", f"{dominant_gender} ({dominant_gender_percent:.1f}%)")
    col4.metric("💉 Common Transfusion Frequency", most_common_transfusion)

    # =========================
    # 📈 VISUALIZATIONS
    # =========================
    st.markdown("---")
    st.subheader("Data Visualizations")

    # Histogram: Age of Participants
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Age_of_Participants'], bins=20, edgecolor='black')
    ax.set_title('Distribution of Age of Participants')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    st.caption("*Figure 1:* Histogram showing the distribution of participant ages.")

    # Pie Chart: Gender Distribution
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
    ax.axis('equal')
    st.pyplot(fig)
    st.caption("*Figure 2:* Pie chart showing gender distribution among participants.")

    # Bar Chart: Frequency of Blood Transfusion
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
    st.caption("*Figure 3:* Bar chart showing frequency of blood transfusion categories.")

else:
    st.error("❌ The DataFrame is empty. Please check the URL or file format.")
