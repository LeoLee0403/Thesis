import numpy as np

# import latitude_longitude
line_count = len(open("lat_long.txt", mode="r" ,encoding="utf-8").readlines())
i = 0
lat_long = np.zeros(line_count)
with open("lat_long.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        lat_long[i] = float(line)
        i += 1

# create latitude array and longitude array 
half_line_count = int(line_count/2)
lat = np.zeros(half_line_count)
long = np.zeros(half_line_count)

j = 0
for i in range(0, line_count, 2):
    lat[j] = lat_long[i]
    long[j] = lat_long[i+1]
    j += 1

# import country
i = 0
country = [0]*half_line_count
with open("country.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()

for i in range(0, half_line_count):
    country[i] = line[i]

# import city
i = 0
city = [0]*half_line_count
with open("city.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()

for i in range(0, half_line_count):
    city[i] = line[i]

# server_count
server_count = [0]*100
for i in range(100):
    server_count[i] = 0

# import domain
i = 0
domain = [0]*half_line_count
with open("domain.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()

for i in range(0, half_line_count):
    domain[i] = line[i]



# Two-dimensional array
data = [[0]*800 for i in range(100)]
for i in range(100):
    for j in range(800):
        data[i][j] = -1
flag = 0
for i in range(0, half_line_count): # scan
    for j in range(100): # Two-dimensional array
        if data[j][0] == -1 and data[j][1] == -1: # match is impossible/repeat, break.
            break
        if lat[i] == data[j][0] and long[i] == data[j][1]: # repeat location
            flag = 1 # find repeat
            k = 6 # 
            while(data[j][k] != -1): # exist a domain in data[j][k]
                k += 1

            data[j][k] = domain[i] # put domain[i] in data[j][k]
            server_count[j] += 1
            break
    if flag != 1: # not repeat, first domain insert to the entry
        for m in range(100):
            if data[m][0] == -1 and data[m][1] == -1: # empty, then set
                data[m][0] = lat[i]
                data[m][1] = long[i]
                data[m][2] = country[i]
                data[m][3] = city[i]
                data[m][6] = domain[i]
                server_count[m] += 1
                break
    else:
        flag = 0 # reset flag

# server count
for i in range(100):
    data[i][5] = server_count[i]


for i in range(100):
    if data[i][0] == -1:
        break
    print("")
    print("")
    print("count", i+1 , end=": ")
    for j in range(800):
        if data[i][j] != -1:
            print(data[i][j], end=", ")