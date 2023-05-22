'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial
import json
import time
import string
import httplib2
import board
import requests
import json
import adafruit_bh1750
import os
import sys
#from serial import Serial
from time import sleep



ser = serial.Serial("/dev/ttyUSB0", 115200)    #Open port with baud rate
#i2c = board.I2C()
#sensor = adafruit_bh1750.BH1750(i2c)
firsttime=1
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
ipadd=ipaddr.split('\n')
url = 'http://127.0.0.1/get_ipsettings.php'
response = requests.post(url, data='')
jsondata = str(response.text)
jsonarray = json.loads(jsondata)

ipstat	= str(jsonarray[0]['staticip']).strip()
ipad	= str(jsonarray[0]['ip']).strip()
netmask	= str(jsonarray[0]['netmask']).strip()
devname	= str(jsonarray[0]['devicename']).strip()
gw		= str(jsonarray[0]['gw']).strip()


if ipstat == "1":

    print ("stat")
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
time.sleep(4)
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
ipadd=ipaddr.split('\n')
ipaddr=ipadd[0].strip()
ipaddr1=ipaddr.strip()
bcounter=0
url = 'http://localhost/setanc.php'
resp, content = httplib2.Http().request(url)
os.system("sudo python3 "+'/home/pi/led/anc_snd_main.py &')
os.system("sudo python "+'/home/pi/led/mod_read.py &')

while 1:
	#brightness=int(sensor.lux)
	brightness=255
	if brightness>255:
		brightness=255
	if brightness<30:
		brightness=30
	str_brightness=str(brightness).zfill(3)

	res_string='<4,'+str_brightness+'>\r\n'
	res_string=res_string.encode()
	if bcounter>5:
		#print(res_string)
		#ser.write(res_string)
		bcounter=0
	bcounter=bcounter+1
	time.sleep(0.2)
	data_left = ser.inWaiting()             #check for remaining byte
	if firsttime==1:
			data_left=1
	if data_left >0:
		
		#received_data = ser.read()              #read serial port
		sleep(0.2)
		# for x in "Lazy Fox Is Jumping Completely Over A Bunch of Straws     Lazy Brown Fox Is Jumping Completely Over A Bunch of Straws     Lazy Brown Fox Is Jumping Completely Over A Bunch of Straws     1111":
		#    ser.write(x)
		#    received_data = ser.read()              #read serial port
		#    data_left = ser.inWaiting() 
		#    received_data += ser.read(data_left)
		#    print (received_data)                   #print received data

		# #data_left = ser.inWaiting()             #check for remaining byte
		# #received_data += ser.read(data_left)
		# #print (received_data)                   #print received data
		#             #transmit data serially

		# sleep(2) 
		print('ss')
		received_data=''
		data_left = ser.inWaiting()             #check for remaining byte
		if data_left >4:
			received_data = ser.read(data_left)
			print (received_data)                   #print received data
		# print('-----')
		if firsttime==1:
			received_data=b'begin'
			print('firsttime')
		if received_data==b'begin':
			print('inside')
			url = 'http://localhost/get_settings.php'
			resp, content = httplib2.Http().request(url)
			paramread2 = json.loads(content)
			str_sspeed=str(paramread2[0]['scroll_speed']).zfill(3)
			res_string='<9,'+str_sspeed+'>\r\n'
			res_string=res_string.encode()
			print(res_string)
			ser.write(res_string)
			sleep(0.1)
			url = 'http://localhost/sel1top0.php'
			resp, content = httplib2.Http().request(url)
			print (content)
			if content!=b'anc':
				#print('111')
				paramread = json.loads(content)
				if firsttime==0:
					paramread[0]['Text']=paramread[0]['Text'].ljust(32)
					paramread[1]['Text']=paramread[1]['Text'].ljust(32)
					paramread[2]['Text']=paramread[2]['Text'].ljust(32)
					url = 'http://localhost/updateanc.php'
					resp, content = httplib2.Http().request(url)
				else:
					paramread[0]['Text']='RG-AD-R10-96-HV32-AA-S/M'
					paramread[1]['Text']='Device Id: RGADR1096HV32-01'
					paramread[2]['Text']='IP Address: '+ipaddr1

					paramread[0]['Text']=paramread[0]['Text'].ljust(32)
					paramread[1]['Text']=paramread[1]['Text'].ljust(32)
					paramread[2]['Text']=paramread[2]['Text'].ljust(32)
					paramread[0]['scroll']='1'
					paramread[1]['scroll']='1'
					paramread[2]['scroll']='1'
					firsttime=0
					
				received_data=''
				res_string='<1,'+paramread[0]['Text']+','+paramread[0]['scroll']+'>'
				res_string=res_string.encode()
				print (res_string)
				ser.write(res_string)
				sleep(0.05)
				res_string='<2,'+paramread[1]['Text']+','+paramread[1]['scroll']+'>'
				res_string=res_string.encode()
				print (res_string) 
				ser.write(res_string)
				sleep(0.05)	
				res_string='<3,'+paramread[2]['Text']+','+paramread[2]['scroll']+'>'
				res_string=res_string.encode()
				print (res_string) 
				ser.write(res_string)
			else:
				res_string='<8,EN>\r\n'
				res_string=res_string.encode()
				print(res_string)
				ser.write(res_string)
				




		#rotstat =str(paramread[0]['rotstat'])                    #rotate status
		#rotstat = rotstat.strip()

