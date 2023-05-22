# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense
import time
import serial
import json
import time
import string
#from serial import Serial
from time import sleep
import board
import adafruit_bh1750

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)
ser = serial.Serial("/dev/ttyACM0", 2400)
received_data=''
while True:
    #print("%.2f Lux" % sensor.lux)
    #time.sleep(2)
    brightness=int(sensor.lux)
    if brightness>255:
    	brightness=255
    if brightness<30:
    	brightness=30
    str_brightness=str(brightness).zfill(3)

    res_string='<4,'+str_brightness+'>\r\n'
    res_string=res_string.encode()
    print(res_string)
    
    ser.write(res_string)
    time.sleep(2)
    data_left = ser.inWaiting()             #check for remaining byte
    if data_left >0:
    	received_data = ser.read(data_left)
    	print (received_data)
      
