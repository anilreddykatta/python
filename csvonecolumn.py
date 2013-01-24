#!/usr/bin/env python
from csv import reader
from csv import writer
import sys
def take_parameters():
    global input_file_name
    input_file_name = raw_input('Enter the filename: ')
    if not input_file_name.endswith('.csv'):
        input_file_name = input_file_name + '.csv'

def read_write():
    input_file_handle = open(input_file_name, 'rb')
    csv_reader = reader(input_file_handle, delimiter = ',' )
    output_file_name = input_file_name.split('.csv')[0]+'_output.csv'
    output_file_handle = open(output_file_name, 'wb')
    csv_writer = writer(output_file_handle, delimiter=',')
    line_number = 0
    for row in csv_reader:
        li = row[0].split('\t')
        line_number += 1
        print(line_number)
        for elem in li:
            if len(elem) != 0:
                print(elem+'\n')
                elem = float(elem)
                elem = [elem]
                csv_writer.writerow(elem)
    input_file_handle.close()
    output_file_handle.close()

if __name__=='__main__':
    take_parameters()
    read_write()
