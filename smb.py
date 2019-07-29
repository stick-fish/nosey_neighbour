#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def smb_windows():
	cmd6 = 'enum4linux ' + target + ' -a |tee enum4linux.txt'
	print '[+] Running enum4linux... '
	os.system(cmd6)
