for ((i=1;i<=60;i++))
do
    for ((j=1;j<=81;j++))
    do
        vpn=$(cat avpns.txt | head -n $j | tail -n 1)
        ingest=$(cat aingest.txt | head -n $i | tail -n 1)
        vpn_to_target_rtt=$(cat ingest_rtt.txt | cut -d '|' -f $i | head -n $j | tail -n 1)
        python3 predict_dist.py $vpn $vpn_to_target_rtt >> predict_${ingest}_dist.txt
    done
done


