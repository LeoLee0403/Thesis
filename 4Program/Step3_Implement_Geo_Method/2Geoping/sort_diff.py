with open("diff.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
diff = [0]*82
for i in range(82):
    diff[i] = float(line[i])

i = 0
with open("avpn.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpn = [0]*82
for i in range(82):
    vpn[i] = line[i]

index_of_diff = [0]*82
for i in range(82):
    index_of_diff[i] = diff[i]

sorted_diff = sorted(diff)
sorted_vpn = [0]*82

for i in range(82):
    for j in range(82):
        if index_of_diff[j] == sorted_diff[i]:
            sorted_vpn[i] = vpn[j]
            print(str(sorted_vpn[i]) + "	" + str(round(float(sorted_diff[i]), 3)))
            break
