# Automating Network Management Activities

Automate workflows, config push, backups, handling of the network dynamics including troubleshooting using python

## Getting Started

This project has few python scripts:
1. Copy image file to tftp server and then to network devices
2. Encrypt device credentials file to use it for login to devices from other programs
3. Push configuration to devices from config file
3. Back up configuration from devices

### Installing

Few things you need to install to get development env running

```
apt-get update 
apt-get install python -y
apt-get install build-essential libssl-dev libffi-dev -y
apt-get install python-pip -y
pip install cryptography
pip install paramiko
pip install netmiko
apt-get install python-pexpect
```

## Deployment

Add additional notes about how to deploy this on a live system

## Versioning



## Authors

** Rahul Deshmukh ** - *Initial work* - [radeshmukh](https://github.com/radeshmukh)

## License
Not licensed. Feel free to use them


