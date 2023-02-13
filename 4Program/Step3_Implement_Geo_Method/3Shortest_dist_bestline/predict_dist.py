import errno
import matplotlib.pyplot as plt   
import numpy as np
import sys

vpn = (sys.argv[1])
target_rtt= float(sys.argv[2]) # can change

# read
with open("xdist_" + vpn + ".txt", mode="r", encoding="utf-8") as file:
    xdist = file.read().splitlines()
    
with open("yrtt_" + vpn + ".txt", mode="r", encoding="utf-8") as file:
    yrtt = file.read().splitlines()

x = [0] * len(xdist)
y = [0] * len(xdist)
for i in range(len(xdist)):
    x[i] = float(xdist[i])
    y[i] = float(yrtt[i])
    
# ==========================================================================
# find bestline

# initial
min_err_sum = 10000000
b = 0
m = 0
node = 0
get_the_node = 0
final_b = 0
final_m = 0
final_node = 0
final_min_err = 0

flag_yrtt_lt_zero = 0
while b <= 400:
    if flag_yrtt_lt_zero == 1:
        break
    for i in range(len(xdist)): # choose ith node for compute m
        get_the_node = 0
        if y[i] < 20: 
            flag_yrtt_lt_zero = 1
            continue
        m = (y[i] - b) / x[i]
        if m < 0: # m < 0, invalid
            continue

        err_sum = 0
        for j in range(len(xdist)): 
            yhat = m * x[j] + b
            if float(y[j]) <= 20: 
                flag_yrtt_lt_zero = 1
                continue
            err = y[j] - yhat
            if err < -0.0001: # the line is not below all nodes
                break
            err_sum += err

            if j == len(xdist) - 1:
                # only one node can pass
                get_the_node = 1
                node = i
                break
        if get_the_node == 1:
            break

    if get_the_node == 1:
        if err_sum < min_err_sum:
            min_err_sum = err_sum
            final_b = b
            final_m = m
            final_node = node
            final_min_err = min_err_sum
    b += 0.1

# ==========================================================================
# Predict the distance here for CBG

if target_rtt < 0.1:
    target_rtt = 0.1

taget_distance_prediction = (target_rtt - final_b) / final_m
print(taget_distance_prediction)

