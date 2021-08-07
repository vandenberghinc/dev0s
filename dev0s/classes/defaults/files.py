#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Must still be recoded with some cleaner code.
"""

# imports.
from dev0s.classes.config import *
from dev0s.classes import utils
from dev0s.classes.defaults.color import color, symbol
from dev0s.classes import console
from dev0s.classes.defaults.exceptions import Exceptions

# pip.
from datetime import datetime, timezone
import shutil, math
from PIL import Image as _Image_

"""
Notes.
All default files & formats must exact the same as the default dict, bool, list etc in the native sense.
There are lots additionals though. But a dict and Dictionary should be able to be used universally as if the user would not know the difference (which could very quickly in some instances).
"""

# the format classes.
class Formats():

	# variables.
	digits = [0,1,2,3,4,5,6,7,8,9,]
	str_digits = ["0","1","2","3","4","5","6","7","8","9"]
	alphabet, capitalized_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], []
	for i in alphabet: capitalized_alphabet.append(i.upper())
	special_characters = ["±","§","!","@","€","#","£","$","¢","%","∞","^","&","ª","(",")","–","_","+","=","{","}","[","]",";",":","'",'"',"|","\\","//","?",">",".",",","<"]

	# check & get format / instance.
	def check(
		nones=None,
		booleans=None,
		none_allowed_booleans=None,
		strings=None,
		none_allowed_strings=None,
		integers=None,
		none_allowed_integers=None,
		bytes_=None,
		none_allowed_bytes=None,
		arrays=None,
		none_allowed_arrays=None,
		dictionaries=None,
		none_allowed_dictionaries=None,
	):
		if nones != None:
			for key,value in nones.items():
				if value == None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [!null].")
		if booleans != None:
			for key,value in booleans.items():
				if not isinstance(value, bool): raise ValueError(f"Invalid [{key}] format [{value}], required format is [bool].")
		if none_allowed_booleans != None:
			for key,value in none_allowed_booleans.items():
				if not isinstance(value, bool) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [bool].")
		if strings != None:
			for key,value in strings.items():
				if not isinstance(value, str): raise ValueError(f"Invalid [{key}] format [{value}], required format is [str].")
		if none_allowed_strings != None:
			for key,value in none_allowed_strings.items():
				if not isinstance(value, str) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [str].")
		if integers != None:
			for key,value in integers.items():
				if not isinstance(value, int): raise ValueError(f"Invalid [{key}] format [{value}], required format is [int].")
		if none_allowed_integers != None:
			for key,value in none_allowed_integers.items():
				if not isinstance(value, int) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [int].")
		if bytes_ != None:
			for key,value in bytes_.items():
				if not isinstance(value, bytes): raise ValueError(f"Invalid [{key}] format [{value}], required format is [bytes].")
		if none_allowed_bytes != None:
			for key,value in none_allowed_bytes.items():
				if not isinstance(value, bytes) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [bytes].")
		if arrays != None:
			for key,value in arrays.items():
				if not isinstance(value, list): raise ValueError(f"Invalid [{key}] format [{value}], required format is [list].")
		if none_allowed_arrays != None:
			for key,value in none_allowed_arrays.items():
				if not isinstance(value, list) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [list].")
		if dictionaries != None:
			for key,value in dictionaries.items():
				if not isinstance(value, dict): raise ValueError(f"Invalid [{key}] format [{value}], required format is [dict].")
		if none_allowed_dictionaries != None:
			for key,value in none_allowed_dictionaries.items():
				if not isinstance(value, dict) and value != None: raise ValueError(f"Invalid [{key}] format [{value}], required format is [dict].")
	def get(value, serialize=False):
		if value == None: return None
		elif isinstance(value, bool): 
			if not serialize:   return bool
			else:               return "bool"
		elif isinstance(value, str): 
			if not serialize:   return str
			else:               return "str"
		elif isinstance(value, int): 
			if not serialize:   return int
			else:               return "int"
		elif isinstance(value, bytes): 
			if not serialize:   return bytes
			else:               return "bytes"
		elif isinstance(value, list): 
			if not serialize:   return list
			else:               return "list"
		elif isinstance(value, dict): 
			if not serialize:   return dict
			else:               return "dict"
		elif isinstance(value, Boolean) or value.__class__.__name__ == "Boolean": 
			if not serialize:   return Boolean
			else:               return "Boolean"
		elif isinstance(value, String) or value.__class__.__name__ == "String": 
			if not serialize:   return String
			else:               return "String"
		elif isinstance(value, Integer) or value.__class__.__name__ == "Integer": 
			if not serialize:   return Integer
			else:               return "Integer"
		elif isinstance(value, Bytes) or value.__class__.__name__ == "Bytes": 
			if not serialize:   return Bytes
			else:               return "Bytes"
		elif isinstance(value, Array) or value.__class__.__name__ == "Array": 
			if not serialize:   return Array
			else:               return "Array"
		elif isinstance(value, Dictionary) or value.__class__.__name__ == "Dictionary": 
			if not serialize:   return Dictionary
			else:               return "Dictionary"
		elif isinstance(value, FilePath) or value.__class__.__name__ == "FilePath": 
			if not serialize:   return FilePath
			else:               return "FilePath"
		elif isinstance(value, object): 
			if not serialize:   return object
			else:               return "object"
		else: raise ValueError(f"Unknown format [{value}].")
		#

	# try to parse variable to format, when failed it returns None.
	def parse(
		# the variable to parse (required) (#1).
		variable, 
		# the expected format (required) (#2).
		format=None, 
		# with safe disabled it throws a ParseError when the variable can't be parsed to the expected format.
		safe=True, 
		# the default return value for when safe is enabled.
		default=None,
	):
		if format in [bool, "bool", Boolean, "Boolean"]:
			try: 
				return bool(variable)
			except:
				if safe:
					return default
				else:
					raise Exceptions.ParseError(f"Unable to parse a bool from ({variable.__class__.__name__}) [{variable}].")
		elif format in [int, "int"]:
			try: 
				return int(variable)
			except:
				if safe:
					return default
				else:
					raise Exceptions.ParseError(f"Unable to parse a int from ({variable.__class__.__name__}) [{variable}].")
		elif format in [float, "float", Integer, "Integer"]:
			try: 
				return float(variable)
			except:
				if safe:
					return default
				else:
					raise Exceptions.ParseError(f"Unable to parse a float from ({variable.__class__.__name__}) [{variable}].")
		elif format in [str, "str", String, "String"]:
			try: 
				return str(variable)
			except:
				if safe:
					return default
				else:
					raise Exceptions.ParseError(f"Unable to parse a str from ({variable.__class__.__name__}) [{variable}].")
		elif format in [list, "list", Array, "Array"]:
			if isinstance(variable, (list,Array)):
				return variable
			elif not isinstance(variable, (str, String)):
				if safe:
					return default
				else:
					raise Exceptions.ParseError(f"Unable to parse an array from ({variable.__class__.__name__}) [{variable}].")
			try: 
				return ast.literal_eval(variable)
			except:
				try: 
					return json.loads(variable)
				except:
					if safe:
						return default
					else:
						raise Exceptions.ParseError(f"Unable to parse an array from ({variable.__class__.__name__}) [{variable}].")
		elif format in [dict, "dict", Dictionary, "Dictionary"]:
			if isinstance(variable, (dict,Dictionary)):
				return variable
			elif not isinstance(variable, (str, String)):
				raise Exceptions.ParseError(f"Unable to parse a dict from ({variable.__class__.__name__}) [{variable}].")
			try: 
				return ast.literal_eval(variable)
			except:
				try: 
					return json.loads(variable)
				except:
					if safe:
						return default
					else:
						raise Exceptions.ParseError(f"Unable to parse a dict from ({variable.__class__.__name__}) [{variable}].")
		else:
			raise Exceptions.InvalidUsage(f"Specified format [{format}] is not a valid format option.")

		#

	# initialize from default format to dev0s format.
	def initialize(variable, file_paths=True):
		if variable.__class__.__name__ in ["str","String"]:
			if file_paths and "/" in variable and Files.exists(variable):
				return FilePath(variable)
			else:
				return String(variable)
		elif variable.__class__.__name__ in ["bool","Boolean"]:
			return Boolean(variable)
		elif variable.__class__.__name__ in ["int","float","Integer"]:
			return Integer(variable)
		elif variable.__class__.__name__ in ["dict","Dictionary"]:
			return Dictionary(variable)
		elif variable.__class__.__name__ in ["list","Array"]:
			return Array(variable)
		else:
			return variable

		#

	# denitialize from dev0s formats to default format.	
	def denitialize(variable, file_paths=True):
		if variable.__class__.__name__ in ["String"]:
			return str(variable)
		elif variable.__class__.__name__ in ["FilePath"]:
			return str(variable)
		elif variable.__class__.__name__ in ["Boolean"]:
			return bool(variable)
		elif variable.__class__.__name__ in ["Integer"]:
			return variable.value
		elif variable.__class__.__name__ in ["Dictionary", "ResponseObject", "OutputObject", "dict"]:
			new = {}
			for key,value in variable.items():
				new[key] = Formats.denitialize(value, file_paths=file_paths)
			return new
		elif variable.__class__.__name__ in ["Array", "list"]:
			new = []
			for value in variable:
				new.append(Formats.denitialize(value, file_paths=file_paths))
			return new
		else:
			return variable
		#
		
	# the file path object class.
	class FilePath(object):
		def __init__(self, path, default=False, check=False, load=False):

			# docs.
			DOCS = {
				"module":"FilePath", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# init.
			self.path = str(self.clean(path=str(path), raw=True))
			if check == False and default == False and path != False:
				if Files.directory(self.path) and self.path[len(self.path)-1] != '/': self.path += '/'
			if check and os.path.exists(self.path) == False: raise FileNotFoundError(f"Path [{self.path}] does not exist.")
			self.ownership = self.Ownership(path=self.path, load=load)
			self.permission = self.Permission(path=self.path, load=load)

			#
		#   -   info:
		def join(self, name=None, type="/"):
			if type not in ["", "/"] and "." not in type:
				type = "." + type
			path = self.path
			if path[len(path)-1] != "/": path += '/'
			return FilePath("{}{}{}".format(path, name, type))
		def name(self, path=None, remove_extension=False,):
			if path == None: path = self.path
			if path in [False, None]: return None
			x = 1
			if path[len(path)-1] == '/': x += 1
			name = path.split('/')[len(path.split('/'))-x]
			if remove_extension:
				count = len(name.split("."))
				if count > 1:
					c, s = 0, None
					for i in name.split("."):
						if c < count-1:
							if s == None: s = i
							else: s += "."+i
						c += 1
					name = s
			return name
		def extension(self, name=None, path=None):
			if path == None: path = self.path
			#   -   check directory:
			extension = None
			if name == None and Files.directory(path): extension = 'dir'
			else:
				#   -   get extension:
				try:
					if name == None: name = self.name(path=path)
					extension = name.split('.')[len(name.split('.'))-1]
				except:
					try:
						name = self.name(path=path)
						extension = name.split('.')[len(name.split('.'))-1]
					except: extension = None
			#   -   check image & video:
			if extension in ["jpg", "png", "gif", "webp", "tiff", "psd", "raw", "bmp", "heig", "indd", "jpeg", "svg", "ai", "eps", "pdf"]: extension = "img"
			elif extension in ["mp4", "m4a", "m4v", "f4v", "f4a", "m4b", "m4r", "f4b", "mov", "3gp", "3gp2", "3g2", "3gpp", "3gpp2", "h.263", "h.264", "hevc", "mpeg4", "theora", "3gp", "windows media 8", "quicktime", "mpeg-4", "vp8", "vp6", "mpeg1", "mpeg2", "mpeg-ts", "mpeg", "dnxhd", "xdcam", "dv", "dvcpro", "dvcprohd", "imx", "xdcam", "hd", "hd422"]: extension = "video"
			return extension
		def base(self, 
			# the path (leave None to use self.path) (param #1).
			path=None,
			# the dirs back.
			back=1,
		):
			if path == None: path = self.path
			return Files.base(path=path, back=back)

			#
		def basename(self, back=1, path=None):
			if path == None: path = self.path
			return self.name(path=self.base(back=back, path=path))
		def size(self, format=str,  mode="auto", path=None, options=["auto", "bytes", "kb", "mb", "gb", "tb"]):
			def __size__(path):
				total = 0
				try:
					# print("[+] Getting the size of", directory)
					for entry in os.scandir(path):
						if entry.is_file():
							# if it's a file, use stat() function
							total += entry.stat().st_size
						elif entry.is_dir():
							# if it's a directory, recursively call this function
							total += __size__(entry.path)
				except NotADirectoryError:
					# if `directory` isn't a directory, get the file size then
					return os.path.getsize(path)
				except PermissionError:
					# if for whatever reason we can't open the folder, return 0
					return 0
				return total
				#
			if path == None: path = self.path
			if path != None: path = str(path)
			return self.convert_bytes(__size__(path), format=format, mode=mode)
		def space(self, format=str,  mode="auto", path=None, options=["auto", "bytes", "kb", "mb", "gb", "tb"]):
			if path == None: path = self.path
			total, used, free = shutil.disk_usage(path)
			total, used, free = self.convert_bytes(total, format=format, mode=mode), self.convert_bytes(used, format=format, mode=mode), self.convert_bytes(free, format=format, mode=mode)
			return {
				"total":total,
				"used":used,
				"free":free,
			}
		def convert_bytes(self, bytes:int, format=str, mode="auto", options=["auto", "bytes", "kb", "mb", "gb", "tb"]):
			if format in [float, "float", "integer", "Integer", Integer]:
				format = float
				if (mode == "bytes" or mode == "bytes".upper()):
					return float(bytes)
			elif format in [int, "int", "integer", "Integer", Integer]:
				format = int
				if (mode == "bytes" or mode == "bytes".upper()):
					return int(round(bytes,0))
			if mode == "auto":
				if int(bytes/1024**4) >= 10:
					bytes = round(bytes/1024**4,2)
					if format not in [int, float]:
						bytes = '{:,} TB'.format(bytes)#.replace(',', '.')
				elif int(bytes/1024**3) >= 10:
					bytes = round(bytes/1024**3,2)
					if format not in [int, float]:
						bytes = '{:,} GB'.format(bytes)#.replace(',', '.')
				elif int(bytes/1024**2) >= 10:
					bytes = round(bytes/1024**2,2)
					if format not in [int, float]:
						bytes = '{:,} MB'.format(bytes)#.replace(',', '.')
				elif int(bytes/1024) >= 10:
					bytes = round(bytes/1024,2)
					if format not in [int, float]:
						bytes = '{:,} KB'.format(bytes)#.replace(',', '.')
				else:
					bytes = int(round(bytes,0))
					if format not in [int, float]:
						bytes = '{:,} Bytes'.format(bytes)#.replace(',', '.')
			elif (mode == "bytes" or mode == "bytes".upper()): 
				bytes = int(round(bytes,0))
				if format not in [int, float]:
					bytes = '{:,} Bytes'.format(bytes)#.replace(',', '.') 
			elif mode == "kb" or mode == "kb".upper(): 
				bytes = round(bytes/1024,2)
				if format not in [int, float]:
					bytes = '{:,} KB'.format(bytes)#.replace(',', '.') 
			elif mode == "mb" or mode == "mb".upper(): 
				bytes = round(bytes/1024**2,2)
				if format not in [int, float]:
					bytes = '{:,} MB'.format(bytes)#.replace(',', '.') 
			elif mode == "gb" or mode == "gb".upper(): 
				bytes = round(bytes/1024**3,2)
				if format not in [int, float]:
					bytes = '{:,} GB'.format(bytes)#.replace(',', '.') 
			elif mode == "tb" or mode == "tb".upper(): 
				bytes = round(bytes/1024**4,2)
				if format not in [int, float]:
					bytes = '{:,} TB'.format(bytes)#.replace(',', '.') 
			else: raise Exceptions.InvalidUsage(f"Selected an invalid size format [{format}], options {options}.")
			return bytes 
		def exists(self, 
			# the path (leave None to use self.path) (#1).
			path=None,
			# root permission required.
			sudo=False,
		):
			if path == None: path = self.path
			path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
			path = str(path)
			if not sudo:
				return os.path.exists(str(path))
			else:
				try:
					output = utils.__execute__(["sudo", "ls","-ld",path])
					if "No such file or directory" in str(output):
						return False   
					else: return True
				except: return False
			#
		def mount(self, 
			# the path (leave None to use self.path) (#1).
			path=None,
		):
			if path == None: path = self.path
			path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
			return os.path.ismount(path)
			#
		def directory(self, 
			# the path (leave None to use self.path) (#1).
			path=None,
		):
			if path == None: path = self.path
			return Files.directory(path)
			#
		def mtime(self, format='%d-%m-%y %H:%M.%S', path=None):
			if path == None: path = self.path
			fname = pathlib.Path(path)
			try: mtime = fname.stat().st_mtime
			except: mtime = fname.stat().ct_mtime
			if format in ['s', "seconds"]:
				return mtime
			else:
				return Formats.Date().from_seconds(mtime, format=format)
		def clean(self, 
			# the path (leave None to use self.path) (param #1).
			path=None, 
			# the clean options.
			remove_double_slash=True, 
			remove_first_slash=False, 
			remove_last_slash=False,
			ensure_first_slash=False,
			ensure_last_slash=False,
			# return the path as a raw string.
			raw=False,
		):
			if path == None: path = self.path
			if not isinstance(path, (str, String)): 
				return path
			path = str(path).replace("~",HOME)
			while True:
				if remove_double_slash and "//" in path: path = path.replace("//","/")
				elif remove_first_slash and len(path) > 0 and path[0] == "/": path = path[1:]
				elif remove_last_slash and len(path) > 0 and path[len(path)-1] == "/": path = path[:-1]
				elif ensure_first_slash and len(path) > 0 and path[0] != "/": path = "/"+path
				elif ensure_last_slash and len(path) > 0 and path[len(path)-1] != "/": path += "/"
				else: break
			if raw:
				return path
			else:
				return FilePath(path)
		def absolute(self, 
			# the path (leave None to use self.path) (param #1).
			path=None,
		):
			if path == None: path = self.path
			return FilePath(os.path.abspath(path))
		# path to python module path.
		def module(self, path=None):
			if path == None: path = self.path
			return gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True, remove_first_slash=True).replace("/",".").replace(".py","").replace(".__init__", "").replace("__init__", "")
		# serialize a requirements file.
		def requirements(self, path=None, format="pip", include_version=True):
			if format in ["pip3"]: format = "pip"
			if format not in ["pip"]: raise ValueError(f"Invalid usage, format [{format}] is not a valid option, options: [pip].")
			# pip requirements.
			if format == "pip":
				requirements = []
				for i in Files.load(path).split("\n"):
					if len(i) > 0 and i[0] != "#" and i not in [""," "]:
						while True:
							if len(i) > 0 and i[len(i)-1] in [" "]: i = i[:-1]
							else: break
						if " " not in i:
							sid = None
							for lid in ["==", ">=", "<="]:
								if lid in i: sid = lid ; break
							if sid != None:
								if include_version:
									requirements.append(i)
								else:
									requirements.append(i.split(sid)[0])
							else:
								requirements.append(i)
				return requirements
		#   -   commands:
		def delete(self, 
			# the path (leave None to use self.path) (param #1).
			path=None,
			# the options.
			forced=False,
			sudo=False,
			silent=False,
		):
			if path == None: path = self.path
			if silent: silent = ' 2> /dev/null'
			else: silent = ""
			if sudo: sudo = "sudo "
			else: sudo = ""
			options = " "
			if forced: 
				options = " -f "
				if Files.directory(path): options = " -fr "
			elif Files.directory(path): options = " -r "
			os.system(f"{sudo}rm{options}{path}{silent}")
		def move(self, 
			# the to path (#1).
			path=None,
			# root permission required.
			sudo=False,
			# root permission required.
			log_level=0,
		):
			return Files.move(
				# the from & to path (#1 & #2).
				self.path, path,
				# root permission required.
				sudo=sudo,
				# root permission required.
				log_level=log_level,
			)
			self.path = gfp.clean(path=path)
		def copy(self, 
			# the to path (#1).
			path=None, 
			# root permission required.
			sudo=False,
			# the active log level.
			log_level=0,
			# the exclude patterns.
			exclude=[],
			# update deleted files.
			delete=True,
		):
			return Files.copy(
				# the from & to path (#1 & #2).
				self.path, path,
				# root permission required.
				sudo=sudo,
				# the active log level.
				log_level=log_level,
				# the exclude patterns.
				exclude=exclude,
				# update deleted files.
				delete=delete,)
		def open(self, sudo=False):
			if sudo: sudo = "sudo "
			else: sudo = ""
			if OS in ["macos"]: 
				os.system(f"{sudo}open {self.path}")
			elif OS in ["linux"]: 
				os.system(f"{sudo}nautulis {self.path}")
			else: raise Exceptions.InvalidOperatingSystem(f"Unsupported operating system [{OS}].")
		def create(self, 
			#   Option 1: (creating a directory)
			#   -   boolean format:
			directory=False,
			#   Option 2: (creating any file extension)
			#   -   string format:
			data="",
			#   Options:
			#   -   integer format:
			permission=None,
			#   -   string format:
			owner=None,
			group=None,
			#   -   boolean format:
			sudo=False,
		):

			#   -   option 1:
			if directory: 
				if sudo: os.system('sudo mkdir -p '+self.path)
				else: os.system('mkdir -p '+self.path)
			
			#   -   option 2:
			elif data != None: 
				if sudo:
					f = Files.File(path='/tmp/tmp_file', data=data)
					f.save()
					os.system(f"sudo mv {f.file_path.path} {self.path}")

				else:
					Files.File(path=self.path, data=data).save()
				#with open
			
			#   -   invalid option:
			else: raise ValueError("Invalid option, either enable the [directory] boolean to create a directory, or specify [path] and [data] to create any file sort.")

			#   -   default:
			if owner != None or group != None: self.ownership.set(owner=owner, group=group, sudo=sudo)
			if permission != None: self.permission.set(permission, sudo=sudo)


			#
		def check(self, 
			#   Option 1: (creating a directory)
			#   -   boolean format:
			directory=False,
			#   Option 2: (creating any file extension)
			#   -   string format:
			data="",
			#   Options:
			#   -   integer format:
			permission=None,
			#   -   string format:
			owner=None,
			group=None,
			#   -   boolean format:
			sudo=False,
			silent=False,
			recursive=False, # for directories only (for permission & ownership check)
		):

			#   -   option 1:
			if not self.exists(sudo=sudo):
				self.create(directory=directory, data=data, permission=permission, owner=owner, group=group, sudo=sudo)
			else:
				#   -   default:
				self.ownership.check(owner=owner, group=group, sudo=sudo, silent=silent, recursive=recursive)
				self.permission.check(permission=permission, sudo=sudo, silent=silent, recursive=recursive)
			
			#
		# support default str functions.
		def split(self, path):
			return Files.Array(self.path.split(str(path)))
		def count(self, path):
			return Formats.Integer(self.path.count(str(path)))
		def replace(self, from_, to_):
			return self.path.replace(str(from_), str(to_))
		def lower(self, path):
			return self.path.lower(str(path))
		def upper(self, path):
			return self.path.upper(str(path))
		# support subscriptionable.
		def __getitem__(self, index):
			return self.path[Formats.denitialize(index)]
		def __setitem__(self, index, value):
			self.path[Formats.denitialize(index)] = str(value)
		# support "+" & "-" .
		def __add__(self, path):
			if isinstance(path, str):
				a=1
			elif isinstance(path, self.__class__):
				path = path.path
			elif not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path + path
		def __sub__(self, path):
			if isinstance(path, str):
				a=1
			elif isinstance(path, self.__class__):
				path = path.path
			elif not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path.replace(path, "")
		# support +.
		def __concat__(self, path):
			if isinstance(path, str):
				a=1
			elif isinstance(path, self.__class__):
				path = path.path
			elif not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path + path
		# support default iteration.
		def __iter__(self):
			return iter(self.path)
		# support '>=' & '>' operator.
		def __gt__(self, path):
			if not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) > len(path.path)
		def __ge__(self, path):
			if not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) >= len(path.path)
		# support '<=' & '<' operator.
		def __lt__(self, path):
			if not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) < len(path.path)
		def __le__(self, path):
			if not isinstance(path, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) <= len(path.path)
		# support '==' & '!=' operator.
		def __eq__(self, path):
			if isinstance(path, str):
				return self.path == path
			elif not isinstance(path, self.__class__):
				return False
			return self.path == path.path
		def __ne__(self, path):
			if isinstance(path, str):
				return self.path != path
			elif not isinstance(path, self.__class__):
				return True
			return self.path != path.path
		# support 'in' operator.
		def __contains__(self, path):
			if isinstance(path, (list, Files.Array)):
				for i in path:
					if i in self.path:
						return True
				return False
			else:
				return path in self.path
			#
		# int representation.
		def __repr__(self):
			return str(self)
		# str representation.
		def __str__(self):
			return str(self.path)
		# int representation.
		def __int__(self):
			return int(self.path)
		# float representation.
		def __float__(self):
			return float(self.path)
		# bool representation.
		def __bool__(self):
			if self.path in [1.0, 1, "true", "True", "TRUE", True]:
				return True
			elif self.path in [0, 0.0, "false", "False", "FALSE", False]:
				return False
			else:
				raise Exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
		# content count.
		def __len__(self):
			return len(self.path)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "FilePath"
			#
		@property
		def __name__(self):
			return self.instance()
		# support self assignment.
		def assign(self, path, load=False):
			if isinstance(path, self.__class__):
				path = path.path
			self.path = gfp.clean(path=path)
			self.ownership = self.Ownership(path=self.path, load=load)
			self.permission = self.Permission(path=self.path, load=load)
			return self
		# return raw data.
		def raw(self):
			return self.path
		#   -   objects:
		class Ownership(object):
			def __init__(self, path=None, load=False):

				# docs.
				DOCS = {
					"module":"FilePath.Ownership", 
					"initialized":False,
					"description":[], 
					"chapter": "Defaults", }

				# init.
				self.path = path
				self.owner = None
				self.group = None
				if load: 
					get = self.get()
					self.owner = get["owner"]
					self.group = get["permission"]

			#   -   info:
			def get(self, path=None):
				if path == None: path = self.path
				owner = pwd.getpwuid(os.stat(path).st_uid).pw_name
				try:
					group = grp.getgrgid(os.stat(path).st_gid).gr_name
				except KeyError: # unknown group likely from different os / machine.
					group = os.stat(path).st_gid
				except Exception as e:
					raise ValueError(f"Unable to retrieve the group of file {path}, error: {e}.")
				return owner, group
			def set(self, 
				# the permission (str) (#1).
				owner=None, 
				# the group (str) (optional) (#2).
				group=None, 
				# the path (optional) (overwrites self.path) (#3).
				path=None,
				# root permission required.
				sudo=False, 
				# recursive.
				recursive=False, 
				# silent.
				silent=False, 
			):
				if path == None: path = self.path
				if group == None:
					if OS in ["macos"]: group = "wheel"
					elif OS in ["linux"]: group = "root"
					else: raise ValueError("Unsupported operating system [{}].".format(OS))
				silent_option = ""
				if silent: silent_option = ' 2> /dev/null'
				if recursive:
					if sudo: os.system("sudo chown -R {} {} {}".format(owner+":"+group, path, silent_option))
					else: os.system("chown -R {} {}".format(owner+":"+group, path))
				else:
					if sudo: os.system("sudo chown {} {} {}".format(owner+":"+group, path, silent_option))
					else: os.system("chown {} {} {}".format(owner+":"+group, path, silent_option))
			def check(self, owner=None, group=None, sudo=False, silent=False, iterate=False, recursive=False, path=None): # combine [recursive] and [iterate] to walk all set all files in an directory and check it with the given permission.
				if path == None: path = self.path
				if group == None:
					if OS in ["macos"]: group = "wheel"
					elif OS in ["linux"]: group = "root"
					else: raise ValueError("Unsupported operating system [{}].".format(OS))
				_owner_, _group_ = self.get(path=path)
				if _owner_ != owner or _group_ != group:
					self.set(owner=owner, group=group, sudo=sudo, silent=silent, recursive=recursive, path=path)
				if recursive and iterate and Files.directory(self.path):
					for dirpath, subdirs, files in os.walk(self.path):
						for path in subdirs: 
							#print("DIRECTORY:",path)
							#print("> FULL PATH NAME:",dirpath+"/"+path)
							if path not in ["lost+found"]:
								file_path = Formats.FilePath(dirpath+"/"+path)
								file_path.ownership.check(owner=owner, group=group, sudo=sudo, silent=silent)
						for path in files: 
							#print("FILE NAME:",path)
							#print("> FULL PATH:",dirpath+"/"+path)
							file_path = Formats.FilePath(dirpath+"/"+path)
							file_path.ownership.check(owner=owner, group=group, sudo=sudo, silent=silent)                           
		class Permission(object):
			def __init__(self, path=None, load=False):

				# docs.
				DOCS = {
					"module":"FilePath.Permission", 
					"initialized":False,
					"description":[], 
					"chapter": "Defaults", }

				# defaults.
				#self.__class__.__name__ = "Permission"

			   # init.
				self.path = path
				self.permission = None
				if load: self.permission = self.get()

			#   -   info:
			def get(self, path=None):
				if path == None: path = self.path
				status = os.stat(path) 
				permission = oct(status.st_mode)[-3:]
				return permission
			def set(self, 
				# the permission (int) (#1).
				permission=None, 
				# the path (optional) (overwrites self.path) (#2).
				path=None,
				# root permission required.
				sudo=False, 
				# recursive.
				recursive=False, 
				# silent.
				silent=False, 
			): 
				if path == None: path = self.path
				silent_option = ""
				if silent: silent_option = ' 2> /dev/null'
				if recursive:
					if sudo: os.system("sudo chmod -R {} {} {}".format(permission, path, silent_option))
					else: os.system("chmod -R {} {} {}".format(permission, path, silent_option))
				else:
					if sudo: os.system("sudo chmod {} {} {}".format(permission, path, silent_option))
					else: os.system("chmod {} {} {}".format(permission, path, silent_option))
			def check(self, permission=None, sudo=False, silent=False, iterate=False, recursive=False, path=None): # combine [recursive] and [iterate] to walk all set all files in an directory and check it with the given permission.
				if path == None: path = self.path
				if self.get(path=path) != permission:
					self.set(permission=permission, sudo=sudo, silent=silent, recursive=recursive, path=path)
				if recursive and iterate and Files.directory(path):
					for dirpath, subdirs, files in os.walk(path):
						for path in subdirs: 
							#print("DIR NAME:",path)
							#print("> FULL PATH:",dirpath+"/"+path)
							if path not in ["lost+found"]:
								file_path = Formats.FilePath(dirpath+"/"+path)
								file_path.permission.check(permission=permission, sudo=sudo, silent=silent)
						for path in files: 
							#print("FILE NAME:",path)
							#print("> FULL PATH:",dirpath+"/"+path)
							file_path = Formats.FilePath(dirpath+"/"+path)
							file_path.permission.check(permission=permission, sudo=sudo, silent=silent)
		#
 
	# the string object class.
	class String(object):
		def __init__(self, 
			# the string's value (str) (#1).
			string="",
			# the path (str, FilePath) (param #2).
			path=False, 
			# load the data on initialization.
			load=False, 
			# the default array (will be created if file path does not exist).
			default=None,
		):
			
			# docs.
			DOCS = {
				"module":"String", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
		    # init.
			self.string = str(string)
			
			# path.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			if default != None and not Files.exists(self.file_path.path): self.save(array=default)
			if load: self.load()

			#
		def save(self, string=None, path=None, sudo=False):
			if string == None: string = self.string
			if path == None: path = self.file_path.path
			utils.__check_memory_only__(path)
			self.string = str(string)
			return Files.save(path, str(string), format="str", sudo=sudo)
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default, sudo=sudo)
			self.string =  Files.load(self.file_path.path, format="str", sudo=sudo)
			return self.string
		def is_numerical(self):
			for i in ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]:
				if i in self.string.lower(): return False
			return True
		def bash(self):
			a = self.string.replace('(','\(').replace(')','\)').replace("'","\'").replace(" ","\ ").replace("$","\$").replace("!","\!").replace("?","\?").replace("@","\@").replace("$","\$").replace("%","\%").replace("^","\^").replace("&","\&").replace("*","\*").replace("'","\'").replace('"','\"')       
			return a
		def identifier(self):
			x = self.string.lower().replace(' ','-')
			return x
		def variable_format(self, 
			exceptions={
				"smart_card":"smartcard", 
				"smart_cards":"smartcards" ,
				"web_server":"webserver" ,
			},
		):
			s, c = "", 0
			for i in self.string:
				try:
					n = self.string[c+1]
				except:
					n = "none"
				try:
					p = self.string[c-1]
				except:
					p = "none"
				if s != "" and i.lower() != i and str(n).lower() == str(n) and str(p).lower() == str(p):
					s += "_"
				s += i.lower()
				c += 1
			if s in list(exceptions.keys()):
				return exceptions[s]
			else:
				return s
		def class_format(self):
			s, next_capital = "", False
			for i in self.string:
				if i == "_":
					next_capital = True
				elif next_capital:
					s += i.upper()
				else:
					s += i
			return s
		def capitalized_scentence(self):
			x = self.string.split(" ")
			cap = [y.capitalize() for y in x]
			return " ".join(cap)
		def capitalized_word(self):
			try:
				new = self.string[0].upper()
				c = 0
				for i in self.string:
					if c > 0: new += i
					c += 1
				return new
			except IndexError: return self.string
		def generate(self, 
			# the length of the generated string.
			length=6, 
			# include digits.
			digits=False, 
			# include capital letters.
			capitalize=False, 
			# include special characters.
			special=False,
		):
			charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
			if capitalize:
				for i in  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]: charset.append(i.upper())
			if digits: digits = ["1","2","3","4","5","6","7","8","9","0"]
			else: digits = []
			if special: special = ["!", "?", "&", "#","@", "*"]
			else: special = []
			s = ""
			for i in range(length):
				if len(digits) > 0 and random.randrange(1,101) <= 40:
					s += digits[random.randrange(0, len(digits))]
				elif len(special) > 0 and random.randrange(1,101) <= 10:
					s += special[random.randrange(0, len(special))]
				else:
					s += charset[random.randrange(0, len(charset))]
			return s
			#
		# iterate a string (backwards) to check the first occurency of a specified charset.
		def first_occurence(self, charset=[" ", "\n"], reversed=False, string=None):
			if string == None: string = self.string
			if reversed:
				c, space_newline_id = len(string)-1, ""
				for _ in string:
					char = string[c]
					if char in charset:
						a = 0
						for i in charset:
							if i == char: return i
					c -= 1
				return None
			else:
				c, space_newline_id = 0, ""
				for _ in string:
					char = string[c]
					if char in charset:
						a = 0
						for i in charset:
							if i == char: return i
					c += 1
				return None
		# splice a string into before/after by a first occurence.
		# if include is True and both include_before and inluce_after are False it includes at before.
		def before_after_first_occurence(self, slicer=" ", include=True, include_before=False, include_after=False, string=None): 
			if isinstance(slicer, list):
				first = self.first_occurence(charset=slicer, string=string)
				return self.before_after_first_occurence(slicer=first, include=include, include_before=include_before, include_after=include_after, string=string)
			else:
				if string == None: string = self.string
				before, after, slice_count, slices, _last_ = "", "", string.count(slicer), 0, ""
				for char in string:
					if len(_last_) >= len(slicer): _last_ = _last_[1:]
					_last_ += char
					if _last_ == slicer: 
						slices += 1
						if include:
							if slices != slice_count or include_before:
								before += char
							elif include_after:
								after += char
							else:
								before += char
					elif slices > 0:
						after += char
					else: 
						before += char
				return before, after
		# splice a string into before/selected/after by a first occurence.
		def before_selected_after_first_occurence(self, slicer=" ", string=None):
			if string == None: string = self.string
			before, selected, after, slice_count, open, _last_ = "", "", "", string.count(slicer), False, ""
			selected_sliced_count = 0
			for char in string:
				if isinstance(slicer, str) and len(_last_) >= len(slicer): _last_ = _last_[1:]
				elif isinstance(slicer, list) and len(_last_) >= len(slicer[selected_sliced_count]): _last_ = _last_[1:]
				_last_ += char
				if (isinstance(slicer, str) and _last_ == slicer) or (isinstance(slicer, list) and _last_ == slicer[selected_sliced_count]): 
					selected_sliced_count += 1
					selected += char
					if open: open = False
					else: open = True
				elif open:
					after += char
				else: 
					before += char
			return before, selected, after
		# splice a string into before/after by a last occurence.
		# if include is True and both include_before and inluce_after are False it includes at before.
		def before_after_last_occurence(self, slicer=" ", include=True, include_before=False, include_after=False, string=None): 
			if string == None: string = self.string
			before, after, slice_count, slices, _last_ = "", "", string.count(slicer), 0, ""
			for char in string:
				if len(_last_) >= len(slicer): _last_ = _last_[1:]
				_last_ += char
				if _last_ == slicer: 
					slices += 1
					if include:
						if slices != slice_count or include_before:
							before += char
						elif include_after:
							after += char
						else:
							before += char
				elif slices == slice_count:
					after += char
				else: 
					before += char
			return before, after
		# splice a string into before/selected/after by a last occurence.
		def before_selected_after_last_occurence(self, slicer=" ", string=None):
			if string == None: string = self.string
			before, selected, after, slice_count, slices, _last_ = "", "", "", string.count(slicer), 0, ""
			for char in string:
				if len(_last_) >= len(slicer): _last_ = _last_[1:]
				_last_ += char
				if _last_ == slicer: 
					slices += 1
					selected += char
				elif slices == slice_count:
					after += char
				else: 
					before += char
			return before, selected, after
		# get the first text between an 2 string identifiers [start,end] by depth.
		# identifiers must be parameter number 1.
		def between(self, identifiers=["{","}"], depth=1, include=True, string=None):

			# vars.
			if string == None: string = self.string
			keep_last = [len(identifiers[0]), len(identifiers[1])]
			last = ["", ""]
			unadded = ""
			s, open, opened, first_open = "", 0, False, False

			# iterate.
			for i in string:

				# set last & unadded.
				unadded += i
				last[0] += i
				last[1] += i
				if len(last[0]) > keep_last[0]:
					last[0] = str(String(last[0]).remove_first(1))
				if len(last[1]) > keep_last[1]:
					last[1] = str(String(last[1]).remove_first(1))

				# check ids.
				if last[0] == identifiers[0]:
					open += 1
					first_open = True
				elif last[1] == identifiers[1]:
					open -= 1
				if open >= depth:
					if include or open == depth: 
						if include and first_open:
							s += identifiers[0]
							unadded = ""
							first_open = False
						else:
							s += unadded
							unadded = ""
					opened = True
				if opened and open < depth:
					if include: 
						s += unadded
						unadded = ""
					break

			# remainders.
			if unadded != "" and opened and open < depth:
				if include: 
					s += unadded
					unadded = ""
				
			# handler.
			return Formats.String(s)

			#
		# get the text with betwee & replace the inside between str with a new str.
		def replace_between(self, 
			# the between identifiers (list) (#1).
			identifiers=["{","}"], 
			# the new string (str) (#2).
			to="", 
			# the identifiers depth.
			depth=1, 
			# the optional string.
			string=None,
		):
			update = False
			if string == None: 
				update = True
				string = self.string
			sliced = self.between(identifiers, depth=depth, include=True, string=string)
			string = string.replace(str(sliced), to)
			if update:
				self.string = string
			return string

			#
		# increase version.
		def increase_version(self):

			# version 2.
			#
			path = "/tmp/increase_version"
			Files.save(path, f"""version='{self.string}"""+"""' && echo $version | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}'""")
			return subprocess.check_output([f"bash", path]).decode().replace("\n","")

			# version 1.
			#
			old_version = self.string
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
		# slice dict from string.
		# get the first {} from the string by depth.
		def slice_dict(self, depth=1):
			return self.between(["{", "}"], depth=depth)
		# slice array from string.
		# get the first [] from the string by depth.
		def slice_array(self, depth=1):
			return self.between(["[", "]"], depth=depth)
		# slice tuple from string.
		# get the first () from the string by depth.
		def slice_tuple(self, depth=1):
			return self.between(["(", ")"], depth=depth)
		# iterate chars.
		# > for charcount, char in String.iterate_chars()
		def iterate_chars(self):
			charcount, items = 0, []
			for char in self.string:
				items.append([charcount, char])
				charcount += 1
			return items
		def iterate_characters(self):
			return self.iterate_chars()
		# iterate lines.
		# > for linecount, line in String.iterate_lines()
		def iterate_lines(self):
			linecount, items = 0, []
			for line in self.string.split("\n"):
				items.append([linecount, line])
				linecount += 1
			return items
		# slice indent from string.
		# get the content bewteen the \n{indent}
		def indent(self, indent=4):
			s = ""
			for i in range(indent): s += " "
			return s
		def line_indent(self, line=""):
			# get line indent.
			line = line.replace("	", "    ")
			if len(line) > 0 and " " in line:
				line_indent = 0
				for c in line:
					if c in [" "]: line_indent += 1
					else: break
			else: line_indent = 0
			return Formats.Integer(line_indent)
		def slice_indent(self, indent=4, depth=1, string=None, remove_indent=True):
			if string == None: string = self.string
			string = string.replace("	", "    ")
			s, open, opened, d = "", 0, False, 0
			for line in string.split("\n"):
				# get line indent.
				if len(line) > 0 and " " in line:
					line_indent = 0
					for c in line:
						if c in [" "]: line_indent += 1
						else: break
				else: line_indent = 0
				# check indent match.
				if (not opened and line_indent == indent) or (opened and line_indent >= indent):
					if d >= depth:
						if remove_indent:
							s += line[indent:]+"\n"
						else:
							s += line+"\n"
						opened = True
					#elif len(line) > 0 and not opened and line_indent == indent:
					#	d += 1
				elif len(line) > 0 and line_indent <= indent:
					if opened:
						break
					else:
						d += 1
			return s
		
		# get the first / last n characters of the string.
		def first(self, count):
			if isinstance(count, (int, float, Integer)):
				count = int(count)
			else:
				count = len(count)
			return self.string[:count]
		def last(self, count):
			if isinstance(count, (int, float, Integer)):
				count = int(count)
			else:
				count = len(count)
			if len(self.string) >= count:
				return self.string[count:]
			else:
				return None
			#
		
		# remove first / last n characters of the string.
		def remove_first(self, count):
			if isinstance(count, (int, float, Integer)):
				count = int(count)
			else:
				count = len(count)
			removed = self.first(count)
			self.string = self.string[count:]
			return self.string
		def remove_last(self, count):
			if isinstance(count, (int, float, Integer)):
				count = int(count)
			else:
				count = len(count)
			removed = self.last(count)
			self.string = self.string[:-count]
			return self.string
			#

		# support default str functions.
		def split(self, string):
			if isinstance(string, (list, Array)):
				if isinstance(string, Array): array = string.array
				else: array = string
				new, last, next_start = [], "", None
				for i in self.string:
					last += i
					newslice = False
					#l_next_start = None
					for test in array:
						if test in last:
							if str(last[-len(test):]) == str(test):
								#l_next_start = last[:-len(test)]
								last = last[:-len(test)]
								newslice = True
								break
					if newslice:
						new.append(last)
						last = ""
						#if next_start == None: new.append(last)
						#elif include: 
						#	new.append(next_start+last)
						#	next_start = None
					#if include and l_next_start != None:
					#	next_start = l_next_start
				if last != "":
					new.append(last)
				return new
			else:
				return Files.Array(self.string.split(str(string)))
		def count(self, string):
			return Formats.Integer(self.string.count(str(string)))
		def replace(self, from_, to_):
			return self.string.replace(str(from_), str(to_))
		def lower(self, string):
			return self.string.lower(str(string))
		def upper(self, string):
			return self.string.upper(str(string))
		# support "+" & "-" .
		def __add__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			return self.string + string
		def __iadd__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			self.string = self.string + string
			return self
		def __sub__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			return self.string.replace(string, "")
		def __isub__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			self.string = self.string.replace(string, "")
			return self
		# support subscriptionable.
		def __getitem__(self, index):
			return self.string[Formats.denitialize(index)]
		def __setitem__(self, index, value):
			self.string[Formats.denitialize(index)] = str(value)
		# support default iteration.
		def __iter__(self):
			return iter(self.string)
		# support '>=' & '>' operator.
		def __gt__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) > len(string)
		def __ge__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) >= len(string)
		# support '<=' & '<' operator.
		def __lt__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) < len(string)
		def __le__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) <= len(string)
		# support '==' & '!=' operator.
		def __eq__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				return False
			return self.string == string
		def __ne__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				return True
			return self.string != string
		# support +.
		def __concat__(self, string):
			if isinstance(string, (str)):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not concat object {self.__class__} & {string.__class__}.")
			return self.string + string
		# support 'in' operator.
		def __contains__(self, string):
			if isinstance(string, (list, Files.Array)):
				for i in string:
					if str(i) in str(self.string):
						return True
				return False
			else:
				return str(string) in str(self.string)
			#
		# representation.
		def __repr__(self):
			return str(self)
		# str representation.
		def __str__(self):
			return str(self.string)
		# int representation.
		def __int__(self):
			return int(self.string)
		# float representation.
		def __float__(self):
			return float(self.string)
		# bool representation.
		def __bool__(self):
			return len(self.string) > 0
			#if self.string in [1.0, 1, "true", "True", "TRUE", True]:
			#	return True
			#elif self.string in [0, 0.0, "false", "False", "FALSE", False]:
			#	return False
			#else:
			#	raise Exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
		# content count.
		def __len__(self):
			return len(self.string)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		#   # object instance.
		def instance(self):
			return "String"
			#
		@property
		def __name__(self):
			return self.instance()
		# support self assignment.
		def assign(self, string):
			if isinstance(string, (int, float)):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {string.__class__}.")
			self.string = str(string)
			return self
		# return raw data.
		def raw(self):
			return self.str
		#

	# the boolean object class.
	class Boolean(object):
		def __init__(self, 
			# the boolean's value (bool) (#1).
			boolean=False,
			# the path (str, FilePath) (param #2).
			path=False, 
			# load the data on initialization.
			load=False, 
			# the default array (will be created if file path does not exist).
			default=None,
		):

			# docs.
			DOCS = {
				"module":"Boolean", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# check self instance.
			if isinstance(boolean, Formats.Boolean):
				boolean = boolean.bool

		    # init.
			self.bool = boolean
			if self.bool in ["true", "True", "TRUE", True]: self.bool = True
			else: self.bool = False

			# path.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			if default != None and not Files.exists(self.file_path.path): self.save(array=default)
			if load: self.load()

			#
		def save(self, bool=None, path=None, sudo=False):
			if bool != None: bool = self.bool
			if path == None: path = self.file_path.path
			utils.__check_memory_only__(path)
			self.bool = bool
			return Files.save(path, str(bool), format="str", sudo=sudo)
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default, sudo=sudo)
			self.bool =  Files.load(self.file_path.path, format="str", sudo=sudo)
			return self.bool
		def string(self, true="True", false="False"):
			if self.bool:
				return true
			else:
				return false
		# native support.
		def __index__(self):
			return int(self)
		# support '==' & '!=' operator.
		def __eq__(self, boolean):
			if isinstance(boolean, bool):
				return self.bool == boolean
			elif not isinstance(boolean, self.__class__):
				return False
			return self.bool == boolean.bool
		def __ne__(self, boolean):
			if isinstance(boolean, bool):
				return self.bool != boolean
			elif not isinstance(boolean, self.__class__):
				return True
			return self.bool != boolean.bool
		# support default iteration.
		def __iter__(self):
			return iter(str(self.bool))
		# support 'in' operator.
		def __contains__(self, string):
			return string in str(self.bool)
			#
		# representation.
		def __repr__(self):
			return str(self)
			#
		# str representation.
		def __str__(self):
			return str(self.bool)
		# int representation.
		def __int__(self):
			if self.bool:
				return 1
			else:
				return 0
		# float representation.
		def __float__(self):
			if self.bool:
				return 1.0
			else:
				return 0.0
		# bool representation.
		def __bool__(self):
			return self.bool
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Boolean"
			#
		@property
		def __name__(self):
			return self.instance()
		# support self assignment.
		def assign(self, boolean):
			if isinstance(boolean, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				boolean = boolean.bool
			elif not isinstance(boolean, self.__class__):
				raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {boolean.__class__}.")
			self.bool = boolean
			return self
		# return raw data.
		def raw(self):
			return self.bool
		#

	# the integer object class.
	class Integer(object):
		def __init__(self, 
			# the integers value (int, float) (param #1).
			value=0, 
			# the path (str, FilePath) (param #2).
			path=False, 
			# the integer format (str) (param #3).
			format="auto",
			# load the data on initialization.
			load=False, 
			# the default array (will be created if file path does not exist).
			default=None,
		):
			
			# docs.
			DOCS = {
				"module":"Integer", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# check self instance.
			if isinstance(value, Formats.Integer):
				if "." in str(value):
					value = value.float
				else:
					value = value.int

			# init.
			if "." in str(value):
				self.format = "float"
				self.value = float(value)
			else:
				self.format = "int"
				self.value = int(value)
			self.int = int(value)
			self.float = float(value)

			# path.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			if default != None and not Files.exists(self.file_path.path): self.save(array=default)
			if load: self.load()

			#
		def save(self, data=None, path=None, sudo=False):
			if data != None: data = self.raw()
			if path == None: path = self.file_path.path
			utils.__check_memory_only__(path)
			if data != self.raw():
				self.assign(data)
			return Files.save(path, str(data), format="str", sudo=sudo)
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default, sudo=sudo)
			data =  Files.load(self.file_path.path, format="str", sudo=sudo)
			self.assign(data)
			return data
		def increase_version(self):

			# version 1.
			#
			old_version = self.value
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
		def round(self, decimals):
			"""
			Returns a value rounded down to a specific number of decimal places.
			"""
			if not isinstance(decimals, int):
				raise TypeError("decimal places must be an integer")
			else:  return round(self.value, decimals)
		def round_down(self, decimals):
			"""
			Returns a value rounded down to a specific number of decimal places.
			"""
			if not isinstance(decimals, int):
				raise TypeError("decimal places must be an integer")
			elif decimals < 0:
				raise ValueError("decimal places has to be 0 or more")
			elif decimals == 0:
				return math.ceil(self.value)
			factor = 10 ** decimals
			return math.floor(self.value * factor) / factor

			#
			
		def generate(self, length=6):
			return utils.generate.pincode(length=length)
			#
		# int format.
		def __index__(self):
			return self.value
		# support "+, -, *, %, @, /, //, **" .
		def __add__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		def __sub__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not sub object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value - value)
		def __iadd__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {value.__class__}.")
			self.value += value
			return self
		def __isub__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not sub object {self.__class__} & {value.__class__}.")
			self.value -= value
			return self
		def __mod__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mod object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value % value)
		def __mul__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value * value)
		def __pow__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value ** value)
		def __div__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value / value)
		def __truediv__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value / value)
		def __floordiv__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value // value)
		def __concat__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		# support "+=" & "-=".
		def __pos__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		def __matmul__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not matmul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value @ value)
		# support //.
		#def __floordiv__(a, b)
		#	return a // b.
		# support default iteration.
		def __iter__(self):
			return iter(str(self.value))
		# support '>=' & '>' operator.
		def __gt__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value > integer
		def __ge__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value >= integer
		# support '<=' & '<' operator.
		def __lt__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value < integer
		def __le__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value <= integer
		# support '==' & '!=' operator.
		def __eq__(self, integer):
			if isinstance(integer, (int,float)):
				return self.value == integer
			elif not isinstance(integer, self.__class__):
				return False
			return self.value == integer.value
		def __ne__(self, integer):
			if isinstance(integer, (int,float)):
				return self.value != integer
			elif not isinstance(integer, self.__class__):
				return True
			return self.value != integer.value
		# support 'in' operator.
		def __contains__(self, integer):
			if isinstance(integer, (list, Files.Array)):
				for i in integer:
					if str(integer) in str(self.value):
						return True
				return False
			else:
				return str(value) in str(self.value)
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
			if self.format == "float":
				return self.float
			else:
				return float(self.int)
		# bool representation.
		def __bool__(self):
			if self.value in [1.0, 1]:
				return True
			elif self.value in [0, 0.0]:
				return False
			else:
				raise Exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
		# content count.
		def __len__(self):
			return len(str(self.value))
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Integer"
			#
		# support self assignment.
		def assign(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise Exceptions.FormatError(f"Can not assign object {self.__class__} & {value.__class__}.")
			self.value = value
			return self
		# return raw data.
		def raw(self):
			return self.value
		#

	# the date object class.
	class Date(object):
		def __init__(self, 
			# 
			# Leave all parameters None to initialize a Date() object with the current date.
			# Pass another Date object, str repr or timestamp in seconds to initialize a Date object from that timestamp.
			#
			# the date parameter (str, int, Date) (optional) (#1).
			date=None,
			# the format for the date (leave None to parse the date format automatically) (str).
			format=None,
		):

			# docs.
			DOCS = {
				"module":"Date", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# formats.
			self.default_format = "%d-%m-%y %H:%M:%S" # is Date() str repr
			self.seconds_format = '%S'
			self.minute_format = '%M'
			self.hour_format = '%H'
			self.day_format = '%d'
			self.day_name_format = '%a'
			self.week_format = '%V'
			self.month_format = '%m'
			self.month_name_format = '%h'
			self.year_format = '%Y'
			self.date_format = '%d-%m-%y'
			self.timestamp_format = '%d-%m-%y %H:%M'
			self.shell_timestamp_format = '%d_%m_%y-%H_%M'
			self.seconds_timestamp_format = '%d-%m-%y %H:%M:%S'
			self.shell_seconds_timestamp_format = '%d_%m_%y-%H_%M_%S'
			self.formats = [
				self.shell_seconds_timestamp_format,
				self.seconds_timestamp_format,
				self.shell_timestamp_format,
				self.timestamp_format,
				self.date_format,
				self.year_format,
				self.seconds_format,
				self.minute_format,
				self.hour_format,
				self.day_format,
				self.day_name_format,
				self.week_format,
				self.month_format,
				self.month_name_format,
			]

			# assign
			if date == None:
				self.initialize()
			else:
				self.assign(date, format=format)

			#
		def initialize(self, 
			# 
			# Leave all parameters None to initialize a Date() object with the current date.
			# 
			# Initialize a future / previous date.
			#   option 1:
			#     specify the timestamp to initialize a previous / future date (format required).
			timestamp=None, 
			#     the timestamp format (leave None to parse).
			format=None,
			#   options 2:
			#     initialize by seconds.
			seconds=None,
			# 	option 3:
			#     define the datetime object.
			datetime_obj=None,
		):

			# defaults.
			#self.__class__.__name__ = "Date"

			# by datetime_obj
			if datetime_obj != None:
				seconds = time.mktime(datetime_obj.timetuple())
				today = datetime.fromtimestamp(float(seconds))

			# by timestamp & format.
			elif timestamp != None:
				if format == None: 
					format = self.parse_format(timestamp)
					if format == None: 
						raise Exceptions.ParseError(f"Unable to parse the date format from timestamp [{timestamp}]. Find out what the required format is and request a commit that updates the Date().parse_format() function with the required format (https://github.com/vandenberghinc/dev0s/).")
				seconds = time.mktime(datetime.strptime(str(timestamp), str(format)).timetuple())
				today = datetime.fromtimestamp(float(seconds))

			# by seconds.
			elif seconds != None:
				today = datetime.fromtimestamp(float(seconds))

			# by current.
			else:
				today = datetime.today()

			# attributes.
			self.seconds = str(today.strftime(self.seconds_format))
			self.minute =  str(today.strftime(self.minute_format))
			self.hour =  str(today.strftime(self.hour_format))
			self.day =  str(today.strftime(self.day_format))
			self.day_name =  str(today.strftime(self.day_name_format))
			self.week =  str(today.strftime(self.week_format))
			self.month =  str(today.strftime(self.month_format))
			self.month_name = str(today.strftime(self.month_name_format))
			self.year =  str(today.strftime(self.year_format))
			self.date =  str(today.strftime(self.date_format))
			self.timestamp =  str(today.strftime(self.timestamp_format))
			self.shell_timestamp =  str(today.strftime(self.shell_timestamp_format))
			self.seconds_timestamp =  str(today.strftime(self.seconds_timestamp_format))
			self.shell_seconds_timestamp =  str(today.strftime(self.shell_seconds_timestamp_format))
			self.time = self.hour + ":" + self.minute
			return self
		def compare(self, comparison=None, current=None, format=None):
			if current == None: current = str(self)
			if isinstance(comparison, Formats.Date):
				comparison = str(comparison)
			if isinstance(current, Formats.Date):
				current = str(current)
			if format == None: 
				comparison_format = self.parse_format(comparison)
				if comparison_format == None: 
					raise Exceptions.ParseError(f"Unable to parse the date format from comparison [{comparison}].")
			else:
				comparison_format = format
			comparison = self.to_seconds(comparison, format=comparison_format)
			if format == None: 
				current_format = self.parse_format(current)
				if current_format == None: 
					raise Exceptions.ParseError(f"Unable to parse the date format from current [{current}].")
			else:
				current_format = format
			current = self.to_seconds(current, format=current_format)
			if comparison >= current:
				return "future"
			elif comparison <= current:
				return "past"
			elif comparison == current:
				return "present"
			else:
				raise ValueError(f"Unexpected error, comparison seconds: {comparison} current seconds: {current}.")
		def increase(self, string=None, weeks=0, days=0, hours=0, minutes=0, seconds=0, format=None):
			if string == None: string = str(self)
			if isinstance(string, Formats.Date):
				string = str(string)
			if format == None: 
				format = self.parse_format(string)
				if format == None: 
					raise Exceptions.ParseError(f"Unable to parse the date format from string [{string}].")
			seconds += 60*minutes
			seconds += 3600*hours
			seconds += 3600*24*days
			seconds += 3600*24*7*weeks
			s = self.to_seconds(string, format=format)
			s += seconds
			return self.from_seconds(s, format=format)
		def decrease(self, string=None, weeks=0, days=0, hours=0, minutes=0, seconds=0, format=None):
			if string == None: string = str(self)
			if isinstance(string, Formats.Date):
				string = str(string)
			if format == None: 
				format = self.parse_format(string)
				if format == None: 
					raise Exceptions.ParseError(f"Unable to parse the date format from string [{string}].")
			seconds += 60*minutes
			seconds += 3600*hours
			seconds += 3600*24*days
			seconds += 3600*24*7*weeks
			s = self.to_seconds(string, format=format)
			s -= seconds
			return self.from_seconds(s, format=format)
		def to_seconds(self, string=None, format=None):
			if string == None: string = str(self)
			if isinstance(string, Formats.Date):
				string = str(string)
			if format == None:
				format = self.default_format
			return time.mktime(datetime.strptime(str(string), str(format)).timetuple())
			#
		def from_seconds(self, seconds, format=None):
			if isinstance(seconds, (str,String,Integer)):
				seconds = float(seconds)
			if format == None:
				format = self.default_format
			return Date().initialize(timestamp=datetime.fromtimestamp(float(seconds)).strftime(format))
			#
		def convert(self, string=None, datetime_obj=None, input=None, output="%Y%m%d"):
			if datetime_obj == None:
				if string == None: string = str(self)
				if isinstance(string, Formats.Date):
					string = str(string)
				if input == None:
					input = self.parse_format(string)
				datetime_obj = datetime.strptime(str(string), str(input))
			return datetime_obj.strftime(str(output))
		def parse_format(self, string):
			if isinstance(string, Formats.Date):
				return self.default_format
			elif isinstance(string, (int,float,Integer)):
				return self.seconds_format
			formats = []
			if "-" in str(string):
				formats += [
					self.shell_seconds_timestamp_format,
					self.seconds_timestamp_format,
					self.shell_timestamp_format,
					self.timestamp_format,
					self.date_format,
				]
			else:
				formats += [
					self.year_format,
					self.seconds_format,
					#self.minute_format,
					#self.hour_format,
					#self.day_format,
					#self.day_name_format,
					#self.week_format,
					#self.month_format,
					#self.month_name_format,
				]
			# plus some custom formats.
			formats += [
				"%d-%m-%y %H:%M.%S", # old default.
				"%Y-%m-%d %H:%M:%S", # stock market
				"%d-%m-%Y", # dd-mm-yyyy.
				"%d-%m-%y %H:%M:%S", # dd-mm-yy hh:mm:ss.
				"%d-%m-%Y %H:%M:%S", # dd-mm-yyyy hh:mm:ss.
				"%Y-%m-%dT%H:%M:%SZ" # rfc-3339.
			]
			for format in formats:
				try:
					datetime.strptime(str(string), str(format))
					return format
				except Exception as e: 
					a=1
			return None
		def assign(self, string, format=None):
			if isinstance(string, Formats.Date):
				self = string
				return self
			else:
				if format == None:
					format = self.parse_format(string)
				if format == None:
					raise Exceptions.ParseError(f"Unable to parse a Date() object from string [{string}].")
				if format == self.seconds_format:
					self.initialize(seconds=float(string))
				else:
					self.initialize(timestamp=string, format=format)
				return self

		# normalize seconds to 10s or 1m etc.
		def normalize_seconds(self, seconds:(int,float)):
			if seconds < 0:
				raise ValueError("Can not normalize negative seconds.")
			if seconds < 0.01:
				return f'{int(seconds*1000)}ms'
			elif seconds <= 60:
				return f'{int(seconds)}s'
			elif seconds <= 60*60:
				return f'{round(seconds/60,1)}m'
			elif seconds <= 60*60*24:
				return f'{round(seconds/(60*60),1)}h'
			elif seconds <= 60*60*24*30:
				return f'{round(seconds/(60*60*24),1)}d'
			elif seconds <= 60*60*24*30*12:
				return f'{round(seconds/(60*60*24*30),1)}m'
			else:
				return f'{round(seconds/(60*60*24*30*12),1)}y'

		# convert to datetime object.
		def datetime(self, timestamp=None):

			# set defaults.
			if timestamp == None: timestamp = str(self)

			# parse format.
			seconds = isinstance(timestamp, (int, float))

			# by timestamp & format.
			if not seconds:
				format = self.parse_format(timestamp)
				if format == None: 
					raise Exceptions.ParseError(f"Unable to parse the date format from timestamp [{timestamp}]. Find out what the required format is and request a commit that updates the Date().parse_format() function with the required format (https://github.com/vandenberghinc/dev0s/).")
				seconds = time.mktime(datetime.strptime(str(timestamp), str(format)).timetuple())
				return datetime.fromtimestamp(float(seconds))

			# by seconds.
			else:
				return datetime.fromtimestamp(float(seconds))

		# convert to rfc_3339 format.
		def rfc_3339(self, timestamp=None):

			# convert.
			return self.datetime(timestamp=timestamp).isoformat('T') + "Z"

			#

		# convert to utc format.
		def utc(self, timestamp=None):

			# convert.
			return self.datetime(timestamp=timestamp).replace(tzinfo=timezone.utc)

			#

		# support default iteration.
		def __iter__(self):
			return iter([self.year, self.month, self.week, self.hour, self.minutes, self.seconds])
		# support '>=' & '>' operator.
		def __gt__(self, date):
			if not isinstance(date, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return float(self) > float(date)
		def __ge__(self, date):
			if not isinstance(date, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return float(self) >= float(date)
		# support '<=' & '<' operator.
		def __lt__(self, date):
			if not isinstance(date, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return float(self) < float(date)
		def __le__(self, date):
			if not isinstance(date, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return float(self) <= float(date)
		# support '==' & '!=' operator.
		def __eq__(self, date):
			if not isinstance(date, self.__class__):
				return False
			return float(self) == float(date)
		def __ne__(self, date):
			if not isinstance(date, self.__class__):
				return True
			return float(self) != float(date)
		# support 'in' operator.
		def __contains__(self, string):
			if isinstance(string, (list, Files.Array)):
				for i in string:
					if i in str(self):
						return True
				return False
			else:
				return string in str(self)
		# support "+", -, =-, =+" .
		def __add__(self, add):
			if isinstance(add, (int,float)):
				add = float(add)
			elif isinstance(add, self.__class__):
				add = add.to_seconds()
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {add.__class__}.")
			return Date().initialize(seconds=self.to_seconds() + add)
		def __iadd__(self, add):
			if isinstance(add, (int,float)):
				add = float(add)
			elif isinstance(add, self.__class__):
				add = add.to_seconds()
			elif not isinstance(add, self.__class__):
				raise Exceptions.FormatError(f"Can not iadd object {self.__class__} & {add.__class__}.")
			self = Date().initialize(seconds=self.to_seconds() + add)
			return self
		def __sub__(self, add):
			if isinstance(add, (int,float)):
				add = float(add)
			elif isinstance(add, self.__class__):
				add = add.to_seconds()
			elif not isinstance(add, self.__class__):
				raise Exceptions.FormatError(f"Can not sub object {self.__class__} & {add.__class__}.")
			return Date().initialize(seconds=self.to_seconds() - add)
		def __isub__(self, add):
			if isinstance(add, (int,float)):
				add = float(add)
			elif isinstance(add, self.__class__):
				add = add.to_seconds()
			elif not isinstance(add, self.__class__):
				raise Exceptions.FormatError(f"Can not isub object {self.__class__} & {add.__class__}.")
			self = Date().initialize(seconds=self.to_seconds() - add)
			return self
		# support +.
		def __concat__(self, add):
			if isinstance(add, (int,float)):
				add = float(add)
			elif isinstance(add, self.__class__):
				add = add.to_seconds()
			elif not isinstance(add, self.__class__):
				raise Exceptions.FormatError(f"Can not sub object {self.__class__} & {add.__class__}.")
			return Date().initialize(seconds=self.to_seconds() - add)
		# representation.
		def __repr__(self):
			return str(self)
			#
		# int representation.
		def __int__(self):
			return int(self.to_seconds(self.seconds_timestamp, format=self.seconds_timestamp_format))
		# float representation.
		def __float__(self):
			return float(self.to_seconds(self.seconds_timestamp, format=self.seconds_timestamp_format))
		# str representation.
		def __str__(self):
			return str(self.seconds_timestamp)
		# content count.
		def __len__(self):
			return len(self.seconds_timestamp)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Date"
			#
		#

# the files class.
class Files():
	#
	# functions.
	def join(path=None, name=None, type=""):
		if type not in ["", "/"] and "." not in type:
			type = "." + type
		path = str(path)
		if os.path.exists(path) and Files.directory(path) and path[len(path)-1] != "/": path += '/'
		return gfp.clean("{}{}{}".format(path, name, type), remove_double_slash=True, remove_last_slash=False)
	def load(path, data="not to be used", format="str", raw=False, sudo=False): # keep data as second param to prevent save load errors.
		# correct format.
		if format in [str, String, "String", "string", "file"]: format = "str"
		if format in [dict, Dictionary, "Dictionary", "dict", "array", "Array"]: format = "json"
		if format in [bytes, Bytes, "Bytes"]: format = "bytes"
		#format = str(format)
		# match format.
		path = str(path)
		data = None

		# sudo.
		if sudo:
			data = utils.__execute__(["sudo", "cat", path])
			if "No such file or directory" in data: raise FileNotFoundError(f"File [{path}] does not exist.")

		# proceed.
		if format == "str":
			if not sudo:
				file = open(path,mode='rb')
				data = file.read().decode()
				file.close()
		elif format == "json":
			if not sudo:
				try: 
					with open(path, 'r+') as json_file:
						data = json.load(json_file)
				except json.decoder.JSONDecodeError as e:
					try:
						data = ast.literal_eval(Files.load(path=path, format="str", raw=True, sudo=sudo))
					except:
						e = f"Unable to decode file [{path}] (sudo: {sudo}), error: {e}."
						raise Exceptions.JSONDecodeError(e)

			else:
				try: 
					data = json.loads(data)
				except json.decoder.JSONDecodeError as e:
					try:
						data = ast.literal_eval(Files.load(path=path, format="str", raw=True, sudo=sudo))
					except:
						e = f"Unable to decode file [{path}] (sudo: {sudo}), error: {e}."
						raise Exceptions.JSONDecodeError(e)
		elif format == "bytes":
			if not sudo:
				with open(path, "rb") as file:
					data = file.read()
			else:
				data = data.encode()
		else: raise ValueError(f"Unknown format {format}.")
		if raw: return data
		else: return Formats.initialize(data)
	def save(
		# the path (str) (#1).
		path, 
		# the data (str, dict, list) (#2).
		data, 
		# the file format, options: [str, bytes, json].
		format="str", 
		# root permission required.
		sudo=False, 
		# json options.
		indent=4, 
		ensure_ascii=False,
		# create backups.
		backups=False,
		# warning: safe True keeps infinitely trying to save the doc when an KeyboardInterrupt is raised by the user.
		safe=True,
		# system functions.
		__loader__=None,
		__checks__=True,
		__keyboard_interrupt__=False,
		__attempt__=1,
		__real_path__=None,
	):
		if __checks__:
			# correct format.
			if format in [str, String, "String", "string", "file"]: format = "str"
			if format in [dict, Dictionary, "Dictionary", "dict", "array"]: format = "json"
			if format in [bytes, Bytes, "Bytes"]: format = "bytes"
			#format = str(format)
			# match format.
			path = gfp.clean(str(path), remove_double_slash=True, remove_last_slash=False)
			if sudo:
				__real_path__ = str(path)
				tmp_path = path = f"/tmp/{String().generate(length=12)}"
		data = Formats.denitialize(data)
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		path = str(path)
		if format == "str":
			file = open(path, "w+") 
			file.write(data)
			file.close()
		elif format == "json":
			if __checks__:
				try:
					test = json.dumps(data)
				except:
					raise Exceptions.JSONDecodeError(f"Unable to dump expected json data: {data}")
			try:
				with open(path, 'w+') as json_file:
					json.dump(data, json_file, ensure_ascii=ensure_ascii, indent=indent)
			except PermissionError:
				with open(path, 'w') as json_file:
					json.dump(data, json_file, ensure_ascii=ensure_ascii, indent=indent)
			except KeyboardInterrupt as e:
				if __loader__ == None:
					__loader__ = console.Loader(f"&RED&Do not interrupt!&END& Saving file [{path}] (attempt: {__attempt__}).")
				if __attempt__ >= 100:
					__loader__.stop(success=False)
					raise KeyboardInterrupt(e)
				return Files.save(
					path, data,
					format=format,
					sudo=sudo,
					indent=indent,
					ensure_ascii=ensure_ascii,
					backups=False,
					safe=safe,
					__loader__=__loader__,
					__checks__=False,
					__keyboard_interrupt__=str(e),
					__attempt__=__attempt__+1,
					__real_path__=__real_path__,)
		elif format == "bytes":
			with open(path, "wb") as file:
				file.write(data)
		else: raise ValueError(f"Unknown format {format}.")
		if sudo:
			if Files.directory(path) and path[len(path)-1] != "/": 
				path += "/"
				if __real_path__[len(__real_path__)-1] != "/": __real_path__ += "/"
			os.system(f"sudo rsync -aq {gfp.clean(path)} {gfp.clean(__real_path__)} && rm -fr {tmp_path}")
			#print(f"sudo mv {gfp.clean(path)} {gfp.clean(__real_path__}")
			#os.system(f"sudo mv {gfp.clean(path)} {gfp.clean(__real_path__}")
			#	os.system(f"sudo rsync -aq {gfp.clean(path)} {gfp.clean(__real_path__} && rm -fr {tmp_path}")
			#else:
			#	os.system(f"sudo rsync -ogq {gfp.clean(path)} {gfp.clean(__real_path__} && rm -fr {tmp_path}")
		if __keyboard_interrupt__ != False:
			if __loader__ != None:
				__loader__.stop()
			raise KeyboardInterrupt(__keyboard_interrupt__)
	def delete(
		# the path (param #1).
		path=None, 
		# root permission required.
		sudo=False, 
		# forced mode.
		forced=False, 
		# hide logs.
		silent=False,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		path = str(path)
		return gfp.delete(path=path, forced=forced, sudo=sudo, silent=silent)
	def chmod(
		# the path (param #1).
		path=None,
		# the new permission. 
		permission=None, 
		# recursive for entire dir.
		recursive=False, 
		# root permission required.
		sudo=False,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		if permission == None: raise Exceptions.InvalidUsage("Define parameter: permission.")
		path = str(path)
		return gfp.permission.set(path=path, permission=permission, recursive=recursive, sudo=sudo)
	def chown(
		# the path (param #1).
		path=None,
		# the new owner. 
		owner=None, 
		# the new group (optional). 
		group=None, 
		# recursive for entire dir.
		recursive=False, 
		# root permission required.
		sudo=False,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		if owner == None: raise Exceptions.InvalidUsage("Define parameter: owner.")
		path = str(path)
		return gfp.ownership.set(path=path, owner=owner, group=group, recursive=recursive, sudo=sudo)
	def exists(path=None, sudo=False):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		return gfp.exists(path=path, sudo=sudo)
		#
	def clean(
		# the path (leave None to use self.path) (param #1).
		path=None, 
		# the clean options.
		remove_double_slash=True, 
		remove_first_slash=False, 
		remove_last_slash=False,
		ensure_first_slash=False,
		ensure_last_slash=False,
	):
		if path == None: 
			raise ValueError("Define parameter: path.")
		path = str(path).replace("~",HOME)
		while True:
			if remove_double_slash and "//" in path: path = path.replace("//","/")
			elif remove_first_slash and len(path) > 0 and path[0] == "/": path = path[1:]
			elif remove_last_slash and len(path) > 0 and path[len(path)-1] == "/": path = path[:-1]
			elif ensure_first_slash and len(path) > 0 and path[0] != "/": path = "/"+path
			elif ensure_last_slash and len(path) > 0 and path[len(path)-1] != "/": path += "/"
			else: break
		return path
	def directory( 
		# the path (#1).
		path=None,
		# root permission required.
		sudo=False,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		path = Files.clean(path=path, remove_double_slash=True, remove_last_slash=True)
		path = str(path)
		return os.path.isdir(path)
		#
	def mounted( 
		# the path (#1).
		path=None,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
		path = str(path)
		return os.path.ismount(path)
		#
	def create(
		# the path to the file (str) (required) (#1).
		path=None,
		# the data (str) (optional).
		data=None,
		# path is directory (bool).
		directory=False,
		# the owner (str) (optional).
		owner=None,
		# the group (str) (optional).
		group=None,
		# the permission (int) (optional).
		permission=None,
		# root permission required.
		sudo=False,
	):
		if path == None: raise Exceptions.InvalidUsage("Define parameter: path.")
		elif Files.exists(path, sudo=sudo): Exceptions.DuplicateError(f"Path [{path}] already exists.")
		sudo_str = Boolean(sudo).string(true="sudo ", false="")
		if directory:
			os.system(f"{sudo_str}mkdir -p {path}")
		else:
			if isinstance(data, (list, Array, dict, Dictionary)):
				if isinstance(data, (Dictionary,Array)):
					data = data.raw()
				Files.save(path=path, data=data, format="json", sudo=sudo, )
			else:
				Files.save(path=path, data=str(data), sudo=sudo)
		if not Files.exists(path, sudo=sudo):
			raise ValueError(f"Unable to create {Boolean(directory).string(true='directory', false='file')} [{path}] (sudo: {sudo}).")
		if permission != None:
			Files.chmod(path=path, permission=permission, sudo=sudo)
		if owner != None:
			Files.chown(path=path, owner=owner, group=group, sudo=sudo)
	def copy(
		# the from & to path (#1 & #2).
		from_, to_,
		# root permission required.
		sudo=False,
		# the active log level.
		log_level=0,
		# the exclude patterns.
		exclude=[],
		# update deleted files.
		delete=True,
	):
		if not Files.exists(from_, sudo=sudo):
			raise FileNotFoundError(f"Specified copy path [{from_}] does not exist.")
		directory = False
		if Files.directory(from_, sudo=sudo):
			directory = True
			from_ += "/"
			to_ += "/"
		from_ = gfp.clean(from_)
		to_ = gfp.clean(to_)
		if not Files.exists(gfp.base(to_), sudo=sudo): Files.create(gfp.base(to_), sudo=sudo, directory=directory)
		exclude_str = ""
		for i in exclude: exclude_str += f" --exclude '{i}'"
		os.system(f"{Boolean(sudo).string(true='sudo ', false='')}rsync -azt{Boolean(log_level >= 1).string(true='P',false='')} {from_} {to_} {Boolean(delete).string(true='--delete', false='')}{exclude_str}")
	def move(
		# the from & to path (#1 & #2).
		from_, to_,
		# root permission required.
		sudo=False,
		# root permission required.
		log_level=0,
	):
		if not Files.exists(from_, sudo=sudo):
			raise FileNotFoundError(f"Specified move path [{from_}] does not exist.")
		directory = False
		if Files.directory(from_, sudo=sudo):
			directory = True
			from_ += "/"
			to_ += "/"
		from_ = gfp.clean(from_)
		to_ = gfp.clean(to_)
		if not Files.exists(gfp.base(to_), sudo=sudo): Files.create(gfp.base(to_), sudo=sudo, directory=directory)
		os.system(f"{Boolean(sudo).string(true='sudo ', false='')}mv {from_} {to_}")
	def base( 
		# the path (str, FilePath) (#1).
		path=None,
		# the dirs back.
		back=1,
	):
		if path == None: raise ValueError("Define parameter: path:str.")
		path = str(path)
		base = path.replace('//','/')
		if base[len(base)-1] == '/': base = base[:-1]
		if len(base.split("/")) <= 1: raise ValueError("Path [{}] has no base.".format(base))
		startslash = True
		if base[0] != "/":
			startslash = False
		base = base.split("/")
		m, c, s = len(base), 0, ""
		for i in base:
			if c >= m-back: break
			if c == 0:
				s = f"/{i}/"
			else:
				s += f"{i}/"
			c += 1
		if startslash:
			return s
		else:
			return s[1:]
		#

	#
	# the file object class.
	class File(object):
		def __init__(self, path=None, data=None, load=False, default=None):

			# docs.
			DOCS = {
				"module":"File", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }

			# check self instance.
			if isinstance(data, Files.File):
				data = data.data
			# init.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			self.data = data
			if default != None and not os.path.exists(self.file_path.path):
				self.save(data=default)
			if load: self.load()
			# can be filled with executing [self.x = x()]:
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(str(self.file_path.path))
			if not os.path.exists(str(self.file_path.path)) and default != None: 
				self.save(data=default, sudo=sudo)
			self.data = Files.load(self.file_path.path, format=str, sudo=sudo)
			return self.data
		def load_line(self, line_number, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(str(default), self.file_path.path, sudo=sudo)
			data = Files.load(self.file_path.path, format=str, sudo=sudo)
			return data.split('\n')[line_number]
		def save(self, data=None, path=None, overwrite_duplicates=True, sudo=False):
			if path == None: path = self.file_path.path
			if data == None: data = self.data
			utils.__check_memory_only__(path)
			if overwrite_duplicates:
				self.data = data
				return Files.save(path, data, sudo=sudo)
			else:
				file_name, original_path = Formats.FilePath(path).name(), path
				extension = file_name.split('.')[file_name.count('.')]
				file_name_without_extension = file_name.replace(extension, '')
				while True:
					if not os.path.exists(path): break
					else: path = original_path.replace(file_name, file_name_without_extension+'-'+str(index)+extension)
				self.data = data
				return Files.save(path, data, sudo=sudo)
		def check(self, default=None, save=True):
			if default != None and isinstance(default, (str, String)):
				if not self.fp.exists():
					self.data = default
					if save:
						self.save(data=default)
		# support default iteration.
		def __iter__(self):
			return iter(self.data)
		# support '>=' & '>' operator.
		def __gt__(self, string):
			if not isinstance(string, str):
				return len(self) > len(string)
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) > len(string.data)
		def __ge__(self, string):
			if not isinstance(string, str):
				return len(self) >= len(string)
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) >= len(string.data)
		# support '<=' & '<' operator.
		def __lt__(self, string):
			if not isinstance(string, str):
				return len(self) < len(string)
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) < len(string.data)
		def __le__(self, string):
			if not isinstance(string, str):
				return len(self) <= len(string)
			elif not isinstance(string, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) <= len(string.data)
		# support '==' & '!=' operator.
		def __eq__(self, string):
			if not isinstance(string, str):
				return self.data == string
			elif not isinstance(string, self.__class__):
				return False
			return self.data == string.data
		def __ne__(self, string):
			if not isinstance(string, str):
				return self.data != string
			elif not isinstance(string, self.__class__):
				return True
			return self.data != string.data
		# support 'in' operator.
		def __contains__(self, key):
			if isinstance(key, (list, Files.Array)):
				for i in key:
					if i in self.data:
						return True
				return False
			else:
				return key in self.data
		# str representation.
		def __str__(self):
			return str(self.data)
		# content count.
		def __len__(self):
			return len(self.data)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "File"
			#
		# support self assignment.
		def assign(self, data):
			if isinstance(data, self.__class__):
				data = data.data
			self.data = data
			return self
		# return raw data.
		def raw(self):
			return self.data
	#
	# the array object class.
	class Array(object):
		def __init__(self, 
			# the array (param #1).
			array=[], 
			# the path (param #2).
			path=False, 
			# load the data on initialization.
			load=False, 
			# the default array (will be created if file path does not exist).
			default=None,
		):

			# docs.
			DOCS = {
				"module":"Array", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }

			# check self instance.
			if isinstance(array, Files.Array):
				array = array.array
			elif not isinstance(array, list):
				raise Exceptions.InstanceError(f"Parameter [{self.__class__.__name__}.array] must be a [Array] or [list], not [{array.__class__.__name__}].")

			# initialize dictionary recursive.
			#new = []
			#for i in array: new.append(Formats.initialize(i))
			#array = new
			#if isinstance(array, Array):
			#	array = array.array

			# init.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			self.array = array
			if default != None and not os.path.exists(self.file_path.path): self.save(array=default)
			if load: self.load()
		def save(self, array=None, path=None, ensure_ascii=False, indent=4, sudo=False):
			if array != None: array = self.array
			if path == None: path = self.file_path.path
			utils.__check_memory_only__(path)
			self.array = array
			return Files.save(path, Formats.denitialize(array), format="json", indent=indent, ensure_ascii=ensure_ascii, sudo=sudo)
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default, sudo=sudo)
			self.array = Files.load(self.file_path.path, format="json", sudo=sudo)
			return self.array
		def string(self, joiner=" ", sum_first=False):
			string = ""
			for x in self.array:
				if sum_first and string == "": string = joiner + str(x)
				elif string == '': string = str(x)
				else: string += joiner + str(x)
			return str(string)
		def divide(self, into=2):
			avg = len(self.array) / float(into)
			out = []
			last = 0.0
			while last < len(self.array):
				out.append(self.array[int(last):int(last + avg)])
				last += avg
			if len(out) > into:
				while len(out) > into:
					last = out.pop(len(out)-1)
					out[len(out)-1] += last
			return out
		def remove(self, indexes=[], values=[], update=True, save=False):
			array = self.array
			for i in indexes:
				try: array.pop(i)
				except: a=1
			if values != []:
				new = []
				for v in array:
					if v not in values: new.append(v)
				array = new
			if update: self.array = array
			if save: self.save()
			return array
		# default list functions.
		def append(self, var):
			return self.array.append(var)
		def pop(self, index):
			return self.array.pop(index)
		def count(self, item=None):
			if item == None:
				return Formats.Integer(len(self.array))
			elif isinstance(item, (str, Formats.String)):
				c = 0
				for i in self:
					if i == item: c += 1
				return Formats.Integer(c)
			elif isinstance(item, (list, Files.Array)):
				c = 0
				for x in self:
					for y in item:
						if x == y: c += 1
				return Formats.Integer(c)
			else: raise Exceptions.InstanceError("Parameter [item] must either be None, String or Array.")
		# check.
		def check(self, default=None, save=True):
			if default != None and isinstance(default, (list, Array)):
				if not self.fp.exists():
					self.array = default
					if save:
						self.save(data=default)
				else:
					for i in default:
						if i not in self.array:
							self.array.append(i)
					if save:
						self.save()
		# clean content.
		def clean(self, 
			# the string replacements.
			#	example: 
			#		{ "Hello":"hello" }
			#		[ ["Hello", "hello"] ]
			replacements={},
			# the first characters to remove (String & Array).
			remove_first=[],
			# the last characters to remove (String & Array).
			remove_last=[],
			# the first characters that are ensured (String & Array) (List: check is one of the list is ensured).
			ensure_first=[],
			# the last characters that are ensured (String & Array) (List: check is one of the list is ensured).
			ensure_last=[],
			# remove all values within the list from the array.
			remove_values=[],
			# update the self array.
			update=True,
			# the dicionary (leave None to use self.array).
			array=None, 
		):
			if array == None: array = self.array
			if isinstance(remove_first, (str, Formats.String)):
				remove_first = [remove_first]
			if isinstance(remove_last, (str, Formats.String)):
				remove_last = [remove_last]
			if isinstance(ensure_first, (str, Formats.String)):
				ensure_first = [ensure_first]
			if isinstance(ensure_last, (str, Formats.String)):
				ensure_last = [ensure_last]
			new = []
			for item in list(array):
				if item not in remove_values:
					while True:
						edits = False
						for i in remove_first:
							if len(item) >= len(i) and item[:len(i)] == i: 
								item = item[len(i):]
								edits = True
						for i in remove_last:
							if len(item) >= len(i) and item[len(i):] == i: 
								item = item[:-len(i)]
								edits = True
						for i in ensure_first:
							if len(item) >= len(i) and item[:len(i)] != i: 
								item = i+item
								edits = True
						for i in ensure_last:
							if len(item) >= len(i) and item[len(i):] != i: 
								item += i
								edits = True
						for from_, to_ in replacements.items():
							if isinstance(item, (str, Formats.String)) and from_ in item:
								item = item.replace(from_, to_)
								edits = True
						if not edits: break
					new.append(item)
			if update: self.array = list(new)
			return new
		# iterations.
		def iterate(self, sorted=False, reversed=False, array=None):
			if array == None: array = self.array
			return self.items(reversed=reversed, sorted=sorted, array=array)
		def items(self, sorted=False, reversed=False, array=None):
			if array == None: array = self.array
			if sorted: array = self.sort(array=array)
			if reversed: return self.reversed(array=array)
			else: return array
		def keys(self, sorted=False, reversed=False, array=None):
			if array == None: array = self.array
			if sorted:
				return self.sort(self.keys(sorted=False, reversed=reversed, array=array))
			if reversed: 
				reversed_keys = []
				c = len(array)-1
				for _ in range(len(array)):
					reversed_keys.append(array[c])
					c -= 1
				return reversed_keys
			else: return self.array
		def reversed(self, array=None):
			if array == None: array = self.array
			return self.keys(reversed=True, array=array)
		def sort(self, alphabetical=True, ascending=False, reversed=False, array=None):
			if array == None: array = self.array
			if alphabetical or ascending:
				return sorted(array, reverse=reversed)
			else: raise ValueError("Unknown behaviour, alphabetical=False.")
		# dump json string.
		def json(self, sorted=False, reversed=False, indent=4, array=None, ):
			#return json.dumps(Formats.denitialize(self), indent=indent)
			if array == None: array = self.array
			return json.dumps(self.serialize(json=False, sorted=sorted, reversed=reversed, array=array), indent=indent)
		# serialize array.
		def serialize(self, sorted=False, reversed=False, json=False, array=None):
			if array == None: array = self.array
			if isinstance(array, Files.Array):
				array = array.array
			if sorted:
				items = self.items(reversed=reversed, array=self.sort(alphabetical=True, array=array))
			else:
				items = self.items(reversed=reversed, array=array)
			new = []
			for value in items:
				if isinstance(value, (dict, Files.Dictionary)):
					value = Files.Dictionary().serialize(json=json, sorted=sorted, reversed=reversed, dictionary=value)
				elif isinstance(value, (list, Files.Array)):
					value = self.serialize(json=json, sorted=sorted, reversed=reversed, array=value)
				elif isinstance(value, object):
					value = str(value)
				elif isinstance(value, str) or isinstance(value, bool) or value == None:
					if value in [True, "True", "True".lower()]: 
						if json:
							value = "true"
						else: 
							value = True
					elif value in [False, "False", "False".lower()]: 
						if json:
							value = "false"
						else: 
							value = False
					elif value in [None, "None", "None".lower()]: 
						if json:
							value = "null"
						else: 
							value = None
				new.append(value)
			return new

		# randomize the content of the array always non recursive.
		def randomize(self, 
			# optionally pass the array (leave None to use self.array).
			array=None,
		):
			if array == None: array = list(self.array)
			randomized = Array([])
			while len(array) > 0:
				index = random.randrange(0, len(array))
				item = array.pop(index)
				randomized.append(item)
			return randomized
			#

		# limit the content of the array.
		def limit(self,
			# limit to the number of samples.
			limit:int,
			# the index to start from.
			start=0,
			# randomize the content before applying the limit.
			randomize=False,
			# optionally pass the array (leave None to use self.array).
			array=None,
		):
			if array == None: array = list(self.array)
			if randomize: array = self.randomize(array=array)
			return Array(array[start:start+limit])

		
		# copy.
		def copy(self):
			return Files.Array(self.array, path=path)
			#
		# support "+", -, =-, =+" .
		def __add__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			return self.array + array
		def __iadd__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			self.array += array
			return self
		def __sub__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			new = []
			for i in self.array:
				if i not in array:
					new.append(i)
			return new
		def __isub__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			new = []
			for i in self.array:
				if i not in array:
					new.append(i)
			self.array = new
			return self
		
		# support +.
		def __concat__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			return self.array + array
		
		# support default iteration.
		def __iter__(self):
			return iter(self.array)
		
		# support '>=' & '>' operator.
		def __gt__(self, array):
			if not isinstance(array, list):
				return len(self.array) > len(array)
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) > len(array.array)
		def __ge__(self, array):
			if not isinstance(array, list):
				return len(self.array) >= len(array)
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) >= len(array.array)
		
		# support '<=' & '<' operator.
		def __lt__(self, array):
			if not isinstance(array, list):
				return len(self.array) < len(array)
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) < len(array.array)
		def __le__(self, array):
			if not isinstance(array, list):
				return len(self.array) <= len(array)
			elif not isinstance(array, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) <= len(array.array)
		
		# support '==' & '!=' operator.
		def __eq__(self, array):
			if not isinstance(array, list):
				return self.array == array
			elif not isinstance(array, self.__class__):
				return False
			return self.array == array.array
		def __ne__(self, array):
			if not isinstance(array, list):
				return self.array != array
			elif not isinstance(array, self.__class__):
				return True
			return self.array != array.array
		
		# support 'in' operator.
		def __contains__(self, key):
			if isinstance(key, (list, Files.Array)):
				for i in key:
					if i in self.array:
						return True
				return False
			else:
				return key in self.array

		# support '*' operator.
		def __mul__(self, value):
			if isinstance(value, int):
				a=1
			else:
				raise Exceptions.FormatError(f"Can not mul object {self.__class__.__name__} & {value.__class__.__name__}.")
			return Array(self.array * value)
		
		# support '/' operator.
		def __div__(self, value):
			if isinstance(value, int):
				a=1
			else:
				raise Exceptions.FormatError(f"Can not div object {self.__class__.__name__} & {value.__class__.__name__}.")
			return Array(self.divide(into=value))

		# support item assignment.
		def __setitem__(self, index, value):
			#if "/" in item
			try:
				self.array[Formats.denitialize(index)] = value
			except IndexError:
				self.array.append(value)
		def __getitem__(self, index):
			return self.array[Formats.denitialize(index)]
		def __delitem__(self, index):
			#if "/" in item
			return self.array.pop(Formats.denitialize(index))
		# representation.
		def __repr__(self):
			return str(self)
			#
		# str representation.
		def __str__(self):
			return str(Formats.denitialize(self.array))
		# content count.
		def __len__(self):
			return len(self.array)
		# object id.
		def __id__(self):
			if len(self.array) > 10:
				return f"({self.instance()}:[{self.array[0]}, {self.array[0]}, {self.array[0]}, ... {self.array[len(self.array)-3]}, {self.array[len(self.array)-2]}, {self.array[len(self.array)-1]}])"
			else:
				return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Array"
			#
		# support self assignment.
		def assign(self, array, save=False):
			if isinstance(array, self.__class__):
				array = array.array
			self.array = array
			if save: self.save()
			return self
		# return raw data.
		def raw(self):
			return self.array
	#
	# the dictionary object class.
	class Dictionary(object):
		def __init__(self, 
			# the dictionary (param #1).
			dictionary={}, 
			# the file path (param #2).
			path=False, 
			# load the file path dictionary on init.
			load=False, 
			# specify default to check & create the dict.
			default=None, 
		):

			# docs.
			DOCS = {
				"module":"Dictionary", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# check self instance.
			if isinstance(dictionary, Files.Dictionary):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, dict):
				max_attempts = 2
				for attempt in range(max_attempts):
					try:
						if 1+attempt == 1:
							dictionary = dictionary.dict()
							break
						elif 1+attempt == 2:
							dictionary = dictionary.json()
							break
					except:
						if 1+attempt >= max_attempts:
							raise Exceptions.InstanceError(f"Parameter [{self.__class__.__name__}.dictionary] must be a [Dictionary] or [dict], not [{dictionary.__class__.__name__}].")

			# initialize dictionary recursive.
			#for key in list(dictionary.keys()): 
			#	dictionary[key] = Formats.initialize(dictionary[key])
			#if isinstance(dictionary, Dictionary):
			#	dictionary = dictionary.dictionary
					
			# arguments.
			self.dictionary = dictionary
			self.path = gfp.clean(path=path)
			self.default = default
			self.file_path = self.fp = None

			# checks.
			if path != False:
				self.file_path = self.fp = Formats.FilePath(path)
			if load: self.load(default=self.default)
			if self.default != None:
				self.load(default=self.default)
				self.check(default=self.default, save=True)
		   

			#
			# can be filled with executing [self.x = x()]:
		def save(self, dictionary=None, path=None, ensure_ascii=False, indent=4, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if dictionary == None: dictionary = self.dictionary
			if path == None: path = self.file_path.path
			self.dictionary = dictionary
			return Files.save(path, Formats.denitialize(dictionary), format="json", indent=indent, ensure_ascii=ensure_ascii, sudo=sudo)
		def load(self, default=None, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default, sudo=sudo)
			self.dictionary = Files.load(self.file_path.path, format="json", sudo=sudo)
			return self.dictionary
		def load_line(self, line_number, sudo=False):
			utils.__check_memory_only__(self.file_path.path)
			data = Files.load(str(self.file_path.path, sudo=sudo))
			return data.split('\n')[line_number]
		def check(self, 
			#   Option 1:
			key=None, # check a certain key, it appends if not present
			value=None, # check a certain key, append the value if not present (no format check)
			#   Option 2:
			default=None, # check based on a default dictionary, it appends it not present.
			#   Optionals:
			dictionary=None, # overwrite the start dictionary, leave None to use self.dictionary.
			save=False, # saves the output & and sets the output to self.dictionary.
		):

			# functions.
			def __iterate_dict__(dictionary, default):
				#print("\niterating new dictionary: [{}] & default [{}]\n".format(dictionary, default))
				for identifier, item in default.items():
					if isinstance(item, (dict,Dictionary)):
						try: dictionary[str(identifier)] = __iterate_dict__(dictionary[str(identifier)], item)
						except KeyError: dictionary[str(identifier)] = dict(item)
					elif isinstance(item, (list,Array)):
						if isinstance(item, (list)): item = list(item)
						elif isinstance(item, (Array)): item = item.array
						try: dictionary[str(identifier)]
						except KeyError: dictionary[str(identifier)] = item
					else:
						try: dictionary[str(identifier)]
						except KeyError: dictionary[str(identifier)] = item
				return dictionary

			# init.
			if dictionary == None: dictionary = self.dictionary
			if not isinstance(dictionary, (dict, Dictionary)):
				raise Exceptions.InvalidUsage(f"<Dictionary.check> parameter [dicionary] requires to be a [dict, Dictionary] not [{dictionary.__class__.__name__}].")
			
			#   -   option 1:
			if key == None and value != None: raise ValueError("Define both parameters: [key & value].")
			elif value == None and key != None: raise ValueError("Define both parameters: [key & value].")
			if key != None and value != None:   
				try: dictionary[key]
				except KeyError: dictionary[key] = value
				return dictionary
			
			#   -   option 2:
			if default == None: default = self.default
			if default == None: raise ValueError("Define both parameters: [key & value] or parameter [default].")
			dictionary = __iterate_dict__(dictionary, default)
			if save:
				self.dictionary = dictionary
				self.save()
			return dictionary
		def divide(self, into=2):
			"Splits dict by keys. Returns a list of dictionaries."
			return_list = [dict() for idx in range(into)]
			idx = 0
			for k,v in self.dictionary.items():
				return_list[idx][k] = v
				if idx < into-1:  # indexes start at 0
					idx += 1
				else:
					idx = 0
			return return_list
		def append(self, 
			# by default it only overwrites if a key does not exist and sums the key if it is a str / int.
			#
			# a dictionary to append.
			dictionary, 
			# the overwrite formats (add "*" for all).
			overwrite=[], 
			# the sum formats (add "*" for all).
			sum=["int", "float"], 
			# the banned dictionary keys.
			banned=[],
			# update the self dict.
			update=True,
			# save the new dict.
			save=False,
			# do not use.
			dictionary_=None,
		):
			if dictionary_ == None: dictionary_ = self.dictionary
			else: dictionary_ = self.dictionary
			if dictionary == dictionary_: return dictionary
			if dictionary_ == {}: return dictionary
			for key, value in dictionary.items():
				if key not in banned:
					#print(f"Append: [{key}] [{value.__class__.__name__}]")
					if isinstance(value, (dict, Dictionary)):
						found = True
						try: dictionary_[key]
						except: found = False
						if found:
							dictionary_[key] = self.append(value, overwrite=overwrite, sum=sum, banned=banned, dictionary_=dictionary_[key], save=False, update=False)
						else:
							dictionary_[key] = value
					else:
						format = value.__class__.__name__
						if "*" in sum or format in sum:
							if format in ["str", "int", "float", "list", "Array"]:
								try: dictionary_[key] += value
								except KeyError: dictionary_[key] = value
							else: # cant be summed.
								dictionary_[key] = value
						elif "*" in overwrite or format in overwrite:
							dictionary_[key] = value
						else:
							try: dictionary_[key]
							except KeyError: dictionary_[key] = value
			if update: self.dictionary = dictionary_
			if save: 
				self.dictionary = dictionary_
				self.save()
			return dictionary_
		# edit.
		def edit(self, 
			# the dictionary (leave None to use self.dictionary).
			dictionary=None,
			# the edits (dict).
			# 	adds / replaces the current (except the exceptions).
			edits={},
			# the edits key Exceptions.
			exceptions=[],
			# the edits value Exceptions.
			value_exceptions=[None],
			# the instances to overwrite (list[str]) (missing stands for the keys that are missing in the dictionary).
			overwite=["missing"],
			# the instances to combine (list[str]) (dict is always recursive).
			combine=["int", "float", "Integer", "list", "Array"],
			# save the edits.
			save=True,
			# the log level.
			log_level=-1,
		):
			def edit_dict(dictionary={}, edits={}):
				c = 0
				for key, value in edits.items():
					found = True
					try: dictionary[key]
					except KeyError: found = False
					# recursive.
					if key not in exceptions and value not in value_exceptions and isinstance(value, (dict, Dictionary)):
						if isinstance(value, (Dictionary)):
							value = value.dictionary
						if found:
							dictionary[key], lc = edit_dict(dictionary=dictionary[key], edits=value)
							c += lc
						else:
							if log_level >= 0:
								print(f"Editing {alias} config {key}: {value}.")
							dictionary[key] = value
							c += 1
					elif key not in exceptions and value not in value_exceptions and not found and "missing" in overwrite:
						if log_level >= 0:
							print(f"Editing {alias} config {key}: {value}.")
						dictionary[key] = value
						c += 1
					elif key not in exceptions and value not in value_exceptions and found and value.__class__.__name__ in combine:
						if log_level >= 0:
							print(f"Editing {alias} config {key}: {value}.")
						dictionary[key] = dictionary[key] + value
						c += 1
				return dictionary, c
			
			# check specific.
			if dictionary == None: dictionary = self.dictionary
			dictionary, c = edit_dict(dictionary=dictionary, edits=edits)
			if (edit_count > 0 or c > 0) and save:
				self.dictionary = dictionary
				if self.fp != None: self.save()
			return dictionary
		# unpack attribute(s).
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
			defaults_ = {}
			if isinstance(keys, (dict, Files.Dictionary)):
				if isinstance(keys, dict):
					defaults_ = dict(keys)
					keys = list(keys.keys())
				else:
					defaults_ = keys.dict()
					keys = keys.keys()
			elif isinstance(keys, str):
				keys = [keys]
			unpacked = []
			for key in keys:
				value, set = None, True
				try: 
					value = self.dictionary[key]
				except KeyError: 
					try:
						value = defaults_[key]
					except KeyError: 
						set = False
				if not set:
					raise Exceptions.UnpackError(f"Dictionary does not contain attribute [{key}].")
				unpacked.append(value)
			if len(unpacked) == 1:
				return unpacked[0]
			else:
				return unpacked
		# remove.
		def remove(self, keys=[], values=[], update=True, save=False, dictionary=None):
			if dictionary == None:
				dictionary = dict(self.dictionary)
			for i in list(keys):
				try: del dictionary[i]
				except: a=1
			if values != []:
				new = {}
				for k,v in dictionary.items():
					if v not in values: new[k] = v
				dictionary = new
			if update:
				self.dictionary = dictionary
			if save: 
				self.dictionary = dictionary
				self.save()
			return dictionary
		# default dict functions.
		def count(self, item=None, values=False):
			if item == None:
				return Formats.Integer(len(self.dictionary))
			elif isinstance(item, (str, Formats.String)):
				c, array = 0, []
				if values:
					array = self.values()
				else:
					array = self.keys()
				for i in array:
					if i == item: c += 1
				return Formats.Integer(c)
			elif isinstance(item, (list, Files.Array)):
				c, array = 0, []
				if values:
					array = self.values()
				else:
					array = self.keys()
				for x in array:
					for y in item:
						if x == y: c += 1
				return Formats.Integer(c)
			else: raise Exceptions.InstanceError(f"Parameter [item] must either be [None], [String] or [Array], not [{item.__class__}].")
		# insert new keys & values.
		def insert(self, dictionary={}, __dictionary__=None):
			update = False
			if __dictionary__ == None: 
				__dictionary__ = self.dictionary
				update = True
			for key,value in dictionary.items():
				if isinstance(value, (dict, Dictionary)):
					if key in __dictionary__:
						__dictionary__[key] = self.insert(value, __dictionary__=__dictionary__[key])
					else:
						__dictionary__[key] = value
				elif isinstance(value, (list, Array)):
					if key in __dictionary__:
						for i in value:
							if i not in __dictionary__[key]: __dictionary__[key].append(i)
					else:
						__dictionary__[key] = value
				else:
					__dictionary__[key] = value
			if update:
				self.dictionary = __dictionary__
			return __dictionary__
		# iterations.
		def iterate(self, sorted=False, reversed=False, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			return self.items(reversed=reversed, sorted=sorted, dictionary=dictionary)
		def items(self, sorted=False, reversed=False, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			if sorted: dictionary = self.sort(dictionary=dictionary)
			if reversed: return self.reversed(dictionary=dictionary).items()
			else: return dictionary.items()
		def keys(self, sorted=False, reversed=False, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			if sorted:
				return self.sort(self.keys(sorted=False, reversed=reversed, dictionary=dictionary))
			if reversed: 
				keys = list(dictionary.keys())
				reversed_keys = []
				c = len(keys)-1
				for _ in range(len(keys)):
					reversed_keys.append(keys[c])
					c -= 1
				return reversed_keys
			else: return list(dictionary.keys())
		def values(self, sorted=False, reversed=False, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			if sorted:
				return self.sort(self.values(sorted=False, reversed=reversed, dictionary=dictionary))
			values = []
			for key, value in self.items(reversed=reversed, dictionary=dictionary):
				values.append(value)
			return values
		def reversed(self, update=True, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			reversed_dict = {}
			for key in self.keys(reversed=True, dictionary=dictionary):
				reversed_dict[key] = dictionary[key]
			if update:
				self.dictionary = reversed_dict
			return reversed_dict
		def sort(self, 
			# option 1:
			# sort alphabetically.
			alphabetical=True, 
			# option 2:
			# sort ascending.
			ascending=False, 
			# option 3:
			# sort descending.
			descending=False, 
			# option 4:
			# sort reversed.
			reversed=False, 
			# update the self variable.
			update=True, 
			# sort the keys or sort the values.
			sort="keys",
			# system parameters.
			dictionary=None,
		):
			if dictionary == None: dictionary = self.dictionary
			if descending:
				return self.reversed(
					update=update,
					dictionary=self.sort(
						ascending=True, 
						dictionary=dictionary, 
						update=False,
						sort=sort,
					),
				)
			else:
				new, reversed_dict = {}, {}
				if alphabetical or ascending:
					if sort == "keys":
						array = list(dictionary.keys())
					elif sort == "values":
						array = list(dictionary.values())
						reversed_dict = self.__reverse_keys_and_values__(dictionary=dictionary)
					else: raise ValueError("Selected an invalid sort mode [{sort}].")
					_sorted_ = Array().sort(alphabetical=alphabetical, ascending=ascending, reversed=reversed, array=array)
				else: raise ValueError("Unknown behaviour, alphabetical=False.")
				for key in _sorted_:
					if sort == "keys":
						new[Formats.denitialize(key)] = dictionary[Formats.denitialize(key)]
					elif sort == "values":
						new[Formats.denitialize(key)] = reversed_dict[Formats.denitialize(key)]
				if sort == "values":
					new = self.__reverse_keys_and_values__(dictionary=new)
				if update:
					self.dictionary = new
				return new
		# dump json string.
		def json(self, sorted=False, reversed=False, indent=4, dictionary=None, ):
			if dictionary == None: dictionary = self.dictionary
			return json.dumps(self.serialize(json=False, sorted=sorted, reversed=reversed, dictionary=dictionary), indent=indent)
		# serialize dict.
		def serialize(self, sorted=False, reversed=False, json=False, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			if isinstance(dictionary, Files.Dictionary):
				dictionary = dictionary.dictionary
			if sorted:
				items = self.items(reversed=reversed, dictionary=self.sort(alphabetical=True, dictionary=dictionary))
			else:
				items = self.items(reversed=reversed, dictionary=dictionary)
			dictionary = {}
			for key, value in items:
				if isinstance(value, (dict, Files.Dictionary)):
					value = self.serialize(json=json, sorted=sorted, reversed=reversed, dictionary=value)
				elif isinstance(value, (list, Files.Array)):
					value = Files.Array(value).serialize(json=json, sorted=sorted, reversed=reversed)
				elif isinstance(value, object):
					value = str(value)
				elif isinstance(value, str) or isinstance(value, bool) or value == None:
					if value in [True, "True", "True".lower()]: 
						if json:
							value = "true"
						else: 
							value = True
					elif value in [False, "False", "False".lower()]: 
						if json:
							value = "false"
						else: 
							value = False
					elif value in [None, "None", "None".lower()]: 
						if json:
							value = "null"
						else: 
							value = None
				dictionary[key] = value
			return dictionary
		# copy.
		def copy(self):
			return Files.Dictionary(self.dictionary, path=path)
			#
		# system functions.
		def __reverse_keys_and_values__(self, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			new = {}
			for key,value in dictionary.items():
				new[value] = key
			return new
		def __serialize_string__(self, string, banned_characters=["@"]):
			c, s, l = 0, "", False
			for char in string:
				if char not in banned_characters:
					# regular letter.
					if char.lower() == char:
						s += char.lower()
						l = False
					# capital letter.
					else:
						if c == 0:
							s += char.lower()
						else:
							if l:
								s += char.lower()
							else:
								s += "_"+char.lower()
						l = True
					c += 1
			return s
		def __serialize_dictionary__(self, response):
			_response_ = {}
			for key,value in response.items():
				s_key = self.__serialize_string__(key)
				if isinstance(value, dict):
					_response_[s_key] = self.__serialize_dictionary__(value)
				elif isinstance(value, str):
					try: integer = int(value)
					except: integer = False
					if integer != False:
						_response_[s_key] = integer
					elif value in ["false", "False", "FALSE", "DISABLED"]:
						_response_[s_key] = False
					elif value in ["true", "True", "TRUE", "ENABLED"]:
						_response_[s_key] = True
					else:
						_response_[s_key] = value
				else:
					_response_[s_key] = value
			return _response_
		# support "+", -, =-, =+" .
		def __add__(self, dictionary):
			if isinstance(dictionary, dict):
				a=1
			elif isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			return self.append(dictionary=dictionary, overwrite=["*"], sum=[], update=False)
		def __iadd__(self, dictionary):
			if isinstance(dictionary, dict):
				a=1
			elif isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			self.append(dictionary=dictionary, overwrite=["*"], sum=[], update=True)
			return self
		def __sub__(self, dictionary):
			if isinstance(dictionary, dict):
				keys = list(dictionary.keys())
			elif isinstance(dictionary, list):
				keys = dictionary
			elif isinstance(dictionary, Files.Array):
				keys = dictionary.array
			elif isinstance(dictionary, self.__class__):
				keys = dictionary.keys()
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			return self.remove(keys=keys, update=False)
		def __isub__(self, dictionary):
			if isinstance(dictionary, dict):
				keys = list(dictionary.keys())
			elif isinstance(dictionary, list):
				keys = dictionary
			elif isinstance(dictionary, Files.Array):
				keys = dictionary.array
			elif isinstance(dictionary, self.__class__):
				keys = dictionary.keys()
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			self.remove(keys=keys, update=True)
			return self
		# support +.
		def __concat__(self, string):
			if isinstance(dictionary, dict):
				a=1
			elif isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			return self.append(dictionary=dictionary, sum=[], overwrite=["*"], update=False)
		# support default iteration.
		def __iter__(self):
			return iter(self.dictionary)
		# support '>=' & '>' operator.
		def __gt__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) > len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) > len(dictionary.dictionary)
		def __ge__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) >= len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) >= len(dictionary.dictionary)
		# support '<=' & '<' operator.
		def __lt__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) < len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) < len(dictionary.dictionary)
		def __le__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) <= len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) <= len(dictionary.dictionary)
		# support '==' & '!=' operator.
		def __eq__(self, dictionary):
			if isinstance(dictionary, dict):
				return str(self.sort()) == str(Dictionary(dictionary).sort())
			elif isinstance(dictionary, Dictionary):
				return str(self.sort()) == str(dictionary.sort())
			else:
				try:
					return str(self.sort()) == str(dictionary.sort())
				except:
					return False
		def __ne__(self, dictionary):
			if isinstance(dictionary, dict):
				return str(self.sort()) != str(Dictionary(dictionary).sort())
			elif isinstance(dictionary, Dictionary):
				return str(self.sort()) != str(dictionary.sort())
			else:
				try:
					return str(self.sort()) != str(dictionary.sort())
				except:
					return False
		# support 'in' operator.
		def __contains__(self, key):
			keys = list(self.dictionary.keys())
			if isinstance(key, (list, Files.Array)):
				for i in key:
					if i in keys:
						return True
				return False
			else:
				return key in keys
		# support item assignment.
		def __setitem__(self, key, value):
			if isinstance(key, (int, Integer)):
				key = self.keys()[key]
			self.dictionary[Formats.denitialize(key)] = value
		def __getitem__(self, key):
			if isinstance(key, slice):
				raise ValueError("Coming soon.")
			elif isinstance(key, (int, Integer)):
				key = self.keys()[key]
			return self.dictionary[Formats.denitialize(key)]
			#
		def __delitem__(self, key):
			if isinstance(key, (int, Integer)):
				key = self.keys()[key]
			del self.dictionary[Formats.denitialize(key)]
		def __splitkey__(self, key):
			if key in self:
				return [key]
			return gfp.clean(path=key, remove_last_slash=True, remove_double_slash=True, remove_first_slash=True).split("/")
		# representation.
		def __repr__(self):
			return str(self)
			#
		# str representation.
		def __str__(self):
			return str(Formats.denitialize(self.dictionary))
		# content count.
		def __len__(self):
			return len(self.dictionary)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self, serialize=False):
			return "Dictionary"
		@property
		def __name__(self):
			return self.instance()
		# support self assignment.
		def assign(self, dictionary, save=False):
			if isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			self.dictionary = dictionary
			if save: self.save()
			return self
		# return raw data.
		def raw(self):
			return self.dictionary
		#  
	#
	# the directory object class.
	class Directory(object):
		def __init__(self, 
			# the dirs file path (param #1).
			path=None, 
			# the hierarchy to check / create.
			hierarchy={}, 
			# load the content.
			#load=False,
			# load recursive.
			#recursive=False,
		):
			
			# docs.
			DOCS = {
				"module":"Directory", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# check self instance.
			if isinstance(path, Files.Directory):
				path = path.fp.path

			# init.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: 
				if path[len(path)-1] != "/": path += "/"
				self.file_path = self.fp = Formats.FilePath(path)
			self.hierarchy = hierarchy
			if self.hierarchy != {}:
				self.check(hierarchy=hierarchy)

			# load.
			#self.content = {}
			#if load:
			#	self.content = {}

			# can be filled with executing [self.x = x()]:
			# executable functions.
		# actions.
		def create(self, file_paths=[], path=None, sudo=False, owner=None, group=None, permission=None):

			#   -   init:
			if path == None: path = self.file_path.path

			#   -   create dir:
			if not os.path.exists(path): 
				if sudo: os.system('sudo mkdir -p '+path)
				else: os.system('mkdir -p '+path)

			#   -   copy files:
			commands = []
			for l_path in file_paths: 
				if sudo:
					command = None
					if Files.directory(l_path): command = 'sudo cp -r {0} {1} '.format(l_path, path+Formats.FilePath(l_path).name())
					else: command = 'sudo cp {0} {1}'.format(l_path, path+Formats.FilePath(l_path).name())
					commands.append(command)
				else:
					command = None
					if Files.directory(l_path): command = 'cp -r {0} {1} '.format(l_path, path+Formats.FilePath(l_path).name())
					else: command = 'cp {0} {1}'.format(l_path, path+Formats.FilePath(l_path).name())
					commands.append(command)
			if len(commands) > 0:
				if sudo:
					script = Files.ShellScript(
						data=command, 
						path='/tmp/shell_script-'+str(random.randrange(23984792,23427687323))+'.sh'
					)
					script.save()
					script.setPermission(755)
					script.execute(sudo=sudo)
					script.delete()
				else: os.system(Files.Array(array=commands,path=False).string(joiner=" \n "))

			if owner != None or group!=None: self.file_path.ownership.set(owner=owner, group=group, sudo=sudo)
			if permission != None: self.file_path.permission.set(permission=permission, sudo=sudo)
		def delete(self, forced=False):
			if forced: os.system('rm -fr {}'.format(self.file_path.path))
			else: os.system('rm -r {}'.format(self.file_path.path))
		def check(self, 
			#   Required:
			#   -   dictionary format:
			hierarchy=None, 
			#   Optionals:
			#   -   string format:
			owner=None, 
			group=None, 
			#   -   boolean format:
			sudo=False,
			#   -   integer format:
			permission=None, # (octal format)
			recursive=False, # for permission/ownership
			silent=False,
		):
			format = {
				"my_directory_name":{
					# Required:
					"path":"my_directory_name/",
					# Optionals:
					"permission":755,
					"owner":"daanvandenbergh",
					"group":None,
					"sudo":False,
					"directory":True,
					"recursive":False, # for permission & ownership (directories).
					"default_data":None, # makes it a file
					"default":None, # makes it a dictionary
				}
			}
			def checkPermissionOwnership(file_path, dictionary, silent=False, recursive=False):
				if dictionary["permission"] != None and dictionary["permission"] != file_path.permission.permission:
					#print("editing file [{}] permission [{}] to [{}]...".format(file_path.path, file_path.permission.permission, dictionary["permission"]))
					file_path.permission.set(permission=dictionary["permission"], sudo=dictionary["sudo"], recursive=recursive, silent=silent)
				if dictionary["owner"] != None and dictionary["owner"] != file_path.ownership.owner:
					#print("editing file [{}] owner [{}] to [{}]...".format(file_path.path, file_path.ownership.owner, dictionary["owner"]))
					file_path.ownership.set(owner=dictionary["owner"], group=file_path.ownership.group, sudo=dictionary["sudo"], recursive=recursive, silent=silent)
				#print("file [{}] current group [{}] wanted group [{}]".format(file_path.path, file_path.ownership.group, dictionary["group"]))
				if dictionary["group"] != None and dictionary["group"] != file_path.ownership.group:
					#print("editing file [{}] group [{}] to [{}]...".format(file_path.path, file_path.ownership.group, dictionary["group"]))
					file_path.ownership.set(owner=file_path.ownership.owner, group=dictionary["group"], sudo=dictionary["sudo"], recursive=recursive, silent=silent)
			if hierarchy == None: hierarchy = self.hierarchy
			#if owner == None: owner = self.owner
			#if group == None: group = self.group
			#if permission == None: permission = self.permission
			file_path = Formats.FilePath(self.file_path.path)
			if file_path.exists(sudo=sudo) == False:
				file_path.create(
					directory=True, 
					permission=permission, 
					group=group, 
					owner=owner,
					sudo=sudo)
			elif group != None or owner != None or permission != None: 
				file_path.permission.permission = file_path.permission.get()
				_owner_,_group_ = file_path.ownership.get()
				file_path.ownership.group = _group_
				file_path.ownership.owner = _owner_
				checkPermissionOwnership(file_path, {"sudo":sudo, "owner":owner, "group":group, "permission":permission}, recursive=recursive, silent=silent)


			if hierarchy == None: raise ValueError("Define dictionary parameter: hierarchy")
			for identifier, dictionary in hierarchy.items():

				#   -   check:
				try: dictionary["path"] = self.file_path.path + dictionary["path"]
				except: raise ValueError("Invalid hierarchy item [{} : {}]. Specify the [path].".format(identifier, "?"))
				try: dictionary["permission"]
				except KeyError: dictionary["permission"] = None
				try: dictionary["owner"]
				except KeyError: dictionary["owner"] = None
				try: dictionary["group"]
				except KeyError: dictionary["group"] = None
				try: dictionary["directory"]
				except KeyError: dictionary["directory"] = False
				try: dictionary["sudo"]
				except KeyError: dictionary["sudo"] = False
				try: dictionary["default_data"]
				except KeyError: dictionary["default_data"] = None
				try: dictionary["default"]
				except KeyError: dictionary["default"] = None
				try: dictionary["recursive"]
				except KeyError: dictionary["recursive"] = False

				#   -   directory:
				if dictionary["directory"]:
					file_path = Formats.FilePath(dictionary["path"])
					if file_path.exists(sudo=dictionary["sudo"]) == False:
						file_path.create(
							directory=True, 
							permission=dictionary["permission"], 
							group=dictionary["group"], 
							owner=dictionary["owner"],
							sudo=dictionary["sudo"],)
					else: 
						file_path.permission.permission = file_path.permission.get()
						_owner_,_group_ = file_path.ownership.get()
						file_path.ownership.group = _group_
						file_path.ownership.owner = _owner_
						#if 'back_up_requests/requests' in file_path.path: 
						#   print("file: {}, owner: {}, group: {}, permission: {}".format(file_path.path, file_path.ownership.owner, file_path.ownership.group, file_path.permission.permission))
						checkPermissionOwnership(file_path, dictionary, silent=silent, recursive=dictionary["recursive"])

				#   -   file:
				elif dictionary["default_data"] != None:
					file = Files.File(path=dictionary["path"])
					if file.file_path.exists(sudo=dictionary["sudo"]) == False:
						file.file_path.create(
							data=dictionary["default_data"], 
							permission=dictionary["permission"], 
							group=dictionary["group"], 
							owner=dictionary["owner"],
							sudo=dictionary["sudo"])
					else: 
						file.file_path.permission.permission = file_path.permission.get()
						_owner_,_group_ = file_path.ownership.get()
						file.file_path.ownership.group = _group_
						file.file_path.ownership.owner = _owner_
						checkPermissionOwnership(file.file_path, dictionary, silent=silent)

				#   -   dictionary:
				elif dictionary["default"] != None:
					file = Files.Dictionary(path=dictionary["path"])
					if file.file_path.exists(sudo=dictionary["sudo"]) == False:
						file.save(dictionary["default"])
						file.file_path.permission.check(
							permission=dictionary["permission"], 
							sudo=dictionary["sudo"])
						file.file_path.ownership.check(
							group=dictionary["group"], 
							owner=dictionary["owner"],
							sudo=dictionary["sudo"])
					else: 
						file.file_path.permission.permission = file_path.permission.get()
						_owner_,_group_ = file_path.ownership.get()
						file.file_path.ownership.group = _group_
						file.file_path.ownership.owner = _owner_
						checkPermissionOwnership(file.file_path, dictionary, silent=silent)
						file.check(default=default, save=True)
				else:
					raise ValueError("Invalid hierarchy item [{} : {}]. Either [directory] must be enabled, or [default_data / default] must be specified.".format(identifier, dictionary["path"]))

				#
		# load & save sub paths.
		def load(self, path=None, format=str, default=None, sudo=False):
			return Files.load(path=self.fullpath(path), format=format, sudo=sudo)
		def save(self, path=None, data=None, format=str, sudo=False):
			return Files.save(path=self.fullpath(path), data=data, format=format, sudo=sudo)
		# returnable functions.
		def paths(self, 
			# get recursively (bool).
			recursive=False, 
			# get files only (bool).
			files_only=False,
			# get firs only (bool). 
			dirs_only=False, 
			# also get empty dirs (bool).
			empty_dirs=True, 
			# the banned full paths (list).
			banned=[], 
			# the banned names (list).
			banned_names=[".DS_Store"], 
			# the banend base names (list).
			banned_basenames=["__pycache__"], 
			# the allowed extensions (list).
			extensions=["*"],
			# the path (leave None to use self.path) (str, FilePath).
			path=None, 
		):
			if dirs_only and files_only: raise ValueError("Both parameters dirs_only & piles_only are True.")
			if path == None: path = self.file_path.path
			path = str(path)
			if not Files.exists(path): return []
			if isinstance(extensions, str): extensions = [extensions]
			if len(banned) > 0:
				l_banned = []
				for i in banned:
					l_banned.append(gfp.clean(f"{path}/{i}"))
				banned = l_banned
			paths = []
			if recursive:
				# does only work with recursive.
				for root, dirs, files in os.walk(path):
					if not dirs_only:
						for name in files:
							if name not in banned_names and ("*" in extensions or gfp.extension(name=name) in extensions ):
								l_path = gfp.clean(path=f"{root}/{name}")
								l_banned = False
								for i in banned_basenames:
									if f"/{i}/" in l_path: l_banned = True ; break
								if l_path not in banned and not l_banned and l_path+"/" not in banned:
									paths.append(l_path)
					if not files_only:
						for name in dirs:
							if name not in banned_names and (dirs_only or "*" in extensions or "dir" in extensions ):
								l_path = gfp.clean(path=f"{root}/{name}/")
								l_banned = False
								for i in banned_basenames:
									if f"/{i}/" in l_path: l_banned = True ; break
								if l_path not in banned and not l_banned and l_path+"/" not in banned:
									paths.append(l_path)
									if recursive:
										paths += self.paths(recursive=recursive, path=l_path, dirs_only=dirs_only, files_only=files_only, banned=banned, banned_names=banned_names, empty_dirs=empty_dirs)
			else:
				for name in os.listdir(path):
					l_path = gfp.clean(path=f"{path}/{name}")
					if not dirs_only and not Files.directory(l_path):
						if name not in banned_names and ("*" in extensions or gfp.extension(name=name) in extensions ):
							l_banned = False
							for i in banned_basenames:
								if f"/{i}/" in l_path: l_banned = True ; break
							if l_path not in banned and not l_banned and l_path+"/" not in banned:
								paths.append(l_path)
					if not files_only and Files.directory(l_path):
						l_path += "/"
						if name not in banned_names and (dirs_only or "*" in extensions or "dir" in extensions ):
							l_banned = False
							for i in banned_basenames:
								if f"/{i}/" in l_path: l_banned = True ; break
							if l_path not in banned and not l_banned and l_path+"/" not in banned:
								paths.append(l_path)
			return paths
		def names(self, 
			# get recursively (bool).
			recursive=False, 
			# get files only (bool).
			files_only=False,
			# get firs only (bool). 
			dirs_only=False, 
			# also get empty dirs (bool).
			empty_dirs=True, 
			# remove the extension names (bool).
			remove_extensions=False,
			# the banned full paths (list).
			banned=[], 
			# the banned names (list).
			banned_names=[".DS_Store"], 
			# the banend base names (list).
			banned_basenames=["__pycache__"], 
			# the allowed extensions (list).
			extensions=["*"],
			# the path (leave None to use self.path) (str, FilePath).
			path=None, 
		):
			names = []
			for _path_ in self.paths(dirs_only=dirs_only, files_only=files_only, empty_dirs=empty_dirs, recursive=recursive, path=path, banned=banned, banned_names=banned_names, extensions=extensions):
				if remove_extensions:
					name = gfp.name(path=_path_)
					names.append(name[:-len(gfp.extension(name=name))])
				else:
					names.append(gfp.name(path=_path_))
			return names
		def oldest(self):
			files = []
			for i in os.listdir(self.file_path.path):
				if i not in [".DS_Store"]:
					path = f'{self.file_path.path}/{i}'.replace("//",'/')
					files.append(path)
			if len(files) == 0: return False
			return min(files, key=os.path.getctime) # oldest is min (this is not a code error)
		def newest(self):
			files = []
			for i in os.listdir(self.file_path.path):
				if i not in [".DS_Store"]:
					path = f'{self.file_path.path}/{i}'.replace("//",'/')
					files.append(path)
			if len(files) == 0: return False
			return max(files, key=os.path.getctime) # newest is max (this is not a code error)
		def random(self):
			files = []
			for i in os.listdir(self.file_path.path):
				if i not in [".DS_Store"]:
					path = f'{self.file_path.path}/{i}'.replace("//",'/')
					files.append(path)
			if len(files) == 0: return False
			return files[random.randrange(0, len(files))]
		def generate(self, length=24, type="/"):
			path, paths = None, self.paths()
			for x in range(1000):
				path = self.join(utils.generate.shell_string(length=length), type)
				if path not in paths:
					break
			if path == None: __error__("Failed to generate a new random path inside directory [{}].".format(self.file_path.path))
			return path
		def structured_join(self, name, type="", structure="alphabetical", create_base=False, sudo=False, owner=None, group=None, permission=None):
			if type not in ["/", ""]:
				type = "."+type
			if structure == "alphabetical":
				alphabetical = None
				try: alphabetical = name[0].upper()
				except: alphabetical = "SPECIAL"
				if str(alphabetical) not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Z","0","1","2","3","4","5","6","7","8","9"]: aplhabetical = "SPECIAL"
				base = self.file_path.path + "/" + alphabetical + "/"
				if create_base and os.path.exists(base) == False:
					self.create(path=base, sudo=sudo, owner=owner, group=group, permission=permission)
				alph_dir = base + name + type
				return alph_dir
			else: raise ValueError("Invalid usage, parameter structure [{}], valid options: {}".format(structure, ["alphabetical"]))
		def contains(self, name=None, type="/", recursive=False):
			return self.join(name, type) in self.paths(recursive=recursive)
			#
		def subpath(self, fullpath):
			return self.fp.clean(path=fullpath.replace(self.fp.path, ""), remove_double_slash=True)
		def fullpath(self, subpath):
			return self.fp.clean(path=f"{self.fp.path}/{subpath}", remove_double_slash=True)
		# set the icon.
		def set_icon(self, 
			# the path to the .png / .jpg icon.
			icon=None, 
			# the directory path (leave None to use self.fp.path).
			path=None,
		):
			if icon == None: raise Exceptions.InvalidUsage("Define parameter: icon.")
			if path == None: path = self.fp.path
			if OS in ["osx", "macos"]:
				utils.__execute_script__(f"""
					#!/bin/bash

					# settings.
					icon="{icon}"
					dest="{path}"

					# check inputs
					if [ ! -f $icon ]; then 
						echo "ERROR: File $1 does not exists"
						exit 1
					elif [[ ! $icon =~ .*\.(png|PNG|jpg|JPG) ]]; then
						echo "ERROR: Icon must be a .png|.jpg file"
						exit 1
					elif [ -f $dest ]; then
						folder=false
					elif [ -d $dest ]; then
						folder=true
					else
						echo 'ERROR: File|Folder destination does not exists'
						exit 1
					fi

					# create icns icon
					sips -i $icon > /dev/null
					DeRez -only icns $icon > /tmp/tmpicns.rsrc

					# set icon
					if [ "$folder" = true ]; then
						Rez -append /tmp/tmpicns.rsrc -o $dest$'/Icon\r'
						SetFile -a C $dest
						SetFile -a V $dest$'/Icon\r'
					else
						Rez -append /tmp/tmpicns.rsrc -o $dest
						SetFile -a C $dest
					fi

					# clean up
					rm /tmp/tmpicns.rsrc
					exit 0
					""")
			else:
				raise OSError("Unsupported operating system.")
		# index the content.
		def index(self, 
			# the wanted options.
			metrics=[],
			options=["size", "mtime", "content", "name", "basename", "extension", "mount", "directory"],
			# optional path (leave None to use self.path).
			path=None,
		):
			def process(path):
				info = {}
				if "mtime" in metrics:
					info["mtime"] = gfp.mtime(path=path, format="seconds")
				if "size" in metrics:
					info["size"] = gfp.size(path=path, format=int)
				directory = None
				if "directory" in metcics:
					directory = info["directory"] = Files.directory(str(path))
				if "content" in metrics:
					if directory == None: raise Exceptions.InvalidUsage("Metric [directory] is required when obtaining metric [content].")
					if not directory:
						info["content"] = Files.load(path)
					else:
						info["content"] = None
				if "mount" in metrics:
					info["mount"] = os.path.ismount(str(path))
				if "name" in metrics:
					info["name"] = gfp.name(path=path)
				if "extension" in metrics:
					info["name"] = gfp.extension(path=path)
				if "basename" in metrics:
					info["basename"] = gfp.basename(path=path)
				return info
				#
			if path == None: path = self.path
			if metrics == []:
				raise Exceptions.InvalidUsage(f'No metrics are specified, metric options: [{Array(options).string(joiner=" ")}].')
			for i in metrics:
				if i not in options:
					raise Exceptions.InvalidUsage(f'Metric [{i}] is not a valid metric option, options: [{Array(options).string(joiner=" ")}].')
			indexed, dir, ids = Dictionary(path=False, dictionary={}), Files.Directory(path=path), []
			for _path_ in dir.paths(recursive=True, files_only=True, banned=[gfp.clean(f"{path}/Icon\r")], banned_names=[".DS_Store", "__pycache__"]):
				if _path_ not in ids and "/__pycache__/" not in _path_ and "/.DS_Store" not in _path_: 
					indexed[_path_] = process(_path_)
					ids.append(_path_)
			for _path_ in dir.paths(recursive=True, dirs_only=True, banned=[gfp.clean(f"{path}/Icon\r")], banned_names=[".DS_Store", "__pycache__"]):
				if _path_ not in ids and "/__pycache__/" not in _path_ and "/.DS_Store" not in _path_: 
					indexed[_path_] = process(_path_)
					ids.append(_path_)
			return indexed.sort(alphabetical=True)
		# open for desktop.
		def open(self, path=None, sudo=False):
			if path == None: path = self.fp.path
			if sudo: sudo = "sudo "
			else: sudo = ""
			if OS in ["macos"]: 
				os.system(f"{sudo}open {path}")
			elif OS in ["linux"]: 
				os.system(f"{sudo}nautulis {path}")
			else: raise Exceptions.InvalidOperatingSystem(f"Unsupported operating system [{OS}].")
		# return references of each file that includes one of the matches.
		def find(self, matches:list, path=None, recursive=False, log_level=0):
			if path == None: path = self.path
			gfp = Formats.FilePath("")
			c, references = 0, {}
			for string in matches:
				if not os.path.exists(path):
					raise ValueError(f"Path {path} does not exist.")
				elif not Files.directory(path):
					raise ValueError(f"Path {path} is not a directory.")
				for i_path in self.paths(recursive=recursive, files_only=True, banned_names=[".DS_Store", ".git"], path=path):
					data = None
					try:
						data = Files.load(i_path)
					except:
						try:
							data = f"{Files.load(i_path, format=bytes)}"
						except: data = None
					if data != None and string in data: 
						if log_level >= 0:
							print("")
							print(f"{i_path}:")
						lines, linecount = data.split("\n"), 0
						for _ in lines:
							if string in lines[linecount]:
								try: before = lines[linecount-1]
								except: before = None
								try: after = lines[linecount+1]
								except: after = None
								if log_level >= 0:
									if before != None: print(" * "+before)
									print(" * "+lines[linecount])
									if after != None: print(" * "+after)
								references[i_path] = lines[linecount]
							linecount += 1
						c += 1
			if log_level >= 0 and c > 0: print("")
			return references
		# replace str within all files.
		def replace(self, replacements:list, path=None, recursive=False, log_level=0):
			if path == None: path = self.path
			gfp = Formats.FilePath("")
			c, updates = 0, []
			for from_, to in replacements:
				if not os.path.exists(path):
					raise ValueError(f"Path {path} does not exist.")
				elif not Files.directory(path):
					raise ValueError(f"Path {path} is not a directory.")
				for path in self.paths(recursive=recursive, banned_names=[".DS_Store", ".git"], path=path):
					if not Files.directory(path):
						try:
							data = Files.load(path)
						except UnicodeDecodeError: a=1
						if from_ in data: 
							if log_level >= 0:
								loader = console.Loader(f"Updating file {path}.")
							Files.save(path, data.replace(from_, to))
							if log_level >= 0:
								loader.stop()
							updates.append(path)
							c += 1
			return updates
		# filepath shortcuts.
		def join(self, name=None, type=""):
			return self.file_path.join(name, type)
		def name(self):
			return self.file_path.name()
		def base(self):
			return self.file_path.base()
		def basename(self):
			return self.file_path.basename()
		# support default iteration.
		def __iter__(self):
			return iter(self.paths())
		# support '>=' & '>' operator.
		def __gt__(self, directory):
			if not isinstance(directory, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) > len(directory.paths())
		def __ge__(self, directory):
			if not isinstance(directory, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) >= len(directory.paths())
		# support '<=' & '<' operator.
		def __lt__(self, directory):
			if not isinstance(directory, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) < len(directory.paths())
		def __le__(self, directory):
			if not isinstance(directory, self.__class__):
				raise Exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) <= len(directory.paths())
		# support '==' & '!=' operator.
		def __eq__(self, directory):
			if not isinstance(directory, self.__class__):
				return False
			return len(self.paths()) == len(directory.paths())
		def __ne__(self, directory):
			if not isinstance(directory, self.__class__):
				return True
			return len(self.paths()) != len(directory.paths())
		# support 'in' operator.
		def __contains__(self, path):
			paths = self.paths()
			if isinstance(path, (list, Files.Array)):
				for i in path:
					if i in paths:
						return True
				return False
			else:
				return path in paths
		# representation.
		def __repr__(self):
			return str(self)
			#
		# system functions.
		def __str__(self):
			return str(self.fp.path)
		# content count.
		def __len__(self):
			return len(self.paths())
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Directory"
			#
		@property
		def __name__(self):
			return self.instance()
		# return raw data.
		def raw(self):
			return self.fp.path
	#
	# the image object class.
	class Image(object):
		def __init__(self, path=None, image=None, load=False):

			# docs.
			DOCS = {
				"module":"Image", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# init.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			self.image = image
			if load: self.load()

			#
		def load(self, path=None):
			if path == None: path = self.file_path.path
			self.image = Image.open(path)
		def edit_pixel(self, pixel=[0, 0], new_pixel_tuple=None):
			pixel = self.image.load()
			pix[15, 15] = value
			self.image.save(self.file_path.path)
		def convert(self, 
			# the input path (str, FilePath) (#1).
			output=None,
			# the input path (str, FilePath) (leave None to use self.fp.path)
			input=None,
		):
			if input == None: input = self.fp.path
			if output == None:
				raise Exceptions.InvalidUsage("Define parameter: [output].")
			img = _Image_.open(str(input))
			img.save(str(output))
			print(f"Successfully converted image {input} to {output}.")
		def replace_pixels(self, input_path=None, output_path=None, input_hex=None, output_hex=None):
			img = _Image_.open(input_path)
			pixels = img.load()
			input_rgb, output_rgb = input_hex, output_hex # self.hex_to_rgb(input_hex), self.hex_to_rgb(output_hex)
			for i in range(img.size[0]): 
				for j in range(img.size[1]):
					print(pixels[i,j], "VS", input_rgb)
					if pixels[i,j] == input_rgb:
						pixels[i,j] = output_rgb
			img.save(output_path)
		def replace_colors(self, input_path=None, output_path=None, hex=None):
			img = _Image_.open(input_path)
			pixels = img.load()
			rgb = hex #self.hex_to_rgb(hex)
			for i in range(img.size[0]):
				for j in range(img.size[1]):
					if pixels[i,j] != rgb and pixels[i,j] != (0, 0, 0, 0):
						pixels[i,j] = rgb
			img.save(output_path)
		def rgb_to_hex(self, tuple):
			return '#%02x%02x%02x' % tuple
		def hex_to_rgb(self, _hex_):
			return tuple(int(_hex_[i:i+2], 16) for i in (0, 2, 4))
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Image"
			#
		@property
		def __name__(self):
			return self.instance()
		# return raw data.
		def raw(self):
			return self.fp.path
		# suport eq.
		def __eq__(self, var):
			if var.__class__.__name__ in ["NoneType"]:
				return False
			else:
				return str(var) == str(self)
		def __ne__(self, var):
			if var.__class__.__name__ in ["NoneType"]:
				return True
			else:
				return str(var) != str(self)
		# repr.
		def __str__(self):
			return str(self.fp)
		def __repr__(self):
			return str(self)
		#
	#
	# the zip object class.
	class Zip(object):
		def __init__(self, path=None, check=False):
			
			# docs.
			DOCS = {
				"module":"Zip", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# init.
			self.file_path = self.fp = Formats.FilePath(path, check=check)

			#
		def create(self,
			# source can either be a string or an array.
			source=None, 
			# remove the source file(s).
			remove=False,
			# sudo required to move/copy source files.
			sudo=False,
		):

			# create tmp dir.
			name = self.file_path.name().replace('.encrypted.zip','').replace("."+self.file_path.extension(),'')
			tmp = Formats.FilePath(f'/tmp/zip-{utils.generate.shell_string(24)}')
			tmp_content = Formats.FilePath(tmp.join(name, ""))
			if tmp.exists(): tmp.delete(forced=True)
			if os.path.exists(tmp.path):os.system(f"rm -fr {tmp.path}")
			os.system(f"mkdir -p {tmp.path}")
			if isinstance(source, str):
				target = Formats.FilePath(source)
				name = target.name().replace('.encrypted.zip','').replace("."+target.extension(),'')
				if remove: target.move(tmp_content.path, sudo=sudo)
				else: target.copy(tmp_content.path, sudo=sudo)
			elif isinstance(source, list):
				tmp_content.create(directory=True)
				for path in source:
					file_path = Formats.FilePath(path)
					if remove: file_path.move("/"+tmp_content.join('/'+file_path.name(),"/"), sudo=sudo)
					else: file_path.copy("/"+tmp_content.join('/'+file_path.name(),"/"), sudo=sudo)
			else: raise ValueError("Parameter [source] must either be a str or list.")

			# write out zip.
			base = self.file_path.base()
			format = self.file_path.extension()
			archive_from = os.path.dirname(tmp_content.path)
			archive_to = os.path.basename(tmp_content.path.strip(os.sep))
			zip_path = shutil.make_archive(name, format, archive_from, archive_to)
			os.system(f'mv {zip_path} {self.file_path.path}')
			tmp.delete(forced=True, sudo=sudo)

			#
		def extract(self, 
			# the base extract directory.
			base=None, 
			# remove the zip after extraction.
			remove=False,
			# if sudo required for removing file path.
			sudo=False,):

			# extract.
			if base == None:
				base = self.file_path.base()
			with zipfile.ZipFile(self.file_path.path, 'r') as zip_ref:
				zip_ref.extractall(base)
			if remove: self.file_path.delete(forced=True, sudo=sudo)
			
			#
		# representation.
		def __repr__(self):
			return str(self)
			#
		# system functions.
		def __str__(self):
			return self.fp.path
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Zip"
			#
		@property
		def __name__(self):
			return self.instance()
		# return raw data.
		def raw(self):
			return self.fp.path
		#
	#
	# the bytes object class.
	class Bytes(object):
		def __init__(self, 
			# the bytes (param #1).
			data=b"",
			# the path (str, FilePath) (param #2).
			path=False, 
			# load the data on initialization.
			load=False, 
			# the default array (will be created if file path does not exist).
			default=None,
		):
		   	
			# docs.
			DOCS = {
				"module":"Bytes", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
		    # check self instance.
			if isinstance(data, Files.Bytes):
				data = data.bytes
			
			# bytes.
			self.bytes = bytes 
		    
		    # path.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			if default != None and not Files.exists(self.file_path.path): self.save(array=default)
			if load: self.load()

			#
		def load(self, sudo=False):
			bytes = Files.load(self.file_path.path, format="bytes", sudo=sudo)
			self.bytes = bytes
			return bytes
		def save(self, bytes=None, sudo=False):
			if bytes == None: bytes = self.bytes
			bytes = Formats.denitialize(bytes)
			self.bytes = bytes
			return Files.save(self.fp.path, bytes, format="bytes", sudo=sudo)
		# suppor default iteration.
		def __iter__(self):
			return iter(self.bytes)
		# support '==' & '!=' operator.
		def __eq__(self, bytes_):
			if isinstance(bytes_, bytes):
				return self.bytes == bytes_
			elif not isinstance(bytes_, self.__class__):
				return False
			return self.bytes == bytes_.bytes
		def __ne__(self, bytes_):
			if isinstance(bytes_, bytes):
				return self.bytes != bytes_
			elif not isinstance(bytes_, self.__class__):
				return True
			return self.bytes != bytes_.bytes
		# support 'in' operator.
		def __contains__(self, bytes_):
			if isinstance(bytes_, (list, Files.Array)):
				for i in bytes_:
					if i == self.bytes:
						return True
				return False
			else:
				return bytes_ in self.bytes
			#
		# representation.
		def __repr__(self):
			return str(self)
			#
		# str representation.
		def __str__(self):
			return str(self.bytes)
		# content count.
		def __len__(self):
			return len(self.bytes)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Bytes"
			#         
		@property
		def __name__(self):
			return self.instance()
		# support self assignment.
		def assign(self, b):
			if isinstance(b, self.__class__):
				b = b.bytes
			self.bytes = b
			return self
		# return raw data.
		def raw(self):
			return self.bytes
			#

		#
	#
	#

# some default classes.
class Classes():

	# the speed class.
	class Speed():

		# the mark function, returns a timestamp used for calculation.
		def mark():
			return Date().seconds_timestamp
			#

		# calculate the difference between the marked timestamp & the current.
		def calculate( 
			# the marked timestamp from self.mark().
			stamp, 
			# the current timestamp (leave None to use Date().seconds_timestamp)
			current=None,
		):
			if current == None: current = Date().seconds_timestamp
			return (Date(current) - Date(stamp)).to_seconds()

# some default objects.
class Objects():

	# the generate object class.
	class Generate(object):
		def __init__(self):
			
			# docs.
			DOCS = {
				"module":"Generate", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
			
			#

		def int(self, length=6):
			charset = Array(Formats.digits).string(joiner="")
			return ''.join(random.choice(charset) for x in range(length))
			#
		def string(self, length=6, capitalize=True, digits=True):
			charset = Array(Formats.alphabet).string(joiner="")
			if capitalize: charset += Array(Formats.capitalized_alphabet).string(joiner="")
			if digits: charset += Array(Formats.digits).string(joiner="")
			return ''.join(random.choice(charset) for x in range(length))
			#

	# the interval object class.
	class Interval(object):
		def __init__(self,
			# the sleep time.
			sleeptime=1,
			# the timeout.
			timeout=60,
		):

			# docs.
			DOCS = {
				"module":"Interval", 
				"initialized":False,
				"description":[], 
				"chapter": "Defaults", }
				
			# attributes.
			self.sleeptime = sleeptime
			self.timeout = timeout

			#
		def __int__(self):
			return int(self.sleeptime)
		def __iter__(self):
			l = []
			for _ in range(int(self.timeout/self.sleeptime)):
				l.append(self)
			return iter(l)
		def sleep(self, chapters=1):
			for _ in range(chapters):
				time.sleep(int(self)/chapters)
		#
		#for interval in Interval(sleeptime=60, timeout=3600):
		#	...
		#	interval.sleep()
	
	#

# shortcuts.
FilePath = Formats.FilePath 
String = Formats.String 
Boolean = Formats.Boolean 
Integer = Formats.Integer 
Date = Formats.Date

File = Files.File
Directory = Files.Directory
Zip = Files.Zip
Image = Files.Image
Bytes = Files.Bytes
Dictionary = Files.Dictionary
Array = Files.Array

Speed = Classes.Speed

Generate = Objects.Generate
Interval = Objects.Interval

# initialized objects.
gfp = Formats.FilePath("") # is required (do not remove).
gd = gdate = Formats.Date()


#
