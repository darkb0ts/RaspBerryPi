import array
import time
import string
import os
import httplib2
import json
import binascii

import numpy as np
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from threading import Thread
from subprocess import check_output
from collections import OrderedDict
from pymodbus.compat import iteritems 
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14,GPIO.HIGH)