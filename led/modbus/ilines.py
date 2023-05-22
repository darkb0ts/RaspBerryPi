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

#regid	=int(str(sys.argv[1]))
# Params	=str(sys.argv[1])
# Params1	=str(sys.argv[2])
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
# ipaddr = "192.168.5.178" 
# ipaddr=check_output(['hostname','-I'])

LNO =   1
LE  =   "YE"
# TXT =   "Sample TXT LINE 4Sample TXT LINE 4Sample TXT LINE 4Sample TXT LI"
FT  =   "EU"
SZ  =   "16"
CL  =   "RE"
FL  =   "NO"
SC  =   "YE"
TP  =   "NO"
FS  =   "NR"



UNIT = 0x01

def run_binary_payload_ex():
    
    global LNO, LE, TXT, FT, SZ, CL, FL, SC, TP, UNIT,FS
    
    X=((LNO-1) * 40)
    
    print 
    
    client = ModbusClient(ipaddr, port=502)
    client.connect()
    
    # if Params == 'ST':
    
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(LE)										                #LINE ENABLE
    payload = builder.to_registers()
    payload = builder.build()
    address = 100 + X 													        #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
    # elif Params == 'CL':
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    # TXT=TXT.ljust(64)
    # print len(TXT)
    # builder.add_string(TXT)										                #TEXT
    # payload = builder.to_registers()
    # payload = builder.build()
    address = address + 1  													    #Reg Addr
    # client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
        
    # elif Params == 'SR':
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(FT)										                #FONT
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 32  													#Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
        
    # elif Params == 'FL':
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(SZ)										                #SIZE
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
            
    # elif Params == 'BR':
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(CL)										                #COLOUR
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
    
    
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(FL)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
 
    
    
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(SC)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
 
    
    
    # print (Params1)
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(TP)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
     # print (Params1)
     
     
     
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_string(FS)										                #FLASH
    payload = builder.to_registers()
    payload = builder.build()
    address = address + 1  													    #Reg Addr
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    
    
    # print TXT + "done"
    client.close()
 


if __name__ == "__main__":
    # global LNO
    
    run_binary_payload_ex()

    client = ModbusClient(ipaddr, port=502)
    client.connect()

    # address = 5  
    # builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   # wordorder=Endian.Little)
    # builder.add_string('L' + str(LNO))										        # State
    # payload = builder.to_registers()
    # payload = builder.build()
                                                                            # Reg Addr
    # client.write_registers(address, payload, skip_encode=True, unit=1)
    # print address    

    client.close()
