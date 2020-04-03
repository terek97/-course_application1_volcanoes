import folium
import pandas

map = folium.Map(location=[38.798510, -104.787883], zoom_start=5)    
fg = folium.FeatureGroup(name="My Map")

db = pandas.read_csv("volcanoes.txt")
coordinates = db.iloc[:,-2:]

count = 0
while count < len(coordinates):
    fg.add_child(folium.Marker(location=[coordinates.LAT[count], coordinates.LON[count]], popup="ВУЛКАН", icon=folium.Icon(color='red')))
    count = count + 1
map.add_child(fg)
map.save("map1.html")





