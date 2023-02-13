echo -n "" > cover.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    cover=$(cat count_${ingest}.txt | head -n 81 | cut -d '|' -f 2)
    echo "$cover" >> cover.txt
    python3 a_sort_cover_rank.py > a_cover_rank_${ingest}.txt
    echo -n "" > cover.txt
done