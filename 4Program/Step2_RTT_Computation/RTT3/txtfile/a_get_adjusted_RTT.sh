echo -n "" > excel_rtt.txt

for ((i=1;i<=82;i++))
do
    vpn_row=$(cat vpn.txt | head -n $i | tail -n 1)
    echo -n "	" >> excel_rtt.txt 
    echo -n "$vpn_row" >> excel_rtt.txt 
    
done
echo "" >> excel_rtt.txt

for ((j=1;j<=82;j++))
do
    vpn=$(cat avpns.txt | head -n $j | tail -n 1)
    vpn_col=$(cat vpn.txt | head -n $j | tail -n 1)
    echo -n "$vpn_col" >> excel_rtt.txt 
    echo -n "	" >> excel_rtt.txt 
    RTT1=$(cat RTT1_for_RTT3.txt | head -n $j | tail -n 1)

    # find min and < 0 RTT
    echo "1000" > min.txt
    echo -n "" > minrtt_lessthan_zero.txt
    for ((i=1;i<=82;i++))
    do
        vpn_be_ping=$(cat avpns.txt | head -n $i | tail -n 1)
        rtt=$(cat avpnping_min.txt | grep "vpn_ping_${vpn}_${vpn_be_ping}" | tail -n 1 | cut -d ' ' -f 3)
        python3 find_min_rtt.py $rtt $RTT1 $i
    done

    for ((i=1;i<=82;i++))
    do
        vpn_be_ping=$(cat avpns.txt | head -n $i | tail -n 1)
        rtt=$(cat avpnping_min.txt | grep "vpn_ping_${vpn}_${vpn_be_ping}" | tail -n 1 | cut -d ' ' -f 3)
        rtt=$(python3 adjust.py $rtt $RTT1)
        echo -n "$rtt	" >> excel_rtt.txt 
    done

    echo "" >> excel_rtt.txt
    
done

cat excel_rtt.txt > RTT3_VPNs.ods

