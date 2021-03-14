#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.response import *
from dev0s.classes.defaults import objects
from dev0s.classes.response import response as _response_

# pip imports.
import urllib
import requests as __requests__

# the requests class.
class Requests(object):
	def __init__(self):
		
		# docs.
		DOCS = {
			"module":"dev0s.requests", 
			"initialized":True,
			"description":[], 
		}

		# attributes.
		self.https = True
		self.allow_redirects = True

	# encode & decode data.
	def encode(self, data={}):
		_data_ = {}
		for key,value in data.items():
			if value.__class__.__name__ in ["OutputObject", "ResponseObject"]:
				value = str(value.dict())
			elif isinstance(value, (list,Array,dict,Dictionary)):
				value = str(value)
			_data_[key] = value
		return f"?{urllib.parse.urlencode(_data_)}"
	def quote(self, data={}):
		return urllib.parse.quote(json.dumps(data))
	def unquote(self, encoded, depth=30):
		return json.loads(urllib.parse.unquote(encoded))

	# get.
	def get(self,
		# the url (str) (#1).
		url=None,
		# the sended post data (dict) (#2).
		data={},
		# serialize output to dictionary.
		serialize=False,
	):
		
		# url.
		url = url.replace("http://", "").replace("https://", "")
		url = f"{Boolean(self.https).string(true='https', false='http')}://"+gfp.clean(f"{url}/", remove_double_slash=True, remove_last_slash=False, remove_first_slash=True)
		if data != {}: url += self.encode(data)

		# request.
		original_request_object = __requests__.get(url, allow_redirects=self.allow_redirects)
		if original_request_object.status_code != 200:
			return _response_.error(f"Invalid request ({url}) [{original_request_object.status_code}]: {original_request_object.text}")
		if serialize:
			try: response = _response_.ResponseObject(original_request_object.json())
			except Exception as e: 
				return _response_.error(f"Request ({url}) [{original_request_object.status_code}]: Unable to serialize output: {original_request_object.text}.")
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
			
			# docs.
			DOCS = {
			"module":"dev0s.requests.RestAPI", 
			"initialized":False,
			"description":[], }

			# defaults.
			objects.Object.__init__(self, traceback="dev0s.requests.RestAPI")
			
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
			return requests.get(serialize=True, url=url, data=data)

			#

		#

	#

# initialized classes.
requests = Requests()

#

#