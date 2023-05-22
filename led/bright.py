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
import adafruit_bh1750
import os
import sys
#from serial import Serial
from time import sleep

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

while 1:
	brightness=int(sensor.lux)
	print(brightness)