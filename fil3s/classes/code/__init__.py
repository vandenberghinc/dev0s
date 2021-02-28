#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from fil3s.classes.defaults import *

# the code classes.
class Code():
	#
	# execute code.
	def execute(self, 
		# the script data (str) (leave none to use default self.data).
		data=None,
		# the script executive (leave none to use default self.executive).
		executive=None,
	):
		if executive == None: executive = self.executive
		if data != None and not isinstance(data, list):
			raise ValueError("Invalid usage, parameter script / self.data requires to be a str.")
		if data == None or self.fp == None or self.fp.path == None:
			if data == None:
				data = self.data
			path = f"/tmp/tmp_script_{Formats.String('').generate()}"
			Files.save(path, data)
			delete = True
		else:
			delete = False
			path = self.fp.path
		try:
			proc = subprocess.run(
				[executive, path],
				check=True,
				capture_output=True,
				text=True,
			)
		except subprocess.CalledProcessError as error:
			error_, output = error.stderr, error.output
			if isinstance(error_, bytes): error_ = error_.decode()
			if isinstance(output, bytes): output = error_.decode()
			return r3sponse.error(f"Failed to execute script ({data}), (output: {output}), (error: {error_}).")
		error_, output = proc.stderr, proc.stdout
		if isinstance(error_, bytes): error_ = error_.decode()
		if isinstance(output, bytes): output = error_.decode()
		if error_ != "":
			return r3sponse.error(f"Failed to execute script ({data}), (output: {output}), (error: {error_}).")
		if len(output) > 0 and output[len(output)-1] == "\n": output = output[:-1]
		if delete: Files.delete(path)
		return r3sponse.success(f"Succesfully executed script ({data}), (output: {output}), (error: {error_}).", {
			"output":output,
			"process":proc,
		})

	# the script object class.
	class Script(Files.File):
		def __init__(self, 
			# the script data (str) (param #1).
			data=None, 
			# the path (str) (param #2).
			path=None, 
			# the script executive.
			executive="sh",
			# load the data.
			load=False, 
			# the default data (create if path does not exist).
			default=None,
		):
			# check self instance.
			if isinstance(data, (Files.File, Code.Script)):
				data = data.data
			if data == None: data = ""
			Files.File.__init__(self,
				path=path,
				data=data,
				load=load,
				default=default,
			)
			self.executive = executive
		def execute(self, 
			# the script data (str) (leave None to use default self.data).
			data=None,
			# the script executive (leave None to use deafult self.executive).
			executive=None,
		):
			if executive == None: executive = self.executive
			if data == None: data = self.data
			return Code.execute(data=data, executive=executive)
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
			elif isinstance(data, (Formats.String)):
				data = data.string
			elif isinstance(data, self.__class__):
				data = data.data
			elif not isinstance(data, self.__class__):
				raise exceptions.FormatError(f"Can not assign object {self.__class__} & {data.__class__}.")
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
			# the script executive.
			executive="python3",
			# load the data.
			load=False, 
			# the default data (create if path does not exist).
			default=None,
		):
			# check self instance.
			if isinstance(data, (Files.File, Code.Script, Code.Python)):
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
			self.executive = executive
		def execute(self, 
			# the script data (str) (leave none to use default self.data).
			data=None,
		):
			if data == None: data = self.data
			return Code.execute(data=data, executive=self.executive)
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
			# the module name to use before the classes (optional) (syst3m.defaults.Traceback always overwrites).
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
			if data == None: data = self.data
			if data == None: raise exceptions.InvalidUsage("Define parameter: [data].")
			data = data.replace("	","    ")
			if not keep_indent: before="\n"
			else: before = " "
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
				else: break
			classes = []
			#slices = data.split(f"{before}class ")
			slices = String(data).split([" class ", "\nclass "])
			if len(slices) == 1:
				if format == dict:
					return {}
				else:
					return ""
			elif len(slices) > 1:
				slices = slices[1:]
			slice_count = 0
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
											inside_class_code_indent = class_code.line_indent(line=class_code.split("\n")[1])
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
			return classes
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
							["r3sponse.success", "response"],
							["r3sponse.error", "response"],
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

			# vars.
			functions = []
			if data == None: data = self.data
			if data == None: raise exceptions.InvalidUsage("Define parameter: [data].")
			
			# normalize.
			data = data.replace("	","    ")
			if len(data) > 0 and data[0] != "\n": data = "\n"+str(data)
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
				else: break
			
			# slice with all indent (less dependable).
			if indent == None:
				slices = String(data).split([" def ", "\ndef "])

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
							if " return r3sponse" in str(raw_class_code) or "\nreturn r3sponse" in str(raw_class_code):
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
			return functions
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
			banned_names=["__main__.py", "utils.py", ".version.py"],
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
			log_level=LOG_LEVEL,
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
				initialized_name = String(info["raw_name"]).variable_format()
				"""
				# fill traceback name.
				# depricated due to module param & detection.
				if len(info["functions"]) > 0:
					for func in info["functions"]:
						if "__init__" in func["name"]:
							set = False
							for test in [
								"syst3m.objects.Traceback",
								"syst3m.objects.Object",
								"syst3m.objects.Thread",
							]:
								if f"{test}.__init__(" in func["code"]:
									params = clean_params(func["code"].split(f"{test}.__init__(")[1].split(")")[0])
									if "raw_traceback=" in params:
										raw_traceback = params.split("raw_traceback=")[1].split(",")[0].replace("'",'').replace('"','')
										if "traceback=" in params: # check if traceback is ClassFormat
											traceback = params.split("traceback=")[1].split(",")[0].replace("'",'').replace('"','')
											if traceback.lower() != traceback:
												info["name"] = traceback
											else:
												info["name"] = raw_traceback
										else:
											info["name"] = raw_traceback
										set = True
										break
									elif "traceback=" in params:
										info["name"] = params.split("traceback=")[1].split(",")[0].replace("'",'').replace('"','')
										set = True
										break
							if set: break
				"""
				parameters = clean_params(info["parameters"]).replace("self.", initialized_name+".")
				doc = (
					"\n\n# initialize the " + str(initialized_name) + " object class." + "\n" +
					#"#" + "\n" +
					str(initialized_name)+" = " + info["name"] + str(parameters) + "\n" +
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
					f"{info['return']} = " + info["name"] + parameters + "\n" +
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

			# slice.
			if path == None: path = self.fp.path
			if gfp.exists(path=path) and gfp.directory(path=path):
				path = Directory(path).paths(extensions=["py"], banned=banned, banned_names=banned_names, banned_basenames=banned_basenames, recursive=True)
			if isinstance(path, (str, String)): path = [path]
			if root != None: root = gfp.clean(path=root)
			docs_dict = {}
			for _path_ in path:

				# load.
				if log_level >= 0:
					loader = utils.Loader(f"Building code examples for [{_path_}].")
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
						if info["raw_name"] in list(docs_dict.keys()):
							try:info["raw_name"] = info["raw_name"].split("-")[0]+"-"+str(int(info["raw_name"].split("-")[1])+1)
							except: info["raw_name"] = info["raw_name"]+"-1"
						else:
							docs_dict[info["raw_name"]] = {
								"docs":build_func_doc(info),
								"raw_name":info["raw_name"].split("-")[0],
								"unique_name":info["raw_name"],
								"type":info["type"],
							}
				for info in classes:
					l_banned = False
					for i in banned_class_types:
						if i in info["class_type"].split(", "):
							l_banned = True
							break
					if not l_banned:
						if info["raw_name"] in list(docs_dict.keys()):
							try:info["raw_name"] = info["raw_name"].split("-")[0]+"-"+str(int(info["raw_name"].split("-")[1])+1)
							except: info["raw_name"] = info["raw_name"]+"-1"
						else:
							docs_dict[info["raw_name"]] = {
								"docs":build_class_doc(info),
								"raw_name":info["raw_name"].split("-")[0],
								"unique_name":info["raw_name"],
								"type":info["type"],
								"functions":info["functions"],
							}
				if log_level >= 0: loader.stop()
			
			# sort alphabetically.
			docs_dict = Dictionary(docs_dict).sort(alphabetical=True)

			# assign unique id's.
			_docs_dict_ = {}
			all_ids = []
			for _, info in docs_dict.items():
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
						_docs_dict_[info["raw_name"]] = info
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
		# build readme code examples.
		def build_readme(self,
			# the package name.
			package="fil3s",
			# the root path in case the path is a dir (optional).
			root=None,
			# the package's description (leave "" or None to ignore).
			description="",
			# the package's install command (leave "" or None to ignore).
			installation="pip3 install fil3s --upgrade",
			# include system functions (aka: def __somefunc__).
			system_functions=False,
			# include different path's or readme str.
			include=[],
			# banned sub paths.
			banned=[],
			# banned names.
			banned_names=["__main__.py", "utils.py", ".version.py"],
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
			log_level=LOG_LEVEL,
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
				for id, example in code_examples.items(): 
					if example["type"] == "class":
						l += f"- [__{example['raw_name']}__](#{example['unique_name'].replace(' ','-').lower()})" + "\n"
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
										l += f"  * [{raw_name}](#{unique_name.replace(' ','-').lower()})" + "\n"	
								else:
									unique_name = str(fexample['raw_name'])
									raw_name = str(fexample['raw_name']).split("-")[0]
									l += f"  * [{raw_name}](#{unique_name.replace(' ','-').lower()})" + "\n"
				l += "\n"#------\n\n"
				_code_examples_ += l
				_readme_ += l
				# add codes.
				for _, example in code_examples.items(): 
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

			# readme export.
			if readme != None:
				if log_level >= 0: loader = utils.Loader(f"Saving created readme to [{readme}]")
				if not os.path.exists(gfp.base(path=readme)): os.system(f"mkdir -p {gfp.base(path=readme)}")
				Files.save(readme, _readme_)
				if log_level >= 0: loader.stop()

			# examples export.
			if examples != None:
				if log_level >= 0: loader = utils.Loader(f"Saving created code examples to [{examples}]")
				if not os.path.exists(gfp.base(path=examples)): os.system(f"mkdir -p {gfp.base(path=examples)}")
				Files.save(examples, _code_examples_)
				if log_level >= 0: loader.stop()

			# handler.
			return _readme_

		#
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
			elif isinstance(data, (Formats.String)):
				data = data.string
			elif isinstance(data, self.__class__):
				data = data.data
			elif not isinstance(data, self.__class__):
				raise exceptions.FormatError(f"Can not assign object {self.__class__} & {data.__class__}.")
			self.data = str(data)
			return self
	#
	#

# shortcuts.
Script = Code.Script
Python = Code.Python