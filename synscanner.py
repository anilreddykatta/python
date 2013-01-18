#!/usr/bin/env python
from threading import Thread
from scapy.all import *
open_file_handler = open('open_port.txt', 'w').close()
close_file_handler = open('close_port.txt','w').close()
open_file_handler = open('open_port.txt', 'a')
close_file_handler = open('close_port.txt','a')

class WorkerThread(Thread):
    def __init__(self, scan_ip, start_port, end_port, thread_id):        
        self.start_port = start_port
        self.scan_ip = scan_ip
        self.end_port = end_port
        self.thread_id = thread_id
        Thread.__init__(self)
    def run(self):
        for port in range(self.start_port, self.end_port):
            print("Following port "+str(port)+" is scanned by "+str(self.thread_id))
            output = sr1(IP(dst = self.scan_ip)/TCP(dport = port, flags = 'S'), timeout = 1)
            if output is not None:
                open_file_handler.write(str(port)+" port is open\n")
            else:
                close_file_handler.write(str(port)+" port is closed\n")

def scan():
    scan_ip = raw_input('Enter the IP/URL to scan: ')
    starting_port = int(raw_input('Enter the starting port: '))
    ending_port = int(raw_input('Enter the starting port: '))
    divisor = 1
    port_range = ending_port - starting_port
    for num in range(1, 50):
        if port_range%num == 0:
            divisor = num
    quotient = port_range/divisor
    threads = []
    for i in range(divisor):
        threads.append(WorkerThread(scan_ip ,starting_port + i*quotient, starting_port + (i+1)*quotient, i))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    open_file_handler.close()
    close_file_handler.close()
 
if __name__=='__main__':
    scan()
