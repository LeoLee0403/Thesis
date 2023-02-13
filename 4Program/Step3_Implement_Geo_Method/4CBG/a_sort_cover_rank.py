with open("cover.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
cover = [0]*81
for i in range(81):
    cover[i] = int(line[i])

rank = [1] * 81
for i in range(81):
    for j in range(81):
        if cover[i] < cover[j]:
            rank[i] += 1
    print(rank[i])


