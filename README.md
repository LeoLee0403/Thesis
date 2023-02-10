# README

## Step 1. Packet Collection

### nordvpn_list_get
- a_main.sh
    - Use the command **`bash a_main.sh`** to run the shell code
    - We can use the command `curl --silent "https://api.nordvpn.com/v1/servers?limit=50000" | jq > nordvpn_raw.txt` to crawl the raw information of Nordvpn. And we arrange some required properties the VPN list. 
- list_vpn.py:
    - It can receive relevant properties and output/arrange them to **lvpn_location_list_2023.txt**
- lvpn_location_list_2023.txt
    - We classify the VPN into the list according to different VPN server location. there are 87 NordVPN locations in 2023, and in each location(row), the list format is *[latitude] [longitude] [country] [city] [servercount] [domain1] [domain2] [domain3] ...*
- a_reset.sh
    - run it by **`bash a_reset.sh`** It will remove all the output files. If you want to redo the experiment, then you can run the file and then run **a_main.sh** again. Besides, all the experiments have **a_main.sh** and **a_reset.sh** for you to redo the experiment.

### Traffic1_Nslab_VPN
- a_main.sh
    - We ping each vpn from NSLAB and use tcpdump to intercept the traffic and save to pcapfile. The example show ping 3 vpn for 10 second. And we will get 3 pcapfile in this example

