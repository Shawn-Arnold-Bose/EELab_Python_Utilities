#!/usr/bin/python3

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

    np_list = svlst.get_list_ntpq(dv_list)
    svlst.get_ntpqname(np_list)
    print("\nNetPREQ List:")
    for item in np_list:
        print(item)

    print("Python Script: END")
    sys.exit(0)

# ---------------------------------------------------------------------------- #
