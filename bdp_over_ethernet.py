#!/usr/bin/python3

DEFAULT_NETPREQ_IP = 49152

import sys
import socket

# ============================================================================ #
# BDP over ethernet

def bdp_over_ethernet( bdp_command, ip_adrs, ip_port = DEFAULT_NETPREQ_IP ) :

    print( "bdp_command:", bdp_command )
    print( "ip_adrs:", ip_adrs )
    print( "ip_port:", ip_port )

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

# ============================================================================ #

if __name__ == '__main__' :

    netpreq_ip_adrs = sys.argv[1]
    bdp_cmd = sys.argv[2]
    netpreq_ip_port = DEFAULT_NETPREQ_IP

    print( "Cmd:", bdp_cmd )
    bdp_rsp = bdp_over_ethernet( bdp_cmd, netpreq_ip_adrs )
    print( "Rsp:", bdp_rsp )

    sys.exit(0)
    
# ---------------------------------------------------------------------------- #
