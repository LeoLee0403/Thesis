echo -n "" > dist.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    dist=$(cat predict_${ingest}_dist.txt | head -n 81)
    echo "$dist" >> dist.txt
    python3 sort_dist.py > a_sorted_${ingest}.txt
    echo -n "" > dist.txt
done