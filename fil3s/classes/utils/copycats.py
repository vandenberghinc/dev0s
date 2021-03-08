#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from fil3s.classes.config import *

# the syst3m.console.* functions (exact copy).
def argument_present(arguments, default=False, count=1):
	if isinstance(arguments, str):
		c = sys.argv.count(arguments)
		if c > 0 and count <= c:
			return True
		else: return default
	elif isinstance(arguments, list):
		for argument in arguments:
			c = sys.argv.count(argument)
			if c > 0 and count <= c:
				return True
		return default
	else: raise ValueError("Invalid usage, arguments must either be a list or string.")
def arguments_present(arguments, default=False, count=1):
	if isinstance(arguments, str): return argument_present(arguments, default=default, count=count)
	else:
		for argument in arguments:
			if argument_present(argument, default=default, count=count):
				return True
		return default
def get_argument(argument, required=True, index=1, count=1, default=None, ):
	if default != None and required: required = False
	
	# set error msg.
	if index == 1:
		empty_error = f"Define argument [{argument}]."
	else:
		empty_error = f"Define argument [{argument}] (index: {index})."

	# check presence.
	if argument not in sys.argv:
		if required:
			raise EmptyArgumentError(empty_error)
		else: return default

	# retrieve.
	y, c = 0, 0
	for x in sys.argv:
		try:
			if x == argument: 
				c += 1
				if count == c:
					return sys.argv[y+index]
		except IndexError:
			if required:
				raise EmptyArgumentError(empty_error)
			else: return default
		y += 1

	# should not happen.
	if required:
		raise EmptyArgumentError(empty_error)
	else: return default

	#

# the syst3m.console.Loader object class (exact copy).
class Loader(threading.Thread):
	def __init__(self, message, autostart=True, log_level=0, interactive=True):
		threading.Thread.__init__(self)
		self.message = self.__clean_message__(message)
		self.last_message = str(self.message)
		self.log_level = log_level
		self.interactive = interactive
		if autostart and self.log_level >= 0: 
			if self.interactive:
				try:
					self.start()
				except KeyboardInterrupt as e:
					self.stop(success=False)
					raise KeyboardInterrupt(f"{e}")
			else:
				print(self.message+".")
	def run(self):
		if self.log_level >= 0: 
			self.running = True
			self.released = True
			while self.running:
				if not self.released:
					time.sleep(1)
				else:
					for i in ["|", "/", "-", "\\"]:
						if not self.released: break
						if self.message != self.last_message:
							print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
							self.message = self.__clean_message__(self.message)
						print(f"{self.message} ... {i}", end="\r")
						self.last_message = self.message
						if not self.running: break
						time.sleep(0.33)
		self.running = "stopped"
	def stop(self, message=None, success=True, response=None, quiet=False):
		if self.log_level >= 0:
			if response == None:
				if message == None: message = self.message
			else:
				if response["error"] == None:
					message = response["message"]
				else:
					success = False
					message = "Error: "+response["error"]
			if self.interactive:
				self.running = False
				for i in range(120):
					if self.running == "stopped": break
					time.sleep(0.5)
				if self.running != "stopped": raise ValueError(f"Unable to stop loader [{self.message}].")
			if not quiet:
				if self.interactive:
					print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
					if success:
						print(f"{message} ... done")
					else:
						print(f"{message} ... {color.red}failed{color.end}")
				else:
					if success:
						print(f"{message}. done")
					else:
						print(f"{message}. {color.red}failed{color.end}")
	def mark(self, new_message=None, old_message=None, success=True, response=None):
		if self.log_level >= 0: 
			if response != None:
				if response["error"] == None:
					success = True
				else:
					success = False
			if old_message == None: old_message = self.message
			if self.interactive:
				print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
				if success:
					print(f"{old_message} ... done")
				else:
					print(f"{old_message} ... {color.red}failed{color.end}")
			else:
				if success:
					print(f"{old_message}. done")
				else:
					print(f"{old_message}. {color.red}failed{color.end}")
			if new_message != None: self.message = new_message
	def hold(self):
		if self.log_level >= 0: 
			self.released = False
			time.sleep(0.33)
	def release(self):
		if self.log_level >= 0: 
			self.released = True
			time.sleep(0.33)
	# system functions.
	def __clean_message__(self, message):
		if message[-len(" ..."):] == " ...": message = message[:-4]
		if message[-len("."):] == ".": message = message[:-1]
		if message[0].upper() != message[0]: message = message[1:]+message[0].upper()+message[1:]
		return color.fill(message)
	def __empty_message__(self, length=len("hello world")):
		s = ""
		for i in range(length): s += " "
		return s