### Traffic2_VPN_ingest
- avpn.txt : VPN locations (named in city)
- a_main.sh
    - First you have to build your own "**ingest_list.txt**". You need to your the order (varies by machines) of Twitch ingest server in the OBS list![](https://i.imgur.com/mUjxMXM.png)and then find the airport code of each ingest server, you can find the airport code in [twitch status](https://twitchstatus.com/) or try to start streaming on each ingest server and intercept the traffic to find the airport code.
    - The script will first run `bash reset.sh`, it will reset the OBS list to the top 1 ingest server. For example in obove figure, it will reset to **Asia: Taiwan, Taipei (3)** ingest server for streaming.
    - This example shows using 3 VPN to probe 3 ingest server. 
    - **ldetet_and_test_example.sh** will get the traffic between the pair of VPN and ingest server, and save the traffic to pcapfiles.
    - After getting pairs of an ingest server and all VPNs, **switch_obs.sh** will switch to next ingest server by OBS
- reset.sh
    - It uses [xdotool](https://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html#keyboard%20commands) to simulate keyboard and mouse operations, then we can operate the OBS GUI (Because OBS currently does not provide a command to select the Twitch ingest server). And this script will reset OBS list to the top ingest server.
    - The number of clicks may change due to the update of OBS. If there is a change, you need to change the number of clicks by yourself.
- switch_obs.sh
    - It will switch the ingest server to the next one according to the OBS list. For example, if now ingest is Taipei(3), then it will switch to Taipei(1) for streaming.
- ldetet_and_test_example.sh
    - It will accept a VPN and a ingest server, and you need to take change vpn_net_interface (varies by machines). You can use ifconfig to find the interface. The **vpn_net_interface** in this case is **nordlynx**, and the **vpn_net_interface IP** usually **10.x.x.x** ![](https://i.imgur.com/zzJ85OF.png)
    - Use `nordvpn connect ${vpn}` to connect the NordVPN, the VPN we used is **city name**, After connection, it will check the connect_status, if VPN failed then change to next VPN with another location to probe the same ingest server.
    - OBS Connection Test: `obs --startstreaming&` to start streaming, it will generate the traffic between the VPN and the ingest server. And you should sleep for more than 10 sec to wait the OBS open. Then this example uses tcpdump to intercept the traffic for 10 sec. If the **reply_packet_count** from twitch ingest server less than threshold (this example set the threshold = 20 packets), then regard it as OBS Failed, then exit and change to next VPN with another location to probe the same ingest server.
    - Formal Tcpdump: If pass the OBS connection test, this example will do formal tcpdump for 10 sec, and if **formal_reply_packet_count** less than 50, then regard it as OBS failed. Else regard it as successfully interception.
    - Besides, all the VPN connection and tcpdump interception process will be recorded in **${ingest}_record.txt**

### Traffic3_VPN_VPN
- a_main.sh
    - This script connects NordVPN by `nordvpn connect ${VP_VPN}` VP_VPN is the [first domain] in each location in lvpn_location_list_2023.txt. For example, first location's VP_VPN is pl128, and second location's VP_VPN is be148. However, sometimes NordVPN does not allow us to connect the VPN with specific domain. If this case happens unfortunately, try to make VPN = **city name**. For example, use `nordvpn connect Warsaw` to connect the VPN, and you need to modify ping_other_vpn.sh
    - The example uses 3 VP_vpn to ping 3 LM_vpn, and use tcpdump to intercept the traffic between them and save the traffic to pcapfile.
- ldetet_and_test_example.sh
    - Choose the correct vpn_net_interface and connect the VPN, and then check the VPN connection status to determine whether it is a successful connection.
    - Formal Tcpdump: In this example, for each VP_VPN, they ping 3 LM_VPN in sequence for 10 sec. If the **reply_packet_count** is less than 5 then regard it as VPN failed. Else it will be a successful interception, and record the interception process in **R_${VP_vpn}_record.txt**

## Step 2. RTT_Computation

### RTT1/example (host ip錄影之後要補改, 還要加上result!)
- nslab_[VPN first domain].pcap
    - These .pcap files are traffic between Nslab and VPN. For example, use `tcpdump -nn -r nslab_pl128.pcap`, we can get the traffic between the host and VPN. Host ip will depend on your host machine, if we want to do the experiment in Nslab, then the host ip will be **140.112.x.x**
    - In this example, **xx.xx.xx.xx** is our host ip. We need to find 
        - Time1 ... IP host_ip > VPN_ip ... **request** ... , seq **i** ...
        - ...
        - ...
        - Time2 ... IP VPN_ip > host_ip ... **reply** ... , seq **j** ...
        - if i == j, then we pair the two packets and the RTT of this pair is Time2 - Time1, and finally get the minimum RTT between all pairs to be the RTT between Nslab and this VPN.
- a_main.sh
    - The example compute the RTT of the three pcapfile we get in Traffic1_Nslab_VPN. First we convert the pcapfile to text file for easy operation.
    - If your host is in the nslab, then the host_ip should change to the nslab ip: **140.112.x.x**.
    - lping_timestamp.txt 
        - Each packet's timestamp. For exapmple, time_stamp = 01:08:31.947975
    - ltime_ping.txt 
        - If time_stamp is 01:08:31.947975, it will be parsed out 0831.947975
    - pingseq.txt
        - record the pingseq of each packet
    - long_ping_which.txt
        - Each packet is IP_A > IP_B, and it records each IP_A
    - **rtt.py** 
        - Get the minimum rtt of each Nslab_VPN pair.
- rtt.py
    - The parsed timestamp will be converted to useful time value (in second). And then minus the bias (first packet's time value) from their time value.
    - If find the packet is host > vpn, and next packet is vpn > host, and pingseq are the same, then pair the two packets and subtract their time value to get the RTT of this pair.
    - Finally output the min_RTT between each Nslab_VPN, and these RTT1 between Nslab and VPN are used to minus the overmeasured RTT2 and RTT3 to get the real RTT2 and RTT3
- Result
- Besides, the file RTT1_for_RTT2.txt RTT1_for_RTT3.txt are RTT1 between NSLAB and 82 VPN in my experiment for subtraction.

### RTT2
- /pcapfile 
    - a_vpn.txt: VPN list (named in city)
    - a_ingest.txt: ingest server list (named in city)
    - lrtt\_[VPN]\_[ingest].pcap
        - These .pcap files are traffic between VPN and ingest server. For example, use `tcpdump -nn -r lrtt_Adelaide_Ashburn_VA3.pcap`, we can get the traffic between Adelaide VPN and Ashburn_VA3 ingest server. And VPN ip will be your **vpn_net_interface\'s IP** (varies by machines).
        - In this example, 
            - Time1 ... IP VPN_ip > ingest_ip ... seq num_s:**num_t** ... 
            - ...
            - ...
            - Time2 ... IP ingest_ip >  VPN_ip ... ack **num** ...
            - if num_t == num, then pair the two packets and compute the RTT of this pair is Time2 - Time1, and finally get the minimum RTT between all pairs, and then pass the RTT to make adjustment to get the adjusted RTT2.
    - a_main.sh
        - To get the RTT of all pairs between 82 VPN and 60 ingest server in my experiment. First we use the script to convert the pcapfile to text file for easy operation.
- /txtfile
    - a_main.sh
        - After the conversion, the for loop will do **lcompute.sh** to compute the RTT between each VPN and each ingest server, but the RTT include the RTT1. So we run **a_get_adjusted_RTT.sh** to minus RTT1 from the RTT, and it will also adjust the RTT to nonnegative value.
        -  `xdg-open RTT2_VPNs.ods` to get the RTT2
    - lcompute.sh
        - timestamp.txt
            - Each packets' timestamp
        - seq_acktime.txt
            - If time_stamp is 05\:27:36.164483, it will be parsed out 0527.36164483
        - seq_or_ack.txt
            - Determine this packet is seq or ack packet
        - tun0ip.txt
            - Get vpn_net_interface IP
        - tun0ip_or_ingestip.txt
            - Determine each packet is VPN_ip > ingest_ip or ingest_ip > VPN_ip
        - **lrtt.py** receive above data to compute the RTT
        - output the minimum RTT to **THIS_minrtt_result.txt**
    - lrtt.py
        - Compute the useful time value (in second) and minus bias to reset the first packet's time value is 0.
        - #Run
            - seq packet (VPN_ip > ingest_ip) will examine whether the packet is retransmission packet by examining prior packets' seqnum. If yes, then the two packet will be invalid. If no retransmission, then add the packet's seqnum to the queue.
            - ack packet (ingest_ip > VPN_ip) will check the seqnum in point_start ~ 
                - point_now. point_now is current packet we examine.
                - point_start is the next seqnum to be checked by the ack packet
            - if queue[i] = acknum[point_now] then pair the two packets and compute the RTT of the pair to output_rtt. And the point_start will also make point_start jump to next valid seqnum in the queue
        - Finally getting all RTT of all pairs.
    - a_get_adjusted_RTT.sh
        - Receive RTT1_for_RTT2.txt, THIS_minrtt_result.txt (minimum RTT from **lcompute.sh**)
        - Run **find_min_rtt.py** to do minimum RTT - RTT1, and between each VPN and all ingest server, output negative minimum RTT.
        - Run **adjust.py** to do: RTT between each VPN to all ingest server will be subtracted by the negative minimum RTT to adjust the RTT value to be non-negative.


### RTT3
- pcapfile
    - vping\_[VP_VPN]\_[LM_VPN].pcap
        - These .pcap files are traffic between VPN each other. For example, use `tcpdump -nn -r vping_al18_ar29.pcap`, we can get the traffic between the al18 VP_VPN and ar29 LM_VPN. And VP_VPN's IP will be vpn_net_interface IP
            - In this example,
            - Time1 ... IP VP_VPN_ip > LM_VPN_ip ... **request** ... , seq **i** ...
            - ...
            - ...
            - Time2 ... IP LM_VPN_ip > VP_VPN_ip ... **reply** ... , seq **j** ...
            - if i == j, then we pair the two packets and the RTT of this pair is Time2 - Time1, and finally get the minimum RTT between all pairs, and then pass the RTT to make adjustment to get the adjusted RTT3.
    - vpn_codename.txt
        - First domain of each VPN in different location.
    - a_main.sh
        - To get the RTT of all pairs between 82 VPN each other in my experiment. First we use the script to convert the pcapfile to text file for easy operation.
- txtfile
    - a_main.sh
        - After the conversion, the for loop will do **compute_RTT.sh** to compute the RTT between VPN each other, but the RTT include the RTT1. So we run **a_get_adjusted_RTT.sh** to minus RTT1 from the RTT, and it will also adjust the RTT to nonnegative value. And then add the manual test result for VPN failed pair.
        -  `xdg-open RTT3_VPNs.ods` to get the RTT3
    -  compute_RTT.sh
        -  vpn1 is VP_VPN
        -  vpn2 is LM_VPN
        -  vpn1ip_behost.txt
            -  VP_VPN IP
        -  vpn2ip.txt
            -  LM_VPN IP
        -  ltime_ping.txt
            -  Parsed timestamp
        -  long_ping_which.txt
            -  Each packet is IP_A > IP_B, and it records each IP_A
        -  long_beping_which.txt
            -  Each packet is IP_A > IP_B, and it records each IP_B
        -  lping_timestamp.txt
            -  Each packet's timestamp
        -  **comput_v1pingv2.py**
            -  Compute the RTT between VP_VPN and LM_VPN
        -  **avpnping_min.txt**
            -  Record minumum RTT of each [VP_VPN, LM_VPN] pair
    -  comput_v1pingv2.py
        - If find the packet is VP_VPN > LM_VPN, and next packet is LM_VPN > VP_VPN, and pingseq are the same, then pair the two packets and subtract their time value to get the RTT of this pair.
        - Finally output minimum RTT.
    -  a_get_adjusted_RTT.sh
        - Receive RTT1_for_RTT3.txt, avpnping_min.txt (minimum RTT from **compute_RTT.sh**)
        - Run **find_min_rtt.py** to do minimum RTT - RTT1, and between each VP_VPN and all LM_VPN, output negative minimum RTT.
        - Run **adjust.py** to do: RTT between each VP_VPN to all LM_VPN will be subtracted by the negative minimum RTT to adjust the RTT value to be non-negative.

## Step 3. Implement Geolocation Methods
- 1shortest_ping
    - ingest_rtt.txt
        - RTT between each VPN and each ingest server, the RTT in (m,n) position is between VPN[m] in **avpn.txt** and ingest[n] in **aingest.txt**
    - a_main.sh
        - For each ingest server, run **sort.py** to sort the VPN according to the RTT between VPN and ingest server
        - `xdg-open 1shortest_ping.ods` to get the shortest ping result
    - sort.py
        - For a ingest server, receive 82 VPN with their RTT to the ingest server, and sort the VPN according to its RTT to ingest server from low to high
    - [outputfile] aa_[ingest].txt
        - VPN and corresponding RTT to this ingest server (from low to high)
        
    
- 2geoping
    - Geoping focus on mapping the ingest server to the VPN with most similar fingerprint, for each ingest server, it will compute the RTT between the ingest server and all VPN to form an target fingerprint, and compute the RTT between a VPN and all the VPN to form a LM fingerprint, and it will form 82 LM fingerprint.
    - a_main.sh
        - top
            - For example, if top = 30, then for each RTT, we only take 30 VPN with the first 30 small RTT to the ingest server. It means Both target(ingest) fingerprint and LM(VPN) fingerprint are only care about the 30 VPN's RTT to them. But now we use all VPN, so set top = 82
        - top_VPN
            - For example, if top = 30, then use **top_vpn.py** to record 30 VPN with the first 30 small RTT to the ingest server
        - top_ingest_rtt
            - For example, if top = 30, then use **top_ingest_rtt.py** to record the first 30 small RTT to the ingest server
        - **geoping.py**
            -  Compute Euclidean Distance between target fingerprint and the LM fingerprint, and record them in the **diff**
        -  sort_diff.py
            -  Sort VPN with the Euclidean Distance between target fingerprint and the LM fingerprint from low to high
        - `xdg-open 2Geoping.ods` to get the geoping result 
    - geoping.py
        - receive 
            1. topvpn (first $top VPN)
            2. ingetrtt (first $top ingest)
            3. vpn (82 VPN) 
            4. vpnrtt (RTT3 between VPN each other)
        - Compute Euclidean Distance by $$\sqrt{\Sigma{(ingestrtt- vpnrtt)^2}}$$ and output Euclidean Distance to **diff**.
    - sort_diff.py
        - receive diff list and sort VPN with diff from low to high
    - [outputfile] aa_[ingest].txt
        - VPN and corresponding Euclidean Distance to this ingest server (from low to high)
And we store the euclidean distance between the target fingerprint and each LM fingerprint to **diff**, and then sort the VPN according to the diff from low to high. 
       
- 3shortest_dist
    - a_main.sh
        - **get_distance_by_latlong.sh** 
            - Get distance (in km) betwenen VPN each other by latitude and longitude
            - **distance.py**
                - Give two position's latitude and longitude, then return the geo-distance between the two position.
            - output to nord_distance.txt
                - **nord_distance.txt** record VPN1 | VPN2 | dist(km) | lat1 | long1 | lat2 | long2
        - **generate_input.sh** 
            - For each VPN, output the RTT and distance to all VPN
            - output to yrtt_[VP_VPN].txt and xdist_[VP_VPN].txt 
        - **predict_dist.sh** 
            - Generate bestline, and use bestline to predict target distance from target RTT
            - for each VPN, for each ingest, call **predict_dist.py**
            - **predict_dist.py**
                - receive target RTT between a VPN and a ingest server
                - find the bestline y = mx + b, the goal is to find out m and b
                    - for each b from 0 to 400
                        - Find out m such that the sum of vertical distance from all points to this line y = mx + b is minimum, and all points cannot be lower than this line
                    - In the several min_sum above, choose the bestline with the smallest min_sum, and we get m and b.
                    - Convert target RTT by the bestline y = mx + b
                        - predict distance = (target rtt - b) / m
            - output the predict target distance to **predict_[ingest]_dist.txt**
        - **generate_dist.sh** 
            - Sort the VPN according to the predict target distance from low to high by **sort_dist.py**
            - output to **a_sorted_[ingest].txt**
        - **generate_dist_rank.sh** 
            - For each ingest server, convert predict target distance of each VPN to short distance rank of each VPN. If the predict target is smaller the rank will be higher (rank 1 is highest). The conversion is done by **sort_dist_rank.py**
            - Output to **a_rank_[ingest].txt**
        - `xdg-open 3Shortest_dist.ods` to get the shortest distance result
        
- 4CBG
    - a_main.sh
        - **CBGcompute.sh** # CBGcompute will predict target distance to get how many circle covers of each VPN
        - **a_generate_cover_rank.sh** # compute each VPN's cover rank according to the circle cover count
        - **map.sh** # plot the circle covers on the map
        - **point_for_pureCBG.sh** # for each VPN's cover rank we give cover point, if cover point is the same, compare dist point according shortest distance method
        - **aa_generate_sorted_point_for_PureCBG.sh** # rank VPN according to total point from high to low and mark cover count
        - `xdg-open 4CBG.ods` to get the CBG result

- 5Hybrid1
    - a_main.sh
        - **point1.sh** # we give a scaled score for Hybird1 method, we have each VPN's cover rank and short distance rank, then we convert them by the scaled score to cover point and short distance point, and then add the two point to get the total point of each VPN.
        - **aa_generate_sorted_point.sh** # rank VPN according to total point from high to low
        - `xdg-open 5Hybrid1.ods` to get the Hybrid1 result
- 6Hybrid2
    - a_main.sh
        - **point2.sh** # Hybrid2 two's procedure is the same as Hybrid1 method, the only different is the scaled score
        - `xdg-open 5Hybrid1.ods` to get the Hybrid2 result
        
## Step 4. Evaluation and Analysis
- Rank difference 
    - a_main.sh
        - first we have ground truth of each ingest server. And we have sorted VPN according to each method's metric. 
        - For example, in **shortest ping**, the RTT is small then the rank will be high. 
        - the for loop find the rank of the ground truth VPN, and minus 1 to get the rank difference of each ingest server of each method
        - and we can use the **performance.sh** script to output the count in each rank difference
    - performance.txt
        - finally the result is shown in this file, we can get the count in each rank difference and get the Cumulative probability in each range.
    
- Error distance
    - a_main.sh
        - first the for loop will get the mapped VPN, which is the first mapping priority VPN in each method, and then compute the distance between the mapped VPN and gournd truth to be error distance of the ingest server of each method.
        - Besides, we caculate the total error distance of each method, this is the most important evaluation metric.
    - performance.txt
        - finally the result is shown in this file, we can get the count in each error distance range and get the Cumulative probability in each range. And the total error ditance is shown below.

## README.txt要補充的
 1. 每個資料夾都有a_main.sh and a_reset.sh
 2. .sh檔用bash執行檔案 e.g. bash a_main.sh
 3. .py用python3執行檔案 e.g. python3.performance.py

 1. 每個資料夾都有a_main.sh and a_reset.sh
 2. .sh檔用bash執行檔案 e.g. bash a_main.sh
 3. .py用python3執行檔案 e.g. python3.performance.py
