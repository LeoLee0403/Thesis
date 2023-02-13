
i = 0
with open("dist.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
dist = [0]*81
for i in range(81):
    dist[i] = float(line[i])

i = 0
with open("avpns.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpn = [0]*81
for i in range(81):
    vpn[i] = line[i]


index_of_dist = [0]*81
for i in range(81):
    index_of_dist[i] = dist[i]


sorted_dist = sorted(dist)
sorted_vpn = [0]*81

for i in range(81):
    for j in range(81):
        if index_of_dist[j] == sorted_dist[i]:
            sorted_vpn[i] = vpn[j]
            # print(str(sorted_vpn[i]) + "	" + str(i+1))
            break

for j in range(81):
    for i in range(81):
        if index_of_dist[j] == sorted_dist[i]:
            print(str(i+1))