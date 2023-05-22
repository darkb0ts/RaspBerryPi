#!/usr/bin/env python
"""
Pymodbus Payload Building/Decoding Example
--------------------------------------------------------------------------

# Run modbus-payload-server.py or synchronous-server.py to check the behavior
"""
import RPi.GPIO as GPIO
from threading import Thread
import time
import string
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np


from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems 
from collections import OrderedDict
from subprocess import check_output

import sys


#regid	=int(str(sys.argv[1]))
#Params	=str(sys.argv[1])
#Params1	=str(sys.argv[2])
ipaddr='192.168.5.129'
# ipaddr=check_output(['hostname','-I'])
i=0

UNIT = 0x01

def run_binary_payload_ex():
	global i
	#client = ModbusClient(ipaddr, port=5020)
	#client.connect()

	#builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   #wordorder=Endian.Little)
	#builder.add_string('YE')										#State
	#payload = builder.to_registers()
	#payload = builder.build()
	#address = 50  													#Reg Addr
	#client.write_registers(address, payload, skip_encode=True, unit=1)
	
	
	#
	rr = client.read_coils(1,9, unit=UNIT)
	print (rr.bits)
	print (i)	
	i=i+1


if __name__ == "__main__":
	client = ModbusClient(ipaddr, port=5020)
	client.connect()
	rq = client.write_coils(1, [1,0,1,0,1,0,1,0], unit=UNIT)
	rq = client.write_coils(2, [1,0,1,0,1,0,1,0], unit=UNIT)
	while(1):
		millis = int(round(time.time() * 1000))
		print millis
		run_binary_payload_ex()
		millis = int(round(time.time() * 1000))
		print millis
		print "-"
