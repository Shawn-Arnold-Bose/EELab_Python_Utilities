#!/usr/bin/python
# ============================================================================ #

import sys

# ============================================================================ #

dms_response_codes = [
# I2C (TWSI) errors
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), #  0
( "I2C_WRITE_ERROR"         , "I2C_WRITE_ERROR"         ), #  1
( "I2C_READ_ERROR"          , "I2C_READ_ERROR"          ), #  2
( "I2C_BUS_BUSY"            , "I2C_BUS_BUSY"            ), #  3
( "I2C_NO_ACK"              , "I2C_NO_ACK"              ), #  4
( "I2C_TIMEOUT"             , "I2C_TIMEOUT"             ), #  5
( "I2C_BAD_BUFFER_PTR"      , "I2C_BAD_BUFFER_PTR"      ), #  6
( "I2C_ILLEGAL_PORT"        , "I2C_ILLEGAL_PORT"        ), #  7
# SPI errors
( "SPI_SIZE_ERROR"          , "SPI_SIZE_ERROR"          ), #  8
( "SPI_NULL_POINTER"        , "SPI_NULL_POINTER"        ), #  9
( "SPI_TIMEOUT"             , "SPI_TIMEOUT"             ), # 10
( "SPI_INVALID_COMMAND"     , "SPI_INVALID_COMMAND"     ), # 11
( "SPI_INVALID_ID"          , "SPI_INVALID_ID"          ), # 12
( "SPI_FAR_POINTER"         , "SPI_FAR_POINTER"         ), # 13
( "SPI_UNAVAILABLE"         , "SPI_UNAVAILABLE"         ), # 14
( "SPI_OVERRUN"             , "SPI_OVERRUN"             ), # 15
# DSP
( "DSP_CMD_CONFLICT"        , "DSP_CMD_CONFLICT"        ), # 16
( "DSP_INVALID_COMMAND"     , "DSP_INVALID_COMMAND"     ), # 17
( "DSP_MORE_DATA"           , "DSP_MORE_DATA"           ), # 18
( "DSP_CHECKSUM_ERROR"      , "DSP_CHECKSUM_ERROR"      ), # 19
( "DSP_INVALID_ID"          , "DSP_INVALID_ID"          ), # 20
( "DSP_BOOT_ERROR"          , "DSP_BOOT_ERROR"          ), # 21
( "DSP_TIMEOUT"             , "DSP_TIMEOUT"             ), # 22
( "DSP_BAD_DOWNLOAD"        , "DSP_BAD_DOWNLOAD"        ), # 23
# NVRAM
( "NVRAM_TIMEOUT"           , "NVRAM_TIMEOUT"           ), # 24
( "NVRAM_HW_FAIL"           , "NVRAM_HW_FAIL"           ), # 25
( "NVRAM_INVALID_TASK"      , "NVRAM_INVALID_TASK"      ), # 26
( "NVRAM_SHUTTING_DOWN"     , "NVRAM_SHUTTING_DOWN"     ), # 27
( "NVRAM_ADDRESS_OOR"       , "NVRAM_ADDRESS_OOR"       ), # 28
( "NVRAM_NULL_POINTER"      , "NVRAM_NULL_POINTER"      ), # 29
( "NVRAM_MULTIPLE_REQUEST"  , "NVRAM_MULTIPLE_REQUEST"  ), # 30
( "NVRAM_DEVICE_BUSY"       , "NVRAM_DEVICE_BUSY"       ), # 31
# DTCP errors
( "DTCP_TOO_MUCH_DATA"      , "DTCP_TOO_MUCH_DATA"      ), # 32
( "DTCP_SESSION_EXISTS"     , "DTCP_SESSION_EXISTS"     ), # 33
( "DTCP_BAD_MESSAGE"        , "DTCP_BAD_MESSAGE"        ), # 34
( "DTCP_MSG_WONT_FIT"       , "DTCP_MSG_WONT_FIT"       ), # 35
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 36
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 37
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 38
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 39
# Drivers errors
( "AMPLIFIER_INVALID_DEVICE", "AMPLIFIER_INVALID_DEVICE"), # 40
( "CODEC_INVALID_DEVICE"    , "CODEC_INVALID_DEVICE"    ), # 41
( "MUX_INVALID_DEVICE"      , "MUX_INVALID_DEVICE"      ), # 42
( "AO_REQUEST_UNAVAILABLE"  , "AO_REQUEST_UNAVAILABLE"  ), # 43
( "AO_REQUEST_LOGGED"       , "AO_REQUEST_LOGGED"       ), # 44
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 45
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 46
( "PLACE_HOLDER"            , "PLACE_HOLDER"            ), # 47
# BAC (or generic command processor) Errors
( "CANCELLED_BY_USER"       , "CANCELLED_BY_USER"       ), # 48
( "DM_CANCELLED"            , "DM_CANCELLED"            ), # 49
( "TIMED_OUT"               , "TIMED_OUT"               ), # 50
( "BAC_TOO_FEW_ARGS"        , "BAC_TOO_FEW_ARGS"        ), # 51
( "BAC_TOO_MANY_ARGS"       , "BAC_TOO_MANY_ARGS"       ), # 52
( "NOT_A_SYNCHRONOUS_CMD"   , "NOT_A_SYNCHRONOUS_CMD"   ), # 53
( "ARG_OUT_OF_RANGE"        , "ARG_OUT_OF_RANGE"        ), # 54
( "INVALID_COMMAND"         , "INVALID_COMMAND"         ), # 55
( "SUPERCEDED"              , "SUPERCEDED"              ), # 56
( "QUEUE_FULL"              , "QUEUE_FULL"              ), # 57
( "BAC_NOT_READY"           , "BAC_NOT_READY"           ), # 58
( "BAC_INTERNAL_ERROR"      , "BAC_INTERNAL_ERROR"      ), # 59
( "BAC_INVALID_QUERY"       , "BAC_INVALID_QUERY"       ), # 60
( "BAC_NULL_POINTER"        , "BAC_NULL_POINTER"        ), # 61
( "BAC_MIC_LEVEL_FAILED"    , "BAC_MIC_LEVEL_FAILED"    ), # 62
( "BAC_SUPERCEDE_FAILED"    , "BAC_SUPERCEDE_FAILED"    ), # 63

