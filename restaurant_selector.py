import streamlit as st
import pandas as pd
import random

# Function to load data from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO/main/restaurants.txt'
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

if st.button('Pick a Random Restaurant'):
    if filtered_data.empty:
        st.write("No restaurants match your criteria.")
    else:
        selected_restaurant = random.choice(filtered_data['Restaurace'].tolist())
        st.write(f"How about: **{selected_restaurant}**")

# Show the filtered list (optional)
if st.checkbox('Show filtered restaurant list'):
    st.write(filtered_data)
