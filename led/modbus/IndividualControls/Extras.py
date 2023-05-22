import sys
import os

comd = int(str(sys.argv[1]))
# comd = int(str(sys.argv[2]))


def run():

	if (comd == 1):
		cmd = 'sudo reboot&'
		# print (cmd)
		os.system(cmd)
	elif(comd == 2):
		cmd = 'sudo shutdown -h now&'
		# print (cmd)
		os.system(cmd)
	else :
		print ("I'm a bot")
if __name__ == "__main__":
	run()