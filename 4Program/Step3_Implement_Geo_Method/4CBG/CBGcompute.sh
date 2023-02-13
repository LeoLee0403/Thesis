count=0
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    radius=$(cat predict_${ingest}_dist.txt)

    for ((k=1;k<=81;k++))
    do
        vpn2=$(cat a_vpns.txt | head -n $k | tail -n 1)
        for ((j=1;j<=81;j++))
        do
            vpn1=$(cat a_vpns.txt | head -n $j | tail -n 1)

            radius_vpn1_target=$(cat predict_${ingest}_dist.txt | head -n $j | tail -n 1)
            int_radius_vpn1_target=$(echo $radius_vpn1_target | awk -F. '{print $1}')

            dist_vpn1_vpn2=$(cat nord_distance.txt | grep "${vpn1}|${vpn2}" | cut -d '|' -f 3)
            int_dist_vpn1_vpn2=$(echo $dist_vpn1_vpn2 | awk -F. '{print $1}')
            if (( $int_dist_vpn1_vpn2 <= $int_radius_vpn1_target )); then
                if (($int_radius_vpn1_target <= 2000)); then
                    count=$(($count+1))
                fi
            fi
        done
        echo "${vpn2}|${count}" >> count_${ingest}.txt
        count=0
    done

done