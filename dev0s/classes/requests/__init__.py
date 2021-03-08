#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.response import *
from dev0s.classes import objects

# pip imports.
import urllib
import requests as __requests__

# the requests class.
class Requests():

	# variables.
	https = True
	allow_redirects = True

	# utils.
	def encode(data):
		return f"?{urllib.parse.urlencode(data)}"
		#

	# get.
	def get(
		# the url (str) (#1).
		url=None,
		# the sended post data (dict) (#2).
		data={},
		# serialize output to dictionary.
		serialize=False,
	):
		
		# url.
		url = f"{Boolean(Requests.https).string(true='https', false='http')}://"+gfp.clean(f"{url}/", remove_double_slash=True, remove_last_slash=False)
		if data != {}: url += Requests.encode(data)

		# request.
		original_request_object = __requests__.get(url, allow_redirects=Requests.allow_redirects)
		if original_request_object.status_code != 200:
			return Response.error(f"Invalid request ({url}) [{original_request_object.status_code}]: {original_request_object.text}")
		if serialize:
			try: response = Response.ResponseObject(json=original_request_object.json())
			except Exception as e: 
				return Response.error(f"Unable to serialize output: {original_request_object}, error: {e}.")
			return response
		return original_request_object


	# the restapi over ssh object class.
	class RestAPI(objects.Object):
		def __init__(self, 
			# the root url (optional).
			url=None,
			# the default data send with every request (will be appended to local data).
			data={
				"api_key":None,
			},
		):
			
			# defaults.
			objects.Object.__init__(self, traceback="Requests.RestAPI")
			
			# attributes.
			self.url = url
			self.data = data

			#
		def request(self, url="/", data={}):
			
			# data.
			for key,value in self.data.items(): 
				data[key] = value

			# url.
			if self.url != None: 
				url = gfp.clean(f"{self.url}/{url}/", remove_double_slash=True, remove_last_slash=False)
			
			# request.
			return Requests.get(serialize=True, url=url, data=data)

			#

		#

	#

#

#