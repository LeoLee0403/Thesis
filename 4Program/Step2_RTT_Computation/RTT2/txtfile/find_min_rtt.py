import sys

with open("min.txt", mode="r", encoding="utf-8") as file:
    min = float(file.read())

rtt = float(sys.argv[1])
RTT1 = float(sys.argv[2])
i = int(sys.argv[3])

if rtt == "None":
    pass
else:
    rtt = rtt
    RTT1 = RTT1
    rtt = rtt - RTT1
    if rtt < min:
        with open("min.txt", mode="w", encoding="utf-8") as file:
            file.write(str(rtt))

if i == 60:
    with open("min.txt", mode="r", encoding="utf-8") as file:
        min = float(file.read())
    with open("minrtt_lessthan_zero.txt", mode="w", encoding="utf-8") as file:
        file.write(str(min))