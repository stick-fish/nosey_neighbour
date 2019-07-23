#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def nikto_http():
	cmd4 = 'nikto -host ' + target + ' -port 80 -evasion 5 |tee nikto.txt'
	os.system(cmd4)

def nikto_https():
	cmd5 = 'nikto -host ' + target + ' -port 443 -evasion 5 |tee nikto.txt'
	os.system(cmd5)

