import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 1: Adding text in page

# Add title to the page
st.title("INTRODUCTION")
# Add section header
st.header("SAMPLE HEADER")

data_load_state = st.text('Loading data...')
data_load_state.markdown('Loading data...**done!**')

st.write("This is our introduction")
my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2'])

if my_page == 'page 1':
    st.title("Data")
    st.header("2016-2019 Philippine Voter Dataset")
    if st.checkbox('Show data', value = True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')
    
elif my_page == 'page 2':
    option = st.sidebar.selectbox('Which region do you want to see?', df['Region'].unique())

    'You selected: ', option

    # Filter the entry in the plot
    province_level = df[df['Region'] == option].groupby("Province")["2019-Registered_Voters"].sum()

    st.header(f"Barchart of {option}")

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(province_level.index, province_level.values) 

    plt.title("Registered Voters by Province", fontsize=16)
    plt.ylabel("Number of Registered Voters", fontsize=12)
    plt.xlabel("Province", fontsize=12)
    plt.xticks(rotation=45)

    # display graph
    st.pyplot(fig)