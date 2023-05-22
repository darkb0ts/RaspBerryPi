#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pymodbus Payload Building/Decoding Example
--------------------------------------------------------------------------

# Run modbus-payload-server.py or synchronous-server.py to check the behavior
"""
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict
from subprocess import check_output
import sys
import os
import time

#regid	=int(str(sys.argv[1]))
# Params	=str(sys.argv[1])
# Params1	=str(sys.argv[2])
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
# ipaddr="192.168.5.249"
# ipaddr=check_output(['hostname','-I'])




UNIT = 0x01

def run_binary_payload_ex():
    
    global LNO, LE, TXT, FT, SZ, CL, FL, SC, TP, UNIT
    
    X=((LNO-1) * 100)
    
    client = ModbusClient(ipaddr, port=502)
    client.connect()

    
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    TXT=TXT.ljust(64)
    print len(TXT)
    builder.add_string(TXT)										                #TEXT
    payload = builder.to_registers()
    payload = builder.build()
    address = 100 + X  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(CL)										                #COLOUR
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 32  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
	
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(FL)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(SC)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
    print TXT + "done"
    client.close()
 


if __name__ == "__main__":
    # global LNO
    LNO = 1
    LE  =   "YE"
    # TXT =   "ºÉÊG ¬ xÉ½Ó"
    TXT =   "[EN06]"#"ERROR other reasons. Not updated in SAP"# [HN18] AB 3282 [HN17][HN16]: TLF [HN15] CAKE"
    FT  =   "HN"
    SZ  =   "10"
    CL  =   "RE"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()
    
    time.sleep(0.1)
    
    LNO = 2
    LE  =   "YE" 
    TXT =   "[HN06]"# TXT LINE 1Sample TXT LINE 1Sample TXT LINE 1Sample TXT 12"
    FT  =   "HN"
    SZ  =   "15"
    CL  =   "BL"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()
    
    time.sleep(0.1)
    
    LNO = 3
    LE  =   "YE"
    TXT =   "[TL06]"
    FT  =   "TM"
    SZ  =   "20"
    CL  =   "GR"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "BD"
    run_binary_payload_ex()

    time.sleep(0.1)
    
    # LNO = 4
    # LE  =   "YE"
    # TXT =   "Sample TXT LINE 4Sample TXT LINE 4Sample TXT LINE 4Sample TXT 12"
    # FT  =   "TM"
    # SZ  =   "30"
    # CL  =   "WH"
    # FL  =   "YE"
    # SC  =   "YE"
    # TP  =   "NO"
    # FS  =   "NR"
    # run_binary_payload_ex()
    
    time.sleep(0.1)
    
    client = ModbusClient(ipaddr, port=502)
    client.connect()

    # address = 5  
    # builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   # wordorder=Endian.Little)
    # builder.add_string('LA')										        # State
    # payload = builder.to_registers()
    # payload = builder.build()
    # client.write_registers(address, payload, skip_encode=True, unit=1)
    # print address    

    client.close()


