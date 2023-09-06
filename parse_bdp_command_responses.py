#!/usr/bin/python3

import sys

# ============================================================================ #

def xlt_sHex_to_sChr( my_strHex, truncate = False ) :
   end = len(my_strHex)
   my_strChr = str( )
   idx = 0
   while( end - idx ) :
      xxx = "0x" + my_strHex[idx:idx+2]     # hex value string
      yyy = int(xxx,16)                     # integer equivalent
      # truncate would be used in the case of a NULL terminated string
      if ( truncate and ( yyy == 0 ) ) :
         break
      if ( (yyy >= 32) and (yyy <= 126) ) :
         zzz = chr(yyy)                     # single character
      else :
         zzz = '#'
      my_strChr = my_strChr + zzz           # build string of characters
      idx = idx + 2
   return ( my_strChr )

# ---------------------------------------------------------------------------- #
# Cypher Out NetPREQ ID Information

def get_netpreq_info_block(info_block_str):

    info_block_lst = list()
    # info_block_str = read_netpreq_info_block(netpreq_ip_address, 0x00000000, 62)
    if len(info_block_str) != 124:
        return info_block_lst

    # 0    4    8            20                                       60
    # |    |    |            |                                        |                                                                124
    # 5c5c.0001.00502e000001.313431375f303731323232000000000000000000.X                                                                |
    # 5c5c.0001.00502e000001.313431375f303731323232000000000000000000.65656c616262656e636831000000000000000000000000000000000000000000.X

    # magic		= info_block_str[  0:  4]		int
    # version	= info_block_str[  4:  8]		int
    # mac		= info_block_str[  8: 20]		string
    # label		= info_block_str[ 20: 60]		string
    # hostname	= info_block_str[ 60:124]		string

    magic = int("0x" + info_block_str[0:4], 16)
    version = int(info_block_str[4:8], 16)
    mac = (
        info_block_str[8:10]
        + ":"
        + info_block_str[10:12]
        + ":"
        + info_block_str[12:14]
        + ":"
        + info_block_str[14:16]
        + ":"
        + info_block_str[16:18]
        + ":"
        + info_block_str[18:20]
    )
    label = xlt_sHex_to_sChr(info_block_str[20:60], True)
    hostname = xlt_sHex_to_sChr(info_block_str[60:124], True)

    # print( "magic   : {:04X} = {:6d}".format(magic , magic) )
    # print( "version : {:04X} = {:6d}".format(version , version) )
    # print( "mac     : {:<s}".format(mac) )
    # print( "label   :", label )
    # print( "hostname:", hostname )

    if (magic == 0x5C5C) and (version == 1):
        # all good
        info_block_lst = [magic, version, mac, label, hostname]
    elif (magic == 0xFFFF) and (version == 0xFFFF):
        # uninitialized eeprom
        info_block_lst = [magic, version, "00:12:34:45:78:9a", "", "magdalene"]
    # else :
    # any other issues

    # print( "NetPREQ Name:", info_block_lst )

    # if len(info_block) != 5:
    #     return "UNKNOWN"
    # else:
    #     return info_block[4]
    return info_block_lst

# ---------------------------------------------------------------------------- #

def parse_command_response_data( bdp_cmd, bdp_dat) :

    if   bdp_cmd == "Gn" :
        # print( "Gn: Read NVRAM" )
        return ( get_netpreq_info_block(bdp_dat) )

    elif bdp_cmd == "GV" :
        # print( "GV: Firmware Version" )
        answer = xlt_sHex_to_sChr( bdp_dat )
        return ( answer )

    elif bdp_cmd == "Gj" :
        # print( "\nGj: Sample Rate" )
        # print( "type:", type(bdp_dat))
        # print( "length data:", len(bdp_dat))
        # print( "data:", bdp_dat)
        answer = int( bdp_dat, 16 )
        # print( "type:", type(answer))
        # print( "answer:", answer)
        return ( answer )

    # elif bdp_cmd == "XX" :
    #     print( "type:", type(bdp_dat))
    #     print( "length data:", bdp_dat)
    #     answer = xlt_sHex_to_sChr( bdp_dat )
    #     print( "type:", type(answer))
    #     print( "answer:", answer)

    else                 :
        print( "That does not compute!" )


# ============================================================================ #

if __name__ == '__main__' :

    print("Python Script: BGN")

    print("Python Script: END")
    sys.exit(0)
    
# ---------------------------------------------------------------------------- #
