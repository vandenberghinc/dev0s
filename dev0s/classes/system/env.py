#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.exceptions import Exceptions
from dev0s.classes.defaults.color import color, symbol
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_

# the env object class.
class Env(object):
	def __init__(self):
		
		# docs.
		DOCS = {
			"module":"dev0s.system.env", 
			"initialized":True,
			"description":[], 
			"chapter": "System", }

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
		if env == None: return _response_.error("Define parameter: env.")
		dictionary = {}
		if isinstance(env, (str, String, FilePath)):
			env = str(env)
			if ".json" in env or env == "json":
				try:
					dictionary = Files.load(env, format="json")
				except FileNotFoundError:
					dictionary = {}
			elif ".sh" in env or env == "bash":
				return _response_.error("Coming soon")
		elif isinstance(env, (dict, Dictionary)):
			dictionary = env
		else: return _response_.error(f"Invalid usage, env requires to be a [str, String, FilePath, dict, Dictionary], not [{env.__class__.__name__}].")
		for key,value in dictionary.items():
			os.environ[str(key)] = str(value)
		return _response_.success(f"Successfully imported {len(dictionary)} env variables.")
		#
	
	# export env.
	def export(self, 
		# the environment to export (dict).
		env=None, 
		# the export path (str) or paths (list).
		# the paths must have .json / .sh extension or be named 'json' / 'bash' when parameter [format] is undefined.
		export=None,
		# the export format (str) (leave None to be detected by parameter [export]).
		format=None,
	):
		if env == None: return _response_.error("Define parameter: env.")
		dictionary = {}
		if isinstance(env, (dict, Dictionary)):
			dictionary = env
		else: return _response_.error(f"Invalid usage, env requires to be a [str, String, FilePath, dict, Dictionary], not [{env.__class__.__name__}].")
		for key,value in dictionary.items():
			os.environ[str(key)] = str(value)
		if export != None:
			if isinstance(export, (str,String,FilePath)):
				exports = [str(export)]
			elif not isinstance(export, (list, Array)):
				raise Exceptions.InvalidUsage(f"<dev0s.system.env>: Parameter export requires to be a [str, list, FilePath], not [{export.__class__.__name__}].")
			else:
				exports = export
			c = 0
			for export in exports:
				if isinstance(format, (list, Array)):
					try:
						l_format = format[c]
					except:
						raise Exceptions.InvalidUsage(f"<dev0s.system.env>: Parameter format [list] does not contain index [{c}] for export [{export}].")
				else:
					l_format = format
				if l_format == "json" or ".json" in export or gfp.name(export) == "json":
					format = "json"
					try:
						exported = Files.load(export, format="json")
					except FileNotFoundError:
						exported = {}
				elif l_format == "bash" or ".sh" in export or gfp.name(export) == "bash":
					format = "bash"
					try:
						exported = Files.load(export, format="str")
					except FileNotFoundError:
						exported = ""
					while True:
						if "\n\n" in exported: exported = exported.replace("\n\n","\n")
						elif len(exported) > 0 and String(exported).last("\n") == "\n": exported = str(String(exported).remove_last("\n"))
						else: break
				else:
					raise Exceptions.InvalidUsage(f"Export file [{export}] must contain an .json / .sh extension or must be named 'bash' / 'json'.")
				for key,value in dictionary.items():
					if format == "json":
						exported[str(key)] = value
					elif format == "bash":
						if f'export {key.upper()}="' in exported:
							l = ""
							for line in exported.split("\n"):
								if f'export {key.upper()}="' in line:
									l += f'export {key.upper()}="{value}"\n'
								else:
									l += line+"\n"
							exported = l
						else:
							exported += '\n'+f'export {key.upper()}="{value}"\n'
				if format == "json":
					Files.save(export, exported, format="json")
				elif format == "bash":
					while True:
						if "\n\n" in exported: exported = exported.replace("\n\n","\n")
						elif len(exported) > 0 and String(exported).last("\n") == "\n": exported = str(String(exported).remove_last("\n"))
						else: break
					Files.save(export, exported, format="str")
				c += 1
		return _response_.success(f"Successfully exported {len(dictionary)} env variables.")
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
		else: raise ValueError(f"Unknown format: {format}.")
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
		else: raise ValueError(f"Unknown format: {format}.")
	def set_string(self, id, value):
		os.environ[id] = value
	def set_boolean(self, id, value):
		e = os.environ.get(id)
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

	# support item assignment.
	def __getitem__(self, key):
		value = self.get(id)
		if value in ["None", "none"]: value = None
		elif value in ["True", "true", "TRUE"]: value = True
		elif value in ["False", "false", "FALSE"]: value = False
		else:
			if "." in str(key):
				try: value = float(value)
				except: a=1
			else:
				try: value = int(value)
				except: a=1
		return value
	def __setitem__(self, key, value):
		self.set(key, str(value), format="str")
	def __delitem__(self, key):
		self.set(key, "")

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

	#
	
# initialized classes.
env = Env()
