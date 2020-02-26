import folium
import  time
import numpy as np
import pandas as pd
import webbrowser
from folium.plugins import HeatMap

posi = pd.read_excel("Cities2015.xlsx")
posi = posi.dropna()

lat = np.array(posi["lat"][0:len(posi)])
lon = np.array(posi["lon"][0:len(posi)])
pop = np.array(posi["pop"][0:len(posi)],dtype=float)
gdp = np.array(posi["GDP"][0:len(posi)],dtype=float)
data1 = [[lat[i],lon[i],pop[i]] for i in range(len(posi))]

map_osm = folium.Map(location=[35,110],zoom_start=5)
HeatMap(data1).add_to(map_osm) 
file_path = "map4.html"
map_osm.save(file_path)   #保存本地
webbrowser.open(file_path) #在本地浏览器打开
