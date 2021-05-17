#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.config import *
from dev0s.classes import code
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_
from dev0s.classes.requests import requests
from dev0s.classes.network import firewall

# pip.
import requests as __requests__

# the network object class.
class Network(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"dev0s.network", 
			"initialized":True,
			"description":[], 
			"chapter": "Network", }

		# variables.
		self._info_ = None
		self.api_key = None
		if os.environ.get("IPINFO_API_KEY") not in ["None", "", None]:
			self.api_key = os.environ.get("IPINFO_API_KEY")

		# firewall.
		self.firewall = None
		if defaults.vars.os in ["linux"]:
			self.firewall = firewall.FireWall()

		# sys vars.
		self.__cache__ = {}
		self.__timestamps__ = {}

		#

		#

	# get network info.
	def info(self):
		try: self.__cache__["info"]
		except KeyError: self.__cache__["info"] = {}
		if self.__cache__["info"] != {}: return self.__cache__["info"]

		# get info.
		"""
		info = None
		if self.api_key == None: 
			request_obj = __requests__.get('https://ipinfo.io/json')
		else: 
			request_obj = __requests__.get('https://ipinfo.io/json', headers={'Authorization': f'Bearer {self.api_key}'})
		try:
			info = request_obj.json()
		except Exception as e:
			return _response_.error(f"Failed to serialze (https://ipinfo.io/json) [{request_obj.status_code}]: {request_obj.text}.")
		try: 
			error = info["error"]
			if "rate limit exceeded" in str(error["title"]).lower():
				return _response_.error(f"(https://ipinfo.io/json) {error['title']}: {error['message'].replace('  ',' ')} Define environment variable $IPINFO_API_KEY to specify an api key.")
			else:
				return _response_.error(f"(https://ipinfo.io/json) {error['title']}: {error['message'].replace('  ',' ')}")
		except KeyError: a=1
		"""

		# request.
		if self.api_key == None:
			response = requests.get('https://ipinfo.io/json', serialize=True)
		else:
			response = requests.get('https://ipinfo.io/json', data={'Authorization': f'Bearer {self.api_key}'}, serialize=True)

		# handle.
		if "success" in response and not response.success: return response
		elif "error" in response:
			if "rate limit exceeded" in str(response["title"]).lower():
				return _response_.error(f"(https://ipinfo.io/json) {response['title']}: {response['message'].replace('  ',' ')} Define environment variable $IPINFO_API_KEY to specify an api key.")
			else:
				return _response_.error(f"(https://ipinfo.io/json) {response['title']}: {response['message'].replace('  ',' ')}")

		# clean.
		if "readme" in response:
			del response["readme"]

		# set.
		info = response
		try: 
			x = info["ip"]
			del(info["ip"])
			info["public_ip"] = x
		except KeyError: 
			return _response_.error("Unable to fetch netork info.")
		try: info["private_ip"] = self.__get_private_ip__()
		except: info["private_ip"] = "unknown"
		try: info["hostname"] = socket.gethostname()
		except: info["hostname"] = "unknown"

		# success.
		self.__cache__["info"] = _response_.success(f"Successfully retrieved the network information.", info)
		return self.__cache__["info"]

		#

	# convert a dns to ip.
	def convert_dns(self, dns, timeout=1):
		response = self.ping(dns, timeout=timeout)
		if response["error"] != None: return response
		if response["ip"] == None: 
			return _response_.error(f"Failed to convert dns [{dns}].")
		return _response_.success(f"Successfully converted dns [{dns}].", {
			"ip":response["ip"]
		})

	# ping an ip.
	def ping(self, ip, timeout=1):

		# set info.
		info = {
			"ip":None,
			"up":False,
		}

		# execute.
		response = code.execute(f"ping {ip}", async_=True, wait=False)
		if not response.success: return response
		process = response.process
		time.sleep(timeout)
		response = process.kill()
		if not response.success: return response
		response = process.read()
		if not response.success: return response
		output = response.output

		# handle.
		info["dns"] = ip
		try: info["ip"] = output.split(f"PING {ip} (")[1].split("):")[0]
		except: info["ip"] = None
		if "Request timeout for" in output:
			info["up"] = False
		elif " bytes from " in output:
			info["up"] = True
		else:
			info["up"] = None

		# success.
		return _response_.success(f"Successfully pinged [{ip}].", info)

		#
	
	# port in use
	def port_in_use(self, port, host="127.0.0.1"):
		a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		location = (host, port)
		result_of_check = a_socket.connect_ex(location)
		if result_of_check == 0: in_use = True
		else: in_use = False
		a_socket.close()
		return in_use
		#
	
	# find free port.
	def free_port(self, start=6080):
		for i in range(10000):
			port = start + i
			if not self.port_in_use(port):
				return _response_.success(f"Successfully found a free port.", {
					"port":port,
				})
		return _response_.error(f"Unable to find a free port.")
		#

	# system functions.
	def __get_private_ip__(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			# doesn't even have to be reachable
			s.connect(('10.255.255.255', 1))
			ip = s.getsockname()[0]
		except Exception:
			ip = '127.0.0.1'
		finally:
			s.close()
		return ip
		#

# initialized classes.
network = Network()

"""

# get network info.
response = network.info("vandenberghinc.com")

# ping an ip.
response = network.ping("192.168.1.200")

# convert a dns.
response = network.convert_dns("vandenberghinc.com")

"""
