#!/usr/bin/env python

from threading import Thread
from subprocess import check_call
from subprocess import CalledProcessError

#ip_results = open('ip_thread_results.txt','w')
def scan(ip_range):
    for in_ip_range in ip_range:
        ip_string = "192.168.1."+str(in_ip_range)
        try:
            count_attr = '-c '+str(1)
            check_call(['ping', ip_string, count_attr, '-W 1'])
        except CalledProcessError:
            ip_results.write(ip_string+'\n')
def main():
    global ip_results
    ip_results = open('ip_thread_results.txt','w')
    lowlist = list(range(100,125))
    highlist = list(range(126,150))
    Thread(target = scan, args =[lowlist]).start()
    Thread(target = scan, args =[highlist]).start()
    #threads = []
    #for diff in range(100//10):
    #    start = diff*10 + 1
    #    Thread(target = scan, args = [range(start, (diff+1)*10)]).start()                                  
if __name__=='__main__':
	main()
