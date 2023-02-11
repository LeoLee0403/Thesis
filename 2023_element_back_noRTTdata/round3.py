import sys
rtt = sys.argv[1]
if rtt == "None":
    print("None")
elif rtt == 0:
    print(0)
else:
    rtt = float(rtt)
    print(round(rtt, 3))