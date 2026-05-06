import streamlit as st
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
from lista_paises import city_info

st.sidebar.header("Controles")
cities = st.sidebar.radio("Choose a city", list(city_info.keys()))
zoom_btn = st.sidebar.button("Zoom na coordenada")

lat = city_info[cities]["lat"]
lon = city_info[cities]["long"]

st.title(f"Exploring {cities}")

# This creates a dedicated section for the text
with st.container():
    st.subheader("About the City")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write(city_info[cities]["desc"])

    with col2:
        st.image(city_info[cities]["img"], use_container_width=True)
    st.divider()  # Adds a clean horizontal line

m = leafmap.Map(center=[lat, lon], zoom=7)

if zoom_btn:
    m.set_center(lon, lat, zoom=10)

m.add_marker(location=[lat, lon], popup="Coordenada selecionada")
m.to_streamlit(height=500)
