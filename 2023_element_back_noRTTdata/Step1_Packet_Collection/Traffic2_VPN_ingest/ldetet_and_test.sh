vpn=${1}
ingest_airport_name=${2}
ingest=${3}
vpn_net_interface="nordlynx" # see ifconfig to choose 10.x.x.x

current_time=$(date '+%m-%d %H:%M:%S') 
echo "${current_time}" >> ${ingest}_record.txt 
echo "nordvpn connecting" >> ${ingest}_record.txt 

# Nordvpn Selection Part: 
# ============================================================================

nordvpn connect ${vpn} >> connect_status.txt # connect_status is used below

# VPN connect status
status=$(cat connect_status.txt | grep -E "You are|Connecting to|Whoops|specified server" | cut -d ' ' -f 5 | cut -c 2 | tail -n 1)

while [ "${status}" != "o" ] # ${status} != "o" means failed VPN connection
do
    exit 0
done

current_time=$(date '+%m-%d %H:%M:%S') 
echo "${current_time}" >> ${ingest}_record.txt 
echo "Connect VPN successfully! -- ${vpn}" >> ${ingest}_record.txt # successful VPN connection

# OBS Connection Test
# ============================================================================
sleep 2
obs --startstreaming&
sleep 20

echo "test tcpdump ${vpn}..." >> ${ingest}_record.txt
sudo timeout 60s tcpdump -i ${vpn_net_interface} host ${ingest_airport_name}.contribute.live-video.net -w ltest_obs.pcap
reply_packet_count=$(tcpdump src host ${ingest_airport_name}.contribute.live-video.net -r ltest_obs.pcap | wc -l)
echo "reply packet count: ${reply_packet_count}" >> ${ingest}_record.txt

if [ ${reply_packet_count} -lt 30 ]; then # packets replied from twitch ingest server < 30?
    echo "${vpn} obs failed, please try it again in the future..." >> ${ingest}_record.txt
    echo "" >> ${ingest}_record.txt
    echo "" >> ${ingest}_record.txt
    pidof obs | xargs kill
    pidof tcpdump | xargs kill
    exit 0
fi
pidof tcpdump | xargs kill

current_time=$(date '+%m-%d %H:%M:%S')
echo "${current_time} start tcpdump ${vpn} !" >> ${ingest}_record.txt


# Formal Tcpdump Part:
# ============================================================================
tcpdump -i ${vpn_net_interface} host ${ingest_airport_name}.contribute.live-video.net -w lrtt_${vpn}_${ingest}.pcap&
sleep 30
pidof tcpdump | xargs kill
sleep 3
formal_reply_packet_count=$(tcpdump src host ${ingest_airport_name}.contribute.live-video.net -r lrtt_${vpn}_${ingest}.pcap | wc -l)

current_time=$(date '+%m-%d %H:%M:%S')
echo "${current_time} tcpdump ${vpn}_${ingest} is finished !" >> ${ingest}_record.txt
echo "Formal reply packet count: ${formal_reply_packet_count}" >> ${ingest}_record.txt
echo "" >> ${ingest}_record.txt
echo "----------------------------------" >> ${ingest}_record.txt
echo "" >> ${ingest}_record.txt

pidof obs | xargs kill
pidof tcpdump | xargs kill
pidof obs | xargs kill
sleep 2

exit 0