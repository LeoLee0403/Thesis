myfunc()
{
    method=$1
    total_dist=0
    for ((i=1;i<=60;i++)) # ingest
    do
        ingest=$(cat a_ingest.txt | head -n $i | tail -n 1)
        file=$(ls ../$method/ | grep $ingest.txt)
        mapped_vpn=$(cat ../${method}/$file | cut -d '|' -f 1 | head -n 1) # sorted vpn in a ingest

        ground_truth1=$(cat ground_truth.txt | head -n $i | tail -n 1 | cut -d '|' -f 1)
        ground_truth2=$(cat ground_truth.txt | head -n $i | tail -n 1 | cut -d '|' -f 2)

        min=1000000
        dist1=$(cat nord_distance.txt | grep "$mapped_vpn|$ground_truth1" | cut -d '|' -f 3)
        dist2=$(cat nord_distance.txt | grep "$mapped_vpn|$ground_truth2" | cut -d '|' -f 3)

        if (( $dist1 < $min )); then
            min=$dist1
        fi
        if (( $dist2 < $min )); then
            min=$dist2
        fi

        if [ $method == "1Shotest_ping" ]; then
            value2=$(cat ../${method}/$file | cut -d '|' -f 2 | head -n 2 | tail -n 1)
            if [ $value2 == "0.0" ]; then
                mapped_vpn2=$(cat ../${method}/$file | cut -d '|' -f 1 | head -n 2 | tail -n 1)
                dist3=$(cat nord_distance.txt | grep "$mapped_vpn2|$ground_truth1" | cut -d '|' -f 3)
                dist4=$(cat nord_distance.txt | grep "$mapped_vpn2|$ground_truth2" | cut -d '|' -f 3)

                if (( $dist3 < $min )); then
                    min=$dist3
                fi
                if (( $dist4 < $min )); then
                    min=$dist4
                fi
            fi         
        fi
        
        echo "$min" >> err_dist_$method.txt
        total_dist=$(($total_dist+$min))
        continue
    done
    echo "$method | $total_dist" >> total_error_dist.txt
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
echo "" >> performance.txt
echo "Total error distance:" >> performance.txt
cat total_error_dist.txt >> performance.txt