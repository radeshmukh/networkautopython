#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import date
import os
from simplecrypt import encrypt, decrypt
import json

with open( '/workspace/python/config-bkup/encr-creds', 'rb' ) as dc_in:
    device_creds_in = json.loads( decrypt( 'json.holds', dc_in.read() ) )
username = device_creds_in[0]
password = device_creds_in[1]

# Open file with list of devices to take config backup
with open('/workspace/python/config-bkup/devices_file') as f:
    devices_list = f.read().splitlines()

# Create directory for saving output            
path = '/workspace/network/backup/' + str(date.today())    
# define the access rights    
access_rights = 0o777    
try:
    os.mkdir(path, access_rights)    
except OSError:    
    print ("Creation of directory %s failed" % path)    
else:
    print ("Successfully created directory %s" % path)    

# logging into all devices from devices_list to take backup
for devices in devices_list:
    print '\nConnecting to device ' + devices
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'Authentication failure on ' + ip_address_of_device
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + ip_address_of_device
        continue
    except (EOFError):
        print "End of file while attempting device " + ip_address_of_device
        continue
    except (SSHException):
        print 'SSH Issue. Are you sure SSH is enabled on ' + ip_address_of_device + '?'
        continue
    except Exception as unknown_error:
        print 'Some other error: ' + str(unknown_error)
        continue

    # Get config from devices
    print 'Executing show run command'
    run_config = net_connect.send_command('show run')

    # Save config to file
    output_file = path + '/' + devices + '-' + str(date.today()) + '.cfg'
    output = open(output_file, 'w')
    output.write(run_config)
    output.close
    print '*** Running config saved for ' + devices + ' ***'

print '\nConfig from all above devices is backed up at ' + path
