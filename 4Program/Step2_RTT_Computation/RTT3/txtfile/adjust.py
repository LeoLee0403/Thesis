import sys

with open("min.txt", mode="r", encoding="utf-8") as file:
    min = float(file.read())
with open("minrtt_lessthan_zero.txt", mode="r", encoding="utf-8") as file:
    adjust_value = float(file.read())

rtt = float(sys.argv[1])
RTT1 = float(sys.argv[2])

if rtt == "None":
    print("None")
elif rtt == 0:
    print(0)
else:
    rtt = rtt
    RTT1 = RTT1
    rtt = rtt - RTT1 # minus RTT1
    rtt = rtt - adjust_value # eliminate negative rtt
    print(round(rtt,3))