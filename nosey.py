#!/usr/bin/python3

import os
import sys
from variables import var
from web_services import *
from nmap_scanning import *



'''
Updated version to now be run in Python 3 instead of 2.
Not too fancy, just a simple idea I had while studying OSCP and HTB.
Similar to others out there but good to know whats been run on your system, 
tried to make this as readable as possible and added comments to explain what I had intended. 

Tested and developed using Metasploitable 2 from Rapid 7 ( https://www.rapid7.com/ )

ASCII ART: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

Eg: python ./nosey.py 192.168.159.5

'''

if len(sys.argv) < 2:
	var.cmd(var.RED)
	print("[!!] Usage: python3 nosey.py 192.168.159.5")
	var.cmd(var.PLAIN)
	sys.exit()

else:
	var.cmd(var.GREEN)
	print(var.BANNER)
	#var.cmd(var.PLAIN)

	# Initial NMAP command, placed here for ease of editing
	nmap_scan.InitialScan()

	# Checking any found web services
	web_scan.InitialWebCheck()
	
