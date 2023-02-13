myfunc()
{
    method=$1
    for ((i=1;i<=60;i++)) # ingest
    do
        ingest=$(cat a_ingest.txt | head -n $i | tail -n 1)
        file=$(ls ../$method/ | grep $ingest.txt)
        vpnlist=$(cat ../${method}/$file | cut -d '|' -f 1) # sorted vpn in a ingest
        ground_truth1=$(cat ground_truth.txt | head -n $i | tail -n 1 | cut -d '|' -f 1)
        ground_truth2=$(cat ground_truth.txt | head -n $i | tail -n 1 | cut -d '|' -f 2)

        for ((j=1;j<=82;j++))
        do
            search_ground_truth=$(echo "$vpnlist" | head -n $j | tail -n 1)
            if [ "$search_ground_truth" == "$ground_truth1" ]; then # find rank difference
                echo "$(($j-1))" >> ${method}_rankdiff.txt
                break
            fi
            if [ "$search_ground_truth" == "$ground_truth2" ]; then # find rank difference
                echo "$(($j-1))" >> ${method}_rankdiff.txt
                break
            fi
        
        done

    done
}

method="1Shotest_ping"
myfunc $method

method="2Geoping"
myfunc $method

method="3Shortest_dist"
myfunc $method

method="4CBG"
myfunc $method

method="5Hybrid1"
myfunc $method

method="6Hybrid2"
myfunc $method

bash performance.sh