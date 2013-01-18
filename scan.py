#!/usr/bin/env python

from subprocess import check_call
from subprocess import CalledProcessError


ip_results = open('ip_results.txt','w')
def main():
    global ip_results
    for ip_range in range(50,100):
	ip_string = '192.168.1.'+str(ip_range)
	scan(ip_string, 1)
    ip_results.close()
def scan(ip_string, number_of_scans):
	try:
		count_attr = '-c '+str(number_of_scans)
		check_call(['ping', ip_string, count_attr, '-W 2'])
	except CalledProcessError:
		ip_results.write(str(ip_string)+"\n")
if __name__=='__main__':
	main()
