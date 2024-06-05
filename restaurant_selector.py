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
st.sidebar.title("Filter Options")
vegan_filter = st.sidebar.checkbox('Show only vegan restaurants', value=False)
eat_in_filter = st.sidebar.checkbox('Show only restaurants with seating', value=False)

# Apply filters to the data
filtered_data = data.copy()
if vegan_filter:
    filtered_data = filtered_data[filtered_data['Veganská'] == 'Yes']
if eat_in_filter:
    filtered_data = filtered_data[filtered_data['Sezení'] == 'Yes']

# Main interface
st.title("Restaurant Selector")
st.write("Select your filters and click the button to pick a random restaurant.")

# Animation and result display
result_placeholder = st.empty()
button_clicked = st.button('Pick a Random Restaurant')

if button_clicked:
    if filtered_data.empty:
        st.write("No restaurants match your criteria.")
    else:
        # Animation effect
        for _ in range(10):  # Number of spins
            selected_restaurant = random.choice(filtered_data['Restaurace'].tolist())
            result_placeholder.markdown(f"### How about: **{selected_restaurant}**")
            time.sleep(0.1)  # Adjust the speed of the animation

        # Final result
        selected_restaurant = random.choice(filtered_data['Restaurace'].tolist())
        result_placeholder.markdown(f"""
        <div style="text-align: center;">
            <h1 style="color: #4CAF50; font-size: 3em;">{selected_restaurant}</h1>
        </div>
        """, unsafe_allow_html=True)

# Show the filtered list (optional)
if st.checkbox('Show filtered restaurant list'):
    st.write(filtered_data)

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
