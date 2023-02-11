import sys
top = int(sys.argv[1])
with open("one_col_ingestrtt.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
ingestrtt = [0]*82
for i in range(82):
    ingestrtt[i] = float(line[i])
    
with open("avpn.txt", mode="r", encoding="utf-8") as file:
    vpn = file.read().splitlines()

sortedvpn = [0]*82
sorted_ingestrtt = sorted(ingestrtt)
    
for i in range(top):
    for j in range(82):
        if ingestrtt[j] == sorted_ingestrtt[i]:
            sortedvpn[i] = vpn[j]
for i in range(top): 
    print(sortedvpn[i])

