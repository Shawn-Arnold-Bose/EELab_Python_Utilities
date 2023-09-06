#!/usr/bin/python
# ============================================================================ #

import sys

# ============================================================================ #

bdp_response_codes = [
( "BDP_SUCCESS"              , "Command Successful"                       ), #  0
( "BDP_FAILED"               , "Command Failed"                           ), #  1
( "INVALID_SINK"             , "Invalid Sink"                             ), #  2
( "INVALID_LENGTH"           , "Invalid Command Length"                   ), #  3
( "INVALID_DATA"             , "Invalid Data"                             ), #  4
( "QUERY_NOT_SUPPORTED"      , "Query Not Supported"                      ), #  5
( "OUT_OF_RANGE"             , "Value out of Range"                       ), #  6
( "CHIME_ID_OUT_OF_RANGE"    , "Selected chime ID out of range"           ), #  7
( "CHIME_CANCELLED"          , "Currently active chime cancelled"         ), #  8
( "CHIME_IN_PROGRESS"        , "Chime currently in progress"              ), #  9
( "TYPE_UNSUPPORTED"         , "Command Type not supported"               ), # 10
( "COMMAND_NOT_FOUND"        , "Command not Found"                        ), # 11
( "POWERING_DOWN"            , "Starting power down"                      ), # 12
( "POWER_DOWN_INHIBITED"     , "Power down inhibited"                     ), # 13
( "POWER_DOWN_UNINHIBITED"   , "Power down unInhibited"                   ), # 14
( "INVALID_DSP_COUNT"        , "Invalid DSP read/write count"             ), # 15
( "INVALID_DSP"              , "DSP Selection invalid"                    ), # 16
( "INVALID_DSP_MEM"          , "DSP memory selection invalid"             ), # 17
( "INVALID_PASSWORD"         , "Invalid Password"                         ), # 18
( "DTC_NOT_SUPPORTED"        , "DTC not supported"                        ), # 19
( "EEPROM_WRITE_FAILED"      , "Failed to store data in persistant memory"), # 20
( "ODD_ADDRESS"              , "Argument points to odd address"           ), # 21
( "SUB_COMMAND_NOT_SUPPORTED", "SubCommand not supported"                 ), # 22
]

# ============================================================================ #

def get_table_entry(index) :
    # print ( "def: name of module:", __name__ )
    sts = 0
    if index <= (len( bdp_response_codes ) - 2) :
        # SUCCESS
        sts = 0
        index = index
    else :
        # FAILURE
        sts = 1
        index = len( bdp_response_codes ) - 1
    return( [ sts, bdp_response_codes[index] ] )

# ============================================================================ #

if __name__ == '__main__' :

    print ( len( bdp_response_codes ) )

    print( "\n" + 32 * "-" )
    i = 0
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 17
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 21
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 22
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 23
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 24
    print( i )
    ttt = get_table_entry(i)
    print( ttt )
    print( ttt[0], ttt[1] )

    print ('name of module:',__name__)
    print ('name of imported module:', sys.__name__)
    
    sys.exit( 0 )

# ============================================================================ #
