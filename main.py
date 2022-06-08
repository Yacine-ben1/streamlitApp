import streamlit as st
import pandas as pd
import numpy as np
import time
import leafmap.foliumap as leafmap

st.set_page_config(page_title="My DashBoard",layout="wide")
# ---------------------------------
df = pd.read_excel('datatest.xlsx')
st.image("logo_anem.png")
kpa1,kpa2=st.columns(2)
with kpa1:
#Metrics
  st.metric(
    label="demandEnrg ",
    value=sum(df["demandEnrg"].values),
    delta=round(20) - 10,
)
with kpa2:
  selectedWilaya = st.selectbox('Wilaya:', df["wilaya"].drop_duplicates())
  df = df[(df["wilaya"] == selectedWilaya)]




#Map
m = leafmap.Map(locate_control=True, zoom=4,plugin_LatLngPopup=True)
m.add_points_from_xy(df, x="lon", y="lat")
m.to_streamlit()














