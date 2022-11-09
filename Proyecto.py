import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import sodapy
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", None)
results = client.get("h9gi-nx95")




# DATA_URL = ("https://github.com/chairielazizi/streamlit-collision/blob/master/Motor_Vehicle_Collisions_-_Crashes.csv?raw=true")

st.title("Trabajo Final Proyecto I - Manuel Hanono y Bruno Soifer.")
st.markdown("This application is streamlit dashboard that can be used to analyze motor vehicle collision in NYC")
st.markdown("This may take a while as the CSV file is 185MB")


@st.cache(persist=True)
def load_data(rows):
    data = pd.DataFrame.from_records(results, nrows= rows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    # data = pd.read_csv(DATA_URL, nrows= rows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    # data.seek(0)
    data.dropna(subset =['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data.rename(columns={'crash_date_crash_time':'date/time'},inplace=True)
    return data

data = load_data(100000)

# for use with dropdown
original_data = data

# analyze to table
st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in NYC",0,19)
st.map(data.query("injured_persons >= @injured_people")[['latitude', 'longitude']].dropna(how="any"))

# visualize on 2D map
st.header("How many collisons occur during a given time of day?")
# hour = st.selectbox("Hour to look at",range(0,24),1)
hour = st.slider("Hour to look at",0,23)
# hour = st.sidebar.slider("Hour to look at",0,23)
data = data[data['date/time'].dt.hour == hour]


# visualize 3D map
st.markdown("Vehicle collision between %i:00 and %i:00" %(hour,(hour+1) % 24))
midpoint = (np.average(data['latitude']), np.average(data['longitude']))

st.write(pdk.Deck(
    map_style = "mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    # add a layer to visualize on 3d map
    layers = [
        pdk.Layer(
            "HexagonLayer",
            data = data[['date/time','latitude','longitude']],
            get_position = ['longitude','latitude'],
            radius = 100,
            extruded = True,
            pickable = True,
            elevation_scale = 4,
            elevation_range = [0,1000],
        ),
    ],
))


# make a dropdown search
st.header("Top 5 dangerous streets affected by types")
select = st.selectbox("Affected by type of people", ['Pedestrians', 'Cyclists', 'Motorists'])

if select == 'Pedestrians':
    st.write(original_data.query("injured_pedestrians >= 1")[['on_street_name', 'injured_pedestrians']].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how='any')[:5])
elif select == 'Cyclists':
    st.write(original_data.query("injured_cyclists >= 1")[['on_street_name', 'injured_cyclists']].sort_values(by=['injured_cyclists'], ascending=False).dropna(how='any')[:5])
elif select == 'Motorists':
    st.write(original_data.query("injured_motorists >= 1")[['on_street_name', 'injured_motorists']].sort_values(by=['injured_motorists'], ascending=False).dropna(how='any')[:5])


if st.checkbox("Show Raw Data",False):
    st.subheader("Raw Data")
    st.write(data)
