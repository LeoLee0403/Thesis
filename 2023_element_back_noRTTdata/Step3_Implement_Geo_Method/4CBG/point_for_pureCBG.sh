for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    for ((j=1;j<=81;j++))
    do
        dist_rank=$(cat dist_rank.txt | head -n $j | tail -n 1 | cut -d '|' -f $i)
        cover_rank=$(cat cover_rank.txt | head -n $j | tail -n 1 | cut -d '|' -f $i)
        
        echo "$dist_rank" > my_dist_rank.txt
        echo "$cover_rank" > my_cover_rank.txt
        point=$(python3 point_for_pureCBG.py)
        echo "$point" >> a_point_${ingest}.txt
    done
done

