
for ((i=1;i<=82;i++))
do
    for ((j=1;j<=82;j++))
    do
        vpn1=$(cat a_space_vpns.txt | head -n $i | tail -n 1)
        lat1=$(cat lvpn_location_list.txt | grep "$vpn1" | cut -d ' ' -f 3 | cut -d ',' -f 1)
        long1=$(cat lvpn_location_list.txt | grep "$vpn1" | cut -d ' ' -f 4 | cut -d ',' -f 1)

        vpn2=$(cat a_space_vpns.txt | head -n $j | tail -n 1)
        lat2=$(cat lvpn_location_list.txt | grep "$vpn2" | cut -d ' ' -f 3 | cut -d ',' -f 1)
        long2=$(cat lvpn_location_list.txt | grep "$vpn2" | cut -d ' ' -f 4 | cut -d ',' -f 1)

        if [ "$vpn1" = "$vpn2" ]; then
            echo "${vpn1}|${vpn2}|0" >> nord_distance.txt
            continue
        fi
        
        echo -n "${vpn1}|${vpn2}|" >> nord_distance.txt
        python3 distance.py $lat1 $long1 $lat2 $long2 >> nord_distance.txt
    done

done


sed -i 's/ /_/g' nord_distance.txt