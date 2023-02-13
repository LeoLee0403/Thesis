echo -n "" > point.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    point=$(cat a_point_${ingest}.txt | head -n 81)
    cover_count=$(cat count_${ingest}.txt | cut -d '|' -f 2)
    echo "$point" >> point.txt
    echo "$cover_count" >> cover_count.txt
    python3 aa_sort_point_for_pureCBG.py > a_sorted_count_${ingest}.txt
    echo -n "" > point.txt
    echo -n "" > cover_count.txt
done