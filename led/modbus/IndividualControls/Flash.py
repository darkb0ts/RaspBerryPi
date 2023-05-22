#!/usr/bin/env python
"""
Pymodbus Payload Building/Decoding Example
--------------------------------------------------------------------------

# Run modbus-payload-server.py or synchronous-server.py to check the behavior
"""

import os
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder 
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict
from subprocess import check_output
import numpy as np
import sys
# --------------------------------------------------------------------------- # 
# configure the client logging
# --------------------------------------------------------------------------- # 
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
ipaddr=ipaddr.strip()

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
		  ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)
UNIT = 0x01

id = int(str(sys.argv[1]))
zone = sys.argv[2]

def run_binary_payload_ex():
	# ----------------------------------------------------------------------- #
	# We are going to use a simple client to send our requests
	# ----------------------------------------------------------------------- #
	client = ModbusClient(ipaddr, port=5020)
	client.connect()
 
	# from pymodbus.transaction import ModbusRtuFramer
	# client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
	# client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
	# client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
	# client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1,
	#                       baudrate=9600)
	#client.connect()

	# ------------------------------------------------------------------------#
	# specify slave to query
	# ------------------------------------------------------------------------#
	# The slave to query is specified in an optional parameter for each
	# individual request. This can be done by specifying the `unit` parameter
	# which defaults to `0x00`
	# ----------------------------------------------------------------------- #


	# ----------------------------------------------------------------------- #
	# example requests
	# ----------------------------------------------------------------------- #
	# simply call the methods that you would like to use. An example session
	# is displayed below along with some assert checks. Note that some modbus
	# implementations differentiate holding/input discrete/coils and as such
	# you will not be able to write to these, therefore the starting values
	# are not known to these tests. Furthermore, some use the same memory
	# blocks for the two sets, so a change to one is a change to the other.
	# Keep both of these cases in mind when testing as the following will
	# _only_ pass with the supplied asynchronous modbus server (script supplied).
	# ----------------------------------------------------------------------- #
	log.debug("Write to a Coil and read back")
	log.debug("Write to a holding register and read back")
	
	regid = 100+((id*40)-39)
	countt=0
	print ( str(regid))
	
	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string(zone)															#Zone
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)

	regid=regid+1

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('1 Welcome to IOCL Cherlapali    ')							#TEXT
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)

	regid=regid+32

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('EN')														#Font
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)

	regid=regid+1

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('18')														#Font Size
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)
	
	regid=regid+1

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('MY')														#Colour
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid 
	# client.write_registers(address, payload, skip_encode=True, unit=1)

	regid=regid+1

	builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   wordorder=Endian.Little)
	builder.add_string(zone)														#Flash
	payload = builder.to_registers()
	payload = builder.build()
	address = regid
	client.write_registers(address, payload, skip_encode=True, unit=1)
	
	regid=regid+1

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('YE')														#Scroll
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)
	
	regid=regid+1

	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('YE')														#Scroll
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = regid
	# client.write_registers(address, payload, skip_encode=True, unit=1)
	
	regid=regid+2	

	client.close()
	print ('done')

if __name__ == "__main__":
	run_binary_payload_ex()
