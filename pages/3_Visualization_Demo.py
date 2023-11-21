import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

import folium
import branca.colormap as cm
from streamlit_folium import folium_static
from branca.colormap import LinearColormap

# plotly express, ini cocok banget untuk visualisasi di streamlit
import plotly.express as px

st.title('🖼️ Demo: Visualizing 🖼️')

st.markdown(
    """
In this script, we will be crafting Python code to carry out the following tasks:

Loading a Dataset 📊: Importing a dataset from our designated folder.
Data Visualization 📈: Conducting visualizations to gain insights from the dataset.

It's crucial to note that almost all options within the script are interactive, requiring careful attention from the user. 🕵️‍♂️

*It's a little bit lagging, please bear with it* ⏳
    """
)

df = pd.read_csv('dataset/Visualization_AirBnB.csv')

@st.cache_data
def show_data():
    st.write(df)


if st.checkbox('Show Data!'):
    show_data()

st.subheader('Map Visualization of Air BnB Rent in New York')

# Slider and Multi Select Box
@st.cache_data
def filter_data(selected_neighbourhoods, price_range, df):
    if 'All' in selected_neighbourhoods or not selected_neighbourhoods:
        selected_neighbourhoods = df['neighbourhood_group'].unique()

    filtered_df = df[(df['neighbourhood_group'].isin(selected_neighbourhoods)) & 
                     (df['price'] >= price_range[0]) & 
                     (df['price'] <= price_range[1])]
    
    return filtered_df

# Create tabs
tabs = st.tabs(['Map', 'Room Type'])

# Map Section
with tabs[0]:

    # Multiselect for choosing multiple neighbourhood_group values
    selected_neighbourhoods_map = st.multiselect('Select Neighbourhood Groups', ['All'] + list(df['neighbourhood_group'].unique()), default=['All'])

    # Slider for selecting the price range
    price_range_map = st.slider('Select Price Range', min_value=50, max_value=1200, step=1, value=(50, 1200))

    # Call the function to filter data and visualize the map
    filtered_df_map = filter_data(selected_neighbourhoods_map, price_range_map, df)

    # Create the map using Plotly Express, color by price
    fig_map = px.scatter_mapbox(filtered_df_map, lat='lat', lon='long', color='price',
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                size_max=15, zoom=10,
                                labels={'price': 'Price'},
                                color_continuous_midpoint=filtered_df_map['price'].mean())

    fig_map.update_layout(mapbox_style="open-street-map",
                          mapbox=dict(center=dict(lat=filtered_df_map['lat'].mean(), lon=filtered_df_map['long'].mean()),  # Set the center
                                      zoom=10),  # Adjust the zoom level
                          width=800, height=800)  # Set the size of the map

    st.plotly_chart(fig_map, use_container_width=True)

# Room Type Section
with tabs[1]:

    # Multiselect for choosing multiple neighbourhood_group values
    selected_neighbourhoods_room = st.multiselect('Select Neighbourhood Groups', ['All'] + list(df['neighbourhood_group'].unique()), default=['All'], key='room_neighbourhood_multiselect')

    # Slider for selecting the price range
    price_range_room = st.slider('Select Price Range', float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())), key='room_price_range_slider')

    # Call the function to filter data and visualize the room type
    filtered_df_room = filter_data(selected_neighbourhoods_room, price_range_room, df)

    # Create the map using Plotly Express, color by room type
    fig_room = px.scatter_mapbox(filtered_df_room, lat='lat', lon='long', color='room_type',
                                color_discrete_map={'Entire home/apt': 'red', 'Private room': 'blue', 'Shared room': 'green', 'Hotel room': 'purple'},
                                size_max=15, zoom=10,
                                labels={'room_type': 'Select Room Type'},
                                )

    fig_room.update_layout(mapbox_style="open-street-map",
                          mapbox=dict(center=dict(lat=filtered_df_room['lat'].mean(), lon=filtered_df_room['long'].mean()),  # Set the center
                                      zoom=10),  # Adjust the zoom level
                          width=800, height=800)  # Set the size of the map

    st.plotly_chart(fig_room, use_container_width=True)













