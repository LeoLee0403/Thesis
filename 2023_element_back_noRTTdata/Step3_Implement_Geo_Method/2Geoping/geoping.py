import math
import sys
top = int(sys.argv[1])

topvpn = [0]*top
ingestrtt = [0]*top
for i in range(top):
    topvpn[i] = sys.argv[i+2]
j = 0
for i in range(top, top*2):
    ingestrtt[j] = float(sys.argv[i+2])
    j += 1

with open("avpn.txt", mode="r", encoding="utf-8") as file:
    vpn = file.read().splitlines()

with open("one_col_vpnrtt.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpnrtt = [0]*82
for i in range(82):
    vpnrtt[i] = float(line[i])

# Compute Euclidean Distance
sum = 0
for i in range(top): 
    for j in range(82):
        if vpn[j] == topvpn[i]:
            sum += (abs(ingestrtt[i] - vpnrtt[j]))**2
sum = sum ** (0.5)
print(sum)
