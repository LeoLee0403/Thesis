echo -n "" > excel_dist.txt
for ((i=1;i<=60 ;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    echo -n "	$ingest" >> excel_dist.txt 
    echo -n "	" >> excel_dist.txt 
done
echo "" >> excel_dist.txt

for ((j=1;j<=81;j++))
do
    for ((i=1;i<=60;i++))
    do
        ingest=$(cat aingest.txt | head -n $i | tail -n 1)
        line=$(cat a_sorted_$ingest.txt | head -n $j | tail -n 1)
        echo -n "$line	" >> excel_dist.txt 
    done
    echo "" >> excel_dist.txt
    
done

cat excel_dist.txt > 3Shortest_dist.ods
