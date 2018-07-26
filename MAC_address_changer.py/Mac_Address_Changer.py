#1/usr/bin/env python

############### Modules
import subprocess
import optparse

############### Global functions
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address of")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+} Changing MC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



################ Main Script
(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
