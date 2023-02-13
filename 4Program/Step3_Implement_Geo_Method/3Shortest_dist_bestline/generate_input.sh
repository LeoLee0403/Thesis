line=$(cat nord_rtt.txt | wc -l)
for ((i=1;i<=$(($line-1));i=i+1))
do
    vpn1=$(cat nord_rtt.txt | cut -d '|' -f 1 | head -n $i | tail -n 1)
    rtt=$(cat nord_rtt.txt | cut -d '|' -f 3 | head -n $i | tail -n 1)
    echo "$rtt" >> yrtt_${vpn1}.txt

    vpn_pair=$(cat nord_rtt.txt | cut -d '|' -f 1,2 | head -n $i | tail -n 1) # index for search distance

    distance=$(cat nord_distance.txt | grep $vpn_pair | cut -d '|' -f 3)
    echo "$distance" >> xdist_${vpn1}.txt
done