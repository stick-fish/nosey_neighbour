#!/usr/bin/python

'''
Nosey Neighbour, simple automated python script using bash to complete simple enum scripts

For now runs broad nmap, dirb, nikto. Modify the commands in each file to get a different result.
ASCII ART: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
Eg: python ./nosey.py 10.10.1.10

'''
print '''
  _   _                        _   _      _       _     _                       
 | \ | | ___  ___  ___ _   _  | \ | | ___(_) __ _| |__ | |__   ___  _   _ _ __  
 |  \| |/ _ \/ __|/ _ \ | | | |  \| |/ _ \ |/ _` | '_ \| '_ \ / _ \| | | | '__| 
 | |\  | (_) \__ \  __/ |_| | | |\  |  __/ | (_| | | | | |_) | (_) | |_| | |    
 |_| \_|\___/|___/\___|\__, | |_| \_|\___|_|\__, |_| |_|_.__/ \___/ \__,_|_|    
                       |___/                |___/                               

stickfish V1.0 2019

'''
import sys, os, time
import nikto
import dirb

target = str(sys.argv[1])

green = 'echo -e "Default \e[32mGreen"'
red = 'echo -e "Default \e[31mRed"'
regular = 'echo -e \e[0m'

def nmap():
	cmd = 'nmap -Pn -p- -T4 ' + target + ' -vv -oA initial-scan'
	os.system(cmd)
		
nmap()
print '\n'
print '-\/-' * 15
print ' '
print '[+] Nmap completed...'
print ' '
print '[+] Checking for Http(s) ports'
time.sleep(3)
print ' '
http = os.system('cat initial-scan.nmap | grep --color 80/tcp')
https = os.system('cat initial-scan.nmap | grep --color 443/tcp')
print ' '
print '-\/-' * 15
print ' '

if http == 0:
	print '[+] starting HTTP Dirb directory scan...\n'
	dirb.dirb_http()
	print '\n'
	print '-\/-' * 15
	print '\n'
	print '[+] starting HTTP Nikto Scan...\n'
	nikto.nikto_http()

elif https == 0:
	print '[+] starting HTTPS Dirb directory scan...\n'
	dirb.dirb_https()
	print '\n'
	print '-\/-' * 15
	print '\n'
	print '[+] starting HTTPS Nikto Scan...\n'
	nikto.nikto_https()

else:
	print 'No HTTP/S ports found on standard numbering, check Nmap results to make sure.'
