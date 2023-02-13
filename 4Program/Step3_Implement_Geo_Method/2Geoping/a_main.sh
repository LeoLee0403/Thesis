echo -n "" > diff.txt
for ((i=1;i<=60;i++))
do
    ingest=$(cat aingest.txt | head -n $i | tail -n 1)
    cat ingest_rtt.txt | cut -d '|' -f $i > one_col_ingestrtt.txt
    top=82
    top_vpn=$(python3 top_vpn.py $top)
    top_ingest_rtt=$(python3 top_ingest_rtt.py $top)

    for ((v=1;v<=82;v++))
    do
        vpn=$(cat avpn.txt | head -n $v | tail -n 1)
        cat vpn_rtt.txt | cut -d '|' -f $v > one_col_vpnrtt.txt
        
        diff=$(python3 geoping.py $top $top_vpn $top_ingest_rtt )
        echo "$diff" >> diff.txt
    done
    python3 sort_diff.py > aa_${ingest}.txt
    echo -n "" > diff.txt
done

bash toex.sh
cat excel.txt > 2Geoping.ods
# xdg-open 2Geoping.ods