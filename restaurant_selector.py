import streamlit as st
import pandas as pd
import random
import time

# Function to load data from GitHub
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/MKSvoboda/RestaurantRoulette/main/restaurants.txt'
    return pd.read_csv(url, sep=',')  # Adjust the separator if needed

# Load the restaurant data
data = load_data()

# Sidebar filters
st.sidebar.title("Možnosti")
vegan_filter = st.sidebar.checkbox('Vegan', value=False)
eat_in_filter = st.sidebar.checkbox('Možnost sezení', value=False)

# Apply filters to the data
filtered_data = data.copy()
if vegan_filter:
    filtered_data = filtered_data[filtered_data['Veganská'] == 'Yes']
if eat_in_filter:
    filtered_data = filtered_data[filtered_data['Sezení'] == 'Yes']

# Main interface
st.title("Obědová ruleta")
st.write("Zvol kritéria a vylosuj podnik na oběd")

# Animation and result display
result_placeholder = st.empty()
button_clicked = st.button('Vybrat podnik:')

if button_clicked:
    if filtered_data.empty:
        st.write("Nebyl nalezen vyhovující podnik.")
    else:
        # Animation effect using the filtered list
        for _ in range(10):  # Number of spins
            selected_restaurant = random.choice(filtered_data['Restaurace'].tolist())
            result_placeholder.markdown(f"### Co třeba: **{selected_restaurant}**")
            time.sleep(0.5)  # Adjust the speed of the animation

        # Final result using the filtered list
        selected_restaurant = random.choice(filtered_data['Restaurace'].tolist())
        result_placeholder.markdown(f"""
        <div style="text-align: center;">
            <h1 style="color: #4CAF50; font-size: 3em;">{selected_restaurant}</h1>
        </div>
        """, unsafe_allow_html=True)

# Link to restaurants.txt
st.markdown("""
    ---
    Seznam restaurací: [restaurants.txt](https://github.com/MKSvoboda/RestaurantRoulette/blob/main/restaurants.txt)
    """)

# General styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #4CAF50;
        }
        .css-1d391kg {
            color: #4CAF50;
        }
    </style>
    """, unsafe_allow_html=True)
