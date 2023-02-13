
for ((i=1;i<=82;i++))
do
    for ((j=1;j<=82;j++))
    do
        x[${i}]=$(cat vpn_codename.txt | head -n $i | tail -n 1)
        y[${j}]=$(cat vpn_codename.txt | head -n $j | tail -n 1)
        bash compute_RTT.sh ${x[$i]} ${y[$j]} 
    done
done
cat a_manual_test.txt >> avpnping_min.txt

bash a_get_adjusted_RTT.sh
bash output_vpn_rtt.sh
bash output_nord_rtt.sh

# xdg-open RTT3_VPNs.ods