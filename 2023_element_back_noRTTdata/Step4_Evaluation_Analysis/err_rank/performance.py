import matplotlib.pyplot as plt
import math

with open("1Shotest_ping_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_shortest_ping = file.read().splitlines()


with open("2Geoping_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_geoping = file.read().splitlines()


with open("3Shortest_dist_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_shortest_dist = file.read().splitlines()


with open("4CBG_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_CBG = file.read().splitlines()


with open("5Hybrid1_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_Hybrid1 = file.read().splitlines()


with open("6Hybrid2_rankdiff.txt", mode="r", encoding="utf-8") as file:
    p_Hybrid2 = file.read().splitlines()

rankdiff_rangemax = 35

method = p_shortest_ping
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1] # start from acc_count[1] = acc_count[1] + acc_count[0]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count1 = count
x1 = [i for i in range(0,rankdiff_rangemax)]
y1 = acc_count_percent


method = p_geoping
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count2 = count
x2 = [i for i in range(0,rankdiff_rangemax)]
y2 = acc_count_percent


method = p_shortest_dist
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count3 = count
x3 = [i for i in range(0,rankdiff_rangemax)]
y3 = acc_count_percent


method = p_CBG
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count4 = count   
x4 = [i for i in range(0,rankdiff_rangemax)]
y4 = acc_count_percent


method = p_Hybrid1
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count5 = count   
x5 = [i for i in range(0,rankdiff_rangemax)]
y5 = acc_count_percent


method = p_Hybrid2
count = [0]* rankdiff_rangemax
for i in range(rankdiff_rangemax):
    count[i] = 0

for i in range(0,rankdiff_rangemax):
    for j in range(60):
        if int(method[j]) == int(i):
            count[i] += 1

acc_count = list(count)
for i in range(1,rankdiff_rangemax):
    acc_count[i] += acc_count[i-1]
acc_count_percent = acc_count
for i in range(0,rankdiff_rangemax):
    acc_count_percent[i] = math.floor(acc_count_percent[i]/60 *100) / 100

count6 = count   
x6 = [i for i in range(0,rankdiff_rangemax)]
y6 = acc_count_percent

# statistic of count
print("\n=========================================")
print("\nThe number of ground truth VPN in each rank difference of each method\n")

print(1,"shortest ping")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count1[i]))
    remainder = remainder - count1[i]
print("rank difference >10 | " + str(remainder))
print("---")

print(2, "GeoPing")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count2[i]))
    remainder = remainder - count2[i]
print("rank difference >10 | " + str(remainder))
print("---")

print(3, "Shortesst Dist")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count3[i]))
    remainder = remainder - count3[i]
print("rank difference >10 | " + str(remainder))
print("---")

print(4, "CBG")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count4[i]))
    remainder = remainder - count4[i]
print("rank difference >10 | " + str(remainder))
print("---")

print(5,"Hybrid1")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count5[i]))
    remainder = remainder - count5[i]
print("rank difference >10 | " + str(remainder))
print("---")

print(6,"Hybrid2")
remainder = 60
for i in range(0,10):
    print("rank difference " + str(i)+ " | " + str(count6[i]))
    remainder = remainder - count6[i]
print("rank difference >10 | " + str(remainder))



# statistic of acc %
print("\n\n=========================================\n")
print("Cumulative probability of rank difference\n")

print(1,"shortest ping")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y1[i]*100)) + "%")
print("---")
print(2, "GeoPing")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y2[i]*100)) + "%")
print("---")
print(3, "Shortesst Dist")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y3[i]*100)) + "%")
print("---")
print(4, "CBG")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y4[i]*100)) + "%")
print("---")
print(5,"Hybrid1")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y5[i]*100)) + "%")
print("---")
print(6,"Hybrid2")
for i in range(0,10):
    print("rank difference 0 ~ " + str(i)+ " | " + str(int(y6[i]*100)) + "%")

# # plot CDF

# plt.plot(x1, y1, label="Shortest_Ping")
# plt.plot(x2, y2, label="GeoPing")
# plt.plot(x3, y3, label="Shortest_Dist")
# plt.plot(x4, y4, label="CBG")
# plt.plot(x5, y5, label="Hybrid1")
# plt.plot(x6, y6, label="Hybrid2")


# plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ,1])  
# plt.xlabel("Rank Difference") 
# plt.ylabel("CDF") 
# # plt.grid(True)
# plt.legend(loc = "lower right")
# plt.show() 





