#!/usr/bin/python3

import os
import sys



class Vars:

	'''
	General class for all shared variables or functions etc
	This page will become the main area for setting preferences eg NMAP flags.
	Will start moving the repeated items here in future updates.
	'''


	BANNER = '''
	  _   _                        _   _      _       _     _                       
	 | \ | | ___  ___  ___ _   _  | \ | | ___(_) __ _| |__ | |__   ___  _   _ _ __  
	 |  \| |/ _ \/ __|/ _ \ | | | |  \| |/ _ \ |/ _` | '_ \| '_ \ / _ \| | | | '__| 
	 | |\  | (_) \__ \  __/ |_| | | |\  |  __/ | (_| | | | | |_) | (_) | |_| | |    
	 |_| \_|\___/|___/\___|\__, | |_| \_|\___|_|\__, |_| |_|_.__/ \___/ \__,_|_|    
	                       |___/                |___/                               

	stickfish V2.0 2021
	><> 
	Basic Target Enumeration 
	'''
	
	# Target system ( RHOST )
	TARGET = str(sys.argv[1])

	# Terminal output colors, kept as class variables for ease
	RED = 'echo "\e[31m"'
	GREEN = 'echo "\e[32m"'
	YELLOW = 'echo "\e[33m"'
	BLUE = 'echo "\e[34m"'
	PLAIN = 'echo "\e[0m"'

	BOLD = 'echo "\e[1m"'

	# Horizontal line seperator for each section
	HORIZ = '---' * 40 + '(0)'

	# Change this if you want scan results saved elsewhere, edit the scan flags in nmap section
	OUTPUT_FILE = "/tmp/nmap-initial.txt"


	# Simple command function to run stuff in terminal
	def cmd(self, command):		
		command = os.system(command)		
		return command




var = Vars()


'''
# Reading file contents to check against ( Left here just in case needed )
def read_file(self):
	with open(self.OUTPUT_FILE) as file:
		content = file.readlines()
		for line in content:
			print(line)
'''
