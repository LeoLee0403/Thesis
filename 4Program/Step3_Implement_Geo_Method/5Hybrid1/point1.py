

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