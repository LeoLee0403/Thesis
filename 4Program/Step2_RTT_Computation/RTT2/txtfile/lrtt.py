
from os import times
import numpy as np
import math

line_count = len(open(r"seq_acktime.txt",'r').readlines())

# tun0ip
with open("tun0ip.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
tun0ip = line[0]

# tun0ip_or_ingestip
tun0ip_or_ingestip = [None]*line_count
with open("tun0ip_or_ingestip.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(line_count):
    tun0ip_or_ingestip[i] = line[i]

# timestamp
timestamp = [None]*line_count
with open("timestamp.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(line_count):
    timestamp[i] = line[i]

# seq_acktime
with open("seq_acktime.txt", mode="r", encoding="utf-8") as file:
    seq_acktime = file.read()

# seq_or_ack
seq_or_ack = [None]*line_count
with open("seq_or_ack.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(line_count):
    seq_or_ack[i] = line[i]

# seq_acknum
seq_acknum = [None]*line_count
with open("seq_acknum.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
for i in range(line_count):
    seq_acknum[i] = line[i]

# acc_time
time = np.zeros(line_count)
t = seq_acktime
i = 0
j = 0
bias = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001

while i <= len(t)-12:
     time[j] = (float(t[i])*10 + float(t[i+1]))*60 + float(t[i+2])*10 + float(t[i+3]) + float(t[i+5])*0.1 + float(t[i+6])*0.01 + float(t[i+7])*0.001 + float(t[i+8])*0.0001 + float(t[i+9])*0.00001 + float(t[i+10])*0.000001 - bias  
     i += 12
     j += 1

# queue
queue = [None]*line_count
for i in range(line_count):
    queue[i] = -1 # empty

# retransmission record
retransmission_num = [None]*line_count
for i in range(line_count):
    retransmission_num[i] = 0

count = 0
output_rtt = [None]*line_count
for i in range(line_count):
    output_rtt[i] = 1000000    

output_timestamp = [None]*line_count
for i in range(line_count):
    output_timestamp[i] = -1  


# Run
re_flag = 0
point_start = 0 # ack packet will check the seqnum in point_start ~ point_now
for point_now in range(line_count):
    if seq_or_ack[point_now] == "seq": # this packet is seq
        if tun0ip_or_ingestip[point_now] == tun0ip: # VPN_ip > ingest_ip
            for i in range(point_start, point_now): # detect retransmission
                if queue[i] == seq_acknum[point_now]: # the same seqnum as prior packet, retransmission occur
                    retransmission_num[i] = -1 # mark the packet to be retransmission (invalid)
                    retransmission_num[point_now] = -1 # mark the packet to be retransmission (invalid)
                    re_flag = 1
                    break
            if re_flag == 1: # retransmission
                re_flag = 0 # reset re_flag
                continue # discard this packet
            queue[point_now] = seq_acknum[point_now] # no retransmission, add seqnum to queue
    else: # this packet is ack
        if tun0ip_or_ingestip[point_now] != tun0ip: # ingest_ip > VPN_ip
            for i in range(point_start, point_now): # ack packet check
                if queue[i] == seq_acknum[point_now]: # find the pair: seqnum = acknum
                    if time[point_now]-time[i] > 0 and retransmission_num[i] != -1: # valid seq packet
                        # change starting check pointer
                        j = i
                        j = j + 1
                        j_is_larger = 0
                        while (queue[j] == -1): # queue[j] empty
                            j = j + 1
                            if j >= point_now:
                                j_is_larger = 1  # from i+1 to point_now are empty or invalid, no need to check these seqnum
                                break
                        if j_is_larger == 1:
                            point_start = point_now # if from i+1 to point_now are empty or invalid, then point_start jump to point_now
                            j_is_larger = 0    
                        else:
                            point_start = j # find queue[j] != -1, seqnum exist, set the point_start to j
                        # set output
                        output_rtt[count] = time[point_now]-time[i]
                        output_timestamp[count] = timestamp[i]
                    count = count + 1

temp_output = sorted(output_rtt)
for i in range(2):
    temp_output[i] = 10000
sorted_output = sorted(temp_output)

minimum = min(sorted_output)*1000

# list all the rtt
for i in range(0, count): 
    with open("THIS_rtt_result.txt", mode="a", encoding="utf-8") as file:
        file.write("Time = " + str(output_timestamp[i]) + "  RTT = " + str(output_rtt[i]*1000) + "\n")

# list min
with open("vpn_ingest.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
ingest = line[0]

with open("THIS_rtt_result.txt", mode="a", encoding="utf-8") as file:
    file.write(ingest + " | " + str(minimum) + "\n")


