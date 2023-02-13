#!/twitch_rtt/bash

vpn=${1}
ingest=${2}
ingest_ip=$(cat lrtt_${vpn}_${ingest}.txt | grep "> 10.8" | head -n 1 | cut -d ' ' -f 3 | cut -d '.' -f 1,2,3,4)

cat lrtt_${vpn}_${ingest}.txt  | grep $ingest_ip | cut -d ' ' -f 1 > timestamp.txt # all packet time stamp
cat lrtt_${vpn}_${ingest}.txt  | grep $ingest_ip | cut -d 'I' -f 1 | cut -c 4,5,7,8,9,10,11,12,13,14,15 > seq_acktime.txt # all packet time
cat lrtt_${vpn}_${ingest}.txt  | grep $ingest_ip | cut -d ',' -f 2 | cut -d ' ' -f 3 | cut -d ':' -f 2 > seq_acknum.txt # al packet seqnum/acknum
cat lrtt_${vpn}_${ingest}.txt  | grep $ingest_ip | cut -d ',' -f 2 | cut -d ' ' -f 2 > seq_or_ack.txt # determine this packet is seq or ack packet
cat lrtt_${vpn}_${ingest}.txt  | grep " > $ingest_ip" | cut -d ' ' -f 3 | cut -d '.' -f 1,2,3,4 | head -n 1 > tun0ip.txt # get vpn_net_interface IP
cat lrtt_${vpn}_${ingest}.txt  | grep $ingest_ip | cut -d ' ' -f 3 | cut -d '.' -f 1,2,3,4 > tun0ip_or_ingestip.txt # determine this packet is VPN > ingest or ingest > VPN

echo "${vpn}_${ingest}" > vpn_ingest.txt
python3 lrtt.py
cat THIS_rtt_result.txt | grep _ > THIS_minrtt_result.txt

exit 0

    