# the Environment.Env object class (exact copy).
class Env(object):
	def __init__(self):
		a=1
		#
	# fill with variables.
	def fill(self, string):
		c = 0
		for i in range(string.count("$")):
			c += 1
			if string[0] == "$" and c == 1:
				variable_id, _ = String(string.split("$")[1]).before_after_first_occurence(slicer=["/","+",">","<","?",";",":","|","\\","]","[","{","}","=","+","(",")","!","@","#","$","%","^","&","*","±","~","`","'",'"'," "], include_after=True)
			else:
				variable_id, _ = String(string.split("$")[c]).before_after_first_occurence(slicer=["/","+",">","<","?",";",":","|","\\","]","[","{","}","=","+","(",")","!","@","#","$","%","^","&","*","±","~","`","'",'"'," "], include_after=True)
			for i in ["/","+",">","<","?",";",":","|","\\","]","[","{","}","=","+","(",")","!","@","#","$","%","^","&","*","±","~","`","'",'"'," "]:
				variable_id = variable_id.replace(i, "")
			variable = os.environ.get(variable_id)
			if variable == None: raise ValueError(f"Required environment variable {variable_id} is undefined.")
			string = string.replace(f"${variable_id}", variable)
		string = string.replace("~",HOME)
		return string
	# import env.
	def import_(self, env=None):
		if env == None: return Response.error("Define parameter: env.")
		dictionary = {}
		if isinstance(env, (str, String, FilePath)):
			env = str(env)
			if ".json" in env or env == "json":
				try:
					dictionary = Files.load(env, format="json")
				except FileNotFoundError:
					dictionary = {}
			elif ".sh" in env or env == "bash":
				return Response.error("Coming soon")
		elif isinstance(env, (dict, Dictionary)):
			dictionary = env
		else: return Response.error(f"Invalid usage, env requires to be a [str, String, FilePath, dict, Dictionary], not [{env.__class__.__name__}].")
		for key,value in dictionary.items():
			os.environ[str(key)] = str(value)
		return Response.success(f"Successfully imported {len(dictionary)} env variables.")
		#
	# export env.
	def export(self, env=None, export=None):
		if env == None: return Response.error("Define parameter: env.")
		dictionary = {}
		if isinstance(env, (dict, Dictionary)):
			dictionary = env
		else: return Response.error(f"Invalid usage, env requires to be a [str, String, FilePath, dict, Dictionary], not [{env.__class__.__name__}].")
		for key,value in dictionary.items():
			os.environ[str(key)] = str(value)
		if export != None:
			try:
				exported = Files.load(export, format="json")
			except FileNotFoundError:
				exported = {}
			for key,value in dictionary.items():
				exported[str(key)] = value
			Files.save(export, exported, format="json")
		return Response.success(f"Successfully exported {len(dictionary)} env variables.")
		#
	# get.
	def get(self, id, default=None, format="str"):
		if format in [str, "str", "string"]:
			return self.get_string(id, default=default)
		elif format in [bool, "bool", "boolean"]:
			return self.get_boolean(id, default=default)
		elif format in [int, float, "int", "float", "integer", "double"]:
			return self.get_integer(id, default=default)
		elif list in [list, "list", "array"]:
			return self.get_array(id, default=default)
		elif dict in [dict, "dict", "dictionary", "json"]:
			return self.get_dictionary(id, default=default)
		else: raise ValueError(f"Unkown format: {format}.")
	def get_string(self, id, default=None):
		e = os.environ.get(id)
		if e == None: 
			return default
		else:
			return e
	def get_boolean(self, id, default=None):
		e = os.environ.get(id)
		if e == None: 
			return default
		elif e in [True, "True", "true", "TRUE"]:
			return True
		else: 
			return False
	def get_integer(self, id, default=None):
		e = os.environ.get(id)
		try:
			if "." in str(e):
				return float(e)
			else:
				return int(e)
		except:
			return default
	def get_array(self, id, default=None):
		e = os.environ.get(id)
		if e == None: 
			return default
		else: 
			a = []
			for i in e.split(","):
				a.append(self.__remove_whitespace__(i))
			return a
	def get_tuple(self, id, default=None):
		e = os.environ.get(id)
		if e == None: 
			return default
		else: 
			a = []
			for i in e.split(","):
				a.append(self.__remove_whitespace__(i))
			return tuple(a)
	def get_dictionary(self, id, default=None):
		e = os.environ.get(id)
		if e == None: 
			return default
		else: 
			a = []
			for i in e.split(","):
				a.append(self.__remove_whitespace__(i))
			d = {}
			for i in a:
				try:
					key,value = i.split(":")
					d[self.__remove_whitespace__(key)] = self.__remove_whitespace__(value)
				except: a=1
			return tuple(a)
	# set.
	def set(self, id, value, format="unknown"):
		if format == "unknown": format = Formats.get(value, serialize=True)
		if format in [str, "str", "string"]:
			self.set_string(id, value)
		elif format in [bool, "bool", "boolean"]:
			self.set_boolean(id, value)
		elif format in [int, float, "int", "float", "integer", "double"]:
			self.set_integer(id, value)
		elif list in [list, "list", "array"]:
			self.set_array(id, value)
		elif dict in [dict, "dict", "dictionary", "json"]:
			self.set_dictionary(id, value)
		else: raise ValueError(f"Unkown format: {format}.")
	def set_string(self, id, value):
		os.environ[id] = value
	def set_boolean(self, id, value):
		if e in [True, "True", "true", "TRUE"]:
			os.environ[id] = "true"
		else: 
			os.environ[id] = "false"
	def set_integer(self, id, value):
		os.environ[id] = str(value)
	def set_array(self, id, value):
		os.environ[id] = Array(value).string(joiner=",")
	def set_tuple(self, id, value):
		os.environ[id] = Array(value).string(joiner=",")
	def set_dictionary(self, id, value, subkey=""):
		for key, value in value.items():
			if subkey == "": lkey = key
			else: lkey = f"{subkey}_{key}"
			if isinstance(value, dict):
				self.set_dictionary(key, value, subkey=lkey)
			else: 
				self.set(lkey, value, format="unknown")
	# system functions.
	def __remove_whitespace__(self, string):
		if isinstance(string, str):
			for attempts in range(101):
				if string[0] == " ":
					string = string[1:]
				elif string[len(string)-1] == " ":
					string = string[:-1]
				else: break
		return string

# initialized classes.
env = Env()