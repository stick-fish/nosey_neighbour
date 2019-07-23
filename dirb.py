#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def dirb_http():
	cmd2 = 'dirb http://' + target + ' -r |tee dirb_http.txt'
	os.system(cmd2)

def dirb_https():
	cmd3 = 'dirb https://' + target + ' -r |tee dirb_https.txt'
	os.system(cmd3)

