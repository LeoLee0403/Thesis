# Thesis

## Step 1
- nordvpn_list_get
    - a_main.sh
        - we can use the command to crawl the raw information of Nordvpn. And we arrange some required properties the VPN list. 
    [RUN 不用拍, 前後有錄就好]
    - lvpn_location_list.txt
        - we classify the VPN into the list according to the different vpn server location. there are 87 locations, and in each location, the value are lattitude and longitude, the two are country and city, and the value is the number of vpn servers, and the following are the domain name of the vpn servers.
    - a_reset.sh
        - it will remove the output file. if you want redo the experiment, then you can run the file and then run a_main.sh again.
        
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
- 4CBG
- 5Hybrid1
- 6Hybrid2

## Step 4


---
## README.txt要補充的
 1. 每個資料夾都有a_main.sh and a_reset.sh
 2. .sh檔用bash執行檔案 e.g. bash a_main.sh
 3. .py用python3執行檔案 e.g. python3.performance.py
