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
Params	=str(sys.argv[1])
Params1	=str(sys.argv[2])
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
# ipaddr=check_output(['hostname','-I'])


UNIT = 0x01

def run_binary_payload_ex():
	
	
	
	client = ModbusClient(ipaddr, port=5020)
	client.connect()
	
	if Params == 'ST':
	
		builder = BinaryPayloadBuilder(byteorder=Endian.Big,
									   wordorder=Endian.Little)
		builder.add_string('YE')										#State
		payload = builder.to_registers()
		payload = builder.build()
		address = 1  													#Reg Addr
		client.write_registers(address, payload, skip_encode=True, unit=1)
		
	
	elif Params == 'CL':
	
		builder = BinaryPayloadBuilder(byteorder=Endian.Big,
									   wordorder=Endian.Little)
		builder.add_string('YE')										#State
		payload = builder.to_registers()
		payload = builder.build()
		address = 2  													#Reg Addr
		client.write_registers(address, payload, skip_encode=True, unit=1)
		
	elif Params == 'SR':
		print (Params1)
		builder = BinaryPayloadBuilder(byteorder=Endian.Big,
									   wordorder=Endian.Little)
		builder.add_string(Params1)										#State
		payload = builder.to_registers()
		payload = builder.build()
		address = 3  													#Reg Addr
		client.write_registers(address, payload, skip_encode=True, unit=1)
		
	elif Params == 'FL':
		print (Params1)
		builder = BinaryPayloadBuilder(byteorder=Endian.Big,
									   wordorder=Endian.Little)
		builder.add_string(Params1)										#State
		payload = builder.to_registers()
		payload = builder.build()
		address = 4  													#Reg Addr
		client.write_registers(address, payload, skip_encode=True, unit=1)
			
	elif Params == 'BR':
		print (Params1)
		builder = BinaryPayloadBuilder(byteorder=Endian.Big,
									   wordorder=Endian.Little)
		builder.add_string(Params1)										#State
		payload = builder.to_registers()
		payload = builder.build()
		address = 5 													#Reg Addr
		client.write_registers(address, payload, skip_encode=True, unit=1)
	
	# builder = BinaryPayloadBuilder(byteorder=Endian.Big,
								   # wordorder=Endian.Little)
	# builder.add_string('10')										#State
	# payload = builder.to_registers()
	# payload = builder.build()
	# address = 802													#Reg Addr
	# client.write_registers(address, payload, skip_encode=True, unit=1)
	# client.close()

	# rr = client.read_holding_registers(802, 2, unit=UNIT)
	# decoder = BinaryPayloadDecoder.fromRegisters(rr.registers,
										# byteorder=Endian.Big,
										# wordorder=Endian.Little)
												 
	# datstate=decoder.decode_string(2)+""

if __name__ == "__main__":
	run_binary_payload_ex()
