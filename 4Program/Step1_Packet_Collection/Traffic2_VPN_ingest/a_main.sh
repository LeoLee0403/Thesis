bash reset.sh # reset OBS
for ((i=1;i<=3;i++)) # sequentially select ingest server for crawling
do
    ingest_airport_name=$(cat ingest_list.txt | cut -d '|' -f 1 | head -n $i | tail -n 1)
    ingest=$(cat ingest_list.txt | cut -d '|' -f 2 | head -n $i | tail -n 1)

    for ((j=1;j<=3;j++)) # sequentially select VPN with unique location for connection
    do
        vpn=$(cat avpn.txt | head -n $j | tail -n 1)   
        bash ldetect_and_test_example.sh $vpn ${ingest_airport_name} ${ingest} # crawling
    done
    bash switch_obs.sh # change to next ingest on OBS
done

pidof obs | xargs kill
pidof tcpdump | xargs kill
nordvpn d



