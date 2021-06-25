#!/usr/bin/python3

from variables import var
from nmap_scanning import *


class WebServices:
	'''
	This will check to see if there are any web related services being run, 
	if any are found then its able to start further enumeration on each port.
	'''

	# Class variables for well known ports usually associated with web, 
	# created lists here should extra ports be added that are not running on common convention 
	HTTP = [80]
	HTTPS = [443]
	DNS = [53]

	
	def InitialWebCheck(self):
		'''
		Primary purpose is to check which tests to be performed based on available ports found.

		'''
		
		# Comparing common port numbers to initial NMAP scan, made global for now temporary fix
		global web_port
		MSG = ""
		URL = ""
		SERVICE = ""
		SERVICE_CMD = ""

		for web_port in nmap_scan.port_open():

			if web_port in self.HTTP:
				URL = "http://"
				self.host_web(MSG, URL, SERVICE, SERVICE_CMD)
				self.directory_scan(MSG, URL, SERVICE, SERVICE_CMD)				
			
			if web_port in self.HTTPS:
				URL = "https://"
				self.host_web(MSG, URL, SERVICE, SERVICE_CMD)
				self.directory_scan(MSG, URL, SERVICE, SERVICE_CMD)
			
			if web_port in self.DNS:
				self.dns(MSG, URL, SERVICE, SERVICE_CMD)
			
			else:
				continue


	
	def template(self, MSG, URL, SERVICE, SERVICE_CMD):
		'''
		Minimal template to keep the web service related info uniform.
		Each web method can now use the same template, but only need to change 2 variables.
		SERVICE & SERVICE_CMD will be the constant across all methods here and only set them 
		for each specific task / check.
		'''

		# TODO: Find a better way to apply coloring to avoid all the extra new lines added
		print(var.HORIZ, end = '\n')		
		var.cmd(var.GREEN + ';' + var.BOLD)		
		
		print(f"[+] {SERVICE}")
		print(f"{MSG}")		
		
		var.cmd(var.BLUE)
		print(f"[!] Command used:\n{SERVICE_CMD}")
		var.cmd(var.YELLOW)
			
		var.cmd(SERVICE_CMD)
		var.cmd(var.PLAIN)
		URL = ""
				

	
	def host_web(self, MSG, URL, SERVICE, SERVICE_CMD):
		'''
		Check to see if any host information is resolvable based on running web service.
		'''
		MSG = ""
		URL = ""

		SERVICE = f"HOSTNAME / IP CHECK TCP: {web_port}"
		SERVICE_CMD = f"host -a {var.TARGET}"
		self.template(MSG, URL, SERVICE, SERVICE_CMD)
		return MSG, URL, SERVICE, SERVICE_CMD


	
	def dns(self, MSG, URL, SERVICE, SERVICE_CMD):
		'''
		Basic tests against any DNS service (TCP:53) found based on initial NMAP scan.
		'''

		SERVICE = f"DNS INFO TCP: {web_port}"
		SERVICE_CMD = f"dnsenum -v {var.TARGET}"
		self.template(MSG, URL, SERVICE, SERVICE_CMD)
		return MSG, URL, SERVICE, SERVICE_CMD


	def directory_scan(self, MSG, URL, SERVICE, SERVICE_CMD):
		'''
		If any possible web related ports found, then one of the most basic checks needed is to run
		directory enumeration in the background. Simple enumeration will be started and the user can 
		then decide if further enum is needed.
		If both 80 & 443 found, will prompt user which service to fuzz (Future TODO)
		MSG: Text line just to use the same one across similar services
		URL: Prepended for either http/s services
		To install sec-lists manually: apt -y install seclists 
		'''

		# Chose to use seclists, short list less than 100 entries
		# If you dont want seclists then you can edit the wordlist to one you prefer
		wordlist = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/Logins.fuzz.txt"
		downloaded_wordlist = "logins.fuzz.txt"

		SERVICE = f"DIRECTORY SCAN ON TCP: {web_port}"
		MSG = "[+] Grabbing Seclist: logins.fuzz.txt"
		SERVICE_CMD = f"wget -q {wordlist} -O logins.fuzz.txt;\ngobuster -m dir -w {downloaded_wordlist} -u {URL}{var.TARGET}"
		
		self.template(MSG, URL, SERVICE, SERVICE_CMD)
		return MSG, URL, SERVICE, SERVICE_CMD




web_scan = WebServices()
