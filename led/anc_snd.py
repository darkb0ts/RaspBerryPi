#!/usr/bin/python3

from gtts import gTTS 
import os 
  
intext = 'Hello Welcome To Magneto Dynamics'
language = 'en-in'
  
t2s = gTTS(text = intext, lang=language, slow=False) 
t2s.save("speech.mp3") 
  
os.system("mpg321 -g 50 speech.mp3") 