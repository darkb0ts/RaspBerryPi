#!/usr/bin/python3
import serial
import json
import time
import string
import httplib2
import board
import adafruit_bh1750
import os
import sys
from pathlib import Path
#from serial import Serial
from time import sleep

import inflect
p = inflect.engine()
url = 'http://localhost/setanc.php'
resp, content = httplib2.Http().request(url)


while 1:
	url = 'http://localhost/ancsel1top0.php'
	resp, content = httplib2.Http().request(url)
	print(content)
	time.sleep(1.75)
	if content!=b'-\r\n':
		paramread = json.loads(content)
		textarr = paramread[0]['audio_text'].split("[")
		# print "caketextarr"
		firstttime=1
		linewidth=0
		for a in range(len(textarr)):
				# print textarr[a]
				time.sleep(0.1)
				if "]" in textarr[a]:
					# ##print "image"+textarr[a]
					textarr2 = textarr[a].split("]")
					# #print textarr2[0] + "is image"
					my_file = Path('/var/www/html/Langs/'+textarr2[0]+'.mp3')
					if my_file.is_file():
						print('/var/www/html/Langs/'+textarr2[0]+'.mp3')
						os.system("mpg321 -g 80 "+'/var/www/html/Langs/'+textarr2[0]+'.mp3')
					else:
						
						print(textarr2[0]+'.mp3')
					if textarr2[1].strip()!="":
						sleep(0.5)
						textarr4=textarr2[1].strip().split(".")
						x=p.number_to_words(int(textarr4[0].strip()))
						x = x.replace(",", "")
						x = x.replace("-", " ")
						textarr3 = x.split(" ")
						for b in range(len(textarr3)):

							print('/home/pi/led/Audio2/'+textarr3[b]+'.mp3')
							os.system("mpg321 -g 80 "+'/home/pi/led/Audio2/'+textarr3[b]+'.mp3')
						if len(textarr4)==2:
							time.sleep(0.5)
							os.system("mpg321 -g 80 "+'/home/pi/led/Audio2/point.mp3')
							for c in range(len(textarr4[1])):
								x1=p.number_to_words(int(textarr4[1][c].strip()))
								print('/home/pi/led/Audio2/'+x1+'.mp3')
								os.system("mpg321 -g 80 "+'/home/pi/led/Audio2/'+x1+'.mp3')


				else:

					print(textarr[a].strip()+'')
		sleep(1)
		url = 'http://localhost/updaterotstat.php?rotid='+paramread[0]['id']
		print(url)
		resp, content = httplib2.Http().request(url)
	else:
		sleep(2)


  
