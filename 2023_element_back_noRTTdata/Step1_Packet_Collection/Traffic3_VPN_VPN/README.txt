1.  This script connect nordvpn by "nordvpn connect ${VP_VPN}" 
    VP_VPN is the [first domain] in each location in lvpn_location_list_2023.txt
    for example, first location's VP_VPN is pl128, and second location's VP_VPN is be148
    but somtimes nordvpn does not allow us connect the VPN with specific domain.
    If this case happens unfortunately, try to make VP_VPN = [city name].
    In above two case will be "nordvpn connect Warsaw" and "nordvpn connect Brussels" and you need to modify ping_other_vpn.sh