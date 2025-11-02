import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(
  page_title="Objective 1"
)
st.header("Objective 1", divider="gray")


# The raw GitHub URL for the CSV file
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv"

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

# The raw GitHub URL for the CSV file (from the previous context)
DATA_URL = "https://raw.githubusercontent.com/aisyah2521/Thalassemia/refs/heads/main/cleaned_thalassemia_qol_data.csv"
DATA_COLUMN = 'Age_of_Participants' # The column to plot

## 💾 Load and Cache Data
# Use st.cache_data for performance, loading the data only once.
@st.cache_data
def load_data(url):
    """Loads the CSV data from a URL into a Pandas DataFrame."""
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        # In a real app, you might want to log this or provide a fallback
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load the data
df = load_data(DATA_URL)

## 📊 Streamlit App Layout
st.title("🩸 Thalassemia Age Distribution Analysis")

if not df.empty and DATA_COLUMN in df.columns:
    st.subheader(f"Distribution of {DATA_COLUMN.replace('_', ' ')}")

    # 1. Create the figure object and plot the histogram
    # You must call plt.figure() before plotting to ensure a new figure is created
    # or Streamlit might reuse a previous one in some environments.
    plt.figure(figsize=(8, 6))
    
    # 2. Plot the histogram using the dataframe column
    plt.hist(df[DATA_COLUMN], bins=20, edgecolor='black', color='#4CAF50')
    
    # 3. Add titles and labels
    plt.title('Distribution of Age of Participants', fontsize=16)
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    
    # 4. Use st.pyplot() to display the current matplotlib figure
    # Note: We remove the original plt.show()
    st.pyplot(plt)

    st.markdown("---")
    st.dataframe(df.head()) # Display the first few rows for context

else:
    st.error(f"Could not load data or the column '{DATA_COLUMN}' was not found in the dataset.")

