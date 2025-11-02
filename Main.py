import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 🎯 PAGE CONFIGURATION
# -------------------------------------------------------
st.set_page_config(page_title="Objective 1", layout="centered")
st.header("Objective 1", divider="gray")

# -------------------------------------------------------
# 💾 LOAD DATA (CACHED)
# -------------------------------------------------------
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv"

@st.cache_data
def load_data(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data(DATA_URL)

# -------------------------------------------------------
# 📊 DISPLAY DATA
# -------------------------------------------------------
if not df.empty:
    st.success(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    st.dataframe(df)
else:
    st.stop()

st.markdown("---")
st.subheader("Quick Data Information")
st.write(df.dtypes)

# -------------------------------------------------------
# 📖 INTRODUCTION
# -------------------------------------------------------
st.markdown("""
**Scientific Visualization** transforms complex scientific data into visual forms
that are easier to understand, interpret, and communicate.
It helps researchers explore datasets, identify hidden patterns, and gain insights
that would otherwise remain obscure in numerical form.
""")

# -------------------------------------------------------
# 📈 VISUALIZATION FUNCTIONS
# -------------------------------------------------------
def plot_age_distribution(data):
    if 'Age_of_Participants' in data.columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data['Age_of_Participants'], bins=20, edgecolor='black')
        ax.set_title('Distribution of Age of Participants')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)
    else:
        st.warning("Column 'Age_of_Participants' not found in dataset.")

def plot_gender_distribution(data):
    if 'Gender' in data.columns:
        gender_counts = data['Gender'].value_counts()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
        ax.set_title('Distribution of Gender')
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.warning("Column 'Gender' not found in dataset.")

def plot_transfusion_frequency(data):
    if 'Frequency_of_Blood_Transfusion' in data.columns:
        counts = data['Frequency_of_Blood_Transfusion'].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(counts.index, counts.values, edgecolor='black')
        ax.set_title('Distribution of Frequency of Blood Transfusion')
        ax.set_xlabel('Frequency of Blood Transfusion')
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Column 'Frequency_of_Blood_Transfusion' not found in dataset.")

# -------------------------------------------------------
# 🧭 SIDEBAR NAVIGATION
# -------------------------------------------------------
st.sidebar.title("📊 Choose Visualization")
options = ["Age Distribution", "Gender Distribution", "Blood Transfusion Frequency"]
choice = st.sidebar.radio("Select a chart to display:", options)

# -------------------------------------------------------
# 🚀 DISPLAY SELECTED VISUALIZATION
# -------------------------------------------------------
if choice == "Age Distribution":
    st.title("Participant Age Data Visualization")
    plot_age_distribution(df)

elif choice == "Gender Distribution":
    st.title("Gender Distribution Visualization")
    plot_gender_distribution(df)

elif choice == "Blood Transfusion Frequency":
    st.title("Blood Transfusion Frequency Analysis")
    plot_transfusion_frequency(df)


st.title("Distribution of Gender")

# Calculate gender counts
gender_counts = df['Gender'].value_counts()

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the pie chart
ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['skyblue', 'lightcoral']
)

# Set title and make it circular
ax.set_title('Distribution of Gender')
ax.axis('equal')  # Ensures the pie is drawn as a circle

# Display the plot in Streamlit
st.pyplot(fig)



