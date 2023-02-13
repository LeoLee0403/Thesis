import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

with open("err_dist_1Shotest_ping.txt", mode="r", encoding="utf-8") as file:
    err_shortest_ping = file.read().splitlines()


with open("err_dist_2Geoping.txt", mode="r", encoding="utf-8") as file:
    err_geoping = file.read().splitlines()


with open("err_dist_3Shortest_dist.txt", mode="r", encoding="utf-8") as file:
    err_shortest_dist = file.read().splitlines()


with open("err_dist_4CBG.txt", mode="r", encoding="utf-8") as file:
    err_cbg = file.read().splitlines()


with open("err_dist_5Hybrid1.txt", mode="r", encoding="utf-8") as file:
    err_Hybrid1 = file.read().splitlines()


with open("err_dist_6Hybrid2.txt", mode="r", encoding="utf-8") as file:
    err_Hybrid2 = file.read().splitlines()

rangemax = 6000

method = err_shortest_ping
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1


acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count1 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x1 = [i for i in range(rangemax)]
y1 = acc_count_percent


method = err_geoping    
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count2 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x2 = [i for i in range(rangemax)]
y2 = acc_count_percent


method = err_shortest_dist
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count3 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x3 = [i for i in range(rangemax)]
y3 = acc_count_percent


method = err_cbg
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count4 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x4 = [i for i in range(rangemax)]
y4 = acc_count_percent


method = err_Hybrid1
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count5 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x5 = [i for i in range(rangemax)]
y5 = acc_count_percent


method = err_Hybrid2
count = [0]* rangemax
for i in range(rangemax):
    count[i] = 0

for i in range(rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rangemax):
    acc_count[i] += acc_count[i-1]
acc_count6 = list(acc_count)
acc_count_percent = list(acc_count)
for i in range(rangemax):
    acc_count_percent[i] = acc_count_percent[i]/60
    
x6 = [i for i in range(rangemax)]
y6 = acc_count_percent

err_dist_range = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 5000]

# statistic of count
print("\n=========================================")
print("\nThe number of mapping in different error distance range of each method\n")

value = [0] * 15
print(1, "shortest ping")

j = 0
for i in err_dist_range:
    value[j] = acc_count1[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count1[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))
print("---")

print(2, "GeoPing")
j = 0
for i in err_dist_range:
    value[j] = acc_count2[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count2[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))
print("---")

print(3, "Shortesst Dist")
j = 0
for i in err_dist_range:
    value[j] = acc_count3[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count3[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))
print("---")

print(4, "CBG")
j = 0
for i in err_dist_range:
    value[j] = acc_count4[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count4[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))
print("---")

print(5,"Hybrid1")
j = 0
for i in err_dist_range:
    value[j] = acc_count5[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count5[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))
print("---")

print(6,"Hybrid2")
j = 0
for i in err_dist_range:
    value[j] = acc_count6[i]
    j = j + 1
for i in range(0, 15):
    if i == 0:
        print("error distance 0 | " + str(acc_count6[0]))
    elif i == 1:
        print("error distance 50 ~ 100 | " + str(value[i]-value[i-1]))
    elif i ==14:
        print("error distance > 3000 | " + str(value[i]-value[i-1]))
    else:
        print("error distance " + str(err_dist_range[i-1]) + " ~ " + str(err_dist_range[i]) + " | " + str(value[i]-value[i-1]))


# statistic of acc %

print("\n\n=========================================\n")
print("Cumulative probability of error distance\n")

err_dist_range2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000]
print(1, "shortest ping")
print("error distance 0" + " | " + str(int(y1[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y1[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y1[5000]*100)) + "%")
print("---")

print(2, "GeoPing")
print("error distance 0" + " | " + str(int(y2[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y2[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y2[5000]*100)) + "%")
print("---")

print(3, "Shortesst Dist")
print("error distance 0" + " | " + str(int(y3[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y3[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y3[5000]*100)) + "%")
print("---")


print(4, "CBG")
print("error distance 0" + " | " + str(int(y4[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y4[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y4[5000]*100)) + "%")
print("---")

print(5,"Hybrid1")
print("error distance 0" + " | " + str(int(y5[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y5[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y5[5000]*100)) + "%")
print("---")

print(6,"Hybrid2")
print("error distance 0" + " | " + str(int(y6[0]*100)) + "%")
for i in err_dist_range2:
    print("error distance 0 ~ " +  str(i)+ " | " + str(int(y6[i]*100)) + "%")
print("error distance > 3000" +  " | " + str(int(y6[5000]*100)) + "%")


# plot CDF
yy1 = [y1[0], y1[100], y1[200], y1[300], y1[400], y1[500], y1[600], y1[700], y1[800], y1[900], y1[1000], y1[1500], y1[2000], y1[3000], 1]
yy2 = [y2[0], y2[100], y2[200], y2[300], y2[400], y2[500], y2[600], y2[700], y2[800], y2[900], y2[1000], y2[1500], y2[2000], y2[3000], 1]
yy3 = [y3[0], y3[100], y3[200], y3[300], y3[400], y3[500], y3[600], y3[700], y3[800], y3[900], y3[1000], y3[1500], y3[2000], y3[3000], 1]
yy4 = [y4[0], y4[100], y4[200], y4[300], y4[400], y4[500], y4[600], y4[700], y4[800], y4[900], y4[1000], y4[1500], y4[2000], y4[3000], 1]
yy5 = [y5[0], y5[100], y5[200], y5[300], y5[400], y5[500], y5[600], y5[700], y5[800], y5[900], y5[1000], y5[1500], y5[2000], y5[3000], 1]
yy6 = [y6[0], y6[100], y6[200], y6[300], y6[400], y6[500], y6[600], y6[700], y6[800], y6[900], y6[1000], y6[1500], y6[2000], y6[3000], 1]

x1 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]
x2 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]
x3 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]
x4 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]
x5 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]
x6 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 3100]

plt.plot(x1, yy1, label="Shortest_Ping")
plt.plot(x2, yy2, label="GeoPing")
plt.plot(x3, yy3, label="Shortest_Dist")
plt.plot(x4, yy4, label="CBG")
plt.plot(x5, yy5, label="Hybrid1")
plt.plot(x6, yy6, label="Hybrid2")


plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ,1])  
plt.xlabel("Error Distance") 
plt.ylabel("CDF") 
# plt.grid(True)
plt.legend(loc = "lower right")
plt.show() 




