import folium
import pandas

db = pandas.read_csv("volcanoes.txt")
lat = list(db["LAT"])
lon = list(db["LON"])
name = list(db["NAME"])
elev = list(db["ELEV"])

def color_maker (elevation):
    if elevation < 1500:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.798510, -104.787883], zoom_start=5, tiles = "Stamen Terrain")    
fg = folium.FeatureGroup(name="My Map")

html = """<h4>Volcano information:</h4>
Volcano name: %s \n
Height: %s m
"""

for lt, ln, na, el in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (na, str(el)), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), 
    fill_color=color_maker(el), fill_opacity = 0.9))

map.add_child(fg)
map.save("map1.html")





