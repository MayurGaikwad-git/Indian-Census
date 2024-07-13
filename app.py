import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
st.set_page_config(layout='wide')
latlong = pd.read_csv("district wise centroids.csv")

df = pd.read_csv("final_data.csv")

L  =df['State'].unique().tolist()
L.sort()
L.insert(0,"Overall India")
state_list = L
col_list = ['Population','sex-ratio','Literacy-Rate','Backward Classes','Muslim-Population','Christian-Population','Buddhist-Population','Minorities']

col_list.sort()



#
st.sidebar.title("Indian-Census-Analysis")

state_selected = st.sidebar.selectbox("Select State",state_list)

primary = st.sidebar.selectbox('Select Primary Parameter',col_list )
sec_list = col_list.copy()
sec_list.remove(primary)
secondary = st.sidebar.selectbox('Select Secondary Parameter',sec_list )

btn = st.sidebar.button("Plot Graph")

if btn:
    if  state_selected == "Overall India":

        st.text("Bubble size represent Primary Paramater")
        st.text("Bubble color represent Secondary Paramater")

        fig = px.scatter_mapbox(df, lat='Latitude', lon="Longitude",size = primary, color = secondary, mapbox_style='carto-positron',
                                zoom=3, width = 1500, height = 600, hover_name=df['District'], size_max= 20,color_continuous_scale='plasma')

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.text("Bubble size represent Primary Paramater")
        st.text("Bubble color represent Secondary Paramater")
        new_data = df[df['State'] == state_selected]
        fig = px.scatter_mapbox(new_data, lat='Latitude', lon="Longitude", size=primary, color=secondary,
                                mapbox_style='carto-positron',
                                zoom=5, width=1500, height=600, hover_name=new_data['District'], size_max=35,color_continuous_scale='plasma')

        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.pie(values =new_data['Population'], names= new_data['District'])
        st.plotly_chart(fig2)

