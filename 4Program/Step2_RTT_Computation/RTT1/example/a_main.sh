
for ((i=1;i<=3;i++))
do
    vpn=$(cat lvpn_location_list_2023.txt | grep -w "count ${i}" | cut -d ',' -f 6 | cut -d ' ' -f 2)

    # pcapfile to txtfile
    tcpdump -nn -r nslab_$vpn.pcap > nslab_$vpn.txt

    host_ip="192.168.0.10" # if you do the experiment in nslab, then the ip will be 140.112.x.x
    cat nslab_$vpn.txt | cut -d ' ' -f 3 > long_ping_which.txt
    cat nslab_$vpn.txt | cut -c 4,5,7,8,9,10,11,12,13,14,15 > ltime_ping.txt
    cat nslab_$vpn.txt | cut -d ',' -f 3 | cut -d ' ' -f 3 > pingseq.txt
    cat nslab_$vpn.txt | cut -d ' ' -f 1 > lping_timestamp.txt

    # get the min vpn RTT
    python3 rtt.py $host_ip $vpn >> RTT.txt
    cat RTT.txt | grep min > min_RTT.txt
    
done
