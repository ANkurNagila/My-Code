from optparse import OptionParser
import subprocess
import re

def get_values():
	parse=OptionParser()
	parse.add_option("-i","--interface",dest="interface",help="This will just add new interface")
	parse.add_option("-m","--mac",dest="mac",help="This will just add new MAC address")

	(options,arguments)=parse.parse_args()

	if not options.interface:	
		parse.error("Please check on --help and fill interface")
	if not options.mac:
		parse.error("Please check on --help and fill mac")

	return options
	#options is a dictionary and (mac, interface) are keyse



def change_mac(interface,new_mac):
	print("Changing Mac address of "+interface+" into "+new_mac)
	
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])




options=get_values()
change_mac(options.interface,options.mac)


print(options,"\n")


ifconfig_result=subprocess.check_output(["ifconfig",options.interface])

print(ifconfig_result)



x=re.findall("ether.+:..",ifconfig_result)

y=x[0]


result=y.split()
if result[1]==options.mac:
	print("Success man")



