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
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
# ipaddr="192.168.5.249"
# ipaddr=check_output(['hostname','-I'])




UNIT = 0x01
 

if __name__ == "__main__":
    # global LNO

    client = ModbusClient(ipaddr, port=502)
    client.connect()

    address = 5  
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little) 
    builder.add_string('DC')				 						        # State
    payload = builder.to_registers()
    payload = builder.build()
    client.write_registers(address, payload, skip_encode=True, unit=1)
    print address    

    client.close()	


