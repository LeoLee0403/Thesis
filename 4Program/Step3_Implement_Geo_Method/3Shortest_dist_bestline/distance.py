import sys
from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):

    # decimal to radian
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # earth ave radius
    return c * r 
lat1 = float(sys.argv[1])
lon1 = float(sys.argv[2])
lat2 = float(sys.argv[3])
lon2 = float(sys.argv[4])

distance = haversine(lat1, lon1, lat2, lon2)
print(str(int(distance)) +  "|" + str(lat1) +  "|" + str(lon1) +  "|" + str(lat2) +  "|" + str(lon2))
