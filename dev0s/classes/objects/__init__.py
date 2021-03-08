#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.exceptions import Exceptions
from dev0s.classes.files import *
from dev0s.classes.response import Response, ResponseObject

# defaults.options.
JSON = "-j" in sys.argv or "--json" in sys.argv

# traceback.
class Traceback(object):
	def __init__(self,
		# the imported traceback (#1).
		traceback="Traceback",
		# the raw traceback (#2).
		raw_traceback="syst3m.classes.objects.Object",
	):

		# defaults.
		self._traceback_ = traceback
		self._raw_traceback_ = traceback

		#
	
	# imported traceback.
	@property
	def traceback(self):
		return self.__traceback__()
	def __traceback__(self, 
		# the function name (optional) (#1).
		function=None,
		# the parameter name (optional) (#2).
		parameter=None,
		# the attrbiute name (optional) (#3).
		attribute=None,
		# raw traceback.
		raw=False,
	):
		options = ""
		if attribute != None:
			options += f".{attribute}"
		elif function != None:
			options += f".{function}"
			if parameter != None:
				options += f".{parameter}"
		if raw:
			return f"<{self._raw_traceback_}{options}>"
		else:
			return f"<{self._traceback_}{options}>"

	#

# object.
class Object(Traceback):
	def __init__(self, 
		# attributes (dict) (#1)
		attributes={},
		# the imported traceback.
		traceback="Object",
		# the raw traceback.
		raw_traceback="syst3m.classes.objects.Object",
	):

		# defaults.
		Traceback.__init__(self, traceback=traceback, raw_traceback=raw_traceback)
		self.assign(attributes)
		#

	# iterations.
	def items(self):
		return vars(self).items()
	def keys(self):
		return list(vars(self).keys())
	def values(self):
		return list(vars(self).values())
	

	# assign self variables by dictionary.
	def assign(self, 
		# the dictionary to self assign.
		dictionary, 
		# serialize dictionary from str to object.
		serialize=True,
		# the keys to get from the dict.
		keys=["*"],
		# safe disabled throws an error when one of the specified keys does not exist.
		safe=True,
	):
		if not isinstance(dictionary, dict):
			raise TypeError("You can only self assign with a dictionary as parameter.")
		if not isinstance(keys, (dict, Dictionary, list, Array) ):
			raise TypeError(f"Parameter [keys] requiers to be a [dict, Dictionary, list, Array] not [{keys.__class__.__name__}].")
		# safe dict keys.
		if isinstance(keys, (dict, Dictionary)):
			for key,value in keys.items():
				skip = False
				if safe:
					try:
						dict_value = dictionary[key]
					except:
						dict_value = value
						skip = False
				else:
					dict_value = dictionary[key]
				if not skip:
					if serialize:
						if dict_value in ["True", "true", "TRUE"]: dict_value = True
						elif dict_value in ["False", "false", "FALSE"]: dict_value = False
						elif dict_value in ["None", "none", "null"]: dict_value = None
					self[key] = dict_value
		# array keys.
		if isinstance(keys, (list, Array)) and "*" not in keys:
			for key in keys:
				skip = False
				if safe:
					try:
						dict_value = dictionary[key]
					except:
						skip = True
				else:
					dict_value = dictionary[key]
				if not skip:
					if serialize:
						if dict_value in ["True", "true", "TRUE"]: dict_value = True
						elif dict_value in ["False", "false", "FALSE"]: dict_value = False
						elif dict_value in ["None", "none", "null"]: dict_value = None
					self[key] = dict_value
		# all keys from dict.
		else:
			for key,value in dictionary.items():
				if serialize:
					if value in ["True", "true", "TRUE"]: value = True
					elif value in ["False", "false", "FALSE"]: value = False
					elif value in ["None", "none", "null"]: value = None
				self[key] = value

	# get all attributes.
	def attributes(self, keys=[]):
		return self.dict(keys=keys)
	def dict(self, keys=[]):
		if keys == []:
			items = self.items()
		else:
			items = []
			for i in keys: items.append([i, self[i]])
		dictionary = {}
		for key, value in items:
			dictionary[key] = value
		return dictionary

		#

	# unpack attributes.
	def unpack(self, 
		# the key / keys / defaults parameter (#1).
		# str instance:
		#   unpack the str key
		# list instance:
		#   unpack all keys in the list.
		# dict instance:
		#   unpack all keys from the dict & when not present return the key's value as default.
		keys,
	):
		defaults = {}
		if isinstance(keys, (dict, Files.Dictionary)):
			if isinstance(keys, dict):
				defaults = dict(keys)
				keys = list(keys.keys())
			else:
				defaults = keys.dict()
				keys = keys.keys()
		elif isinstance(keys, str):
			keys = [keys]
		unpacked = []
		for key in keys:
			value, set = None, True
			try: 
				value = self[key]
			except KeyError: 
				try:
					value = defaults[key]
				except KeyError: 
					set = False
			if not set:
				raise Exceptions.UnpackError(f"Dictionary does not contain attribute [{key}].")
			unpacked.append(value)
		if len(unpacked) == 1:
			return unpacked[0]
		else:
			return unpacked

	# support item assignment.
	def __setitem__(self, key, value):
		setattr(self, key, value)
	def __getitem__(self, key):
		return getattr(self, key)
	def __delitem__(self, key):
		delattr(self, key)

		#

	#