( "DM_BLOCK_VALID_WORD_BAD" , "DM_BLOCK_VALID_WORD_BAD" ), # 64
( "DM_CANT_READ_BLOCK_VALID", "DM_CANT_READ_BLOCK_VALID"), # 65
( "DM_INVALID_INDEX"        , "DM_INVALID_INDEX"        ), # 66
( "DM_FIXED_DB_INVALID"     , "DM_FIXED_DB_INVALID"     ), # 67
( "DM_NOT_INITIALIZED"      , "DM_NOT_INITIALIZED"      ), # 68
( "DM_SIZE_OOR"             , "DM_SIZE_OOR"             ), # 69
( "DM_UNAUTHORIZED"         , "DM_UNAUTHORIZED"         ), # 70
( "DM_LOCKING_ERROR"        , "DM_LOCKING_ERROR"        ), # 71
( "DM_ALREADY_OWNED_BLOCK"  , "DM_ALREADY_OWNED_BLOCK"  ), # 72
( "DM_EEPROM_CRC_ERROR"     , "DM_EEPROM_CRC_ERROR"     ), # 73
( "DM_CANT_WRITE_FLASH"     , "DM_CANT_WRITE_FLASH"     ), # 74
( "DM_RELOC_DB_NOT_OKAY"    , "DM_RELOC_DB_NOT_OKAY"    ), # 75

( "DM_ERROR_SENTINEL"       , "DM_ERROR_SENTINEL"       ), # 76
]

# ============================================================================ #

def get_table_entry(index) :
    # print ( "def: name of module:", __name__ )
    sts = 0
    if index <= (len( dms_response_codes ) - 2) :
        # SUCCESS
        sts = 0
        index = index
    else :
        # FAILURE
        sts = 1
        index = len( dms_response_codes ) - 1
    return( [ sts, dms_response_codes[index] ] )

# ============================================================================ #

if __name__ == '__main__' :

    print ( len( dms_response_codes ) )

    print( "\n" + 32 * "-" )
    i = 0
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 43
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 75
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 76
    print( i )
    ttt = get_table_entry(i)
    print( ttt )

    print( "\n" + 32 * "-" )
    i = 77
    print( i )
    ttt = get_table_entry(i)
    print( ttt )
    print( ttt[0], ttt[1] )

    print ('name of module:',__name__)
    print ('name of imported module:', sys.__name__)
    
    sys.exit( 0 )

# ============================================================================ #
