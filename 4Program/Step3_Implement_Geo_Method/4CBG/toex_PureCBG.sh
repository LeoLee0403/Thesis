echo -n "" > excel.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    echo -n "	$ingest" >> excel.txt 
    echo -n "	" >> excel.txt

done
echo "" >> excel.txt

for ((j=1;j<=81;j++))
do
    for ((i=1;i<=60;i++))
    do
        ingest=$(cat aingest.txt | head -n $i | tail -n 1)
        line=$(cat a_sorted_count_$ingest.txt | head -n $j | tail -n 1)
        echo -n "$line	" >> excel.txt 
    done
    echo "" >> excel.txt
    
done

cat excel.txt > 4CBG.ods