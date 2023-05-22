import os
import csv
import json
import time
import string
import httplib2
import requests
import json
import RPi.GPIO as GPIO
from threading import Thread
from subprocess import check_output
from collections import OrderedDict
from pymodbus.compat import iteritems 
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

UNIT=0x01
firsttime=1
def bits(f):
    bytes = (ord(b) for b in f)
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1

def run_sync_client():
	global gw,firsttime
	error=0
	url = 'http://localhost/settingread.php'
	resp, content = httplib2.Http().request(url)
	settingread = json.loads(content)
	servip =str(settingread[0]['servip'])
	RegID=int(str(settingread[0]['RegID']))
	RegLen=int(str(settingread[0]['RegLen']))
	Modenable=int(str(settingread[0]['Modenable']))
	print(servip+'-'+str(RegID)+'-'+str(RegLen)+str(Modenable)+"----- mod enable")
	url = 'http://localhost/reg0fix.php?len='+str(RegLen)
	resp, content = httplib2.Http().request(url)
	####print url
	if (Modenable==1):
		try:
			client = ModbusClient(servip, port=502)
			client.connect()

			address = RegID
			count   = RegLen
			result  = client.read_holding_registers(address, count,  unit=1)
			decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                 byteorder=Endian.Big,
                                                 wordorder=Endian.Little)
			kstr=""
			for b in range(count):
			   dispreg = decoder.decode_16bit_uint()
			   print(dispreg)
			   kstr=kstr+("{0:b}".format(dispreg)).zfill(16)+""
				
			
			
			url = 'http://localhost/updatesel.php?val='+kstr
			resp, content = httplib2.Http().request(url)
			####print resp
			print(url)


			client.close() 
		except Exception as e:
			error=1
			cmd = 'sudo route add default gw '+gw
			print (cmd)
			os.system(cmd)
			cmd = 'sudo route add default gw '+gw
			print (cmd)
			os.system(cmd)

			print("error"+str(e))
url = 'http://localhost/get_ipsettings.php'
response = requests.post(url, data='')
jsondata = str(response.text)
jsonarray = json.loads(jsondata)
        
ipstat	= str(jsonarray[0]['staticip']).strip()
ipad	= str(jsonarray[0]['ip']).strip()
netmask	= str(jsonarray[0]['netmask']).strip()
devname	= str(jsonarray[0]['devicename']).strip()
gw		= str(jsonarray[0]['gw']).strip()
        
        
if ipstat == "1":

    print("stat")
    ipaddr= ipad
    cmd = 'sudo ifconfig eth0 down'
    print (cmd)
    #os.system(cmd)

    cmd = 'sudo ifconfig eth0 '+ipad+' netmask '+netmask
    print (cmd)
    os.system(cmd)

    cmd = 'sudo route add default gw '+gw
    print (cmd)
    os.system(cmd)

    cmd = 'sudo ifconfig eth0 up'
    print (cmd)
    #os.system(cmd)

while 1:
    run_sync_client()
    time.sleep(2)
