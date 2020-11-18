import streamlit as st
import pandas as pd
import numpy as np

st.title("Data App")


# -----------------------------------------------------------------
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv')


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
# ----------------------------------------------------------------


# SELECT BOX------------------------------------------------------
occupation = st.selectbox(
    "Ton poste", ['Data Scientist', 'Programmer', 'Doctor', 'Businessman'])
st.write("So, you are a ", occupation)
# ----------------------------------------------------------------
