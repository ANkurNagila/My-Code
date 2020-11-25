import optparse
import subprocess

parse=optparse.OptionParser()
parse.add_option("-i","--interface",dest="new1",help="This will just add new interface")
parse.add_option("-m","--mac",dest="mac",help="This will just add new MAC address")

(option,arguments)=parse.parse_args()

new1=option.new1
mac=option.mac

print("These are some new things :",new1,mac)
