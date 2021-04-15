#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.defaults.exceptions import *
from dev0s.classes import utils
from dev0s.classes.response import response as _response_
import datetime 

# argument functions.
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
			raise Exceptions.EmptyArgumentError(empty_error)
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
				raise Exceptions.EmptyArgumentError(empty_error)
			else: return default
		y += 1

	# should not happen.
	if required:
		raise Exceptions.EmptyArgumentError(empty_error)
	else: return default

	#

# system functions.
def __str_representable__(dict):
	str = json.dumps(dict, indent=4, ensure_ascii=False)[:-2][2:].replace('    "', '    ').replace('": "', " : ")
	s, c, max = "", 0, len(str.split('\n'))
	for i in str.split('\n'):
		if i not in ["", " "]:
			if c < max-1:
				s += i[:-2]+"\n"
			else:
				s += i[:-1]+"\n"
		c += 1
	return s[:-1].replace(": : \n"," :\n").replace(" : \n",":\n")

# a default cli object
class CLI(object):
	def __init__(self, 
		# the alias (str).
		alias=None, 
		# the modes (dict).
		modes={}, 
		# the options (dict).
		options={}, 
		# the documentation notes (dict).
		notes={}, 
		# the path to the executable (str, FilePath).
		executable=__file__, 
		# the author's name (str).
		author="Daan van den Bergh",
	):

		# docs.
		DOCS = {
			"module":"dev0s.cli.CLI", 
			"initialized":False,
			"description":[], 
			"chapter": "CLI", }

		# arguments.
		self.alias = alias
		self.modes = modes
		self.options = options
		self.notes = notes
		self.author = author
		self.executable = str(executable)
		self.arguments = self.Arguments(attributes={
			"executable":self.executable, 
			"docs":self.docs, 
			"stop":self.stop,
		})
		self.arguments.documentation = self.documentation = self.__create_docs__()
		self.options = self.Options(attributes={
			"arguments":self.arguments,
		})

		#

	# stop.
	def stop(self,
		# success exit (bool).
		success=True,
		# optional order 1 success message (overwrites success to response.success) (ResponseObject, OutputObject, dict).
		response={},
		# optional order 2 success message (overwrites success to True) (str).
		message=None,
		# optional order 3 message (str).
		error=None,
		# json format (bool).
		json=False,
	):
		if response != {}:
			if response["success"] in [True, "True", "true", "TRUE"]:
				success = True
				message = response["message"]
			else:
				success = False
				error = response["error"]
		if message != None: 
			success = True
			_response_.log(message=message, json=json)
		elif error != None: 
			success = False
			_response_.log(error=error, json=json)
		if success: sys.exit(0)
		else: sys.exit(1)

	# show docs.
	def docs(self, 
		# the chapter (optional) (str).
		chapter=None,
		# the mode (optional) (str).
		mode=None,
		# success exit.
		success=True,
		# optional order 1 success message (overwrites success to response.success) (ResponseObject, OutputObject).
		response={},
		# optional order 2 success message (overwrites success to True) (str).
		message=None,
		# optional order 3 message (str).
		error=None,
		# dump response as json format (bool).
		json=False,
		# stop after show  (bool).
		stop=True,
		# overwrite default notes (optional)  (dict).
		notes=None,
	):
		"""
		if not json:
			docs = self.documentation
			if chapter != None:
				s = self.documentation.split("\nModes:\n")
				before = s[0]+"\nModes:\n"
				s = s[1].split("\nAuthor:")
				after = "\nAuthor:"+s[1]
				new, include, indent, indent_str = "", False, 0, ""
				for line in s[0].split("\n"):
					if f" {chapter.lower()}: " in line.lower():
						indent = len(line.split(f"{mode}:")[0])
						indent_str = ""
						for _ in range(indent): indent_str += " "
						include = True
					elif include:
						s = ""
						for i in line:
							if i != " ": break
							s += i
						if s == indent_str and ":" in line:
							l = line[indent:].split(":")[0]
							if not(len(l) > 0 and len[0] == "-"):
								include = False
					if include: new += line+"\n"
				if mode != None and (f" {mode}: " in new or f" {mode} " in new):
					id = String(line).first_occurence(charset=[f" {mode} ", f" {mode}: "])
					s = new.split(id)
					before = s[0]+id
					_new_, include, indent = "", False, None
					for line in new.split("\n"):
						if id in new:
							indent = len(line.split(id)[0])
							include = True
						elif indent != None and ":" in line:
							l = line[indent:].split(":")[0]
							if " " not in l and len(l) > 0 and l[0] == "-":
								include = False
						if include: _new_ += line+"\n"
					docs = before + _new_ + after
				else:
					docs = before + new + after
			if mode != None and (f" {mode}: " in new or f" {mode} " in new):
				id = String(line).first_occurence(charset=[f" {mode} ", f" {mode}: "])
				s = docs.split(id)
				before = s[0]+id
				_new_, include, indent = "", False, None
				for line in docs.split("\n"):
					if id in docs:
						indent = len(line.split(id)[0])
						include = True
					elif indent != None and ":" in line:
						l = line[indent:].split(":")[0]
						if " " not in l and len(l) > 0 and l[0] == "-":
							include = False
					if include: _new_ += line+"\n"
				docs = before + _new_ + after
			print(docs)
		"""
		
		# default notes.
		if notes == None: notes = self.notes

		# json mode.
		if not json:

			# create modes & options.
			modes, options, chapters, iterating_chapter, iterating_mode, previous_mode_indent = {}, {}, [], None, None, None
			for key, value in self.modes.items():
				
				# set iterating chapter.
				if (chapter != None or mode != None) and value.lower() == "*chapter*":
					c = 0
					for i in key:
						if i != " ": break
						c += 1
					sliced_key = key[c:]
					if sliced_key[len(sliced_key)-1] == ":": sliced_key = sliced_key[:-1]
					chapters.append(sliced_key)
					iterating_chapter = sliced_key
					previous_mode_indent = None
					value = ""
				
				# set iterating mode.
				if mode != None and (mode in key or (previous_mode_indent != None and len(key) >= len(f"{String().indent(indent=previous_mode_indent)}-") and key[:len(f"{String().indent(indent=previous_mode_indent)}-")] == f"{String().indent(indent=previous_mode_indent)}-") ):
					mode_indent = 0
					for i in key:
						if i != " ": break
						mode_indent += 1
					# previous mode indent needs to be resetted when to None when the mode lines are finished.
					if previous_mode_indent == None or mode_indent == previous_mode_indent:
						sliced_key = key[mode_indent:]
						if " / " in sliced_key:
							set, new = True, []
							for i in sliced_key.split(" / "):
								# only proceed with modes without an example value.
								# aka when there is not a space
								if " " in i:
									set = False
									break
								new.append(i)
							if set: sliced_key = list(new)
						if isinstance(sliced_key, str) and " " in sliced_key:
							sliced_key = sliced_key.split(" ")[0]
						local_modematch = False
						if iterating_mode != None:
							if isinstance(iterating_mode, str):
								local_modematch = iterating_mode == mode or f"{mode} " in iterating_mode
							elif isinstance(iterating_mode, str):
								for i in iterating_mode:
									if iterating_mode == mode or f"{mode} " in iterating_mode:
										local_modematch = True
										break
						if iterating_mode == None or local_modematch:
							previous_mode_indent = mode_indent
							iterating_mode = sliced_key


				# set mode match.
				modematch = False
				if isinstance(iterating_mode, str):
					modematch = iterating_mode == mode or f"{mode} " in iterating_mode
				elif isinstance(iterating_mode, str):
					for i in iterating_mode:
						if iterating_mode == mode or f"{mode} " in iterating_mode:
							modematch = True
							break

				# add to modes.
				if mode != None and chapter != None:
					if modematch and chapter.lower() == iterating_chapter.lower():
						modes[key] = value
				elif chapter != None:
					if chapter.lower() == iterating_chapter.lower():
						modes[key] = value
				elif mode != None:
					if modematch:
						modes[key] = value
				else:
					modes[key] = value

			# print docs.
			docs = self.__create_docs__(modes=modes, options=options, notes=notes)
			print(docs)

		# stop.
		if stop:
			self.stop(
				success=success, 
				response=response, 
				message=message, 
				error=error, 
				json=json)

	# selected an invalid mode.
	def invalid(self, 
		# the selected error (str).
		error="Selected an invalid mode.", 
		# the selected chapter (str).
		chapter=None, 
		# the active mode (str).
		mode=None, 
		# dump response as json format (bool).
		json=False,
	):
		if not json:
			self.docs(
				chapter=chapter,
				mode=mode, 
				stop=False,)
		self.stop(error=error, json=json)
		#
	
	# system functions.
	def __create_docs__(self, modes=None, options=None, notes=None):
		if modes == None: modes = self.modes
		if options == None: options = self.options
		if notes == None: notes = self.notes
		self.modes_str  = self.arguments.modes_str = m = __str_representable__(modes)
		self.options_str = self.arguments.options_str = o = __str_representable__(options)
		n = __str_representable__(notes)
		c = f"\nAuthor: {self.author}. \nCopyright: © {self.author} 2020 - {datetime.datetime.today().strftime('%Y')}. All rights reserved."
		doc = "Usage: "+self.alias+" <mode> <options> "
		if m != "": doc += "\nModes:\n"+m
		if o != "": doc += "\nOptions:\n"+o
		if n != "": doc += "\nNotes:\n"+n
		doc += c
		return doc.replace(": : *chapter*", ":").replace("*chapter*", "")
	def __str_representable__(self, dict, start_indent=4):
		str = json.dumps(dict, indent=4, ensure_ascii=False)[:-2][2:].replace('    "', '    ').replace('": "', " : ").replace('": ', " : ")
		s, c, max = "", 0, len(str.split('\n'))
		for i in str.split('\n'):
			if i not in ["", " "]:
				#if c < max-1:
				#if (len(i) >= len('",\n') and i[:len('",\n')] == '",\n') or (len(i) >= len(',\n') and i[:len(',\n')] == ',\n') or (len(i) >= len('"\n') and i[:len(',\n')] == '"\n'):
				#	s += i[:-2]+"\n"
				#else:
				if len(i) > 0 and i[len(i)-1] == ',': i = i[:-1]
				if len(i) > 0 and i[len(i)-1] == '\n': i = i[:-1]
				if len(i) > 0 and i[len(i)-1] == '"': i = i[:-1]
				s += i+"\n"
			c += 1
		if len(s) > 0 and s[len(s)-1] == "\n": s = s[:-1]
		if len(s) > 0 and s[len(s)-1] == "}": s = s[:-1]
		if len(s) > 0 and s[0] == "\n": s = s[1:]
		if len(s) > 0 and s[0] == "{": s = s[1:]
		string = s.replace(": : \n"," :\n").replace(" : \n",":\n")
		if start_indent != 4:
			newstring, lindent = "", None
			for i in string.split("\n"):
				newstring += i[4:]+"\n"
			string = newstring
		while True:
			if len(string) > 0 and string[len(string)-1] == "\n": string = string[:-1]
			else: break
		return string.replace(" : {", " :").replace(" :\n", ":\n").replace(" : ", ": ")

	# the arguments object class.
	class Arguments(object):
		def __init__(self, attributes={}):

			#
			self.assign(attributes)

			#
		def iterate(self):
			return sys.argv
		def present(self, argument, default=False, count=1):
			if isinstance(argument, str):
				return argument_present(argument, default=False, count=count)
			else:
				return arguments_present(argument, default=False, count=count)
		def get(self, 
			# the argument id (str) (example: --path).
			argument, 
			# whether the argument is required or not (bool).
			required=True, 
			# the plus index (int).
			index=1, 
			# the argument id count index (int).
			count=1, 
			# the value format (str, list) (example: formats=[str].
			format="*",
			# pack multiple into tuple (bool).
			pack=True, 
			# default value when empty (bool, int, float, str, dict, list).
			default=None, 
			# docs chapter (str).
			chapter=None, 
			# docs mode (str).
			mode=None, 
			# json mode (bool).
			json=False,
			# overwrite default notes (dict).
			notes=None,
		):

			# check & clean format.
			def clean_string(string="", remove_first_space=False, remove_last_space=False):
				while True:
					if string in [str, bool, int, float, dict, list, object, tuple]: break
					elif remove_first_space and len(string) > 0 and string[0] == " ": string = string[1:]
					elif remove_last_space and len(string) > 0 and string[len(string)-1] == " ": string = string[:-1]
					else: break
				return string
			def clean_array(array=["x", "y"] or "x,y", remove_first_space=False, remove_last_space=False):
				if isinstance(array, str): 
					array = array.split(",")
				new = []
				for i in array: new.append(clean_string(i, remove_first_space=remove_first_space, remove_last_space=remove_last_space))
				return new
			def clean_dict(dictionary={} or "x:0,y:1"):
				if isinstance(dictionary, str): dictionary = clean_array(dict.split(","), remove_first_space=True, remove_last_space=True)
				if isinstance(dictionary, list):
					new = {}
					for key in dictionary:
						new[clean_string(key, remove_first_space=remove_first_space, remove_last_space=remove_last_space)] = clean_string(value, remove_first_space=remove_first_space, remove_last_space=remove_last_space)
					return new
				elif isinstance(dictionary, dict):
					new = {}
					for key,value in dictionary.items():
						new[clean_string(key, remove_first_space=remove_first_space, remove_last_space=remove_last_space)] = clean_string(value, remove_first_space=remove_first_space, remove_last_space=remove_last_space)
					return new
			if not isinstance(format, list):
				if format not in [str, bool, int, float, dict, list, object, tuple]:
					try:
						format = format.split(",")
					except: 
						format = [format]
				else:
					format = [format]
			if "*" not in format:
				l = []
				for i in clean_array(format, remove_first_space=True, remove_last_space=True):
					if i not in [
						str, "str", "string",
						bool, "bool", "boolean",
						int, "int", "integer",
						float, "float", "double",
						dict, "dict", "json", "dictionary",
						list, "list", "array",
						object, "object", "obj",
						tuple, "tuple",
					]:
						format_error = f"""Specified an invalid format type [{i}], valid formats: {str([str, bool, int, float, tuple, dict, list, object]).replace("'",'')}."""
						if json:
							_response_.log(error=empty_error, json=True)
							sys.exit(1)
						else:
							self.docs(stop=False, chapter=chapter, mode=mode, notes=notes)
							sys.tracebacklimit = -1 ; sys.traceback_limit = -1
							raise Exceptions.InvalidFormatError(invalid_format_error)

					if i in [str, "str", "string"]: i = str
					if i in [bool, "bool", "boolean"]: i = int
					if i in [int, "int", "integer"]: i = int
					if i in [float, "float", "double"]: i = float
					if i in [dict, "dict", "json", "dictionary"]: i = dict
					if i in [list, "list", "array"]: i = list
					if i in [object, "object", "obj"]: i = object
					if i in [tuple, "tuple"]: i = tuple
					l.append(i)
				format = l

			# handle string.
			if isinstance(argument, str):
				
				# set error msg.
				if index == 1:
					empty_error = f"Define argument [{argument}]."
				else:
					empty_error = f"Define argument [{argument}] (index: {index})."

				# check presence.
				if argument not in sys.argv:
					if required:
						if json:
							_response_.log(error=empty_error, json=True)
							sys.exit(1)
						else:
							self.docs(stop=False, chapter=chapter, mode=mode, notes=notes)
							sys.tracebacklimit = -1 ; sys.traceback_limit = -1
							raise Exceptions.EmptyArgumentError(empty_error)
					else: return default

				# retrieve.
				y, c = 0, 0
				for x in sys.argv:
					# get value.
					failed = False
					try:
						if x == argument: 
							c += 1
							if c == count:
								value = sys.argv[y+index]
								# check format.
								if "*" not in format:
									x_format = Formats.get(value, serialize=False)
									error = False
									if x_format == str and int in format:
										try:
											value = int(value)
										except: error = True
									if x_format == str and bool in format:
										try:
											if value in ["true", True, "True", "TRUE"]:
												value = True
											else: 
												value = False
										except: error = True
									if x_format == str and float in format:
										try:
											value = float(value)
										except: error = True
									if x_format == str and list in format:
										try:
											value = clean_array(value, remove_first_space=True, remove_last_space=True)
										except: error = True
									if x_format == str and dict in format:
										try:
											value = clean_dict(value, remove_first_space=True, remove_last_space=True)
										except: error = True
									x_format = Formats.get(value, serialize=False)
									if error or x_format not in format:
										format_error = f"""Provided an incorrect [{argument}] format: [{value}:{x_format}], valid format options: {str(format).replace("'",'')}."""
										if json:
											_response_.log(error=format_error, json=True)
											sys.exit(1)
										else:
											self.docs(stop=False, chapter=chapter, mode=mode, notes=notes)
											sys.tracebacklimit = -1 ; sys.traceback_limit = -1
											raise Exceptions.ArgumentFormatError(format_error)
								return value
					except IndexError: failed = True
					# not present.
					if failed:
						if required:
							if json:
								_response_.log(error=empty_error, json=True)
								sys.exit(1)
							else:
								self.docs(stop=False, chapter=chapter, mode=mode, notes=notes)
								sys.tracebacklimit = -1 ; sys.traceback_limit = -1
								raise Exceptions.EmptyArgumentError(empty_error)
						else: return default
					y += 1

				# should not happen.
				if required:
					if json:
						_response_.log(error=empty_error, json=True)
						sys.exit(1)
					else:
						self.docs(stop=False, chapter=chapter, mode=mode, notes=notes)
						sys.tracebacklimit = -1 ; sys.traceback_limit = -1
						raise Exceptions.EmptyArgumentError(empty_error)
				else: return default

			else:
				if pack:
					arguments = []
					for i in argument: 
						arguments.append(self.get(i, required=required, index=index,default=default, mode=mode, chapter=chapter, notes=notes, json=json, count=count))
					return arguments	
				else:
					for i in argument: 
						a = self.get(i, required=required, index=index,default=default, mode=mode, chapter=chapter, notes=notes, json=json, count=count)
						if a != default: return a
					return default
		def check(self, 
			# the passed args to except (list).
			exceptions=[], 
			# json mode (bool).
			json=False,
		):
			exceptions += ["--log-level", "--create-alias", "-v", "--version", "-j", "--json", "--non-interactive"]
			lexecutable = self.executable
			while True:
				if len(lexecutable) > 0 and lexecutable[len(lexecutable)-1] == "/": lexecutable = lexecutable[:-1]
				elif "//" in lexecutable: lexecutable = lexecutable.replace("//","/")
				else: break
			for i in sys.argv:
				if i not in ["", lexecutable] and not Files.exists(i) and (len(i) < 1 or (i[0] == "-")):
					try:
						int(i)
						integer = True
					except: integer = False
					if not integer:
						if i not in exceptions and f" {i}: " not in self.modes_str and f" {i}: " not in self.options_str and f" {i} " not in self.modes_str and f" {i} " not in self.options_str:
							error = f"Argument [{i}] is not a valid mode nor option."
							if json:
								_response_.log(error=error, json=True)
								sys.exit(1)
							else: 
								self.docs(stop=False)
								sys.tracebacklimit = -1 ; sys.traceback_limit = -1
								raise Exceptions.UnknownArgumentError(error)
		# defaults.
		def items(self):
			return vars(self).items()
		def keys(self):
			return list(vars(self).keys())
		def values(self):
			return list(vars(self).values())
		def dict(self, 
			# serialize to json (bool).
			serializable=False,
		):
			dictionary = {}
			for key, value in self.items():
				if serializable:
					if isinstance(value, object):
						value = str(value)
					elif value == "True": value = True
					elif value == "False": value = False
					elif value == "None": value = None
				dictionary[key] = value
			return dictionary
		# assign self variables by dictionary.
		def assign(self, dictionary):
			if not isinstance(dictionary, dict):
				raise TypeError("You can only self assign with a dictionary as parameter.")
			for key,value in dictionary.items():
				if value in ["False", "false"]: value = False
				elif value in ["True", "true"]: value = True
				elif value in ["None", "none", "null", "nan"]: value = None
				else:
					if isinstance(value, str):
						if "." in str(value):
							try: value = float(value)
							except: a=1
						else:
							try: value = int(value)
							except: a=1
				self[key] = value
		# unpack keys as tuple.
		def unpack(self, 
			# the variable keys (#1 parameter) (list).
			keys=[],
		):
			list = []
			for key in keys:
				list.append(self[key])
			return list
		# count items.
		def __len__(self):
			return len(self.keys())
		# support item assignment.
		def __setitem__(self, key, value):
			setattr(self, key, value)
		def __getitem__(self, key):
			return getattr(self, key)
		def __delitem__(self, key):
			delattr(self, key)
		# string format.
		def __str__(self):
			return json.dumps(self.dict(serializable=True), indent=4) # necessary for str(self)
			return self.dict(serializable=True) # seems to work for django.
			if isinstance(self, dict):
				return json.dumps(self, indent=4)
			else:
				return json.dumps(self.dict(), indent=4)

	# the options object class.
	class Options(object):
		def __init__(self, attributes={}):
			self.assign(attributes)
		# iterate over self keys & variables.
		def items(self):
			return vars(self).items()
		def keys(self):
			return list(vars(self).keys())
		def values(self):
			return list(vars(self).values())
		def dict(self, 
			# serialize to json (bool).
			serializable=False,
		):
			dictionary = {}
			for key, value in self.items():
				if serializable:
					if isinstance(value, object):
						value = str(value)
					elif value == "True": value = True
					elif value == "False": value = False
					elif value == "None": value = None
				dictionary[key] = value
			return dictionary
		# assign self variables by dictionary.
		def assign(self, dictionary):
			if not isinstance(dictionary, dict):
				raise TypeError("You can only self assign with a dictionary as parameter.")
			for key,value in dictionary.items():
				if value in ["False", "false"]: value = False
				elif value in ["True", "true"]: value = True
				elif value in ["None", "none", "null", "nan"]: value = None
				else:
					if isinstance(value, str):
						if "." in str(value):
							try: value = float(value)
							except: a=1
						else:
							try: value = int(value)
							except: a=1
				self[key] = value
		# unpack keys as tuple.
		def unpack(self, 
			# the variable keys (#1 parameter) (list).
			keys=[],
		):
			list = []
			for key in keys:
				list.append(self[key])
			return list
		# clean default values.
		def clean(self):
			for i in ["error", "message", "success"]:
				del self[i]
				#except: a=1
			return self
		# count items.
		def __len__(self):
			return len(self.keys())
		# support item assignment.
		def __setitem__(self, key, value):
			setattr(self, key, value)
		def __getitem__(self, key):
			return getattr(self, key)
		def __delitem__(self, key):
			delattr(self, key)
		# string format.
		def __str__(self):
			return json.dumps(self.dict(serializable=True), indent=4) # necessary for str(self)
			return self.dict(serializable=True) # seems to work for django.
			if isinstance(self, dict):
				return json.dumps(self, indent=4)
			else:
				return json.dumps(self.dict(), indent=4)
		def json(self,):
			return json.dumps(self.dict(serializable=True), indent=4)
			return self.dict(serializable=True) # seems to work for django.
			return self.dict(serializable=True)
			return json.dumps(self.dict(serializable=True), indent=4)
			return json.dumps(self)
			return json.dumps(self, default=lambda o: o.__dict__)

	#

#

#