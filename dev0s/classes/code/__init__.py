#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.exceptions import Exceptions
from dev0s.classes import utils
from dev0s.classes import console
from dev0s.classes.defaults.files import *
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_

# include "execute" functions & classes.
from dev0s.classes.code.execute import processes, kill, execute, Spawn, OutputObject

# askpass still to create.
def askpass():
	if defaults.vars.os in ["linux"]:
		askpass = f"""echo '#!/bin/bash' > /tmp/askpass.sh && echo 'zenity --password --title="{ALIAS} requires root permissions."' >> /tmp/askpass.sh && export SUDO_ASKPASS="/tmp/askpass.sh" """
		output = dev0s.utils.__execute_script__(f"cd ~ && rm -fr /tmp/{ALIAS}/ && git clone -q https://github.com/vandenberghinc/{ALIAS} /tmp/{ALIAS}/ && chmod +x /tmp/{ALIAS}/requirements/installation.sh && {askpass} && sudo -A -u {user} bash /tmp/{ALIAS}/requirements/installation.sh")
	else:
		askpass = f"""/usr/bin/osascript -e 'do shell script "/tmp/{ALIAS}/requirements/installation.sh" with administrator privileges'"""

# the version object class.
class Version(object):
	def __init__(self, 
		# the version value (#1).
		value="1.0.00",
		# the file path (optional) (str, FilePath).
		path=None,
		# the default value (opional) (str)
		default=None,
		# load the specified path data on initialization (bool).
		load=False,
	):

		# docs.
		DOCS = {
			"module":"Version", 
			"initialized":False,
			"description":[], 
			"chapter": "Code", }

		# defaults.
		#self.__class__.__name__ = "Version"

		# check self instance.
		if isinstance(value, Version):
			self.value = value.value

		# init.
		self.value = str(value).replace(" ","").replace("\n","").replace("\r","")
		self.int = int(str(self.value).replace(".",""))

		# path.
		if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
		else: self.file_path = self.fp = Formats.FilePath(path)
		if default != None and not Files.exists(self.file_path.path): self.save(array=default)
		if load: self.load()

		#
	def save(self, value=None, path=None, sudo=False):
		if value == None: value = self.value
		if path == None: path = self.file_path.path
		utils.__check_memory_only__(path)
		self.assign(string)
		return Files.save(path, str(string), format="str", sudo=sudo)
	def load(self, default=None, sudo=False):
		utils.__check_memory_only__(self.file_path.path)
		if not os.path.exists(self.file_path.path) and default != None: 
			self.save(default, sudo=sudo)
		self.assign(Files.load(self.file_path.path, format="str", sudo=sudo))
		return self.value
	def increase(self, value=None, count=1):
		if value == None: value = self.value

		# version 2.
		path = "/tmp/increase_version"
		Files.save(path, """version=''$1'' && echo $version | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}'""")
		for i in range(int(count)):
			value = subprocess.check_output([f"bash", path, str(value)]).decode().replace("\n","")
		self.assign(value=value)
		return value

		# version 1.
		#
		old_version = value
		base, _base_= [], old_version.split(".")
		increase = True
		for i in _base_:
			base.append(int(i))
		count = len(base)-1
		for i in range(len(base)):
			if increase:
				if base[count] >= 9:
					if count > 0:
						base[count-1] += 1
						base[count] = 0
						increase = False
					else:
						base[count] += 1
						break
				else:
					base[count] += 1
					break
			else:
				if count > 0 and int(base[count]) >= 10:
					base[count-1] += 1
					base[count] = 0
					increase = False
				elif count == 0: break
			count -= 1
		version = ""
		for i in base:
			if version == "": version = str(i)
			else: version += "."+str(i) 
		return version
		#
	# int format.
	def __index__(self):
		return self.int
	# support "+, -, +=, -=" .
	def __add__(self, count):
		if isinstance(count, (int, float)):
			a=1
		elif isinstance(count, Integer):
			count = int(count.value)
		else:
			raise Exceptions.FormatError(f"Can not add object {self.__class__} & {count.__class__}, a version should be incremented with a count (example: 1).")
		value = self.increase(value=self.value, count=count)
		return Version(value)
	def __concat__(self, count):
		if isinstance(vercount, (int, float)):
			a=1
		elif isinstance(count, Integer):
			count = int(count.value)
		else:
			raise Exceptions.FormatError(f"Can not concat object {self.__class__} & {count.__class__}, a version should be incremented with a count (example: 1).")
		value = self.increase(value=self.value, count=count)
		return Version(value)
	def __pos__(self, count):
		if isinstance(count, (int, float)):
			a=1
		elif isinstance(count, Integer):
			count = int(count.value)
		else:
			raise Exceptions.FormatError(f"Can not pos object {self.__class__} & {count.__class__}, a version should be incremented with a count (example: 1).")
		value = self.increase(value=self.value, count=count)
		return Version(value)
	def __iadd__(self, count):
		if isinstance(count, (int, float)):
			a=1
		elif isinstance(count, Integer):
			count = int(count.value)
		else:
			raise Exceptions.FormatError(f"Can not add object {self.__class__} & {count.__class__}, a version should be incremented with a count (example: 1).")
		self.assign(self.increase(value=self.value, count=count))
		return self
	def __sub__(self, count):
		raise Exceptions.InvalidUsage("A version can not be decremented.")
	def __isub__(self, count):
		raise Exceptions.InvalidUsage("A version can not be decremented.")

	# support default iteration.
	def __iter__(self):
		return iter(self.value.split("."))
	
	# support '>=' & '>' & '<=' & '<' operator.
	def __gt__(self, version):
		if not isinstance(version, self.__class__):
			raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {version.__class__}.")
		else:
			version = version.int
		return self.int > version
	def __ge__(self, version):
		if not isinstance(version, self.__class__):
			raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {version.__class__}.")
		else:
			version = version.int
		return self.int >= version
	def __lt__(self, version):
		if not isinstance(version, self.__class__):
			raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {version.__class__}.")
		else:
			version = version.int
		return self.int < version
	def __le__(self, version):
		if not isinstance(version, self.__class__):
			raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {version.__class__}.")
		else:
			version = version.int
		return self.int <= version
	
	# support '==' & '!=' operator.
	def __eq__(self, version):
		if isinstance(version, None.__class__):
			return False
		elif isinstance(version, self.__class__):
			return self.int == version.int
		else:
			return str(self.int) == str(version)
	def __ne__(self, version):
		if isinstance(version, None.__class__):
			return True
		elif isinstance(version, self.__class__):
			return self.int != version.int
		else:
			return str(self.int) != str(version)
	
	# support 'in' operator.
	def __contains__(self, string):
		if isinstance(string, (list, Files.Array)):
			for i in string:
				if str(i) in str(self.value):
					return True
			return False
		else:
			return str(string) in str(self.value)
		#
	# representation.
	def __repr__(self):
		return str(self)
		#
	# str representation.
	def __str__(self):
		return str(self.value)
	# int representation.
	def __int__(self):
		return self.int
	# float representation.
	def __float__(self):
		return float(self.int)
	# content count.
	def __len__(self):
		return len(str(self.value))
	# object id.
	def __id__(self):
		return f"({self.instance()}:{str(self)})"
	# object instance.
	def instance(self):
		return "Version"
		#
	# support self assignment.
	def assign(self, value):
		if isinstance(value, (str, String)):
			a=1
		elif isinstance(value, self.__class__):
			value = value.value
		elif not isinstance(value, self.__class__):
			raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {value.__class__}.")
		self.value = str(value)
		self.int = int(str(self.value).replace(".",""))
		return self
	# return raw data.
	def raw(self):
		return self.value
	#

