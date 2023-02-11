cp -r predict_target_dist/* .
bash a_generate_cover_rank.sh # compute each VPN's cover rank according to the circle cover count
bash map.sh # plot the circle cover on the map
bash to_cover_rank.sh 
bash toex_rank.sh

# for each rank give cover point(increase with cover count increase), if cover point is the same, 
# compare dist point(increase with prediect target distance decrease)
bash point_for_pureCBG.sh 

bash aa_generate_sorted_point_for_PureCBG.sh # rank VPN according to total point from high to low and mark cover count
bash toex_PureCBG.sh