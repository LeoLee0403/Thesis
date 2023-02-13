
for ((i=1;i<=82;i++))
do
    vpn=$(cat a_vpn.txt | head -n $i | tail -n 1)
    
    for ((j=1;j<=60;j++))
    do
        ingest=$(cat a_ingest.txt | head -n $j | tail -n 1)
        bash lcompute.sh $vpn $ingest
    done

done

bash a_get_adjusted_RTT.sh
bash output_ingest_rtt.sh

# xdg-open RTT2_VPN_ingest.ods