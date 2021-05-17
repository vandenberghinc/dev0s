#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.config import *
from dev0s.classes import code
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_

# the wifi object class.
class WiFi(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"dev0s.wifi", 
			"initialized":True,
			"description":[], 
			"chapter": "Network", }

		#

	# connect with a wifi network.
	def connect(self,
		# the network's ssid.
		ssid=None,
		# the network's password.
		password=None,
	):

		# linux.
		if defaults.vars.os in ["linux"]:
			path = f"/etc/netplan/{ssid}.yaml"
			Files.Save(path, f"""network:
		wifis:
	    	wlan0:
	        	dhcp4: true
	        	optional: true
	        	access-points:
	            	"{ssid}":
	            	    password: "{password}" """, sudo=True)
			response = code.execute("sudo netplan generate")
			if not response.success: return response
			response = code.execute("sudo netplan apply")
			if not response.success: return response
			return _response_.success(f"Successfully connected with {ssid}.")
		
		# invalid os.
		else:
			return _response_.error(f"Invalid operating system {defaults.vars.os}.")


# initialized classes.
wifi = WiFi()
