import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from pathlib import Path

import pickle
from sklearn.ensemble import RandomForestRegressor

st.title('🔮 Demo: Machine Learning 🔮')

st.markdown("""
    - The model encompasses numerous variables, so making slight changes won't significantly alter its pricing. 📊💼
    - I suggest you to play with the slider's value to see the significant price change 🔄🔍""")

###
@st.cache_data 
def load_model():
    return pickle.load(open('model/Regression.pkl', 'rb'))
###
@st.cache_data 
def load_region_data():
    return pd.read_csv('dataset/region.csv')

model = load_model()
region_data = load_region_data()

st.subheader("Fill in your desired AirBnB facilities, and we'll guess the price and the AirBnB category! 🏡💰")

###

host = st.radio('Host: ', ['Unconfirmed', 'Verified'])
if host == 'Unconfirmed':
    host = 0
else:
    host = 1

###

sorted_regions = sorted(region_data.neighbourhood_group.unique())
region = st.selectbox("Where is your Air BnB located? (Neighbourhood Group)", sorted_regions)

if region:
    # Filter data based on the selected region
    filtered_data = region_data.query(f"neighbourhood_group == '{region}'")

    # Get unique localities for the selected region and sort them alphabetically
    sorted_localities = sorted(filtered_data['neighbourhood'].unique())
    locality = st.selectbox("Where is your Air BnB located? (Neighbourhood)", sorted_localities)

    # Further processing with selected_region
    selected_region = filtered_data.query(f"neighbourhood == '{locality}'").reset_index(drop=True)

if region == 'Bronx':
    region = 0
elif region == 'Brooklyn':
    region = 1
elif region == 'Manhattan':
    region = 2
elif region == 'Queens':
    region = 3
else:
    region = 4

long = selected_region.long.values[0]
lat = selected_region.lat.values[0]

###

ib = st.radio('Instant Bookable: ', ['False', 'True'])
ib = 1 if ib == 'True' else 0

cp = st.radio('Cancellation Policy: ', ['Flexible', 'Moderate', 'Strict'])
cp = 0 if cp == 'Flexible' else 1 if cp == 'Moderate' else 2

rt = st.radio('Room Type: ', ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'])
rt = 0 if rt == 'Entire home/apt' else 1 if rt == 'Hotel room' else 2 if rt == 'Private room' else 3


###
sorted_construction_years = sorted(region_data.construction_year.unique())
construction_year = st.selectbox("Construction Year", sorted_construction_years)

###

service_fee = st.slider('Service Fee Tolerance', 0,250,150, step = 50)

###

mn = st.slider('Minimum Nights to Stay', 0,365, 7, step = 7)

###

review = st.slider('Air BnB Star Rating', 0, 5, 3)

###

number_of_reviews = st.slider('Air BnB Review Count', 0, 1300, 600, step = 100)

###

chlc = st.slider('Total hotels guest count', 0, 400,100, step = 10)

###

a365 = st.slider('Airbnb availability in days per year', 0, 365, 30, step = 7)

###

your_apartment = pd.DataFrame({
    'host_identity_verified': [host],
    'neighbourhood_group': [region],
    'lat': [lat],
    'long': [long],
    'instant_bookable': [ib],
    'cancellation_policy': [cp],
    'room_type': [rt],
    'construction_year': [construction_year],
    'service_fee': [service_fee],
    'minimum_nights': [mn],
    'number_of_reviews': [number_of_reviews],
    'review_rate_number': [review],
    'calculated_host_listings_count': [chlc],
    'availability_365': [a365]
})

###


if st.button('Calculate Price!'):
    your_apartment_price = model.predict(your_apartment)
    your_apartment_price = your_apartment_price[0]
    your_apartment_price = your_apartment_price/10

    st.write(f"### Your AirBnB's daily rent price is predicted at: $ {int(your_apartment_price)}")

    # Segmentation based on predicted price
    if your_apartment_price < 250:
        category = "Guest House 🏡"
        description = "- Lower Price\n- No verified host\n- Not instant bookable\n- Quite popular\n- Suitable for backpackers"
    elif 250 <= your_apartment_price < 550:
        category = "Boarding House 🏠"
        description = "- Lower Mid Price\n- Verified host\n- Not instant bookable\n- Suitable for students"
    elif 550 <= your_apartment_price < 650:
        category = "Lodging 🛌"
        description = "- Mid Price\n- No verified host\n- Not instant bookable\n- Quite popular\n- Suitable for worker/tourism"
    elif 650 <= your_apartment_price < 975:
        category = "Motel 🏨"
        description = "- Mid to High Price\n- Verified host\n- Not instant bookable\n- Quite empty\n- Suitable for times alone"
    elif 975 <= your_apartment_price < 1030:
        category = "Hotel 🏩"
        description = "- High Price\n- No verified host\n- Not instant bookable\n- Many reviews\n- Good facilities"
    else:
        category = "Luxury Hotel 🌟"
        description = "- Higher Price\n- Verified Host\n- Instant Bookable\n- Many reviews\n- Good facilities, but quite expensive\n- Can be booked from afar\n- Suitable for family vacations"

    st.write(f"### Based on the predicted price, your AirBnB falls into the category of {category}.")
    st.write("Description:")
    st.write(description)

    # Create a folium map and add a marker
    map_center = [lat, long]
    m = folium.Map(location=map_center, zoom_start=12)
    folium.Marker(location=map_center, popup='Your AirBnB Location').add_to(m)

    # Display the map
    st.write("### Your AirBnB Location on the Map:")
    folium_static(m)
