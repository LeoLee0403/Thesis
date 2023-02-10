# 說明稿

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