# thread.
class Thread(Object, threading.Thread):
	def __init__(self, 
		# the threads id (#1).
		id="Thread",
		# the imported traceback.
		traceback="Thread",
		# the raw traceback.
		raw_traceback="syst3m.classes.objects.Thread",
		# the threads log level.
		log_level=-1,
	):

		# defaults.
		Object.__init__(self, traceback=traceback, raw_traceback=raw_traceback)
		threading.Thread.__init__(self)

		# args.
		self.log_level = log_level

		# vars.
		try: self.id = id
		except: a=1
		self.__status__ = "initialized"
		self.__response__ = None
		
		#

	# default start (should not be overwritten, use: __run__.
	def run(self):
		self.log(f"Starting thread {self.id}.")
		self.__status__ = "running"
		response = None
		try:
			response = self.__run__()
		except AttributeError:  raise Exceptions.InvalidUsage(f"Thread [{self.id}] is missing the main [__run__] function.")
		if isinstance(response, ResponseObject):
			if response.success:
				self.send_crash(response=response)
			else:
				self.send_stop(response=response)
		else:
			self.send_stop(response=response)
		return self.send_stop(f"Thread [{self.id}] has finished running.")

	# safely start & stop the thread.
	def safe_start(self, timeout=120, sleeptime=1):
		self.log(f"Stopping thread {self.id}.")
		self.start()
		for i in range(int(timeout/sleeptime)):
			if self.running: break
			time.sleep(sleeptime)
		if not self.running: 
			return Response.error(f"Unable to start thread {self}.", log_level=self.log_level, required_log_level=0)
		return Response.success(f"Successfully started thread {self.id}.", log_level=self.log_level, required_log_level=0)
	def safe_stop(self, timeout=120, sleeptime=1):
		self.log(f"Stopping thread {self.id}.")
		self.send_stop()
		for i in range(int(timeout/sleeptime)):
			if self.stopped: break
			time.sleep(sleeptime)
		if not self.stopped: 
			return Response.error(f"Unable to stop thread {self}.")
		found = False
		try:
			response = self.stop()
			found = True
		except AttributeError: response = None
		if not found:
			try:
				response = self.__stop__()
				found = True
			except AttributeError: response = None
		if isinstance(response, ResponseObject) and not response.success:
			return response
		return Response.success(f"Successfully stopped thread {self.id}.", required_log_level=0)

		#

	# send stop & crash from within the __run__ function only.
	def send_stop(self, 
		# all optional.
		# option 1: the success message.
		message=None, # (1)
		args={}, # (2)
		# option 2: the error message.
		error=None,
		# option 3: the response object.
		response=None, 
		# save the message/error/response.
		save=False,
		# the active log level (int) (leave None to use self.log_level).
		log_level=None,
		# the required log level for when to print to console (leave None to use Response.log_level ; default: 0).
		required_log_level=Response.log_level,
	):
		if log_level == None: log_level = self.log_level
		if isinstance(message, (str,String)):
			self.__response__ = Response.success(message, args, log_level=-1, save=False)
			msg = message
		elif isinstance(error, (str,String)):
			self.__response__ = Response.error(error, log_level=-1, save=False)
			msg = error
		elif isinstance(response, ResponseObject):
			self.__response__ = response
			if response["success"]:	
				msg = response["message"]
			else:
				msg = response["error"]
		else:
			raise Exceptions.InvalidUsage("Define one of the following parameters: [message:str, error:str, response:ResponseObject].")
		self.__status__ = "stopping"
		if log_level >= required_log_level or save:
			Response.log(response=self.__response__, save=save, log_level=log_level, required_log_level=required_log_level)
		return self.__response__
		#
	def send_crash(self, 
		# all optional.
		# option 1: the success message.
		message=None, # (1)
		args={}, # (2)
		# option 2: the error message.
		error=None,
		# option 3: the response object.
		response=None, 
		# save the message/error/response.
		save=False,
		# the active log level (int) (leave None to use self.log_level).
		log_level=None,
		# the required log level for when to print to console (leave None to use Response.log_level ; default: 0).
		required_log_level=Response.log_level,
	):
		if log_level == None: log_level = self.log_level
		if isinstance(message, (str,String)):
			self.__response__ = Response.success(message, args, log_level=-1, save=False)
			msg = message
		elif isinstance(error, (str,String)):
			self.__response__ = Response.error(error, log_level=-1, save=False)
			msg = error
		elif isinstance(response, ResponseObject):
			self.__response__ = response
			if response["success"]:
				msg = response["message"]
			else:
				msg = response["error"]
		else:
			raise Exceptions.InvalidUsage("Define one of the following parameters: [message:str, error:str, response:ResponseObject].")
		self.__status__ = "crashed"
		if log_level >= required_log_level or save:
			Response.log(response=self.__response__, save=save, log_level=log_level, required_log_level=required_log_level)
		return self.__response__
		#

		#

	# copy functions.
	def log(self, 
		# option 1:
		# the message (#1 param).
		message=None,
		# option 2:
		# the error.
		error=None,
		# option 3:
		# the response dict (leave message None to use).
		response={},
		# print the response as json.
		json=JSON,
		# optionals:
		# the active log level (leave None to use self.log_level).
		log_level=None,
		# the required log level for when printed to console.
		required_log_level=0, 
		# save to log file.
		save=False,
		# save errors always (for options 2 & 3 only).
		save_errors=None,
		# the log mode (leave None for default).
		mode=None,
	):
		if log_level == None: log_level = self.log_level
		return Response.log( 
			# option 1:
			# the message (#1 param).
			message=message,
			# option 2:
			# the error.
			error=error,
			# option 3:
			# the response dict (leave message None to use).
			response=response,
			# print the response as json.
			json=json,
			# optionals:
			# the active log level.
			log_level=log_level,
			# the required log level for when printed to console (leave None to use self.log_level).
			required_log_level=required_log_level, 
			# save to log file.
			save=save,
			# save errors always (for options 2 & 3 only).
			save_errors=save_errors,
			# the log mode (leave None for default).
			mode=mode,
		)

	#properties
	@property
	def run_permission(self):
		return self.__status__ in ["running"]
	@property
	def running(self):
		return self.__status__ in ["running", "stopping"]
	@property
	def stopped(self):
		return self.__status__ in ["stopped"]
	@property
	def crashed(self):
		return self.__status__ in ["crashed"]
	@property
	def response(self):
		return self.__response__
	# str representation.
	def __str__(self):
		error = None
		if self.crashed:
			try: error = self.response.error
			except: error = None
		if error != None:
			return f"<{self.__traceback__()[1:-1]} (crashed: {self.crashed}) (error: {error}) >"
		else:
			return f"<{self.__traceback__()[1:-1]} (running: {self.running}) (stopped: {self.stopped}) (crashed: {self.crashed}) >"
	# representation.
	def __repr__(self):
		return str(self)

		#

	#
	
#