# Scatter plot 
st.subheader('Scatterplot of Price and Review')

unique_ng_list = ['All']
unique_ng_list.extend(df.neighbourhood_group.unique().tolist())

ng_select = st.selectbox('Select Neighbourhood Group:', unique_ng_list)

@st.cache_data
def visualize_scatterplot(neighbourhood_group):
    if neighbourhood_group == 'All':
        fig = px.scatter(df, x = 'price', y = 'number_of_reviews', color = 'room_type')
        st.plotly_chart(fig, theme = 'streamlit')
    else:
        df_select = df[df['neighbourhood_group'] == neighbourhood_group]
        fig = px.scatter(df_select, x = 'price', y = 'number_of_reviews', color = 'room_type')
        st.plotly_chart(fig, theme = 'streamlit')        

visualize_scatterplot(ng_select)

# Boxplot

st.subheader('Price Boxplot for Air BnB in New York')

@st.cache_data
def visualize_boxplot():
    tab1, tab2, tab3, tab4 = st.tabs(['By Type of Bedrooms', 'By Neighbourhood Group', 'Cancellation Policy', 'Review Rate Number'])

    with tab1:
        fig = px.box(df, x='room_type', y='price', color='room_type')  # Added color parameter
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    with tab2:
        fig = px.box(df, x='neighbourhood_group', y='price', color='neighbourhood_group')  # Added color parameter
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    with tab3:
        fig = px.box(df, x='cancellation_policy', y='price', color='cancellation_policy')  # Added color parameter
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    with tab4:
        fig = px.box(df, x='review_rate_number', y='price', color='review_rate_number')  # Added color parameter
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)
visualize_boxplot()

# Bar Chart

st.subheader('Detail View on Each Neighbourhood Group')

@st.cache_data
def visualize_bar_charts():
    with st.container():
        tabs = st.tabs(['Day Booked', 'Number of Guests', 'Minimum Nights (Days)', 'Availability (Days)'])

        with tabs[0]:
            avg_avail = df.groupby('neighbourhood_group')['availability_365'].mean().nlargest(10).reset_index()
            fig1 = px.bar(avg_avail, x='availability_365', y='neighbourhood_group', orientation='h',
                          title='Average Day Booked per Neighbourhood Group',
                          labels={'availability_365': 'Day Booked', 'neighbourhood_group': 'Neighbourhood'},
                          color='neighbourhood_group', text='availability_365', height=500)
            st.plotly_chart(fig1)

        with tabs[1]:
            x = 'calculated_host_listings_count'
            total_values = df.groupby('neighbourhood_group')[x].mean().reset_index()
            fig2 = px.bar(total_values, x=x, y='neighbourhood_group', title=f'Average Number of Guests per Neighbourhood Group',
                          labels={x: x, 'neighbourhood_group': 'Neighbourhood'},
                          text=x, color='neighbourhood_group', height=500)
            st.plotly_chart(fig2)

        with tabs[2]:
            x = 'minimum_nights'
            avg_min_nights = df.groupby('neighbourhood_group')[x].mean().nlargest(10).reset_index()
            fig3 = px.bar(avg_min_nights, x=x, y='neighbourhood_group', orientation='h',
                          title=f'Average Minimum Nights per Neighbourhood Group',
                          labels={x: 'Average Minimum Nights', 'neighbourhood_group': 'Neighbourhood'},
                          color='neighbourhood_group', text=x, height=500)
            st.plotly_chart(fig3)

        with tabs[3]:
            x = 'availability_365'
            avg_avail_365 = df.groupby('neighbourhood_group')[x].mean().nlargest(10).reset_index()
            fig4 = px.bar(avg_avail_365, x=x, y='neighbourhood_group', orientation='h',
                          title=f'Average Availability per Neighbourhood Group',
                          labels={x: 'Average Availability', 'neighbourhood_group': 'Neighbourhood'},
                          color='neighbourhood_group', text=x, height=500)
            st.plotly_chart(fig4)

# Call the function to display the charts
visualize_bar_charts()