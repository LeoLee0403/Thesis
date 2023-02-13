for ((i=1;i<=60;i++))
do
    echo -n "" > avpns_lat.txt
    echo -n "" > avpns_long.txt
    echo -n "" > predict_as_radius.txt

    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    echo "$ingest" > now_ingest.txt
    
    for ((j=1;j<=81;j++))
    do
        vpn=$(cat avpns_space.txt | head -n $j | tail -n 1)
        lat=$(cat lvpn_location_list.txt | grep "$vpn" | cut -d ' ' -f 3 | cut -d ',' -f 1)
        long=$(cat lvpn_location_list.txt | grep "$vpn" | cut -d ' ' -f 4 | cut -d ',' -f 1)
        echo "$lat" >> avpns_lat.txt
        echo "$long" >> avpns_long.txt
    done
    radius=$(cat predict_${ingest}_dist.txt)
    echo "$radius" > predict_as_radius.txt
    python3 map.py

done