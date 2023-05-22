#!/usr/bin/env python
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
ipaddr=str(os.popen("ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
ipadd=ipaddr.split('\n')
ipaddr=ipadd[0].strip()
ipaddr=ipaddr.strip()
print(ipaddr)
# ipaddr=check_output(['hostname','-I'])




UNIT = 0x01

def run_binary_payload_ex():
    
    global LNO, LE, TXT, FT, SZ, CL, FL, SC, TP, UNIT,FS
    
    X=((LNO-1) * 100)
    
    #print 
    
    client = ModbusClient(ipaddr, port=502)
    client.connect()

    
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    TXT=TXT.ljust(64)
    #print len(TXT)
    builder.add_string(TXT)										                #TEXT
    payload = builder.to_registers()
    payload = builder.build()
    address = 100 + X  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    #print address    

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(CL)										                #COLOUR
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 32  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    #print address    
	
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(FL)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    #print address    

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(SC)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    #print address    
    
    #print TXT + "done"
    client.close()
 

def Params():
    
    
    
    client = ModbusClient(ipaddr, port=502)
    client.connect()
    
    # if Params == 'ST':
    
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string('NO')										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 0  													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
        
    
    # elif Params == 'CL':
    
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string('YE')										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 1  													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
        
    # elif Params == 'SR':
    # #print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string("05")										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 2  													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
        
    # elif Params == 'FL':
    # #print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string("05")										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 3  													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
            
    # elif Params == 'BR':
    # #print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string("05")										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 4 													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string("Magneto Dynamicshttps://magdyn.com/ RGB TND LED RGB-P67-96HV48RGB-P67-96HV48-TCP-IP-MB1.1.0 ")										#State
    payload = builder.to_registers()
    payload = builder.build()
    address = 10 													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)

if __name__ == "__main__":
    # global LNO
    LNO = 1
    LE  =   "NO"
    TXT =   "                                                               "
    FT  =   "EU"
    SZ  =   "17"
    CL  =   "GR"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()
    
    time.sleep(0.1)
    
    LNO = 2
    LE  =   "NO"
    TXT =   "                                                                "
    FT  =   "EU"
    SZ  =   "15"
    CL  =   "GR"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()
    
    time.sleep(0.1)
    
    LNO = 3
    LE  =   "NO"
    TXT =   "                                                                "
    FT  =   "EU"
    SZ  =   "15"
    CL  =   "GR"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()

    time.sleep(0.1)
    
    LNO = 4
    LE  =   "NO"
    TXT =   "                                                                "
    FT  =   "EU"
    SZ  =   "15"
    CL  =   "GR"
    FL  =   "NO"
    SC  =   "YE"
    TP  =   "NO"
    FS  =   "NR"
    run_binary_payload_ex()
    
    time.sleep(0.1)

    Params()
    
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
    # #print address    

    client.close()


