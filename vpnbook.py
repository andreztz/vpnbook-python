#!/usr/bin/python
''' Fetches Password for vpnbook and then connects the system to the VPN '''
import re
import os

from lxml import html
import requests



# GET weburl containing the password
website = requests.get('http://vpnbook.com/#openvpn')
# Structures the website content
tree = html.fromstring(website.content)

# xpath is a way of locating information in structure documents such as HTML or XML
passwd_file = tree.xpath('//li/strong/text()')


psswd = ""
usrnm = ""
got_password = False
got_username = False


if ('yes' in  raw_input("Do you need to fetch password (yes/no)? ")):
	for things in passwd_file:
		if re.search('Username:', things):
			print things
			usrnm = things
			got_username = True
	
		if re.search('Password:', things):
			'''re library provides a search function 
			with the syntax re.search(search_term, <any line>) '''
			print things
			psswd = things
			got_password = True
	
		# breaks out of the loop once the username and password is found
		if (got_username and got_password):
			break


print "\n\n"
os.system('ls -R /etc/openvpn')
print "\n\n"
vpn_config = raw_input("VPN Configuration file location :")

os.system('sudo openvpn --config ' + vpn_config)



	
