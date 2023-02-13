from types import coroutine
import numpy as np
import math
        
# parsed timestamp
with open("ltime_ping.txt", mode="r", encoding="utf-8") as file:
    t = file.read()
line_count = len(open(r"ltime_ping.txt",'r').readlines())
time = np.zeros(line_count)
    
# whichone  >
whichone = [None]*line_count
with open("long_ping_which.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for k in range(line_count):
    whichone[k] = line[k]

# > whichonelatter
whichonelatter = [None]*line_count
with open("long_beping_which.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for k in range(line_count):
    whichonelatter[k] = line[k]

# timestamp
i = 0
times_tamp = [None]*line_count
with open("lping_timestamp.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
    times_tamp = line

i = 0
j = 0

bias = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001
while i <= len(t)-12:
     time[j] = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001 - bias  
     i += 12
     j += 1

with open("vpn1ip_behost.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpn1ip_behost = line[0]

with open("vpn2ip.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
vpn2ip = line[0]

pingseq = [None]*line_count
with open("pingseq.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for k in range(line_count):
    pingseq[k] = line[k]

finaltimestamp = [None]*line_count

output = np.zeros(int(line_count))


# Run, Compute RTT
j = 0
for i in range(0,line_count-1):
    if whichone[i] == vpn1ip_behost and whichonelatter[i] == vpn2ip: # VP_VPN > LM_VPN
        if whichone[i+1] == vpn2ip and whichonelatter[i+1] == vpn1ip_behost and pingseq[i] == pingseq[i+1]: # LM_VPN > VP_VPN
            if (time[i+1] - time[i]) > 0:
                output[j] = time[i+1] - time[i] # get RTT
                finaltimestamp[j] = times_tamp[i] # get timestamp
                j += 1
    else:
        continue 
count = j

# min 
tempt = np.zeros(count)
for i in range(count):
    tempt[i] = output[i]
minimum = min(tempt)

# output minimum RTT
min = 100000
for i in range(0, count):
    if output[i] < min:
        min = output[i]
    with open("avpnping.txt", mode="a", encoding="utf-8") as file:
        file.write("Time = " + finaltimestamp[i] + "  RTT = " + str(output[i]*1000) + "\n")

with open("a_minRTT.txt", mode="w", encoding="utf-8") as file:
    file.write(str(min*1000) + "\n")
