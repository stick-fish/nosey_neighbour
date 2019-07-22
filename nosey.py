#!/usr/bin/python

'''
Nosey Neighbour, simple automated python script using bash to complete simple enum scripts

For now runs broad nmap, dirb, nikto

'''
import sys, os, time


class Nosey_neighbor:

	def nmap(self, nmap):
		cmd = 'nmap -Pn -p- -T4 ' + target + ' -vv -oA initial-scan'
		os.system(cmd)

	def dirb(self, cmd2):
		cmd2 = 'dirb http://' + target + ' -r |tee dirb-initial.txt'
		cmd3 = 'dirb https://' + target + ' -r |tee dirb-initial.txt'
		#os.system(cmd)

	def nikto(self, cmd4):
		cmd4 = 'nikto -host ' + target + ' -port 80 -evasion 5 |tee nikto.txt'
		cmd5 = 'nikto -host ' + target + ' -port 443 -evasion 5 |tee nikto.txt'
		#os.system(cmd)

nosey = Nosey_neighbor()

if len(sys.argv) < 2:
	print 'Usage: ' + sys.argv[1] + ' Host'

else:
	# Remote Host
	target = str(sys.argv[1])

	# Initial Scan performed
	nosey.nmap(target)
	print '[+] Nmap completed...'
	time.sleep(5)

	# Grep files and also show output of open HTTP/S
	print '[+] Checking for Http(s) ports'
	time.sleep(5)
	http = os.system('cat initial-scan.nmap | grep --color 80/tcp')
	https = os.system('cat initial-scan.nmap | grep --color 443/tcp')

	if http:
		nosey.dirb(cmd2)
		nosey.nikto(cmd4)
	elif https:
		nosey.dirb(cmd3)
		nosey.nikto(cmd5)
	else:
		print 'No HTTP/S ports found, check Nmap results to make sure.'
