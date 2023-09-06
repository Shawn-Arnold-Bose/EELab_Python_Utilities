#!/usr/bin/python3

G_CMND = "ip"
G_OPTN = "neigh"
G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+eth\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"
# G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+enp7s\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"

G_MAC_UNPROG_NTPQ = "00:12:34:56:78:9a"
G_MAC_PREFIX_NTPQ = "^00:50:2e:"
G_MAC_PREFIX_PREQ = "^1c:1b:0d:"

import sys
import re
import shell_command as shcmd
import bdp_over_ethernet as boe
import parse_bdp_command_responses as pcr

# ============================================================================ #

def get_list_full( ) :
    lines = shcmd.shell_command( [G_CMND, G_OPTN] )
    device_list = list()
    for line in lines:
        # print( "line:", line )
        tst = re.match(G_MAC_MATCH, line)
        # group(1) = IP address
        # group(2) = univeral address OR eeprom prefix address
        if tst:
            # print( "HIT:", line)
            mac_in_eeprom = tst.group(2)[0:9]
            # print( tst.group(1), tst.group(2), mac_in_eeprom )
            device_list.append([tst.group(2), tst.group(1), "undetermined"])

    return device_list

# ---------------------------------------------------------------------------- #
# Parse the Shell Command Response

def get_list_ntpq( dev_list ) :
    ntpq_list = list()
    for dev in dev_list:
        # print( "dev:", dev )
        # dev[0] = MAC address
        # dev[1] = IP address
        # dev[2] = Hostname
        if (dev[1] == G_MAC_UNPROG_NTPQ) or (re.match(G_MAC_PREFIX_NTPQ, dev[0])):
            # print( "HIT:", dev)
            ntpq_list.append(dev)
    return ntpq_list

# ---------------------------------------------------------------------------- #
# Parse the Shell Command Response

def get_list_pcpq( dev_list ) :
    pcpq_list = list()
    for dev in dev_list:
        # print( "dev:", dev )
        # dev[0] = MAC address
        # dev[1] = IP address
        # dev[2] = Hostname
        if re.match(G_MAC_PREFIX_PREQ, dev[0]) :
            # print( "HIT:", dev)
            pcpq_list.append(dev)
    return pcpq_list

# ---------------------------------------------------------------------------- #
# Parse the Shell Command Response

def get_list_lptp( dev_list, mach_list ) :
    xxxx_list = dev_list.copy()
    lptp_list = list()
    for mch in mach_list:
        # print( len(xxx_list) )
        for dev in xxxx_list:
            # print( "dev:", dev )
            # dev[0] = MAC address
            # dev[1] = IP address
            # dev[2] = Hostname
            if mch == dev[0] :
                # print( "HIT:", dev)
                xxxx_list.remove(dev)
                lptp_list.append(dev)
    return lptp_list

# ---------------------------------------------------------------------------- #
# 

def get_hostname( dev_list ) :
    for dev in dev_list:
        # print( "dev:", dev )
        # dev[0] = MAC address
        # dev[1] = IP address
        # dev[2] = Hostname
        # response = shell_command( "nslookup " + dev[1] )
        response = shcmd.shell_command( ["nslookup", dev[1]] )
        # print( response )
        for line in response :
            # print( "Line::", line )
            # tst = re.match("name = \S+\.bose\.com", line)
            # tst = re.match(".name", line)
            tst = re.match(".+name = (\S+)\.bose\.com", line)
            if tst:
                # print( "HIT!" )
                hostname = tst.group(1)
                # print( "HIT!", hostname )
                dev[2] = hostname
                # break
    return

# ---------------------------------------------------------------------------- #
# 

def get_ntpqname( dev_list ) :
    for dev in dev_list:
        # print( "dev:", dev )
        bdp_data = boe.bdp_response_data("?Gn00000000003E", dev[1])
        # print( "BDP: Data:", bdp_data )
        xxx = pcr.parse_command_response_data( "Gn", bdp_data)
        # print( "NetPREQ Name:", xxx[4] )
        dev[2] = xxx[4]
        # print( "NetPREQ Name:", xxx )

    return

# ============================================================================ #

if __name__ == '__main__' :

    print("Python Script: BGN")

    dv_list = get_list_full()
    # print("Device List")
    # for item in dv_list:
    #     print(item)

    pq_list = get_list_pcpq(dv_list)
    get_hostname(pq_list)
    print("PC-PREQ List")
    for item in pq_list:
        print(item)

    print( "length bfr:", len(dv_list) )
    test_list = ["10:65:30:b9:1a:22", "98:e7:43:cd:16:3b"]
    lt_list = get_list_lptp(dv_list, test_list)
    get_hostname(lt_list)
    print("Laptop List")
    for item in lt_list:
        print(item)
    print( "length aft:", len(dv_list) )

    np_list = get_list_ntpq(dv_list)
    get_ntpqname(np_list)
    print("NetPREQ List")
    for item in np_list:
        print(item)

    print("Python Script: END")
    sys.exit(0)

# ---------------------------------------------------------------------------- #
