ls | grep count_ | grep .txt | xargs rm
ls | grep a_cover_rank | grep .txt | xargs rm
ls | grep map_ | grep .html | xargs rm
ls | grep predict_ | grep dist.txt | xargs rm

rm cover_rank.txt
rm cover.txt
rm avpns_lat.txt
rm avpns_long.txt
rm predict_as_radius.txt
rm excel_rank.txt

ls | grep a_point_ | xargs rm
ls | grep a_sorted_point | xargs rm
rm Hybrid_excel.txt
rm excel.txt
rm point.txt
rm cover_count.txt
rm my_cover_rank.txt
rm my_dist_rank.txt
rm one_col_count.txt
rm now_ingest.txt
rm 4CBG.ods