# the script object class.
class Script(Files.File):
	def __init__(self, 
		# the script data (str) (param #1).
		data=None, 
		# the path (str) (param #2).
		path=None, 
		# the script executable.
		executable="sh",
		# load the data.
		load=False, 
		# the default data (create if path does not exist).
		default=None,
	):
		
		# docs.
		DOCS = {
			"module":"Script", 
			"initialized":False,
			"description":[], 
			"chapter": "Code", }

		# check self instance.
		if isinstance(data, (Files.File, Script)):
			data = data.data
		if data == None: data = ""
		Files.File.__init__(self,
			path=path,
			data=data,
			load=load,
			default=default,
		)
		self.executable = executable

		#

	# execute.
	def execute(self, 
		# the script executable (leave None to use deafult self.executable) (#1).
		executable=None,
		# the script path (str) (leave None to use default self.path) (#2).
		path=None,
	):
		if data == None: data = self.data
		if executable == None: executable = self.executable
		return execute(path=data, executable=executable)

		#

	# object instance.
	def instance(self):
		return "Script"
	@property
	def __name__(self):
		return self.instance()
		#
	# support self assignment.
	def assign(self, string):
		if isinstance(data, (int, float)):
			a=1
		elif isinstance(data, (String)):
			data = data.string
		elif isinstance(data, self.__class__):
			data = data.data
		elif not isinstance(data, self.__class__):
			raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {data.__class__}.")
		self.data = str(data)
		return self
	#

