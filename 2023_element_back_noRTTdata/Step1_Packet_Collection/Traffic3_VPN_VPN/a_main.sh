for ((j=1;j<=3;j++))
do
    VP_vpn=$(cat lvpn_location_list_2023.txt | grep -w "count ${j}" | cut -d ',' -f 6 | cut -d ' ' -f 2)
    file_exist=$(ls | grep "vping_${VP_vpn}")
    if [ "$file_exist" == "" ]; then
        bash ping_other_vpn_example.sh ${VP_vpn} ${j} # ping the LM_vpn
    else
        continue
    fi
done