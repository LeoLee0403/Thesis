for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    cat ingest_rtt.txt | cut -d '|' -f $i > one_col_ingestrtt.txt

    python3 sort.py > sorted_vpn_ingestrtt.txt # for each ingest, sort RTT between vpn and ingest
    cat sorted_vpn_ingestrtt.txt > aa_${ingest}.txt
done
bash toex.sh

# xdg-open 1shortest_ping.ods