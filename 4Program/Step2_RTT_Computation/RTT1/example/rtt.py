from types import coroutine
import numpy as np
import sys

host_ip = sys.argv[1]
vpn = sys.argv[2]

with open("ltime_ping.txt", mode="r", encoding="utf-8") as file:
    t = file.read()
line_count = len(open(r"ltime_ping.txt",'r').readlines())
time = np.zeros(line_count)

# which one ping: xxxx >
whichone = [None]*line_count
with open("long_ping_which.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for k in range(line_count):
    whichone[k] = line[k]

pingseq = [None]*line_count
with open("pingseq.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for k in range(line_count):
    pingseq[k] = line[k]

times_tamp = [None]*line_count
with open("lping_timestamp.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
    times_tamp = line

# set time start at 0s
i = 0
j = 0
bias = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001
while i <= len(t)-12:
     time[j] = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001 - bias  
     i += 12
     j += 1

j = 0
finaltimestamp = [None]*line_count
output = np.zeros(int(line_count))

for i in range(line_count-1):
    if whichone[i] == host_ip: # host > vpn
        if whichone[i+1] != host_ip: # vpn > host
            if pingseq[i] == pingseq[i+1]: # the same seq
                if (time[i+1] - time[i]) > 0:
                    output[j] = time[i+1] - time[i]
                    finaltimestamp[j] = times_tamp[i]
                    j += 1
rtt_count = j

# rearrange list size
arranged_output = np.zeros(rtt_count)
for i in range(rtt_count):
    arranged_output[i] = output[i]
min_rtt = min(arranged_output)

for i in range(rtt_count):
    print(finaltimestamp[i], "| RTT =", round(arranged_output[i]*1000, 3), "ms |", vpn)
print("min_rtt =", round(min_rtt*1000, 3), "ms |", vpn)
print("\n---------------------------------------\n")
