#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
import csv
import json
 
#---- Read in pertinent information from user
dc_in_filename = raw_input('\nInput CSV filename (creds) :  ') or 'creds'
key            = raw_input(  'Encryption key (cisco)     :  ') or 'cisco'
 
#---- Read in the device credentials from CSV file into list of device credentials
with open( dc_in_filename, 'r' ) as dc_in:
    device_creds_reader = csv.reader( dc_in )
    device_creds_list1 = [device for device in device_creds_reader]
device_creds_list = [device_creds_list1[0][0], device_creds_list1[0][1]] 
print '\n----- device_creds ---------------------------------------------------'
print( device_creds_list )
 
#---- Encrypt the device credentials using ken from user
encrypted_dc_out_filename = raw_input('\nOutput encrypted filename (encr-creds):  ') or 'encr-creds'
 
with open( encrypted_dc_out_filename, 'wb' ) as dc_out:
    dc_out.write( encrypt( key, json.dumps( device_creds_list ) ) )
 
print "encrypted file is created"
 
with open( encrypted_dc_out_filename, 'rb' ) as dc_in:
    device_creds_in = json.loads( decrypt( key, dc_in.read() ) )
 
print '\n----- confirm: device_creds json in -----------------------------------'
print( device_creds_in )
