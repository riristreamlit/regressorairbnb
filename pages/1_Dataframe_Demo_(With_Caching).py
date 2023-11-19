import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('📊 Demonstration: Loading Air BnB Clean Data with Caching 📊')

st.markdown("""🌐 Source Data [Kaggle](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata)""")

# Ini buat nambahin cache biar dia ga reload ulang
@st.cache_data 
def load_data(nrow):

    ### Simulating Loading a Large Dataset
    data = pd.read_csv('dataset/Visualization_AirBnB.csv', nrows=nrow)

    chunk_1 = data[0:200]
    chunk_2 = data[200:400]
    chunk_3 = data[400:600]
    chunk_4 = data[600:800]
    chunk_5 = data[800:]

    all_chunk = [chunk_1, chunk_2, chunk_3, chunk_4, chunk_5]

    new_data = pd.DataFrame()
    counter_text = st.text('Processing...')
    for i, chunk in enumerate(all_chunk):
        counter_text.text(f"Processing Part {i+1}/{len(all_chunk)}")
        time.sleep(0.6)
        new_data = new_data.append(chunk).reset_index(drop = True)
    del counter_text
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done!')

# Nilai default checkbox adalah false
if st.checkbox('Show raw data'):
    st.subheader('Raw data') # Kalau diklik muncul ini
    st.write(data)

# Cache Demo
st.markdown(
    """
Now, let's jazz up the app! 🔄 Ideally, the app shouldn't have to redownload the dataset.

Caching allows us to store the results of a function in Streamlit. So, when the app is refreshed and there are
no changes to a particular function, the cached results are retrieved, preventing the function from being rerun
every time the app is refreshed. 🚀
    """
)


# Penjelasan
st.markdown("""This is the dataset we will use for visualization and machine learning later
            🧹The dataset has already been cleaned, as I have completed the:""")

st.markdown("- Data Cleaning")

st.image('1.png', caption='Database Source', use_column_width=True)

st.markdown("- Missing Values")

st.image('2.png', caption='Missing Values', use_column_width=True)

st.markdown("- Handling Outlier")

st.image('3.png', caption='Handling Outlier', use_column_width=True)