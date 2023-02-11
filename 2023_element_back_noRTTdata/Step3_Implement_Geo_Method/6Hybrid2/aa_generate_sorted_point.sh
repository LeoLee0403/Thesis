echo -n "" > point.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    point=$(cat a_point_${ingest}.txt | head -n 81)
    echo "$point" >> point.txt
    python3 aa_sort_point.py > a_sorted_point_${ingest}.txt
    echo -n "" > point.txt
done