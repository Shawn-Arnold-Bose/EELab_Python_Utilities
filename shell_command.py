#!/usr/bin/python3

import sys
import subprocess
from subprocess import Popen

# ============================================================================ #
# execute a shell command and capture the response

def shell_command_XXX( shell_command_str ) :
    # print( "Command:", shell_command_str )
    response = subprocess.check_output( shell_command_str, shell=True, universal_newlines=True )
    # print( "Respnse:", response )
    lines = response.split("\n")
    # for line in lines:
    #     print( "line:", line )
    return lines

# ---------------------------------------------------------------------------- #
# execute a shell command and capture the response

def shell_command( shell_command_lst ) :
    # print( "Command:", shell_command_lst )
    proc = Popen( shell_command_lst, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
    exit_status = proc.wait()
    (stdo_response, stde_errors) = proc.communicate()
    # print( "Respnse:", stdo_response )
    # type(exit_status) )   ==> int
    # type(stdo_response) ) ==> str
    # type(stde_errors) )   ==> str
    # print( "[p = Popen] exit_status:", exit_status )
    # print( "[p = Popen] exit_status:", proc.returncode )
    # print( "exit_status  :", exit_status )
    # print( "stdo_response:\n", stdo_response, "#" )
    # print( "stde_errors  :\n", stde_errors, "#" )
    return ( stdo_response.split("\n") )

# ============================================================================ #

G_CMD = "ip"
G_OPT = "neigh"

if __name__ == '__main__' :

    print("Python Script: BGN")

    lines = shell_command( [G_CMD, G_OPT] )
    for line in lines:
        print( "line:", line )

    print("Python Script: END")
    sys.exit(0)

# ---------------------------------------------------------------------------- #
