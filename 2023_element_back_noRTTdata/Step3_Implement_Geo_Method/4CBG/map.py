import folium
import numpy as np


i = 0
lat = np.zeros(83)
with open("lat.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        lat[i] = float(line)
        i += 1

i = 0
long = np.zeros(83)
with open("long.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        long[i] = float(line)
        i += 1

i = 0
location_name = [0]*83
with open("location_name.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(83):
    location_name[i] = line[i]

# =====================================================================

i = 0
avpns_lat = np.zeros(81)
with open("avpns_lat.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        avpns_lat[i] = float(line)
        i += 1

i = 0
avpns_long = np.zeros(81)
with open("avpns_long.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        avpns_long[i] = float(line)
        i += 1

i = 0
predict_as_radius = np.zeros(81)
with open("predict_as_radius.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        predict_as_radius[i] = float(line)
        i += 1

i = 0
avpns_location_name = [0]*81
with open("avpns.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(81):
    avpns_location_name[i] = line[i]

m = folium.Map(location=[0,0], tiles='openstreetmap',zoom_start=3, min_zoom=3, max_zoom=10, zoom_control='True')

for i in range(83): # point
    folium.Circle(location=[lat[i], long[i]],
        color='#d2691e', # Circle 顏色
        radius=10000, # Circle 寬度
        tooltip=location_name[i], # 彈出視窗內容
        fill=True, # 填滿中間區域
        fill_opacity=0.5 # 設定透明度
    ).add_to(m)


for i in range(81):
    if predict_as_radius[i] > 2000:
        continue
    folium.Circle(
        radius = predict_as_radius[i]*1000, # meters
        location=[avpns_lat[i],avpns_long[i]],
        tooltip=avpns_location_name[i],
        color='gray',
        fill_opacity=0.055,
        fill=True,
    ).add_to(m)


with open("now_ingest.txt", mode="r", encoding="utf-8") as file:
    ingest = file.read().splitlines()
m.save("map_" + str(ingest[0]) + ".html")