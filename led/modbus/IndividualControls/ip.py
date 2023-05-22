import sys
import os
import time
import requests
import json
import RPi.GPIO as GPIO

ser_write_pin = 16
mode_pin = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


workmode = True

GPIO.setup(ser_write_pin, GPIO.OUT)
GPIO.setup(mode_pin,GPIO.IN)

GPIO.output(ser_write_pin,GPIO.HIGH)

# comd = int(str(sys.argv[1]))
# comd = int(str(sys.argv[2]))
ipaddr=str(os.popen("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'").read())
ipadd=ipaddr.split('\n')
ipaddr=ipadd[0].strip()
ipaddr=ipaddr.strip()
print(ipaddr) 

 
def run():
    time.sleep(1) 
    global ipaddr 
    if ipaddr.strip()=="":
        
        ipad	= '10.10.10.10'
        netmask	= '255.255.255.0'
        gw		= '10.10.10.1'
        
        cmd = 'sudo ifconfig eth0 down'
        print (cmd)
        os.system(cmd)

        cmd = 'sudo ifconfig eth0 '+ipad+' netmask '+netmask
        print (cmd)
        os.system(cmd)
        
        cmd = 'sudo route add default gw '+gw
        print (cmd)
        os.system(cmd)
        
        cmd = 'sudo ifconfig eth0 up'
        print (cmd)
        os.system(cmd)
        time.sleep(10)
        #cmd = 'sudo python /home/pi/C1/ipchecker.py '+(ipad.strip())
        #print (cmd)
        #os.system(cmd)
        url = 'http://'+(ipad.strip())+'/get_ipsettings.php'
        response = requests.post(url, data='')
        jsondata = str(response.text)
        jsonarray = json.loads(jsondata)
        
        ipstat	= str(jsonarray[0]['staticip']).strip()
        ipad	= str(jsonarray[0]['ip']).strip()
        netmask	= str(jsonarray[0]['netmask']).strip()
        devname	= str(jsonarray[0]['devicename']).strip()
        gw		= str(jsonarray[0]['gw']).strip()
        
        
        if ipstat == "1":

            print "stat"
            ipaddr= ipad
            cmd = 'sudo ifconfig eth0 down'
            print (cmd)
            os.system(cmd)

            cmd = 'sudo ifconfig eth0 '+ipad+' netmask '+netmask
            print (cmd)
            os.system(cmd)

            cmd = 'sudo route add default gw '+gw
            print (cmd)
            #os.system(cmd)

            cmd = 'sudo ifconfig eth0 up'
            print (cmd)
            os.system(cmd)

            #cmd = 'sudo python /home/pi/C1/ipchecker.py '+(ipad.strip())
            #print (cmd)
            #os.system(cmd)

            time.sleep(5)
            # url = 'http://10.10.10.10/initAck.php'
            # print(url) 
            # response = requests.post(url, data='')	
        
            url = 'http://localhost/clearonboot.php'
            print url
            response = requests.post(url, data='')		

            
            cmd = 'sudo python /home/pi/C1/blinkstarter.py&'
            print (cmd)
            os.system(cmd)
            
            if GPIO.input(mode_pin) == workmode:
            
                print "ip"
                
                cmd = 'sudo python /home/pi/C1/modbus/synchronous_server.py&'
                print (cmd)
                os.system(cmd)
                
                time.sleep(5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modbus/modinit.py&'
                print (cmd)
                os.system(cmd)

                time.sleep(2.5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modread.py&'
                print (cmd)
                os.system(cmd)
            
            else:
                
                time.sleep(5)
            
                print "ser"
            
                cmd = 'sudo python /home/pi/C1/seread.py&'
                print (cmd)
                os.system(cmd)
            
        else:
			
			# url = 'http://10.10.10.10/initAck.php'
			# print(url) 
			# response = requests.post(url, data='')	
			
			url = 'http://localhost/clearonboot.php'
			print(url) 
			response = requests.post(url, data='')	

			# url = 'http://localhost/setSD.php'
			# resp, content = httplib2.Http().request(url)
			# print url
			# print content        
			
			cmd = 'sudo python /home/pi/C1/blinkstarter.py&'
			print (cmd)
			os.system(cmd)
			
			if GPIO.input(mode_pin) == workmode:
				
				print "ip"
				
				cmd = 'sudo python /home/pi/C1/modbus/synchronous_server.py&'
				print (cmd)
				os.system(cmd)
				
				time.sleep(5)
				
				GPIO.output(ser_write_pin,GPIO.HIGH)
				cmd = 'sudo python /home/pi/C1/modbus/modinit.py&'
				print (cmd)
				os.system(cmd)

				time.sleep(2.5)
				
				GPIO.output(ser_write_pin,GPIO.HIGH)
				cmd = 'sudo python /home/pi/C1/modread.py&'
				print (cmd)
				os.system(cmd)
			
			else:
				
				time.sleep(7.5)
			
				print "ser"
			
				cmd = 'sudo python /home/pi/C1/seread.py&'
				print (cmd)
				os.system(cmd)
            
    else:
        url = 'http://'+(ipaddr.strip())+'/get_ipsettings.php'
        response = requests.post(url, data='')
        jsondata = str(response.text)
        jsonarray = json.loads(jsondata)
        
        ipstat	= str(jsonarray[0]['staticip']).strip()
        ipad	= str(jsonarray[0]['ip']).strip()
        netmask	= str(jsonarray[0]['netmask']).strip()
        devname	= str(jsonarray[0]['devicename']).strip()
        gw		= str(jsonarray[0]['gw']).strip()
        
        
        if ipstat == "1":

            print "stat"
            ipaddr= ipad
            cmd = 'sudo ifconfig eth0 down'
            print (cmd)
            os.system(cmd)

            cmd = 'sudo ifconfig eth0 '+ipad+' netmask '+netmask
            print (cmd)
            os.system(cmd)

            cmd = 'sudo route add default gw '+gw
            print (cmd)
            #os.system(cmd)

            cmd = 'sudo ifconfig eth0 up'
            print (cmd)
            os.system(cmd)

            #cmd = 'sudo python /home/pi/C1/ipchecker.py '+(ipad.strip())
            #print (cmd)
            #os.system(cmd)

            time.sleep(5)
            # url = 'http://10.10.10.10/initAck.php'
            # print(url) 
            # response = requests.post(url, data='')	
        
            url = 'http://localhost/clearonboot.php'
            print url
            response = requests.post(url, data='')		

            
            cmd = 'sudo python /home/pi/C1/blinkstarter.py&'
            print (cmd)
            os.system(cmd)
            
            if GPIO.input(mode_pin) == workmode:
            
                print "ip"
                
                cmd = 'sudo python /home/pi/C1/modbus/synchronous_server.py&'
                print (cmd)
                os.system(cmd)
                
                time.sleep(5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modbus/modinit.py&'
                print (cmd)
                os.system(cmd)

                time.sleep(2.5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modread.py&'
                print (cmd)
                os.system(cmd)
            
            else:
                
                time.sleep(5)
            
                print "ser"
            
                cmd = 'sudo python /home/pi/C1/seread.py&'
                print (cmd)
                os.system(cmd)
            

        else:
            print "dyn"
            time.sleep(5)
            url = 'http://'+(ipaddr.strip())+'/set_ipsettings.php?ip='+(ipaddr.strip())
            response = requests.post(url, data='')
            jsondata = str(response.text)
            
            # url = 'http://10.10.10.10/initAck.php'
            # print(url) 
            # response = requests.post(url, data='')	
        

            url = 'http://'+(ipaddr.strip())+'/clearonboot.php'
            response = requests.post(url, data='')		

            cmd = 'sudo python /home/pi/C1/blinkstarter.py&'
            print (cmd)
            os.system(cmd)

            # cmd = 'sudo python /home/pi/C1/ipchecker.py '+(ipaddr.strip())
            # print (cmd)
            # os.system(cmd)

            #time.sleep(1)
            if GPIO.input(mode_pin) == workmode:
            
                print "ip"
        
                cmd = 'sudo python /home/pi/C1/modbus/synchronous_server.py&'
                print (cmd)
                os.system(cmd)

                time.sleep(5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modbus/modinit.py&'
                print (cmd)
                os.system(cmd)

                time.sleep(2.5)
                
                GPIO.output(ser_write_pin,GPIO.HIGH)
                cmd = 'sudo python /home/pi/C1/modread.py&'
                print (cmd)
                os.system(cmd)
            
            else:
                
                time.sleep(5)
            
                print "ser"
            
                cmd = 'sudo python /home/pi/C1/seread.py&'
                print (cmd)
                os.system(cmd)

            # cmd = 'sudo reboot'
            # os.system(cmd)
            # cmd = 'sudo python /home/pi/C1/modbus/synchronous_server.py'
            # print (cmd)
            # os.system(cmd)
            


#ipaddr=""
if __name__ == "__main__":
    run()
