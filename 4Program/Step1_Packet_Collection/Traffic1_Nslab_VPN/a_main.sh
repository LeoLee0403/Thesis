for ((i=1;i<=3;i++))
do
    vpn=$(cat lvpn_location_list_2023.txt | grep -w "count ${i}" | cut -d ',' -f 6 | cut -d ' ' -f 2)
    ping $vpn.nordvpn.com&
    sudo timeout 10s tcpdump host $vpn.nordvpn.com -w nslab_$vpn.pcap
    pidof ping | xargs kill
done

for ((i=1;i<=3;i++))
do
    vpn=$(cat lvpn_location_list_2023.txt | grep -w "count ${i}" | cut -d ',' -f 6 | cut -d ' ' -f 2)
    cp nslab_$vpn.pcap ../../Step2_RTT_Computation/RTT1/example/
done