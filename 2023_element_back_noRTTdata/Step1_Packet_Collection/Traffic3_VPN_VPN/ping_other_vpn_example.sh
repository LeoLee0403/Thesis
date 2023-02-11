
VP_vpn=${1}
vpn_count=${2}
vpn_net_interface="nordlynx" # see ifconfig to choose 10.x.x.x
current_time=$(date '+%m-%d %H:%M:%S') 
echo "${current_time}" >> R_${VP_vpn}_record.txt 
echo "nordvpn connecting" >> R_${VP_vpn}_record.txt 

# Nordvpn Selection Part: 
# ============================================================================

nordvpn connect ${VP_vpn} >> connect_status.txt # connect_status is used below

# VPN connect status
status=$(cat connect_status.txt | grep -E "You are|Connecting to|Whoops|specified server" | cut -d ' ' -f 5 | cut -c 2 | tail -n 1)

while [ "${status}" != "o" ] # ${status} != "o" means failed VPN connection
do
    exit 0
done

current_time=$(date '+%m-%d %H:%M:%S') 
echo "$current_time | Connect VPN successfully! -- ${VP_vpn}" >> R_${VP_vpn}_record.txt  # pass

# Formal Tcpdump Part:
# ============================================================================

for ((i=1;i<=3;i++))
do
    LM_vpn=$(cat lvpn_location_list_2023.txt | grep -w "count ${i}" | cut -d ',' -f 6 | cut -d ' ' -f 2)
    if [ "$vpn_count" == "${i}" ]; then
        continue
    fi
    ping ${LM_vpn}.nordvpn.com&
    tcpdump host $LM_vpn.nordvpn.com -i ${vpn_net_interface} -w vping_${VP_vpn}_${LM_vpn}.pcap&
    sleep 10 # example collects 10s traffic between VP_VPN and LM_VPN

    pidof tcpdump | xargs kill
    pidof ping | xargs kill
    sleep 3

    reply_packet_count=$(tcpdump dst 10.5.0.2 -nn -r vping_${VP_vpn}_${LM_vpn}.pcap | wc -l)
    if [ ${reply_packet_count} -lt 5 ]; then
        echo "ping ${LM_vpn} failed." >> R_${VP_vpn}_record.txt
    else
        echo "reply packet count: ${reply_packet_count}" >> R_${VP_vpn}_record.txt
        echo "ping ${LM_vpn} successfully !" >> R_${VP_vpn}_record.txt
    fi

    echo "" >> R_${VP_vpn}_record.txt
    echo "----------------------------------" >> R_${VP_vpn}_record.txt
    echo "" >> R_${VP_vpn}_record.txt
done

pidof tcpdump | xargs kill
pidof ping | xargs kill

exit 0