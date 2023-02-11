

with open("my_dist_rank.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
dist_rank = float(line[0])


with open("my_cover_rank.txt", mode="r", encoding="utf-8") as file:
    line = file.read().splitlines()
cover_rank = float(line[0])

switch_dist = {
1 : 100,
2 : 90,
3 : 80,
4 : 77,
5 : 74,
6 : 71,
7 : 69,
8 : 67,
9 : 65,
10 : 62,
11 : 61,
12 : 60,
13 : 59,
14 : 58,
15 : 57,
16 : 56,
17 : 55,
18 : 54,
19 : 53,
20 : 52,
21 : 51,
22 : 50,
23 : 49,
24 : 48,
25 : 47,
26 : 46,
27 : 45,
28 : 44,
29 : 43,
30 : 42


}

switch_cover = {


1 : 100,
2 : 95,
3 : 90,
4 : 87,
5 : 84,
6 : 81,
7 : 79,
8 : 77,
9 : 75,
10 : 72,
11 : 71,
12 : 70,
13 : 69,
14 : 68,
15 : 67,
16 : 66,
17 : 65,
18 : 64,
19 : 63,
20 : 62,
21 : 61,
22 : 60,
23 : 59,
24 : 58,
25 : 57,
26 : 56,
27 : 55,
28 : 54,
29 : 53,
30 : 52,
}

if dist_rank <= 30:
    point_dist = switch_dist[dist_rank]
else:
    point_dist = 0

if cover_rank <= 30:
    point_cover = switch_cover[cover_rank]
else:
    point_cover = 0

point = point_dist + point_cover
print(point)