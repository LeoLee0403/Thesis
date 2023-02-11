bash get_distance_by_latlong.sh # get distance betwenen VPN each other by latitude and longitude
bash generate_input.sh # for each VPN, get the RTT and distance to all the VPN
bash predict_dist.sh # generate bestline, and use bestline to predict target distance from target RTT
bash generate_dist.sh # sort the VPN according to the predict target distance from low to high
bash generate_dist_rank.sh # rank each VPN according to the predict target distance from low to high
bash toex_dist.sh
bash toex.sh

# xdg-open 3Shortest_dist.ods