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


# --- 🧪 Example DataFrame creation (Replace this with your actual data loading) ---
# This creates a dummy DataFrame for demonstration since the original code relies on 'df'
import numpy as np
np.random.seed(42)
data = {'Age_of_Participants': np.random.randint(18, 65, size=100)}
df = pd.DataFrame(data)
# -----------------------------------------------------------------------------------

# Add the main introduction paragraph
st.write(
  """
  **Scientific Visualization** is a multidisciplinary field that focuses on transforming complex
scientific data into visual forms that are easier to understand, interpret, and communicate.
  Through the use of computational techniques, visualization helps researchers explore datasets,
identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
  """
)

def plot_age_distribution(data_frame):
    """Generates and displays the age distribution histogram in Streamlit."""
    
    # Create the Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Generate the histogram on the axes
    ax.hist(data_frame['Age_of_Participants'], bins=20, edgecolor='black')

    # Set the title and labels
    ax.set_title('Distribution of Age of Participants')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    
    # Display the figure using st.pyplot()
    st.pyplot(fig)

# --- 🚀 Streamlit App Execution ---
st.title('Participant Age Data Visualization')

# Call the function to display the plot
plot_age_distribution(df)


# --- 🧪 Example DataFrame creation (Replace this with your actual data loading) ---
# This creates a dummy DataFrame for demonstration since the original code relies on 'df'
np.random.seed(42)
data = {'Gender': np.random.choice(['Male', 'Female',], size=100, p=[0.55, 0.45])}
df = pd.DataFrame(data)
# -----------------------------------------------------------------------------------

def plot_gender_distribution(data_frame):
    """Generates and displays the gender distribution pie chart in Streamlit."""
    
    # 1. Calculate the counts (same as your original code)
    gender_counts = data_frame['Gender'].value_counts()
    
    # 2. Create the Matplotlib figure and axes
    # We use subplots() to explicitly define the figure (fig)
    fig, ax = plt.subplots(figsize=(8, 8)) 

    # 3. Generate the pie chart on the axes (ax)
    ax.pie(
        gender_counts, 
        labels=gender_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=['skyblue', 'lightcoral', 'lightgreen'] # Added a third color for 'Other'
    )
    
    # 4. Set the title and ensure it's a circle
    ax.set_title('Distribution of Gender')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # 5. Display the figure using st.pyplot()
    st.pyplot(fig)

# --- 🚀 Streamlit App Execution ---
st.title('Gender Distribution Visualization')

# Call the function to display the plot
plot_gender_distribution(df)


# --- 🧪 Example DataFrame creation (Replace this with your actual data loading) ---
# This creates a dummy DataFrame for demonstration
np.random.seed(42)
transfusion_data = np.random.choice(
    ['Weekly', 'Monthly', 'Quarterly', 'Annually', 'Never'], 
    size=200, 
    p=[0.1, 0.3, 0.25, 0.15, 0.2]
)
df = pd.DataFrame({'Frequency_of_Blood_Transfusion': transfusion_data})
# -----------------------------------------------------------------------------------

def plot_transfusion_frequency(data_frame):
    """Generates and displays the frequency of blood transfusion bar chart in Streamlit."""
    
    # 1. Calculate the counts (same logic as your original code)
    counts = data_frame['Frequency_of_Blood_Transfusion'].value_counts()
    
    # 2. Create the Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # 3. Generate the bar chart on the axes (ax)
    # Since you used the pandas .plot(kind='bar') method, we'll use ax.bar() 
    # for better control within the subplots structure.
    # The counts.index are the labels (x-values), and counts.values are the heights (y-values).
    ax.bar(counts.index, counts.values, edgecolor='black')

    # 4. Set the title and labels
    ax.set_title('Distribution of Frequency of Blood Transfusion')
    ax.set_xlabel('Frequency of Blood Transfusion')
    ax.set_ylabel('Count')

    # 5. Rotate x-axis labels
    ax.tick_params(axis='x', rotation=45) 
    # ax.tick_params() handles both rotation and alignment (ha='right' is default for 45 deg rotation)

    # 6. Adjust layout and display using st.pyplot()
    fig.tight_layout() # Equivalent to plt.tight_layout() on the figure object
    st.pyplot(fig)

# --- 🚀 Streamlit App Execution ---
st.title('Blood Transfusion Frequency Analysis')

# Call the function to display the plot
plot_transfusion_frequency(df)

this is my codding