# the python object class.
class Python(Files.File):
	def __init__(self, 
		# the script data (str) (param #1).
		data=None, 
		# the path (str) (param #2).
		path=None, 
		# the script executable.
		executable="python3",
		# load the data.
		load=False, 
		# the default data (create if path does not exist).
		default=None,
	):

		# docs.
		DOCS = {
			"module":"Python", 
			"initialized":False,
			"description":[], 
			"chapter": "Code", }

		# check self instance.
		if isinstance(data, (Files.File, Script, Python)):
			data = data.data
		if data == None: data = ""
		self.directory = False
		if path != None and gfp.exists(path=path) and gfp.directory(path=path):
			self.directory = True
			load = False
		Files.File.__init__(self,
			path=path,
			data=data,
			load=load,
			default=default,
		)
		self.executable = executable
		
		#
		#
	# execute.
	def execute(self, 
		# the script executable (leave None to use defult self.executable) (#1).
		executable=None,
		# the script path (str) (leave None to use default self.path) (#2).
		path=None,
	):
		if data == None: data = self.data
		if executable == None: executable = self.executable
		return execute(path=data, executable=executable)

		#
		#
	# slice classes.
	def slice_classes(self,
		# the data (str).
		data=None, 
		# the wanted indent of the init line (optional).
		indent=None,
		# skip unparsable functions & classes.
		skip_errors=False,
		# the banned classes.
		banned_classes=[],
		# the banned functions.
		banned_functions=[],
		# the module name to use before the classes (optional) (defaults.Traceback always overwrites).
		module=None,
		# get inside classes.
		inside_classes=True,
		# get inside functions (recursive is always False).
		inside_functions=True,
		# include system functions (aka: def __somefunc__).
		system_functions=False,
		# only for self recursive use.
		keep_indent=False,
	):

		# checks.
		if data == None: data = self.data
		if data == None: raise Exceptions.InvalidUsage("Define parameter: [data].")

		# normalize.
		data = data.replace("	","    ")
		before = "\n"
		if len(data) > 0 and data[0] != before: data = before+str(data)
		while True:
			if "	" in data: data = data.replace("	","    ")
			elif ") :" in data: data = data.replace(") :","):")
			elif ")  :" in data: data = data.replace(")  :","):")
			elif ")   :" in data: data = data.replace(")   :","):")
			elif ")    :" in data: data = data.replace(")    :","):")
			elif ")     :" in data: data = data.replace(")     :","):")
			elif ")      :" in data: data = data.replace(")      :","):")
			elif ")       :" in data: data = data.replace(")       :","):")
			elif "): \n" in data: data = data.replace("): \n","):\n")
			elif "):  \n" in data: data = data.replace("):  \n","\n")
			elif "):   \n" in data: data = data.replace("):   \n","):\n")
			elif "):    \n" in data: data = data.replace("):    \n","):\n")
			elif "):     \n" in data: data = data.replace("):     \n","):\n")
			elif "):      \n" in data: data = data.replace("):      \n","):\n")
			elif "):       \n" in data: data = data.replace("):       \n","):\n")
			elif "):        \n" in data: data = data.replace("):        \n","):\n")
			#elif "\n " in data: data = data.replace("\n ", "\n")
			elif " \n" in data: data = data.replace(" \n", "\n")
			elif "DOCS =  " in data: data = data.replace("DOCS =  ", "DOCS = ")
			elif "DOCS  = " in data: data = data.replace("DOCS  = ", "DOCS = ")
			elif "DOCS   = " in data: data = data.replace("DOCS   = ", "DOCS = ")
			elif "DOCS    = " in data: data = data.replace("DOCS    = ", "DOCS = ")
			elif "DOCS     = " in data: data = data.replace("DOCS     = ", "DOCS = ")
			else: break

		# vars.
		classes = []
		to_slice = []
		for i in range(100):
			l = "\n"
			for _ in range(i): l += " "
			l += "class "
			to_slice.append(l)
		slices = String(data).split(to_slice)
		if len(slices) == 1:
			if format == dict:
				return {}
			else:
				return ""
		elif len(slices) > 1:
			slices = slices[1:]
		slice_count = 0

		# slice.
		for class_ in slices:
			if class_ not in ["", " "]:
				try: previous = slices[slice_count-1]
				except IndexError: previous = None
				if previous == None:
					init_line_indent = 0
				else:
					init_line_indent = 0
					l = len(previous)
					for _ in range(len(previous)):
						l -= 1
						if previous[l] != " ": break
						init_line_indent += 1
					if init_line_indent > 0: init_line_indent += 1 # beause of the space after [class ].
				if indent == None or str(init_line_indent) == str(int(indent)):
					class_ = String("class "+class_)
					class_line = class_.split("\n")[0]
					class_name = class_.split("(")[0].replace("class ","")
					if class_name not in banned_classes:
						if module != None:
							if module[len(module)-1] == ".": module = module[:-1]
							class_name = f"{module}.{class_name}"
						if class_name not in banned_classes:
							if "\n" not in class_:
								class_indent = init_line_indent+1
							else:
								class_indent = class_.line_indent(line=class_.split("\n")[1])
							class_code = class_.slice_indent(indent=class_indent, depth=1, remove_indent=True)
							raw_class_code = class_.slice_indent(indent=class_indent, depth=1, remove_indent=False)
							class_type = String(class_).slice_tuple(depth=1)[1:-1].replace(" ","").replace(",",", ")
							class_parameters = String(class_code).slice_tuple(depth=1)
							#print("class_name:".upper(),class_name)
							#print("class_type:".upper(),class_type)
							#print("class_parameters:".upper(),class_parameters)
							raw_name = str(class_name)
							if "." in raw_name: raw_name = raw_name.split('.')[len(raw_name.split('.'))-1]
							l_classes, functions = [], []
							recursive_clases = 0
							if inside_classes:
								while True:
									if ("\nclass " in class_code or " class " in class_code or (len(class_code) >= len("class ") and class_code[:len("class ")] == "class ")) and class_code != data and len(class_code) > 0:
										# get the depth of the class inside the class.
										inside_class_code_indent = String(class_code).line_indent(line=class_code.split("\n")[1])
										inside_class_code_depth = 0
										for line in class_code.split("\n"):
											if str(String(line).line_indent(line=line)) == str(0):
												inside_class_code_depth += 1
											if (len(line) >= len("class ") and line[:len("class ")] == "class ") or "\nclass " in line or " class " in line: 
												break
											#if (len(line) >= len("def ") and line[:len("def ")] == "def ") or "\ndef " in line or " def " in line: 
											#	inside_class_code_depth += 1
											#elif (len(line) >= len("class ") and line[:len("class ")] == "class ") or "\nclass " in line or " class " in line: 
											#	inside_class_code_depth += 1
											#	break
										inside_class_line = "class "+(class_.split(" class ")[1].split("\n")[0])
										#print("inside_class_line:".upper(),inside_class_line)
										#print("inside_class_code_indent:".upper(),inside_class_code_indent)
										#print("inside_class_code_depth:".upper(),inside_class_code_depth)
										#print(f"CLASS_CODE: [\n{class_code}]")
										inside_class_code = String(class_code).slice_indent(indent=inside_class_code_indent, depth=inside_class_code_depth, remove_indent=False)
										clean_inside_class_code = String(class_code).slice_indent(indent=inside_class_code_indent, depth=inside_class_code_depth, remove_indent=True)
										a = inside_class_line.split("(")
										a.pop(0)
										inside_class_type = String("("+str(Array(a).string(joiner=" "))+str(inside_class_code)).slice_tuple(depth=1).replace(" ","").replace(",",", ")
										#print(f"BEFORE CLASS_CODE: [\n{class_code}]")
										#print(f"INSIDE_CLASS_CODE: [\n{inside_class_code}]")
										old = str(class_code)
										full_inside_class = f"{inside_class_line.split('(')[0]}{inside_class_type}:\n{inside_class_code}"
										class_code = class_code.replace("):  \n","):\n").replace("):   \n","):\n").replace("):    \n","):\n").replace("):     \n","):\n").replace("):	\n","):\n").replace(full_inside_class, "")
										if old == class_code:
											if skip_errors:
												break
											else:
												raise ValueError(f"Replaced class code is the same as old class code: [{full_inside_class}]")
										#print(f"AFTER CLASS_CODE: [\n{class_code}]")
										#quit()
										l_module = module + "." + class_name
										classes += self.slice_classes(data=full_inside_class, keep_indent=keep_indent, inside_classes=inside_classes, inside_functions=True, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes, module=l_module)
										#print(f"{inside_class_line}\n{clean_inside_class_code}")
										#quit()
										if ("\nclass " in class_code or " class " in class_code or (len(class_code) >= len("class ") and class_code[:len("class ")] == "class ")) and class_code != data and len(class_code) > 0:
											recursive_clases += 1
										else:
											break
									else:
										break
									#print(f"detected new class [{class_code}] from code [{class_}] ")
							if inside_functions:
								if ("\ndef " in class_code or " def " in class_code or (len(class_code) >= len("def ") and class_code[:len("def ")] == "def ")) and class_code != data and len(class_code) > 0:
									functions = []
									#l_module = module + "." + String(class_name).variable_format()
									l_module = String(raw_name).variable_format()
									for i in self.slice_functions(inside_classes=False, inside_functions=False, data=class_code, indent=0, keep_indent=False, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes, module=l_module):
										skip = False
										old = str(class_code)
										class_code = class_code.replace(str(i["raw"]), "")
										#class_code = class_code.replace(i["raw_full_code"], "")
										#class_code = class_code.replace(i["init_line"].split("(")[0]+i["parameters"], "")
										#class_code = class_code.replace(i["raw_code"], "")
										if class_code == old:
											if skip_errors:
												skip = True
											else:
												raise ValueError(f"Replaced class code is the same as old class code, includes: {i['raw_full_code'] in class_code}, replacement: [{i['raw_full_code']}], code: [{class_code}].")
										if i["classes"] != {}:
											classes += i["classes"]
										del i["classes"]
										if not skip:
											functions.append(i)
							classes.append({
								"name":str(class_name),
								"raw_name":str(raw_name),
								"raw":class_,
								"code":str(class_code),
								"raw_code":str(raw_class_code),
								"indent":int(class_indent),
								"init_line":str(class_line),
								"parameters":str(class_parameters),
								"class_type":str(class_type),
								"functions":functions,
								"type":"class",
							})
			slice_count += 1

		# fill DOCS customization.
		_classes_ = []
		for info in classes:
			initialized, module, description, chapter = False, None, [], None
			if len(info["functions"]) > 0:
				for func in info["functions"]:
					if "__init__" in func["name"]:
						test = "DOCS = {"
						if test in func["code"]:
							customization = ast.literal_eval(str(String(func["code"].split(test[:-1])[1]).slice_dict(depth=1)))
							if "initialized" in customization:
								info["initialized"] = customization["initialized"]
							if "module" in customization:
								info["module"] = customization["module"]
							if "notes" in customization:
								info["description"] = customization["description"]
							if "chapter" in customization:
								info["chapter"] = customization["chapter"]
							#if "return" in customization:
							#	info["return"] = customization["return"]
							break
			for key,value in {
				"initialized":False,
				"module":None,
				"description":[],
				"chapter":None,
				#"return":"_",
			}.items():
				try:info[key]
				except: info[key] = value
			_classes_.append(info)
		classes = _classes_

		# handler.
		return classes

		#

	# slice functions.
	def slice_functions(self,
		# the data (str).
		data=None, 
		# the wanted indent of the init line (optional).
		indent=None,
		# for self recursive use.
		keep_indent=False,
		# get inside classes.
		inside_classes=True,
		# get inside functions (recursive is always False).
		inside_functions=False,
		# include system functions (aka: def __somefunc__).
		system_functions=False,
		# skip unparsable functions & classes.
		skip_errors=False,
		# the banned classes.
		banned_classes=[],
		# the banned functions.
		banned_functions=[],
		# the module name to use before the 1st indent functions (optional).
		module=None,
	):	
		# func.
		def parse_variable_format(variable, code):
			def parse_value(value):
				if len(value) > 0 and value[0] == "[":
					return "list"
				elif len(value) > 0 and value[0] == "{":
					return "dict"
				elif len(value) > 0 and value[0] in ["'", '"']:
					return "str"
				else:
					for i, return_ in [
						["None", "_"],
						["str", "str"],
						["int", "int"],
						["float", "float"],
						["list", "list"],
						["dict", "dict"],
						["FilePath", "FilePath"],
						["String", "String"],
						["Integer", "Integer"],
						["Boolean", "Boolean"],
						["Array", "Array"],
						["Dictionary", "Dictionary"],
						["response.success", "response"],
						["response.error", "response"],
					]:
						if len(value) >= len(i) and value[:len(i)] == i:
							return return_
					try: 
						int(value.split("\n")[0])
						if "." in value.split("\n")[0]:
							try:
								float(value.split("\n")[0])
								return "float"
							except: return "int"
						else:
							return "int"
					except: a=1
					return "parameter:"+value.split("\n")[0]
				#

			code = code.replace(" =","=").replace("= ","=").replace(" =","=").replace("= ","=").replace(" =","=").replace("= ","=").replace(" =","=").replace("= ","=").replace(" ,",",").replace(", ",",").replace(" ,",",").replace(", ",",").replace(" ,",",").replace(", ",",").replace(" ,",",").replace(", ",",")
			return_ = None
			# version 2.
			lines = code.split("\n")
			l = len(lines)
			for _ in range(len(lines)):
				l -= 1
				line = lines[l]
				if line.count("=") == 1 and variable in line:
					before,after = line.split("=")
					before = before[String().line_indent(line=before):]
					local = None
					if "," in before:
						if variable in before: # must include in before = because it assigns.
							c = None
							for i in before.split(","):
								if c == None: c = 0
								if i == variable:
									break
								c += 1
							if c == None:
								raise ValueError(f"Unable to find the tuple place of variable [{variable}] in tuple [{before}].")
							value = after.split(",")[c]
							if value != variable:
								local = parse_value(value)
								if len(local) >= len("parameter:") and local[:len("parameter:")] == "parameter:":
									new_var = local[len("parameter:"):]
									if new_var != variable:
										return parse_variable_format(new_var, code)
									else:
										local = None
					else:
						if after != variable: # aka $var = ... / not $other_var = $var
							local = parse_value(after)
							if len(local) >= len("parameter:") and local[:len("parameter:")] == "parameter:":
								new_var = local[len("parameter:"):]
								if new_var != variable:
									return parse_variable_format(new_var, code)
								else:
									local = None
					if local != None:
						return_ = local
						break
			return return_
			#
		def func_allowed(name, strip=False):
			if strip and "." in name: name = name.split(".")[len(name.split("."))-1]
			if name in banned_functions: return False
			if not system_functions and "__init__" not in name and len(name) >= 4 and name[:2] == "__" and name[-2:] == "__": return False
			return True
			#

		# vars.
		functions = []
		if data == None: data = self.data
		if data == None: raise Exceptions.InvalidUsage("Define parameter: [data].")
		
		# normalize.
		data = data.replace("	","    ")
		before = "\n"
		if len(data) > 0 and data[0] != before: data = before+str(data)
		while True:
			if "	" in data: data = data.replace("	","    ")
			elif ") :" in data: data = data.replace(") :","):")
			elif ")  :" in data: data = data.replace(")  :","):")
			elif ")   :" in data: data = data.replace(")   :","):")
			elif ")    :" in data: data = data.replace(")    :","):")
			elif ")     :" in data: data = data.replace(")     :","):")
			elif ")      :" in data: data = data.replace(")      :","):")
			elif ")       :" in data: data = data.replace(")       :","):")
			elif "): \n" in data: data = data.replace("): \n","):\n")
			elif "):  \n" in data: data = data.replace("):  \n","\n")
			elif "):   \n" in data: data = data.replace("):   \n","):\n")
			elif "):    \n" in data: data = data.replace("):    \n","):\n")
			elif "):     \n" in data: data = data.replace("):     \n","):\n")
			elif "):      \n" in data: data = data.replace("):      \n","):\n")
			elif "):       \n" in data: data = data.replace("):       \n","):\n")
			elif "):        \n" in data: data = data.replace("):        \n","):\n")
			#elif "\n " in data: data = data.replace("\n ", "\n")
			elif " \n" in data: data = data.replace(" \n", "\n")
			elif "	\n" in data: data = data.replace("	\n", "\n")
			elif "DOCS =  " in data: data = data.replace("DOCS =  ", "DOCS = ")
			elif "DOCS  = " in data: data = data.replace("DOCS  = ", "DOCS = ")
			elif "DOCS   = " in data: data = data.replace("DOCS   = ", "DOCS = ")
			elif "DOCS    = " in data: data = data.replace("DOCS    = ", "DOCS = ")
			elif "DOCS     = " in data: data = data.replace("DOCS     = ", "DOCS = ")
			else: break
		
		# slice with all indent (less dependable).
		if indent == None:
			to_slice = []
			for i in range(100):
				l = "\n"
				for _ in range(i): l += " "
				l += "def "
				to_slice.append(l)
			slices = String(data).split(to_slice)

		# slice by ident line.
		else:
			slices = data.split("\n"+String().indent(indent=indent)+"def ")

		# handle slices.
		if len(slices) == 1:
			return []
		elif len(slices) > 1:
			slices = slices[1:]
		slice_count = 0

		
		# iterate.
		for class_ in slices:
			if class_ not in [""," "]:
				type = "function"
				try: previous = slices[slice_count-1]
				except IndexError: previous = None
				if previous == None:
					init_line_indent = 0
				else:
					init_line_indent = 0 
					l = len(previous)
					for _ in range(len(previous)):
						l -= 1
						if previous[l] != " ": break
						init_line_indent += 1
					if init_line_indent > 0: init_line_indent += 1 # beause of the space after [class ].
				if previous != None and "@property" in previous:
					type = "property"
				if indent == None or str(init_line_indent) == str(int(indent)):
					class_ = String("def "+class_)
					class_line = class_.split("\n")[0]
					class_name = class_.split("(")[0].replace("def ","")
					if module != None:
						if module[len(module)-1] == ".": module = module[:-1]
						class_name = f"{module}.{class_name}"
					if func_allowed(class_name) and func_allowed(class_name, strip=True):
						class_parameters = String(class_).slice_tuple(depth=1)
						l_class = class_.replace(class_parameters+":","")
						for attempt in range(100):
							try:
								class_indent = String(l_class).line_indent(line=l_class.split("\n")[attempt])
								if class_indent != init_line_indent: break
							except IndexError:
								raise IndexError(f"Unable to determine the class indent of code: (\n{str(l_class)}\n).")
						if "\n" in class_parameters:
							class_code = class_.slice_indent(indent=class_indent, depth=2, remove_indent=not keep_indent)
							raw_class_code = class_.slice_indent(indent=class_indent, depth=2, remove_indent=False)
						else:
							class_code = class_.slice_indent(indent=class_indent, depth=1, remove_indent=not keep_indent)
							raw_class_code = class_.slice_indent(indent=class_indent, depth=1, remove_indent=False)
						classes, l_functions  = [], []
						if inside_classes and (("\nclass " in class_code or " class " in class_code) and class_code != data and len(class_code) > 0):
							l_module = module + "." + class_name
							classes = self.slice_classes(data=class_code, keep_indent=keep_indent, inside_functions=False, inside_classes=inside_classes, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes, module=l_module)
							for i in classes:
								full_inside_class = f"{i['init_line'].split('(')[0]}{i['class_type']}:\n{i['raw_code']}"
								class_code = class_code.replace("):  \n","):\n").replace("):   \n","):\n").replace("):    \n","):\n").replace("):     \n","):\n").replace("):	\n","):\n").replace(full_inside_class, "")
								#class_code = class_code.replace(i["init_line"].split("(")[0]+class_parameters+":\n"+i["code"], "")
						if inside_functions and (("\ndef " in class_code or " def " in class_code) and class_code != data and len(class_code) > 0):
							l_module = module + "." + class_name
							l_functions = self.slice_functions(data=class_code, keep_indent=keep_indent, inside_classes=False, inside_functions=False, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes, module=l_module)
							for i in l_functions:
								full_inside_class = f"{i['init_line'].split('(')[0]}{i['parameters']}:\n{i['raw_code']}"
								class_code = class_code.replace("):  \n","):\n").replace("):   \n","):\n").replace("):    \n","):\n").replace("):     \n","):\n").replace("):	\n","):\n").replace(full_inside_class, "")
						return_ = None
						if (" return response" in str(raw_class_code) or "\nreturn response" in str(raw_class_code)) or (" return dev0s.response." in str(raw_class_code) or "\nreturn dev0s.response." in str(raw_class_code)) or (" return _response_." in str(raw_class_code) or "\nreturn _response_." in str(raw_class_code)):
							return_ = "response"
						elif " return " not in str(raw_class_code) or "\nreturn " not in str(raw_class_code):
							return_ = "_"
						else:
							variables = raw_class_code.split(" return ")[len(raw_class_code.split(" return "))-1].split("\n")[0].replace(" ","").replace(",",", ")
							formats = []
							for variable in variables.split(", "):
								format = parse_variable_format(variable, class_parameters+":\n"+raw_class_code)
								if format == None:
									if skip_errors:
										format = "..."
									else:
										raise ValueError(f"Unable to determine the return format (#1) for function [{class_name}], code: [{class_code}]")
								formats.append(format)
							if len(formats) <= 0:
								if skip_errors:
									return_ = "..."
								else:
									raise ValueError(f"Unable to determine the return format (#2) for function [{class_name}], code: [{class_code}]")
							elif len(formats) <= 1:
								return_ = formats[0]
							else:
								return_ = Array(formats).string(joiner=", ")
						raw_name = str(class_name)
						if "." in raw_name: raw_name = raw_name.split('.')[len(raw_name.split('.'))-1]
						functions.append({
							"name":str(class_name),
							"raw_name":str(raw_name),
							"code":str(class_code),
							"raw":class_,
							"raw_code":str(raw_class_code),
							"full_code":f"{class_line.split('(')[0]}{class_parameters}:\n{class_code}",
							"raw_full_code":f"{class_line.split('(')[0]}{class_parameters}:\n{raw_class_code}",
							"indent":int(class_indent),
							"init_line":str(class_line),
							"parameters":str(class_parameters),
							"classes":classes,
							"functions":l_functions,
							"type":type,
							"return":return_,
						})
			slice_count += 1

		# fill DOCS customization.
		_functions_ = []
		for info in functions:
			initialized, module, description, chapter = False, None, [], None
			if "__init__" not in info["name"]:
				test = "DOCS = {"
				if test in info["code"]:
					customization = ast.literal_eval(str(String(info["code"].split(test[:-1])[1]).slice_dict(depth=1)))
					if "initialized" in customization:
						info["initialized"] = customization["initialized"]
					if "module" in customization:
						info["module"] = customization["module"]
					if "description" in customization:
						info["description"] = customization["description"]
					if "chapter" in customization:
						info["chapter"] = customization["chapter"]
					if "return" in customization:
						info["return"] = customization["return"]
					break
			for key,value in {
				"initialized":False,
				"module":None,
				"description":[],
				"chapter":None,
				"return":"_",
			}.items():
				try:info[key]
				except: info[key] = value
			_functions_.append(info)
		functions = _functions_

		# handler.
		return functions

		#

	# build code examples.
	def build_code_examples(self,
		# the path (leave None to use self.fp.path).
		path=None,
		# the package name (optional).
		package=None,
		# the root path in case the path is a dir (optional).
		root=None,
		# include system functions (aka: def __somefunc__).
		system_functions=False,
		# banned sub paths.
		banned=[],
		# banned names.
		banned_names=["__main__.py", "utils.py", ".version"],
		# banned basenames.
		banned_basenames=["utils", "__pycache__", ".legacy"],
		# banned class types.
		banned_class_types=["Exception"],
		# the banned classes.
		banned_classes=[],
		# the banned functions.
		banned_functions=[],
		# return format (str / dict) (always returns dict if parameter path is a list).
		format=str,
		# readme enabled.
		readme=False,
		# the log level.
		log_level=defaults.options.log_level,
		# get all ids (should not be used).
		get_all_ids=False,
	):

		# funcs.
		def clean_params(params):
			clean = params.replace('(self)', '()').replace('self  ,', '').replace('self ,', '').replace('self,', '').replace("\n)", " )")
			while True:
				if clean[:len("( ")] == "( ":
					clean = "("+clean[2:]
				else: break
			return clean
		def build_class_doc(info):
			unique_name = str(info["raw_name"])
			info['raw_name'] = info['raw_name'].split("-")[0]
			if "." in info["raw_name"]: l = info["raw_name"].split(".")[len(info["raw_name"].split("."))-1]
			else: l = info["raw_name"]
			initialized_name = String(l).variable_format()
			old_init_name = initialized_name
			#class_holder_class = True
			#if len(initialized_name) >= 2 and String(initialized_name).first("__") == "__":
			#	initialized_name = String(initialized_name).remove_first("__")
			#else: class_holder_class = False
			#if len(initialized_name) >= 2 and String(initialized_name).last("__") == "__":
			#	initialized_name = String(initialized_name).remove_last("__")
			#else: class_holder_class = False
			#if class_holder_class:
			#	initialized_name = String(initialized_name).capitalized_word()
			""" """

			# fill DOCS customization.
			initialized, module, description = info["initialized"], info["module"], info["description"]
			if module == None:
				module = info["name"]

			# docs.
			parameters = clean_params(info["parameters"]).replace("self.", initialized_name+".")
			if initialized == True:
				doc = "\n"
				if description != None:
					for i in description: doc += f"{i}\n".replace("</attribute>", "").replace("<attribute>", "").replace("</parameter>", "").replace("<parameter>", "")
				doc += (
					"\n# import the " + str(module) + " object class." + "\n" +
					"")
				doc += (
					#f"from {package} import " + module.split('.')[0] + "\n" +
					f"import {package}" + "\n" +
					"")
			else:
				doc = "\n"
				if description != None:
					for i in description: doc += f"{i}\n".replace("</attribute>", "").replace("<attribute>", "").replace("</parameter>", "").replace("<parameter>", "")
				doc += (
					"\n# initialize the " + str(module) + " object class." + "\n" +
					"")
				doc += (
					str(initialized_name)+" = " + module + str(parameters) + "\n" +
					"")
			if readme:
				doc = (
					f"## {info['raw_name']}:" + "\n" +
					f"The {initialized_name} object class." + "\n" +
					f"``` python " + "\n" +
					doc + "\n" +
					f"```" + "\n" +
					"")
			properties = []
			c = 0
			for i in info["functions"]:
				if "__init__" not in i["name"]:
					#if module != None:
					#	i["name"] = i["name"].replace(f"{old_init_name}.", f"{module}.")
					#	i["raw_name"] = i["raw_name"].replace(f"{old_init_name}.", f"{module}.")
					if "." in i["name"]:
						l = i["name"].split(".")[len(i["name"].split("."))-1]
					else:
						l = i["name"]
					i["name"] = f'{initialized_name}.{l}'
					#i["raw_name"] = f'{initialized_name}.{l}'
					i["parameters"] = clean_params(i["parameters"]).replace("self.", initialized_name+".") # just for the self / initialized_name replacement.
					if i["type"] == "property":
						properties.append(i)
					else:
						if c == 0:
							doc += "\n#### Functions:" + "\n\n"
						c += 1
						doc += build_func_doc(i, small_readme=True)
			if c > 0: doc += "\n"
			if len(properties) > 0: 
				doc += "#### Properties:" + "\n"
				for i in properties: 
					if "__init__" not in i["name"]:
						doc += build_property_doc(i)
				doc += "\n"
			return doc
		def build_func_doc(info, small_readme=False):
			unique_name = str(info["raw_name"])
			info['raw_name'] = info['raw_name'].split("-")[0]
			parameters = clean_params(info["parameters"])
			doc = (
				"\n# call " + info["name"] + "." + "\n" +
				f"{info['return']} = " + info['name'] + parameters + "\n" +
				"")
			if "__init__" in info["name"]:
				return ""
			if readme:
				if small_readme:
					doc = (
						f"##### {info['raw_name']}:" + "\n" +
						f"``` python" + "\n" +
						doc + "\n" +
						f"```" + "\n" +
						"")
				else:
					doc = (
						f"#### {info['raw_name']}:" + "\n" +
						f"The {info['name']} function." + "\n" +
						f"``` python" + "\n" +
						doc + "\n" +
						f"```" + "\n" +
						"")
			return doc
		def build_property_doc(info):
			full_name = str(info["name"])
			if "." in info["name"]:
				info["name"] = info["name"].split(".")[1]
			doc = (
				"```python" + "\n"
				"\n# the " + info["name"].replace("_"," ") + " property." + "\n" +
				info["name"]+" = " + full_name + "\n" +
				"```" + "\n"
				"")
			return doc
			#

		# slice.
		if path == None: path = self.fp.path
		if path == None:
			raise dev0s.exceptions.InvalidUsage(f"Define parameter [path] (str).")
		if gfp.exists(path=path) and gfp.directory(path=path):
			path = Directory(path).paths(extensions=["py"], banned=banned, banned_names=banned_names, banned_basenames=banned_basenames, recursive=True)
		if isinstance(path, (str, String)): path = [path]
		if root != None: root = gfp.clean(path=root)
		docs_dict = {}
		for _path_ in path:

			# load.
			if log_level >= 0:
				loader = console.Loader(f"Building code examples for [{_path_}].")
			data = Files.load(_path_)
			module = None
			if root != None: 
				module = gfp.module(path=_path_.replace(root, ""))
				if package != None:
					module = package+"."+module
			first_indent_functions = self.slice_functions(indent=0, module=module, data=data, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes)
			classes = self.slice_classes(data=data, module=module, system_functions=system_functions, banned_functions=banned_functions, banned_classes=banned_classes)

			# iterate.
			for info in first_indent_functions:
				if "__init__" not in info["name"]:
					try: info["chapter"]
					except KeyError: info["chapter"] = "Functions"
					if info["chapter"] == None: info["chapter"] = "Functions"
					try: docs_dict[info["chapter"]]
					except KeyError: docs_dict[info["chapter"]] = {}
					if info["raw_name"] in list(docs_dict[info["chapter"]].keys()):
						try:info["raw_name"] = info["raw_name"].split("-")[0]+"-"+str(int(info["raw_name"].split("-")[1])+1)
						except: info["raw_name"] = info["raw_name"]+"-1"
					docs_dict[info["chapter"]][info["raw_name"]] = {
						"docs":build_func_doc(info),
						"name":info["name"],
						"raw_name":info["raw_name"].split("-")[0],
						"unique_name":info["raw_name"],
						"type":info["type"],
						#
						"parameters":info["parameters"],
						"initialized":info["initialized"],
						"module":info["module"],
						"description":info["description"],
						"chapter":info["chapter"],
						"return":info["return"],
						"path":_path_,
					}
			for info in classes:
				l_banned = False
				for i in banned_class_types:
					if i in info["class_type"].split(", "):
						l_banned = True
						break
				if not l_banned:
					try: info["chapter"]
					except KeyError: info["chapter"] = "Classes"
					if info["chapter"] == None: info["chapter"] = "Classes"
					try: docs_dict[info["chapter"]]
					except KeyError: docs_dict[info["chapter"]] = {}
					if info["raw_name"] in list(docs_dict[info["chapter"]].keys()):
						try:info["raw_name"] = info["raw_name"].split("-")[0]+"-"+str(int(info["raw_name"].split("-")[1])+1)
						except: info["raw_name"] = info["raw_name"]+"-1"
					functions = []
					for func in info["functions"]:
						func["path"] = _path_
						functions.append(func)
					info["functions"] = functions
					docs_dict[info["chapter"]][info["raw_name"]] = {
						"docs":build_class_doc(info),
						"name":info["name"],
						"raw_name":info["raw_name"].split("-")[0],
						"unique_name":info["raw_name"],
						"type":info["type"],
						"functions":info["functions"],
						#
						"parameters":info["parameters"],
						"initialized":info["initialized"],
						"module":info["module"],
						"description":info["description"],
						"chapter":info["chapter"],
						"path":_path_,
					}
			if log_level >= 0: loader.stop()
		
		# sort alphabetically.
		docs_dict = Dictionary(docs_dict).sort(alphabetical=True)

		# assign unique id's.
		_docs_dict_ = {}
		all_ids = []
		for chapter, l_docs_dict in docs_dict.items():
			try: _docs_dict_[chapter]
			except KeyError: _docs_dict_[chapter] = {}
			for _, info in l_docs_dict.items():
				while True:
					if info["raw_name"] in all_ids:
						try:info["raw_name"] = info["raw_name"].split("-")[0]+"-"+str(int(info["raw_name"].split("-")[1])+1)
						except: info["raw_name"] = info["raw_name"]+"-1"
					else:
						all_ids.append(info["raw_name"])
						if info["type"] == "class":
							new = []
							for _info_ in info["functions"]:
								if "__init__" not in _info_["name"]:
									while True:
										if _info_["raw_name"] in all_ids:
											#print(_info_["name"], "vs", all_ids)
											try:_info_["raw_name"] = _info_["raw_name"].split("-")[0]+"-"+str(int(_info_["raw_name"].split("-")[1])+1)
											except: _info_["raw_name"] = _info_["raw_name"]+"-1"
										else:
											all_ids.append(_info_["raw_name"]) 
											break
									new.append(_info_)
							info["functions"] = new
						_docs_dict_[chapter][info["raw_name"]] = info
						break
		docs_dict = _docs_dict_

		# return.
		if format == str and len(docs_dict) == 1:
			if get_all_ids:
				return docs_dict[_path_], all_ids
			else:
				return docs_dict[_path_]
		else:
			if get_all_ids:
				return docs_dict, all_ids
			else:
				return docs_dict

		#

	# build readme code examples.
	def build_readme(self,
		# the package name.
		package="dev0s",
		# the root path in case the path is a dir (optional).
		root=None,
		# the package's description (leave "" or None to ignore).
		description="",
		# the package's install command (leave "" or None to ignore).
		installation="pip3 install dev0s --upgrade",
		# include system functions (aka: def __somefunc__).
		system_functions=False,
		# include different path's or readme str.
		include=[],
		# banned sub paths.
		banned=[],
		# banned names.
		banned_names=["__main__.py", "utils.py", ".version"],
		# banned basenames.
		banned_basenames=["utils", "__pycache__", ".legacy"],
		# banned class types.
		banned_class_types=["Exception"],
		# the banned classes.
		banned_classes=[],
		# the banned functions.
		banned_functions=[],
		# the readme export path (leave None to ignore).
		readme=None,
		# the examples export path (leave None to ignore).
		examples=None,
		# the log level.
		log_level=defaults.options.log_level,
		# the post readme replacements.
		replacements={},
	):
		
		# header.
		_readme_ =  ""
		header = (
			f"""# {package}""" + "\n" + 
			"""Author(s):  Daan van den Bergh.<br>""" + "\n" + 
			"""Copyright:  © 2020 Daan van den Bergh All Rights Reserved.<br>""" + "\n" + 
			"""Supported Operating Systems: macos & linux.<br>""" + "\n" + 
			"""<br>""" + "\n" + 
			"""<br>""" + "\n" + 
			"""<p align="center">""" + "\n" + 
			"""  <img src="https://raw.githubusercontent.com/vandenberghinc/public-storage/master/vandenberghinc/icon/icon.png" alt="Bergh-Encryption" width="50"> """ + "\n" + 
			"""</p>""" + "\n" + 
			"")

		# description.
		if description not in ["", None]:
			description = description.replace("\n", "<br>")
			_readme_ += (
				f"""\n# Description:""" + "\n" + 
				f"""{description}""" + "\n" + 
				"")

		# installation.
		if installation not in ["", None]:
			installation = installation.replace("\n", "<br>")
			_readme_ += (
				f"""\n# Installation:""" + "\n" + 
				f"""Install the package.""" + "\n" + 
				f"""\n	{installation}""" + "\n" + 
				"")

		# include.
		if include not in ["", None]:
			if isinstance(include, str):
				if os.path.exists(include):
					include = Files.load(include)
				_readme_ += (
					f"""\n{include}""" + "\n" + 
					"")
			elif isinstance(include, (list,Array)):
				for i in include:
					if os.path.exists(i):
						i = Files.load(i)
					_readme_ += (
						f"""\n{i}""" + "\n" + 
						"")

		# code examples.
		code_examples, all_ids = self.build_code_examples(format=dict, readme=True, get_all_ids=True, system_functions=system_functions, banned=banned, banned_names=banned_names, banned_basenames=banned_basenames, banned_class_types=banned_class_types, banned_classes=banned_classes, banned_functions=banned_functions, log_level=log_level, root=root, package=package)
		_code_examples_ = ""
		if len(code_examples) > 0:
			l = (
				f"""\n# Code Examples:""" + "\n" + 
				"")
			
			# add table content.
			l += f"""\n### Table of content:""" + "\n"
			last_chapter = None
			for chapter, l_code_examples in code_examples.items():
				for id, example in l_code_examples.items(): 
					if example["type"] == "class":
						if chapter == None: chapter = "Classes"
						if chapter != last_chapter:
							l += f"- [__{chapter}__](#{chapter.replace(' ','-').lower()})" + "\n"
							last_chapter = chapter
						l += f"  - [__{example['raw_name']}__](#{example['unique_name'].replace(' ','-').lower()})" + "\n"
						properties = False
						for fexample in example["functions"]:
							if "__init__" not in fexample["raw_name"]: 
								if fexample["type"] in ["property"]:
									if not properties:
										properties = True
										unique = "properties"
										while True:
											if unique not in all_ids:
												all_ids.append(unique)
												break
											else:
												try:unique = unique.split("-")[0]+"-"+str(int(unique.split("-")[1])+1)
												except: unique = unique+"-1"
										unique_name = str(unique)
										raw_name = str(fexample['raw_name']).split("-")[0]
										l += f"    * [{raw_name}](#{unique_name.replace(' ','-').lower()})" + "\n"	
								else:
									unique_name = str(fexample['raw_name'])
									raw_name = str(fexample['raw_name']).split("-")[0]
									l += f"    * [{raw_name}](#{unique_name.replace(' ','-').lower()})" + "\n"
			l += "\n"#------\n\n"
			_code_examples_ += l
			_readme_ += l
			
			# add codes.
			for chapter, l_code_examples in code_examples.items():
				for _, example in l_code_examples.items(): 
					#print(example)
					_code_examples_ += example["docs"]
					_readme_ += example["docs"]

		# create header table of content.
		code_open, headers = False, []
		for line in _readme_.split("\n"):
			if '```' in line: 
				if code_open: code_open = False
				else: code_open = True
			if not code_open and len(line) >= len("# ") and line[:len("# ")] == "# ":
				h = line[len("# "):].replace(":","")
				while True:
					if len(h) > 0 and h[len(h)-1] == " ": h = h[:-1]
					elif len(h) > 0 and h[0] == " ": h = h[1:]
					else: break
				headers.append(h)
		table = f"""\n## Table of content:""" + "\n"
		for name in headers: 
			table += f"  * [{name}](#{name.replace(' ','-').lower()})" + "\n"
		table += "\n"#------\n\n"
		_readme_ = header + table + _readme_

		# normalize.
		_readme_ = _readme_.replace("\n\n\n","\n\n").replace("\n\n\n","\n\n").replace("\n\n\n","\n\n").replace("\n\n\n","\n\n")
		_code_examples_ = _code_examples_.replace("\n\n\n","\n\n").replace("\n\n\n","\n\n").replace("\n\n\n","\n\n").replace("\n\n\n","\n\n")

		# replacements must be at the end so the user can test and add replacements.
		for from_, to_ in replacements.items():
			_readme_ = _readme_.replace(from_, to_)
			_code_examples_ = _code_examples_.replace(from_, to_)

		# readme export.
		if readme != None:
			if log_level >= 0: loader = console.Loader(f"Saving created readme to [{readme}]")
			if not os.path.exists(gfp.base(path=readme)): os.system(f"mkdir -p {gfp.base(path=readme)}")
			Files.save(readme, _readme_)
			if log_level >= 0: loader.stop()

		# examples export.
		if examples != None:
			if log_level >= 0: loader = console.Loader(f"Saving created code examples to [{examples}]")
			if not Files.exists(gfp.base(examples)): Files.create(gfp.base(examples), directory=True)
			Files.save(examples, _code_examples_)
			if log_level >= 0: loader.stop()

		# handler.
		return code_examples, _readme_
		
		#

	# clean python code.
	def clean(self,
		# forced enabled ignored the warning prompt (bool).
		forced=False,
		# the self path (str) (leave None to use self.path).
		path=None,
	):

		raise ValueError("Coming soon.")

		# prompt warning.
		if not forced and not console.input(f"&RED&Warning&END&: You are cleaning python code [{path}], do you wish to proceed?", yes_no=True):
			raise Exceptions.AbortError("User aborted.")

		# vars.
		if path == None: path = self.fp.path
		if path == None: raise Exceptions.InvalidUsage("<Python.clean> define parameter: [path].")

		""" load data """
		data = Files.load(path=path, format="str")

		""" normalize data """
		while True:
			if "	" in data: data = data.replace("	", "    ")
			else: break

		"""
		add # to the the end of each indentation.
		"""
		def check_indentation_end(data):
			new_data, string = "", String()
			items = String(data).iterate_lines()
			max = len(items)-1
			last_indent = None
			last_chars = {
				"1":"",
				"blank":False,
			}
			for linecount, line in items:
				indent = string.line_indent(line=line)
				print(f"{indent}:[{line}]")
				if last_indent != None and last_chars["1"] != "#" and indent < last_indent:
					print("Found lower indent difference")
					difference = indent - last_indent
					new_data += string.indent(indent=last_indent)+"#\n"
				if linecount == max: new_data += line
				else: new_data += line+"\n"
				last_indent = indent
				if len(line) > 0: l = line[len(line)-1]
				else: l = ""

				# add last chars.
				last_chars["blank"] = line in [""]
				for key, _ in last_chars.items():
					if key not in ["blank"]:
						last_chars[key] += l
						while True:
							if len(last_chars[key]) >= int(key): last_chars[key] = last_chars[key][:-1]
							else: break

				#

			return new_data

		# call cleanings.
		old = str(data)
		data = check_indentation_end(data)

		# results.
		print("\n=====================================\nFrom:\n"+old)
		print("\n=====================================\nTo:\n"+data)


	# object instance.
	def instance(self):
		return "Python"
	@property
	def __name__(self):
		return self.instance()
		
		#

	# support self assignment.
	def assign(self, string):
		if isinstance(data, (int, float)):
			a=1
		elif isinstance(data, (String)):
			data = data.string
		elif isinstance(data, self.__class__):
			data = data.data
		elif not isinstance(data, self.__class__):
			raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {data.__class__}.")
		self.data = str(data)
		return self
		
		#

	#

#
