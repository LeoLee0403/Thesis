vpn1=${1}
vpn2=${2}

a=$(cat vping_${vpn1}_${vpn2}.txt)

cat vping_${vpn1}_${vpn2}.txt | wc -l > test.txt
count=$(cat test.txt)
if [ $count == 0 ]; then
    exit
fi

if [ $vpn1 == $vpn2 ]; then
    echo "vpn_ping_${vpn1}_${vpn2} | 0" >> avpnping_min.txt
    exit
fi

is_vpn2ip=$(cat vping_${vpn1}_${vpn2}.txt | head -n 1 | cut -d ' ' -f 3 | cut -d ':' -f 1 | cut -d '.' -f 1,2)
if [ "$is_vpn2ip" == "10.8" ]; then
    vpn2_ip=$(cat vping_${vpn1}_${vpn2}.txt | head -n 1 | cut -d ' ' -f 5 | cut -d ':' -f 1 )
else
    vpn2_ip=$(cat vping_${vpn1}_${vpn2}.txt | head -n 1 | cut -d ' ' -f 3 | cut -d ':' -f 1 )
fi
echo "$vpn2_ip" > vpn2ip.txt # LM_VPN IP

# vpn1 ping vpn2 !!
cat vping_${vpn1}_${vpn2}.txt | grep "IP 10.8." | cut -d ' ' -f 3 | head -n 1 > vpn1ip_behost.txt # VP_VPN IP
cat vping_${vpn1}_${vpn2}.txt | cut -c 4,5,7,8,9,10,11,12,13,14,15 > ltime_ping.txt # parsed timestamp
cat vping_${vpn1}_${vpn2}.txt | cut -d ' ' -f 3 | cut -d '.' -f 1,2,3,4 > long_ping_which.txt # traffic A > B, then record A
cat vping_${vpn1}_${vpn2}.txt | cut -d ' ' -f 5 | cut -d ':' -f 1 > long_beping_which.txt # traffic A > B, then record B
cat vping_${vpn1}_${vpn2}.txt | cut -d ',' -f 3 | cut -d ' ' -f 3 > pingseq.txt # seqnum
cat vping_${vpn1}_${vpn2}.txt | cut -d ' ' -f 1 > lping_timestamp.txt # timestamp

echo "" > a_minRTT.txt
echo "vpn_ping_${vpn1}_${vpn2}" >> avpnping.txt
python3 comput_v1pingv2.py

minRTT=$(cat a_minRTT.txt)
if [ "$minRTT" == "" ]; then
    minRTT="None"
fi
echo "vpn_ping_${vpn1}_${vpn2} | $minRTT" >> avpnping.txt
echo "vpn_ping_${vpn1}_${vpn2} | $minRTT" >> avpnping_min.txt # min RTT of all pairs

echo "" >> avpnping.txt
