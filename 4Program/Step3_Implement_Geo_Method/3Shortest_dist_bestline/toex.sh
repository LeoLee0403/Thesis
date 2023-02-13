
echo -n "" > dist_rank.txt

for ((j=1;j<=81;j++))
do
    for ((i=1;i<=60;i++))
    do
        ingest=$(cat aingest.txt | head -n $i | tail -n 1)
        line=$(cat a_rank_$ingest.txt | head -n $j | tail -n 1)
        echo -n "$line" >> dist_rank.txt 
        if [ $i != 60 ]; then
            echo -n "|" >> dist_rank.txt 
        fi
    done
    echo "" >> dist_rank.txt
    
done