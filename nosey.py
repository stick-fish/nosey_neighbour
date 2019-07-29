#!/usr/bin/python

import sys, os, time
import nikto
import dirb
import smb

target = str(sys.argv[1])

'''
cmd 2,3 = dirb
cmd 4,5 = nikto
cmd 6 = smb
Nosey Neighbour, simple automated python script using bash to complete simple enum scripts

For now runs broad nmap, dirb, nikto, smb. Modify the commands in each file to get a different result.
Still a work in progress, figuring it out.
ASCII ART: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
Eg: python ./nosey.py 10.10.1.10

'''
# Bling section:

green = 'echo "\e[32m"'
red = 'echo "\e[31m"'
yellow = 'echo "\e[33m"'
plain = 'echo "\e[0m"'


os.system(yellow)

print '''
  _   _                        _   _      _       _     _                       
 | \ | | ___  ___  ___ _   _  | \ | | ___(_) __ _| |__ | |__   ___  _   _ _ __  
 |  \| |/ _ \/ __|/ _ \ | | | |  \| |/ _ \ |/ _` | '_ \| '_ \ / _ \| | | | '__| 
 | |\  | (_) \__ \  __/ |_| | | |\  |  __/ | (_| | | | | |_) | (_) | |_| | |    
 |_| \_|\___/|___/\___|\__, | |_| \_|\___|_|\__, |_| |_|_.__/ \___/ \__,_|_|    
                       |___/                |___/                               

stickfish V1.1 2019

'''

os.system(plain)

def nmap():
	cmd = 'nmap -Pn -p- -T4 ' + target + ' -vv -oA initial-scan '
	os.system(green)
	print '[+] Command run: ' + cmd
	os.system(plain)
	os.system(cmd)
		
nmap()
print '\n'
print '-\/-' * 15
print ' '
os.system(green)
print '[+] Nmap completed...'
print ' '
os.system(plain)
print '[+] Checking for open ports'
time.sleep(3)
print ' '

http = os.system('cat initial-scan.nmap | grep --color 80/tcp')
https = os.system('cat initial-scan.nmap | grep --color 443/tcp')
smb = os.system('cat initial-scan.nmap | grep --color 445/tcp')
# future = os.system('cat initial-scan.nmap | grep --color 443/tcp')

print ' '
print '-\/-' * 15
print ' '

# Change to a master function to replace multiple ifs...

if http == 0:
	os.system(green)
	print '[+] Starting HTTP Dirb directory scan...\n'
	os.system(plain)
	dirb.dirb_http()
	print '\n'
	print '-\/-' * 15
	print '\n'
	os.system(green)
	print '[+] Starting HTTP Nikto Scan...\n'
	os.system(plain)
	nikto.nikto_http()

elif https == 0:
	os.system(green)
	print '[+] Starting HTTPS Dirb directory scan...\n'
	os.system(plain)
	dirb.dirb_https()
	print '\n'
	print '-\/-' * 15
	print '\n'
	os.system(green)
	print '[+] Starting HTTPS Nikto Scan...\n'
	os.system(plain)
	nikto.nikto_https()

else:
	os.system(red)
	print 'No HTTP/S ports found on standard numbering, check Nmap results to make sure.'
	os.system(plain)

# If tcp 445 open

if smb == 0:
	os.system(green)
	print '[+] Starting SMB / Samba service scan...\n'
	os.system(plain)
	smb.smb_windows()
	print '\n'
	print '-\/-' * 15
	print '\n'
	
else:
	os.system(red)
	print 'No open SMB ports found on standard numbering, check Nmap results to make sure.'
	os.system(plain)

os.system(green)
print '[+] Listing scan results ...'
os.system(plain)

os.system('ls -la')
exit(0)
