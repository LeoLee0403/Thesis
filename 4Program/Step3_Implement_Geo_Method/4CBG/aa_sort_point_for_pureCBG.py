
i = 0
with open("point.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
point = [0]*81
for i in range(81):
    point[i] = float(line[i])

with open("cover_count.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
cover_count = [0]*81
for i in range(81):
    cover_count[i] = float(line[i])

i = 0
with open("avpns.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpn = [0]*81
for i in range(81):
    vpn[i] = line[i]


index_of_point = [0]*81
for i in range(81):
    index_of_point[i] = point[i]

point_copy = point
sorted_point = [0]*81
sorted_cover_count = [0]*81
sorted_vpn = [0]*81
max = -1
max_vpn = ""
reset_point = 0
for i in range(81):
    for j in range(81):
        if point_copy[j] > max:
            max = point_copy[j]
            max_cover_count = cover_count[j]
            max_vpn = vpn[j]
            reset_point = j
    sorted_point[i] = max
    sorted_cover_count[i] = max_cover_count
    sorted_vpn[i] = max_vpn
    point_copy[reset_point] = -1
    max = -1
    print(str(sorted_vpn[i]) + "	" + str(int(sorted_cover_count[i])))


            



