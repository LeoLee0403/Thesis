with open("one_col_ingestrtt.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
ingestrtt = [0]*82
for i in range(82):
    ingestrtt[i] = float(line[i])
    

with open("avpn.txt", mode="r", encoding="utf-8") as file:
    vpn = file.read().splitlines()


sortedvpn = [0]*82  

sorted_ingestrtt = sorted(ingestrtt)

vpnflag = [0]*82
for i in range(82):
    vpnflag[i] = 0

for i in range(82):
    for j in range(82):
        if ingestrtt[j] == sorted_ingestrtt[i]:
            if vpnflag[j] == 0:
                sortedvpn[i] = vpn[j]
                vpnflag[j] = 1 # vpn[j] has been chosen
                break


for i in range(82): 
    print(str(sortedvpn[i]) + "	" + str(sorted_ingestrtt[i]))

