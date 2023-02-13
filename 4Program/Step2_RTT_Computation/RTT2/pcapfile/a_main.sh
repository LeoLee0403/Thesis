
for ((v=1;v<=82;v++)) # ingest
do
    for ((i=1;i<=60;i++)) # ingest
    do
        vpn=$(cat a_vpn.txt | head -n $v | tail -n 1)
        ingest=$(cat a_ingest.txt | head -n $i | tail -n 1)
        pair=$(tcpdump -r lrtt_${vpn}_${ingest}.pcap)
        if [ "$pair" != "" ]; then 
            tcpdump -nn -r lrtt_${vpn}_${ingest}.pcap > ../txtfile/lrtt_${vpn}_${ingest}.txt
        else
            echo "${vpn}_${ingest}" >> aneedpair.txt
        fi
    done
done