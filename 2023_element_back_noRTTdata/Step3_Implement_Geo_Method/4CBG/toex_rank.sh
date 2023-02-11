echo -n "" > excel_rank.txt 
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    echo -n "	$ingest" >> excel_rank.txt  
    # echo -n "	" >> excel_rank.txt  
done
echo "" >> excel_rank.txt 

for ((j=1;j<=81;j++))
do
    for ((i=1;i<=60;i++))
    do
        ingest=$(cat aingest.txt | head -n $i | tail -n 1)
        line=$(cat a_cover_rank_$ingest.txt | head -n $j | tail -n 1)
        echo -n "$line	" >> excel_rank.txt  
    done
    echo "" >> excel_rank.txt 
    
done