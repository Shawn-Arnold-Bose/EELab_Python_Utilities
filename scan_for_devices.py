#!/usr/bin/python3

G_COMMAND = "ip"
G_OPTION = "neigh"
G_MAC_UNIVERSAL = "00:12:34:56:78:9a"
G_MAC_EEPROM = "00:50:2e:"
# G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+enp7s\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"
G_MAC_MATCH = "^(\d+\.\d+\.\d+\.\d+)\s+dev\s+eth\d+\s+lladdr\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+"

DEFAULT_NETPREQ_IP = 49152

import sys
import subprocess
from subprocess import Popen
import re

# ============================================================================ #
# execute a shell command and return response

def shell_command_XXX( shell_command_str ) :
    # print( "Command:", shell_command_str )
    response = subprocess.check_output( shell_command_str, shell=True, universal_newlines=True )
    # print( "Respnse:", response )
    lines = response.split("\n")
    # for line in lines:
    #     print( "line:", line )
    return lines

# ---------------------------------------------------------------------------- #

def shell_command( shell_command_lst ) :
    print( "Command:", shell_command_lst )
    proc = Popen( shell_command_lst, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
    exit_status = proc.wait()
    (stdo_response, stde_errors) = proc.communicate()
    print( "Respnse:", stdo_response )
    # type(exit_status) )   ==> int
    # type(stdo_response) ) ==> str
    # type(stde_errors) )   ==> str
    # print( "[p = Popen] exit_status:", exit_status )
    # print( "[p = Popen] exit_status:", proc.returncode )
    # print( "exit_status  :", exit_status )
    # print( "stdo_response:\n", stdo_response, "#" )
    # print( "stde_errors  :\n", stde_errors, "#" )
 
    # return ( stdo_response )
    return ( stdo_response.split("\n") )

# ---------------------------------------------------------------------------- #

def get_list_full( ) :
    # lines = shell_command( G_COMMAND + " " + G_OPTION )
    lines = shell_command( [G_COMMAND, G_OPTION] )
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
        if (dev[1] == G_MAC_UNIVERSAL) or (re.match("^00:50:2e:", dev[0])):
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
        if re.match("^1c:1b:0d:", dev[0]) :
            # print( "HIT:", dev)
            pcpq_list.append(dev)
    return pcpq_list

# ---------------------------------------------------------------------------- #
# Parse the Shell Command Response

mach_list = ["10:65:30:b9:1a:22", "98:e7:43:cd:16:3b"]

def get_list_lptp( dev_list ) :
    xxx_list = dev_list.copy()
    lptp_list = list()
    for mch in mach_list:
        # print( len(xxx_list) )
        for dev in xxx_list:
            # print( "dev:", dev )
            # dev[0] = MAC address
            # dev[1] = IP address
            # dev[2] = Hostname
            if mch == dev[0] :
                # print( "HIT:", dev)
                xxx_list.remove(dev)
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
        response = shell_command( ["nslookup", dev[1]] )
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

# ============================================================================ #

if __name__ == '__main__' :

    print("Python Script: BGN")

    dv_list = get_list_full()
    # print("Device List")
    # for item in dv_list:
    #     print(item)

    np_list = get_list_ntpq(dv_list)
    print("NetPREQ List")
    for item in np_list:
        print(item)

    pq_list = get_list_pcpq(dv_list)
    # print("PC-PREQ List")
    # for item in pq_list:
    #     print(item)
    get_hostname(pq_list)
#    for item in pq_list:
#        print(item)

    # print( "length bfr:", len(dv_list) )
    lt_list = get_list_lptp(dv_list)
    # print("Laptop List")
    # for item in lt_list:
    #     print(item)
    # print( "length aft:", len(dv_list) )
    get_hostname(lt_list)
#    for item in lt_list:
#        print(item)

    print("Python Script: END")
    sys.exit(0)

# ---------------------------------------------------------------------------- #
