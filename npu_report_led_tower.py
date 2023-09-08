#!/usr/bin/python3

import sys
import bdp_over_eth as bdp
DEFAULT_NETPREQ_IP = 49152

# ============================================================================ #
# 

# // GPIO_LED1_GREEN
# 	GPIO_SET(GPIO_LED1_PIN_G);
# 	GPIO_CLR(GPIO_LED1_PIN_R);

# // GPIO_LED1_RED
# 	GPIO_CLR(GPIO_LED1_PIN_G);
# 	GPIO_SET(GPIO_LED1_PIN_R);

# // GPIO_LED1_OFF
# 	GPIO_CLR(GPIO_LED1_PIN_G);
# 	GPIO_CLR(GPIO_LED1_PIN_R);

# bdp:               REG_PORTF_DATA -> ?Dw00013100428C
# bdp:               REG_PORTE_DATA -> ?Dw00013100420C

    #LED 1:
    #LED 2:

    #LED 3: ?Gw01013100420C
    # 		bitt=$(($nmbr & 0x0080))

    #LED 4: ?Gw01013100420C
    # 		bitt=$(($nmbr & 0x0100))
    # Rsp: $Gw004000000100
# Rsp: $Gw004000000100


if __name__ == '__main__' :

    netpreq_ip_adrs = sys.argv[1]

    led1_grn_mask = 0x1000 # if PE_12 (bit index 12) PE Data is set, LED is GREEN
    led1_red_mask = 0x0020 # if PE_05 (bit index  5) PE Data is set, LED is RED
    led2_grn_mask = 0x0004 # if PF_02 (bit index  2) PF Data is set, LED is GREEN
    led2_red_mask = 0x0040 # if PE_06 (bit index  6) PE Data is set, LED is RED
    led3_grn_mask = 0x0008 # if PF_03 (bit index  3) PF Data is set, LED is GREEN
    led3_red_mask = 0x0080 # if PE_07 (bit index  7) PE Data is set, LED is RED
    led4_grn_mask = 0x0010 # if PF_04 (bit index  4) PF Data is set, LED is GREEN
    led4_red_mask = 0x0100 # if PE_08 (bit index  8) PE Data is set, LED is RED

    port_e_data = "?Gw00013100420C"
    port_f_data = "?Gw00013100428C"

    bdp_rsp_port_e_data = bdp.bdp_over_ethernet(port_e_data, netpreq_ip_adrs)
    # print( "Rsp PORTE Data:", bdp_rsp_port_e_data )
    port_e_data = int("0x" + bdp_rsp_port_e_data[11:15], 16)
    # print( "PORTE Data: 0x{:04X}".format( port_e_data ) )

    bdp_rsp_port_f_data = bdp.bdp_over_ethernet(port_f_data, netpreq_ip_adrs)
    # print( "Rsp PORTF Data:", bdp_rsp_port_f_data )
    port_f_data = int("0x" + bdp_rsp_port_f_data[11:15], 16)
    # print( "PORTF Data: 0x{:04X}".format( port_f_data ) )

    # print( "LED1 red bit: 0x{:04X}".format( port_e_data & led1_red_mask) )
    # print( "LED1 grn bit: 0x{:04X}".format( port_e_data & led1_grn_mask) )
    # print( "LED2 red bit: 0x{:04X}".format( port_e_data & led2_red_mask) )
    # print( "LED2 grn bit: 0x{:04X}".format( port_f_data & led2_grn_mask) )
    # print( "LED3 red bit: 0x{:04X}".format( port_e_data & led3_red_mask) )
    # print( "LED3 grn bit: 0x{:04X}".format( port_f_data & led3_grn_mask) )
    # print( "LED4 red bit: 0x{:04X}".format( port_e_data & led4_red_mask) )
    # print( "LED4 grn bit: 0x{:04X}".format( port_f_data & led4_grn_mask) )

    if port_e_data & led2_red_mask :
        print( "LED2 is RED: Sharc Core #1 has crashed ==> RESET the NetPREQ" )
    else :
        print( "LED2 is green" )

    if port_e_data & led3_red_mask :
        print( "LED3 is RED: Sharc Core #2 has crashed ==> RESET the NetPREQ" )
    else :
        print( "LED3 is green" )

    if port_e_data & led4_red_mask :
        print( "LED4 is RED: No JACK Connection with PC-PREQ" )
    else :
        print( "LED4 is green" )

    sys.exit(0)
    
# ---------------------------------------------------------------------------- #
