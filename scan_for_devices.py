#!/usr/bin/python3

G_COMMAND = "ip"
G_OPTION = "neigh"
G_MAC_UNIVERSAL = "00:12:34:56:78:9a"
G_MAC_EEPROM = "00:50:2e:"
# G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+enp7s\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"
G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+eth\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"

import sys
import device_lists as svlst

# ============================================================================ #

mach_list = ["10:65:30:b9:1a:22", "98:e7:43:cd:16:3b"]

# ============================================================================ #

if __name__ == '__main__' :

    print("Python Script: BGN")

    dv_list = svlst.get_list_full()
    # print("Device List:")
    # for item in dv_list:
    #     print(item)

    np_list = svlst.get_list_ntpq(dv_list)
    print("\nNetPREQ List:")
    for item in np_list:
        print(item)

    pq_list = svlst.get_list_pcpq(dv_list)
    svlst.get_hostname(pq_list)
    print("\nPC-PREQ List:")
    for item in pq_list:
        print(item)

    lt_list = svlst.get_list_lptp(dv_list, mach_list)
    svlst.get_hostname(lt_list)
    print("\nLaptop List:")
    for item in lt_list:
        print(item)

    print("Python Script: END")
    sys.exit(0)

# ---------------------------------------------------------------------------- #
