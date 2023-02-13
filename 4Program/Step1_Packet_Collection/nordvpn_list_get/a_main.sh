# crawl nordvpn information
curl --silent "https://api.nordvpn.com/v1/servers?limit=50000" | jq > nordvpn_raw.txt

# get required properties
cat nordvpn_raw.txt | grep -B 2 country | grep -E "lat|long" | cut -d ':' -f 2 | cut -d ' ' -f 2 | cut -d ',' -f 1 > lat_long.txt
cat nordvpn_raw.txt | grep -A 3 country | grep name | cut -d '"' -f 4 > country.txt
cat nordvpn_raw.txt | grep -v "dns_name" | grep -A 2 city | grep name | cut -d '"' -f 4 > city.txt
cat nordvpn_raw.txt | grep hostname | cut -d '"' -f 4 | cut -d '.' -f 1 > domain.txt

# form the nordvpn list
python3 list_vpn.py > lvpn_location_list_2023.txt 

exit 0