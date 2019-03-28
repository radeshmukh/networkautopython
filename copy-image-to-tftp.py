#!/usr/bin/env python

import os
from getpass import getpass

USERNAME = raw_input('Enter your SCP username (rdeshmu2): ') or 'rdeshmu2'
FILEPATH = raw_input('Enter file path including filename: ')

COPIED_FILESIZE = 0
FILESIZE = os.path.getsize(FILEPATH)
LIST = FILEPATH.split('/')
FILE = LIST[-1]
COPIED_FILE = '/tftpboot/' + FILE

while FILESIZE != COPIED_FILESIZE:
    os.system('scp ' + USERNAME + '@atc-view1-new:' + FILEPATH + ' /tftpboot/')
    COPIED_FILESIZE = os.path.getsize(COPIED_FILE)

print ('File is copied in its entirety, Original filesize:' + str(FILESIZE) + ' and copied filesize:' + str(COPIED_FILESIZE))
os.system('chmod 755 ' + COPIED_FILE)
print ('File permissions are changed to 755')
