# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:04:37 2020

@author: dr.rakibulhasan@gmail.com
"""

## Application Web-Map
import pandas as pd
import folium

## Adding Volcano Locations
data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Dynamic Coloring based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
# for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(el) + " m", 
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))

# Adding Geo Json object
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("world.json", mode="r", encoding='utf-8-sig').read())))



# map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a marker", icon=folium.Icon(color="green")))
# Adding Layer Control
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")

