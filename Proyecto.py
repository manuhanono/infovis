import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

#DATA_URL = ("https://github.com/chairielazizi/streamlit-collision/blob/master/Motor_Vehicle_Collisions_-_Crashes.csv?raw=true")

DATA_URL1 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-1.csv")
DATA_URL2 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-2.csv")
DATA_URL3 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-3.csv")
DATA_URL4 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-4.csv")
DATA_URL5 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-5.csv")
DATA_URL6 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-6.csv")
DATA_URL7 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-7.csv")
DATA_URL8 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-8.csv")
DATA_URL9 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-9.csv")
DATA_URL10 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-10.csv")
DATA_URL11 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-11.csv")
DATA_URL12 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-12.csv")
DATA_URL13 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-13.csv")
DATA_URL14 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-14.csv")
DATA_URL15 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-15.csv")
DATA_URL16 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-16.csv")
DATA_URL17 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-17.csv")
DATA_URL18 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-18.csv")
DATA_URL19 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-19.csv")
DATA_URL20 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-20.csv")
DATA_URL21 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-21.csv")
DATA_URL22 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-22.csv")
DATA_URL23 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-23.csv")
DATA_URL24 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-24.csv")
DATA_URL25 = ("https://raw.githubusercontent.com/manuhanono/infovis/main/splitcsv-c9ce4b82-b1ac-45ed-9e57-bbbd7dbcfc8d-results/crashes-25.csv")


st.title("Trabajo Final Proyecto I - NY Crashes")
st.markdown("Manuel Hanono y Bruno Soifer.")

@st.cache(persist=True)
def load_data(rows):
    #data = pd.read_csv(DATA_URL1, nrows= rows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    df1 = pd.read_csv(DATA_URL1)
    df2 = pd.read_csv(DATA_URL2)
    df3 = pd.read_csv(DATA_URL3)
    df4 = pd.read_csv(DATA_URL4)
    df5 = pd.read_csv(DATA_URL5)
    df6 = pd.read_csv(DATA_URL6)
    df7 = pd.read_csv(DATA_URL7)
    df8 = pd.read_csv(DATA_URL8)
    df9 = pd.read_csv(DATA_URL9)
    df10 = pd.read_csv(DATA_URL10)
    df11 = pd.read_csv(DATA_URL11)
    df12 = pd.read_csv(DATA_URL12)
    df13 = pd.read_csv(DATA_URL13)
    df14 = pd.read_csv(DATA_URL14)
    df15 = pd.read_csv(DATA_URL15)
    df16 = pd.read_csv(DATA_URL16)
    df17 = pd.read_csv(DATA_URL17)
    df18 = pd.read_csv(DATA_URL18)
    df19 = pd.read_csv(DATA_URL19)
    df20 = pd.read_csv(DATA_URL20)
    df21 = pd.read_csv(DATA_URL21)
    df22 = pd.read_csv(DATA_URL22)
    df23 = pd.read_csv(DATA_URL23)
    df24 = pd.read_csv(DATA_URL24)
    df25 = pd.read_csv(DATA_URL25)
    data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25],ignore_index=True, nrows=rows)
    # data.seek(0)
    data.dropna(subset =['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data.rename(columns={'crash_date_crash_time':'date/time'},inplace=True)
    return data

data = load_data(1950000)

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
