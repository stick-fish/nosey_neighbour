#!/usr/bin/python3

from variables import var
from time import sleep
from nmap import *
import sys


class Nmap:

	'''
	Initial nmap scan against target, outputs results in all formats depending which you prefer to use. 
	The start of the program is here, based on what the NMAP module is able to find will determine the rest of the checks.
	Should the NMAP scan take too long or you know the ports beforehand, edit the 'host' and 'ports' variables below.
	Built and tested on nmap version python-nmap 0.6.4 library (https://pypi.org/project/python-nmap/)   
	'''


	def InitialScan(self):
		'''
		The start of the program is here, based on what the NMAP module is able to find will determine the rest of the checks.
		Should the NMAP scan take too long or you know the ports beforehand, edit the 'host' and 'ports' variables below.
		'''

		status = "open"
		host = var.TARGET

		#ports = "1-65535"                      # All port scan, uncomment if you in a rush.
		ports = "1-100"                         # NMAP Default
		scan_args = "-T5 -sV"           # Can add in NMAP args here, at a later stage will add this to a launch menu

		try:

			var.cmd(var.GREEN)
			print("[+] Running NMAP initial scan...")
			var.cmd(var.PLAIN)

			scanner.scan(host, ports, arguments=scan_args)

			# Prints command used by NMAP library
			print("[!] Command used: %s" % scanner.command_line() + "\n")

			print(var.HORIZ)

			var.cmd(var.GREEN)
			print("[+] TARGET IP / (HOSTNAME) : %s (%s)" % (host, scanner[host].hostname()))


			if scanner[host].state() == "down":
				# If the host is down
				var.cmd(var.RED)
				print("[-] CURRENT STATUS : %s" % scanner[host].state().upper())
				print("[-] Seems %s may be down or incorrect IP used." % var.TARGET)
				sys.exit()

			else:
				# If the host is up
				print("[+] CURRENT STATUS : %s" % scanner[host].state().upper())

				# Check if TCP or UDP in use, depends on NMAP flags
				for proto in scanner[host].all_protocols():
					found_ports = scanner[host][proto].keys()
					print("[+] PROTOCOL : %s" % proto.upper())


				print(f"[+] PORTS FOUND : {len(found_ports)}")
				var.cmd(var.YELLOW)

				# List the ports found with status, well known service name, version info if any
				# If no version info found the field will be blank

				# Heading for port outputs
				print("PORT\t\tSTATUS\t\tSERVICE\t\t\tVERSION\n" + var.HORIZ)

				global port_list 
				port_list = []
				for port in found_ports:
					# Shortend this to avoid overflow
					host_attr = scanner[host][proto][port]
					print(" %s\t \t%s \t\t%s \t\t\t%s %s" % (port, host_attr['state'], host_attr['name'], host_attr['product'], host_attr['extrainfo']))

					port_list.append(port)


			var.cmd(var.PLAIN)				

		except:
			print("[-] Seems %s may be down or incorrect IP used." % var.TARGET)
			sys.exit()



	def port_open(self):
		return port_list


nmap_scan = Nmap()
scanner = nmap.PortScanner()
