# README

## Step 1
- nordvpn_list_get
    - a_main.sh
        - Use the command **`bash a_main.sh`** to run the shell code
        - We can use the command `curl --silent "https://api.nordvpn.com/v1/servers?limit=50000" | jq > nordvpn_raw.txt` to crawl the raw information of Nordvpn. And we arrange some required properties the VPN list. 
    - list_vpn.py:
        - It can receive relevant properties and output/arrange them to **lvpn_location_list_2023.txt**
    - lvpn_location_list_2023.txt
        - We classify the VPN into the list according to different VPN server location. there are 87 NordVPN locations in 2023, and in each location(row), the list format is *[latitude] [longitude] [country] [city] [servercount] [domain1] [domain2] [domain3] ...*
    - a_reset.sh
        - run it by **`bash a_reset.sh`** It will remove all the output files. If you want to redo the experiment, then you can run the file and then run **a_main.sh** again. Besides, all the experiments have **a_main.sh** and **a_reset.sh** for you to redo the experiment.
        
- Traffic1_Nslab_VPN
    - a_main.sh
        - We ping each vpn from NSLAB and use tcpdump to intercept the traffic and save to pcapfile. The example show ping 3 vpn for 10 second. And we will get 3 pcapfile in this example
- Traffic2_VPN_ingest
    - avpn.txt : VPN locations (named in city)
    - a_main.sh
        - First you have to build your own "**ingest_list.txt**". You need to your the order (varies by machines) of Twitch ingest server in the OBS list![](https://i.imgur.com/mUjxMXM.png)and then find the airport code of each ingest server, you can find the airport code in [twitch status](https://twitchstatus.com/) or try to start streaming on each ingest server and intercept the traffic to find the airport code.
        - This example shows using 3 VPN to probe 3 ingest server. 
        - **ldetet_and_test_example.sh** will get the traffic between the pair of VPN and ingest server
        - After getting pairs of an ingest server and all VPNs, **switch_obs.sh** will switch to next ingest server by OBS
    - ldetet_and_test_example.sh
        - It will accept a VPN and a ingest server, and you need to take change vpn_net_interface (varies by machines). You can use ifconfig to find the interface. The NordVPN interface usually **10.x.x.x** ![](https://i.imgur.com/zzJ85OF.png)
        - After connect the VPN, it will check the connect_status, if VPN failed then change to next VPN with another location to probe the same ingest server.
        - OBS Connection Test: `obs --startstreaming&` to start streaming, it will generate the traffic between the VPN and the ingest server. And you should sleep for more than 10 sec to wait the OBS open. Then this example uses tcpdump to intercept the traffic for 10 sec. If the **reply_packet_count** from twitch ingest server less than threshold (this example set the threshold = 20 packets), then regard it as OBS Failed, then exit and change to next VPN with another location to probe the same ingest server.
        - Formal Tcpdump: If pass the OBS connection test, this example will do formal tcpdump for 10 sec, and if **formal_reply_packet_count** less than 50, then regard it as OBS failed. Else regard it as successfully interception.
        - Besides, all the VPN connection and tcpdump interception process will be recorded in **${ingest}_record.txt**



- Traffic3_VPN_VPN
    - a_main.sh
        - the example use 3 VP_vpn to ping 3 LM_vpn and use tcpdump to intercept the traffic and save to pcapfile. [Run要拍]
        
## Step 2
- RTT1 - example
    - a_main.sh
        - the example compute the RTT of the three pcapfile we get. First we convert the pcapfile to text file for easy operation.
        - if your host is in the nslab, then the host ip should change to the nslab ip.
        - and we use rtt.py to get the minimum rtt of each file
        - [RUN 結果要展示 finally we get the min RTT of each file]
    - Besides, the file RTT1_for_RTT2.txt RTT1_for_RTT3.txt are RTT1 between NSLAB and 82 VPN in my experiment for subtraction.
- RTT2
    - pcapfile - aconvert_totxt.sh
        - we want to get compute the RTT of all pair between 82 VPN and 60 ingest server. First we use the script to convert the pcapfile to text file for easy operation
    - txtfile
        - a_main.sh
            - after the conversion, the for loop will compute the RTT, but the RTT include the RTT1. So we run the following script **a_get_adjusted_RTT.sh** to minus RTT1 from the RTT and adjust the RTT to nonnegative value.
            -  [excel] finally in this file we get the RTT of each VPN_ingest pair.

- RTT3
    - pcapfile - aconvert_totxt.sh
        - we want to get compute the RTT of all pair between 82 VPN each other, and use the script to convert the pcapfile to text file.
    - txtfile
        - a_main.sh
            - like getting RTT2, the for loop compute the RTT, and use **a_get_adjusted_RTT.sh.sh** to minus RTT1 from the RTT and adjust the RTT to nonnegative value.
            - [excel] finally in the file we get the RTT between VPN each other

## Step 3
- 1shortest_ping
    - a_main.sh
        - shortest ping focus on mapping the ingest server to the VPN with smallest RTT. 
for each ingest server, it will sort VPN according to the RTT from low to high.
        - [RUN]
        - **xdg-open 1shortest_ping.ods** to get the shortest ping result
- 2geoping
    - a_main.sh
        - geoping focus on mapping the ingest server to the VPN with most similar fingerprint
        - In the script, for each ingest server, it will compute the RTT between the ingest server and all VPN to form an target fingerprint, and compute the RTT between a VPN and all the VPN to form a LM fingerprint, and it will form 82 LM fingerprint. 
And we store the euclidean distance between the target fingerprint and each LM fingerprint to **diff**, and then sort the VPN according to the diff from low to high. 
        - **xdg-open 2Geoping.ods** to get the geoping result
- 3shortest_dist
    - a_main.sh
        - **get_distance_by_latlong.sh** # get distance betwenen VPN each other by latitude and longitude
        - **generate_input.sh** # for each VPN, we get the RTT and distance to all VPN
            - **predict_dist.sh** # generate bestline, and use bestline to predict target distance from target RTT
        - **generate_dist.sh** # sort the VPN according to the predict target distance from low to high
        - **generate_dist_rank.sh** # rank each VPN according to the predict target distance from low to high
        - **xdg-open 3Shortest_dist.ods** to get the shortest distance result
        
- 4CBG
    - a_main.sh
        - **CBGcompute.sh** # CBGcompute will predict target distance to get how many circle covers of each VPN
        - **a_generate_cover_rank.sh** # compute each VPN's cover rank according to the circle cover count
        - **map.sh** # plot the circle covers on the map
        - **point_for_pureCBG.sh** # for each VPN's cover rank we give cover point, if cover point is the same, compare dist point according shortest distance method
        - **aa_generate_sorted_point_for_PureCBG.sh** # rank VPN according to total point from high to low and mark cover count
        - **xdg-open 4CBG.ods** to get the CBG result

- 5Hybrid1
    - a_main.sh
        - **point1.sh** # we give a scaled score for Hybird1 method, we have each VPN's cover rank and short distance rank, then we convert them by the scaled score to cover point and short distance point, and then add the two point to get the total point of each VPN.
        - **aa_generate_sorted_point.sh** # rank VPN according to total point from high to low
        - **xdg-open 5Hybrid1.ods** to get the Hybrid1 result
- 6Hybrid2
    - a_main.sh
        - **point2.sh** # Hybrid2 two's procedure is the same as Hybrid1 method, the only different is the scaled score
        - **xdg-open 5Hybrid1.ods** to get the Hybrid2 result
## Step 4
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

---
## README.txt要補充的# 說明稿

## Step 1
- nordvpn_list_get
    - a_main.sh
        - we can use the command to crawl the raw information of Nordvpn. And we arrange some required properties the VPN list. 
    [RUN 不用拍, 前後有錄就好]
    - lvpn_location_list.txt
        - we classify the VPN into the list according to the different vpn server location. there are 87 locations, and in each location, the value are lattitude and longitude, the two are country and city, and the value is the number of vpn servers, and the following are the domain name of the vpn servers.
    - a_reset.sh
        - it will remove the output file. if you want redo the experiment, then you can run the file and then run a_main.sh again. 
        - Besides, the all the experiments I will introduce later will have a_main.sh and a_reset.sh for you to redo the experiment.
        
- Traffic1_Nslab_VPN
    - a_main.sh
        - we ping each vpn from NSLAB and use tcpdump to intercept the traffic and save to pcapfile. The example show ping 3 vpn for 10 second. [RUN要拍] and we finally get 3 pcapfile

- Traffic2_VPN_ingest
    - a_main.sh
        - first we should reset the obs to the first ingest server as our target. this example show using 3 vpn to probe 3 ingest server. 
        - **ldetet_and_test_example.sh** this script will get the traffic between the pair of vpn and ingest server
        - after getting the pair of an ingest server and all vpn, it will **switch** to next ingest server by obs
        - [RUN要拍] (講解可能另外錄)

- Traffic3_VPN_VPN
    - a_main.sh
        - the example use 3 VP_vpn to ping 3 LM_vpn and use tcpdump to intercept the traffic and save to pcapfile. [Run要拍]
        
## Step 2
- RTT1 - example
    - a_main.sh
        - the example compute the RTT of the three pcapfile we get. First we convert the pcapfile to text file for easy operation.
        - if your host is in the nslab, then the host ip should change to the nslab ip.
        - and we use rtt.py to get the minimum rtt of each file
        - [RUN 結果要展示 finally we get the min RTT of each file]
    - Besides, the file RTT1_for_RTT2.txt RTT1_for_RTT3.txt are RTT1 between NSLAB and 82 VPN in my experiment for subtraction.
- RTT2
    - pcapfile - aconvert_totxt.sh
        - we want to get compute the RTT of all pair between 82 VPN and 60 ingest server. First we use the script to convert the pcapfile to text file for easy operation
    - txtfile
        - a_main.sh
            - after the conversion, the for loop will compute the RTT, but the RTT include the RTT1. So we run the following script **a_get_adjusted_RTT.sh** to minus RTT1 from the RTT and adjust the RTT to nonnegative value.
            -  [excel] finally in this file we get the RTT of each VPN_ingest pair.

- RTT3
    - pcapfile - aconvert_totxt.sh
        - we want to get compute the RTT of all pair between 82 VPN each other, and use the script to convert the pcapfile to text file.
    - txtfile
        - a_main.sh
            - like getting RTT2, the for loop compute the RTT, and use **a_get_adjusted_RTT.sh.sh** to minus RTT1 from the RTT and adjust the RTT to nonnegative value.
            - [excel] finally in the file we get the RTT between VPN each other

## Step 3
- 1shortest_ping
    - a_main.sh
        - shortest ping focus on mapping the ingest server to the VPN with smallest RTT. 
for each ingest server, it will sort VPN according to the RTT from low to high.
        - [RUN]
        - **xdg-open 1shortest_ping.ods** to get the shortest ping result
- 2geoping
    - a_main.sh
        - geoping focus on mapping the ingest server to the VPN with most similar fingerprint
        - In the script, for each ingest server, it will compute the RTT between the ingest server and all VPN to form an target fingerprint, and compute the RTT between a VPN and all the VPN to form a LM fingerprint, and it will form 82 LM fingerprint. 
And we store the euclidean distance between the target fingerprint and each LM fingerprint to **diff**, and then sort the VPN according to the diff from low to high. 
        - **xdg-open 2Geoping.ods** to get the geoping result
- 3shortest_dist
    - a_main.sh
        - **get_distance_by_latlong.sh** # get distance betwenen VPN each other by latitude and longitude
        - **generate_input.sh** # for each VPN, we get the RTT and distance to all VPN
            - **predict_dist.sh** # generate bestline, and use bestline to predict target distance from target RTT
        - **generate_dist.sh** # sort the VPN according to the predict target distance from low to high
        - **generate_dist_rank.sh** # rank each VPN according to the predict target distance from low to high
        - **xdg-open 3Shortest_dist.ods** to get the shortest distance result
        
- 4CBG
    - a_main.sh
        - **CBGcompute.sh** # CBGcompute will predict target distance to get how many circle covers of each VPN
        - **a_generate_cover_rank.sh** # compute each VPN's cover rank according to the circle cover count
        - **map.sh** # plot the circle covers on the map
        - **point_for_pureCBG.sh** # for each VPN's cover rank we give cover point, if cover point is the same, compare dist point according shortest distance method
        - **aa_generate_sorted_point_for_PureCBG.sh** # rank VPN according to total point from high to low and mark cover count
        - **xdg-open 4CBG.ods** to get the CBG result

- 5Hybrid1
    - a_main.sh
        - **point1.sh** # we give a scaled score for Hybird1 method, we have each VPN's cover rank and short distance rank, then we convert them by the scaled score to cover point and short distance point, and then add the two point to get the total point of each VPN.
        - **aa_generate_sorted_point.sh** # rank VPN according to total point from high to low
        - **xdg-open 5Hybrid1.ods** to get the Hybrid1 result
- 6Hybrid2
    - a_main.sh
        - **point2.sh** # Hybrid2 two's procedure is the same as Hybrid1 method, the only different is the scaled score
        - **xdg-open 5Hybrid1.ods** to get the Hybrid2 result
## Step 4
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

---
## README.txt要補充的
 1. 每個資料夾都有a_main.sh and a_reset.sh
 2. .sh檔用bash執行檔案 e.g. bash a_main.sh
 3. .py用python3執行檔案 e.g. python3.performance.py

 1. 每個資料夾都有a_main.sh and a_reset.sh
 2. .sh檔用bash執行檔案 e.g. bash a_main.sh
 3. .py用python3執行檔案 e.g. python3.performance.py
