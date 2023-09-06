#!/usr/bin/python3

DEFAULT_NETPREQ_IP = 49152

import sys
import socket

import response_codes_dms as dms
import response_codes_bdp as bdp


# ============================================================================ #
# BDP over ethernet

def bdp_over_ethernet( bdp_command, ip_adrs, ip_port = DEFAULT_NETPREQ_IP ) :

    # print( "bdp_command:", bdp_command )
    # print( "ip_adrs:", ip_adrs )
    # print( "ip_port:", ip_port )

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ip_adrs, ip_port))

    outgoing_msg = bdp_command + "\r\0"
    mysock.send(outgoing_msg.encode())

    incoming_msg = ""
    while True:
        data = mysock.recv(4)
        xxx = data.decode()
        incoming_msg = incoming_msg + xxx
        if xxx[len(xxx) - 1] == "\0":
            incoming_msg = incoming_msg.strip("\0")
            break

    mysock.close()

    return incoming_msg.strip("\n")

# ---------------------------------------------------------------------------- #

def bdp_parse_response( bdp_rsp ) :

    rsp_cmd = bdp_rsp[1:3]
    rsp_bdp = int( bdp_rsp[3: 5],16 )        # BDP error code
    rsp_pof = int( bdp_rsp[5: 7],16 ) & 0xC0 # Pass or Fail
    rsp_dms = int( bdp_rsp[5: 7],16 ) & 0x2F # Module error code
    rsp_dat = bdp_rsp[7:].strip()
    # print(rsp_cmd, rsp_bdp, rsp_pof, rsp_dms, rsp_dat)
    return [rsp_cmd, rsp_bdp, rsp_pof, rsp_dms, rsp_dat]

# ---------------------------------------------------------------------------- #

def bdp_response_data( bdp_cmd, netpreq_ip_adrs ) :

    # print( "Cmd:", bdp_cmd )
    bdp_rsp = bdp_over_ethernet( bdp_cmd, netpreq_ip_adrs )
    # print( "Rsp:", bdp_rsp )
    xxx_list = bdp_parse_response(bdp_rsp)
    # print( "Lst:", bdp_rsp )
    return(xxx_list[4])



# ---------------------------------------------------------------------------- #

def bdp_response_report( rsp_list ) :
    # Success
    if ( (rsp_list[2] == 0x40) and (rsp_list[1] == 0) ) :
        print( "SUCCESS" )
    # Failure
    else :
        print( "FAILURE" )
    return

# ============================================================================ #

if __name__ == '__main__' :

    netpreq_ip_adrs = sys.argv[1]
    bdp_cmd = sys.argv[2]
    netpreq_ip_port = DEFAULT_NETPREQ_IP

    # print( "Cmd:", bdp_cmd )
    bdp_rsp = bdp_over_ethernet( bdp_cmd, netpreq_ip_adrs )
    # print( "Rsp:", bdp_rsp )
    xxx_list = bdp_parse_response(bdp_rsp)

    bdp_response_report( xxx_list )

    print( "Rsp:", xxx_list )
    ttt = bdp.get_table_entry(xxx_list[1])
    print( ttt )
    ttt = dms.get_table_entry(xxx_list[3])
    print( ttt )

    data = bdp_response_data( bdp_cmd, netpreq_ip_adrs )
    print( "Data:", data )

    sys.exit(0)
    
# ---------------------------------------------------------------------------- #
