
for ((i=1;i<=82;i=i+1)) 
do
    for ((j=1;j<=82;j=j+1))
    do
        host_or_vpn1=$(cat vpn_codename.txt | head -n $i | tail -n 1)
        vpn2=$(cat vpn_codename.txt | head -n $j | tail -n 1)

        if [ "$host_or_vpn1" = "$vpn2" ]; then
            continue
        fi

        tcpdump icmp -nn -r vping_${host_or_vpn1}_${vpn2}.pcap | wc -l > test.txt
        count=$(cat test.txt)
        if [ $count == 0 ]; then
            continue
        fi

        tcpdump icmp -nn -r vping_${host_or_vpn1}_${vpn2}.pcap > ../txtfile/vping_${host_or_vpn1}_${vpn2}.txt
    done
done
