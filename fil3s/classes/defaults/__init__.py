#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from fil3s.classes.config import *
from fil3s.classes import utils, exceptions
import time

"""
Notes.
All default files & formats must exact the same as the default dict, bool, list etc in the native sense.
There are lots additionals though. But a dict and Dictionary should be able to be used universally as if the user would not know the difference (which could very quickly in some instances).
"""

# settings.
LOG_LEVEL = utils.log_level(default=0)


# the format classes.
class Formats():
	#
	# variables.
	digits = [0,1,2,3,4,5,6,7,8,9,]
	str_digits = ["0","1","2","3","4","5","6","7","8","9"]
	alphabet, capitalized_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], []
	for i in alphabet: capitalized_alphabet.append(i.upper())
	special_characters = ["±","§","!","@","€","#","£","$","¢","%","∞","^","&","ª","(",")","–","_","+","=","{","}","[","]",";",":","'",'"',"|","\\","//","?",">",".",",","<"]
	#
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
		elif isinstance(value, Boolean): 
			if not serialize:   return Boolean
			else:               return "Boolean"
		elif isinstance(value, String): 
			if not serialize:   return String
			else:               return "String"
		elif isinstance(value, Integer): 
			if not serialize:   return Integer
			else:               return "Integer"
		elif isinstance(value, Bytes): 
			if not serialize:   return Bytes
			else:               return "Bytes"
		elif isinstance(value, Array): 
			if not serialize:   return Array
			else:               return "Array"
		elif isinstance(value, Dictionary): 
			if not serialize:   return Dictionary
			else:               return "Dictionary"
		elif isinstance(value, object): 
			if not serialize:   return object
			else:               return "object"
		else: raise ValueError(f"Unknown format [{value}].")
		#
	#
	# initialize from default format to fil3s format.
	def initialize(
		# the object / value (#1 param).
		obj=None, 
		# list / dict with objects.
		objects=None, 
		# initialize file paths.
		file_paths=False,
		# the forced format.
		format=None,
	):
		#if obj == None and objects == None: raise exceptions.InvalidUsage("Define either parameter obj (#1) or objects.")
		if objects == None:
			if format in ["file_path", "path"] or (file_paths and os.path.exists(obj)):
				if os.path.isdir(obj):
					obj = Files.Directory(path=obj)
				else:
					obj = Formats.FilePath(obj)
			elif format in [str, "str", "string"] or isinstance(obj, str):
				obj = Formats.String(obj)
			elif format in [bool, "bool", "boolean"] or isinstance(obj, bool):
				obj = Formats.Boolean(obj)
			elif format in [int, "int", "integer"] or isinstance(obj, int):
				obj = Formats.Integer(obj)
			elif format in [float, "float", "double"] or isinstance(obj, float):
				obj = Formats.Integer(obj, format="float")
			elif format in [list, "list", "array"] or isinstance(obj, list):
				obj = Files.Array(obj)
			elif format in [dict, "dict", "dictionary"] or isinstance(obj, dict):
				obj = Files.Dictionary(obj)
			return obj
		else:
			if isinstance(objects, dict) or isinstance(objects, Dictionary):
				objs = {}
				for i,default in objects.items(): 
					try:
						objs[i] = self.serialize(i, file_paths=file_paths)
					except:
						objs[i] = default
			else:
				objs = []
				for i in objects: objs.append(self.serialize(i, file_paths=file_paths))
				return objs
	# denitialize from fil3s formats to default format.
	def denitialize(
		# the object / value (#1 param).
		obj=None, 
		# list / dict with objects.
		objects=None, 
		# initialize file paths.
		file_paths=True,
	):
		#if obj == None and objects == None: raise exceptions.InvalidUsage("Define either parameter obj (#1) or objects.")
		if objects == None:
			if file_paths and isinstance(obj, Directory):
				obj = str(obj)
			elif file_paths and isinstance(obj, FilePath):
				obj = str(obj)
			elif isinstance(obj, String):
				obj = str(obj)
			elif isinstance(obj, Boolean):
				obj = bool(obj)
			elif isinstance(obj, Integer):
				obj = obj.value
			elif isinstance(obj, (list, Array)):
				new = []
				for i in obj:
					new.append(Formats.denitialize(i, file_paths=file_paths))
				obj = new
			elif isinstance(obj, (dict, Dictionary)):
				new = {}
				for k,v in obj.items():
					new[Formats.denitialize(k)] = Formats.denitialize(v, file_paths=file_paths)
				obj = new
			return obj
		else:
			if isinstance(objects, dict) or isinstance(objects, Dictionary):
				objs = {}
				for i,default in objects.items(): 
					try:
						objs[Formats.denitialize(i)] = Formats.denitialize(i, file_paths=file_paths)
					except:
						objs[Formats.denitialize(i)] = default
			else:
				objs = []
				for i in objects: objs.append(Formats.denitialize(i, file_paths=file_paths))
				return objs
	#
	# the file path object class.
	class FilePath(object):
		def __init__(self, path, default=False, check=False, load=False):

			# check self instance.
			#str.__init__(self)
			if isinstance(path, Formats.FilePath):
				path = path.path
			elif isinstance(path, Formats.String):
				path = path.string
			else:
				path = str(path)

			# init.
			self.path = self.clean(path=path)
			if check == False and default == False and path != False:
				if os.path.isdir(self.path) and self.path[len(self.path)-1] != '/': self.path += '/'
			if check and os.path.exists(self.path) == False: raise FileNotFoundError("Path [{}] does not exist.".format(self.path))
			self.ownership = self.Ownership(path=self.path, load=load)
			self.permission = self.Permission(path=self.path, load=load)

			#
		#   -   info:
		def join(self, name=None, type="/"):
			if type not in ["", "/"] and "." not in type:
				type = "." + type
			path = self.path
			if path[len(path)-1] != "/": path += '/'
			return "{}{}{}".format(path, name, type)
		def name(self, remove_extension=False, path=None):
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
			if name == None and os.path.isdir(path): extension = 'dir'
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
			###### OLD.
			base = path.replace('//','/')
			if len(base.split("/")) <= 1: raise ValueError("Path [{}] has no base.".format(base))
			if base[len(base)-1] == '/': base = base[:-1]
			for x in range(back, back+1):
				last = (base.split('/')[len(base.split('/'))-1]).replace('//','/')
				base = base[:-len("/"+last)]
			while True:
				if '//' in base: base = base.replace('//','/')
				else: break
			if base[len(base)-1] != "/": base += '/'
			return base
			"""splitted, result, count = path.split('/'), "", 0
			for i in splitted:
				if count < len(splitted) - 1 - back:
					result += '/' + i
				else: result += "/"
				count += 1
			"""
		def basename(self, back=1, path=None):
			if path == None: path = self.path
			return self.name(path=self.base(back=back, path=path))
		def size(self, mode="auto", options=["auto", "bytes", "kb", "mb", "gb", "tb"], format=str, path=None):
			if path == None: path = self.path
			def get_directory_size1(directory):
				total_size = 0
				for path, dirs, files in os.walk(path):
					for f in files:
						fp = os.path.join(path,f)
						try: total_size += os.path.getsize(fp)
						except: a=1
				return total_size
			#dirs_dict = {}
			#for root, dirs, files in os.walk(path ,topdown=False):
			#   size = sum(os.path.getsize(os.path.join(root, name)) for name in files) 
			#   try: subdir_size = sum(dirs_dict[os.path.join(root,d)] for d in dirs)
			#   except KeyError:
			#       dirs_dict[os.path.join(root,d)] = 0
			#       subdir_size = sum(dirs_dict[os.path.join(root,d)] for d in dirs)
			#   total_size = size + subdir_size
			def get_directory_size2(directory):
				total = 0
				try:
					# print("[+] Getting the size of", directory)
					for entry in os.scandir(directory):
						if entry.is_file():
							# if it's a file, use stat() function
							total += entry.stat().st_size
						elif entry.is_dir():
							# if it's a directory, recursively call this function
							total += get_directory_size2(entry.path)
				except NotADirectoryError:
					# if `directory` isn't a directory, get the file size then
					return os.path.getsize(directory)
				except PermissionError:
					# if for whatever reason we can't open the folder, return 0
					return 0
				return total
			total_size = get_directory_size2(path)
			if mode == "auto":
				if int(total_size/1024**4) >= 10:
					total_size = '{:,} TB'.format(int(round(total_size/1024**4,2))).replace(',', '.')
				elif int(total_size/1024**3) >= 10:
					total_size = '{:,} GB'.format(int(round(total_size/1024**3,2))).replace(',', '.')
				elif int(total_size/1024**2) >= 10:
					total_size = '{:,} MB'.format(int(round(total_size/1024**2,2))).replace(',', '.')
				elif int(total_size/1024) >= 10:
					total_size = '{:,} KB'.format(int(round(total_size/1024,2))).replace(',', '.')
				else:
					total_size = '{:,} Bytes'.format(int(int(total_size))).replace(',', '.')
			elif mode == "bytes" or mode == "bytes".upper(): total_size = '{:,} Bytes'.format(int(total_size)).replace(',', '.') 
			elif mode == "kb" or mode == "kb".upper(): total_size = '{:,} KB'.format(int(round(total_size/1024,2))).replace(',', '.') 
			elif mode == "mb" or mode == "mb".upper(): total_size = '{:,} MB'.format(int(round(total_size/1024**2,2))).replace(',', '.') 
			elif mode == "gb" or mode == "gb".upper(): total_size = '{:,} GB'.format(int(round(total_size/1024**3,2))).replace(',', '.') 
			elif mode == "tb" or mode == "tb".upper(): total_size = '{:,} TB'.format(int(round(total_size/1024**4,2))).replace(',', '.') 
			else: __error__("selected an invalid size mode [{}], options {}.".format(mode, options))
			if format in [int, "int", "integer", "Integer", Integer]:
				return int(total_size.split(" ")[0])
			else: return total_size 
		def exists(self, 
			# the path (leave None to use self.path) (#1).
			path=None,
			# root permission required.
			sudo=False,
		):
			if path == None: path = self.path
			path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
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
			path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
			return os.path.isdir(path)
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
			return path
		def absolute(self, 
			# the path (leave None to use self.path) (param #1).
			path=None,
		):
			if path == None: path = self.path
			return os.path.abspath(path)
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
				if os.path.isdir(path): options = " -fr "
			elif os.path.isdir(path): options = " -r "
			os.system(f"{sudo}rm{options}{path}{silent}")
		def move(self, path=None, sudo=False, silent=False):
			if path == None: raise exceptions.InvalidUsage("Define parameter: [path].")
			if silent: silent = ' 2> /dev/null'
			else: silent = ""
			if sudo: sudo = "sudo "
			else: sudo = ""
			os.system(f"{sudo}mv {self.path} {path}{silent}")
			self.path = gfp.clean(path=path)
		def copy(self, path=None, sudo=False, silent=False):
			if path == None: raise exceptions.InvalidUsage("Define parameter: [path].")
			if silent: silent = ' 2> /dev/null'
			else: silent = ""
			if sudo: sudo = "sudo "
			else: sudo = ""
			if self.directory(): dir = "-r "
			else: dir = ""
			os.system(f"{sudo}cp {dir}{self.path} {path}{silent}")
		def open(self, sudo=False):
			if sudo: sudo = "sudo "
			else: sudo = ""
			if OS in ["macos"]: 
				os.system(f"{sudo}open {self.path}")
			elif OS in ["linux"]: 
				os.system(f"{sudo}nautulis {self.path}")
			else: utils.__invalid_os__(OS)
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
				if sudo: os.system('sudo mkdir '+self.path)
				else: os.system('mkdir '+self.path)
			
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path + path
		def __sub__(self, path):
			if isinstance(path, str):
				a=1
			elif isinstance(path, self.__class__):
				path = path.path
			elif not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path.replace(path, "")
		# support +.
		def __concat__(self, path):
			if isinstance(path, str):
				a=1
			elif isinstance(path, self.__class__):
				path = path.path
			elif not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {path.__class__}.")
			return self.path + path
		# support default iteration.
		def __iter__(self):
			return iter(self.path)
		# support '>=' & '>' operator.
		def __gt__(self, path):
			if not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) > len(path.path)
		def __ge__(self, path):
			if not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) >= len(path.path)
		# support '<=' & '<' operator.
		def __lt__(self, path):
			if not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
			return len(self.path) < len(path.path)
		def __le__(self, path):
			if not isinstance(path, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {path.__class__}.")
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
			return self.path
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
				raise exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
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
		#   -   objects:
		class Ownership(object):
			def __init__(self, path=None, load=False):
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
				group = grp.getgrgid(os.stat(path).st_gid).gr_name
				return owner, group
			def set(self, owner=None, group=None, sudo=False, recursive=False, silent=False, path=None):
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
				if recursive and iterate and os.path.isdir(self.path):
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
			def set(self, permission=None, sudo=False, recursive=False, silent=False, path=None):
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
				if recursive and iterate and os.path.isdir(path):
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
	#   
	# the string object class.
	class String(object):
		def __init__(self, string=""):

			# check self instance.
			#str.__init__(self)
			if isinstance(string, Formats.String):
				string = string.string
			elif isinstance(string, Formats.FilePath):
				string = string.path
			else:
				string = str(string)
			

		   # init.
			self.string = string
			# can be filled with executing [self.x = x()]:
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
			if string == None: string = self.string
			s, open, opened = "", 0, False
			for i in string:
				if i == identifiers[0]:
					open += 1
				elif i == identifiers[1]:
					open -= 1
				if open >= depth:
					if include or open == depth: s += i
					opened = True
				if opened and open < depth:
					if include: s += i
					break
			return Formats.String(s)
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			return self.string + string
		def __iadd__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			self.string = self.string + string
			return self
		def __sub__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
			return self.string.replace(string, "")
		def __isub__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {string.__class__}.")
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
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) > len(string)
		def __ge__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) >= len(string)
		# support '<=' & '<' operator.
		def __lt__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self.string) < len(string)
		def __le__(self, string):
			if isinstance(string, str):
				a=1
			elif isinstance(string, self.__class__):
				string = string.string
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
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
				raise exceptions.FormatError(f"Can not concat object {self.__class__} & {string.__class__}.")
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
			return self.string
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
			#	raise exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
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
				raise exceptions.FormatError(f"Can not assign object {self.__class__} & {string.__class__}.")
			self.string = string
			return self
		#
	#
	# the boolean object class.
	class Boolean(object):
		def __init__(self, boolean=False):

			# check self instance.
			if isinstance(boolean, Formats.Boolean):
				boolean = boolean.bool

		   # init.
			self.bool = boolean
			if self.bool in ["true", "True", "TRUE", True]: self.bool = True
			else: self.bool = False
			# can be filled with executing [self.x = x()]:
		def convert(self, true="True", false="False"):
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
				raise exceptions.FormatError(f"Can not assign object {self.__class__} & {boolean.__class__}.")
			self.bool = boolean
			return self
		#
	#
	# the integer object class.
	class Integer(object):
		def __init__(self, value=0, format="auto"):

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
			# self.int = double(value)

			# can be filled with executing [self.x = x()]:
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		def __sub__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not sub object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value - value)
		def __iadd__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {value.__class__}.")
			self.value += value
			return self
		def __isub__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not sub object {self.__class__} & {value.__class__}.")
			self.value -= value
			return self
		def __mod__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mod object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value % value)
		def __mul__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value * value)
		def __pow__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value ** value)
		def __div__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value / value)
		def __truediv__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value / value)
		def __floordiv__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value // value)
		def __concat__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		# support "+=" & "-=".
		def __pos__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not mul object {self.__class__} & {value.__class__}.")
			return Formats.Integer(self.value + value)
		def __matmul__(self, value):
			if isinstance(value, (int, float)):
				a=1
			elif isinstance(value, self.__class__):
				value = value.value
			elif not isinstance(value, self.__class__):
				raise exceptions.FormatError(f"Can not matmul object {self.__class__} & {value.__class__}.")
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
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value > integer
		def __ge__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value >= integer
		# support '<=' & '<' operator.
		def __lt__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
			else:
				integer = integer.value
			return self.value < integer
		def __le__(self, integer):
			if isinstance(integer, (int,float)):
				integer = integer
			elif not isinstance(integer, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {integer.__class__}.")
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
					if i == self.value:
						return True
				return False
			else:
				return string in self.string
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
				raise exceptions.FormatError(f"Could not parse a bool from {self.__id__()}.")
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
				raise exceptions.FormatError(f"Can not assign object {self.__class__} & {value.__class__}.")
			self.value = value
			return self
		#
	#
	# the date object class.
	class Date(object):
		def __init__(self):
			today = datetime.today()
			self.seconds_format = '%S'
			self.seconds = str(today.strftime(self.seconds_format))
			self.minute_format = '%M'
			self.minute =  str(today.strftime(self.minute_format))
			self.hour_format = '%H'
			self.hour =  str(today.strftime(self.hour_format))
			self.day_format = '%d'
			self.day =  str(today.strftime(self.day_format))
			self.day_name_format = '%a'
			self.day_name =  str(today.strftime(self.day_name_format))
			self.week_format = '%V'
			self.week =  str(today.strftime(self.week_format))
			self.month_format = '%m'
			self.month =  str(today.strftime(self.month_format))
			self.month_name_format = '%h'
			self.month_name = str(today.strftime(self.month_name_format))
			self.year_format = '%Y'
			self.year =  str(today.strftime(self.year_format))
			self.date_format = '%d-%m-%y'
			self.date =  str(today.strftime(self.date_format))
			self.timestamp_format = '%d-%m-%y %H:%M'
			self.timestamp =  str(today.strftime(self.timestamp_format))
			self.shell_timestamp_format = '%d_%m_%y-%H_%M'
			self.shell_timestamp =  str(today.strftime(self.shell_timestamp_format))
			self.seconds_timestamp_format = '%d-%m-%y %H:%M.%S'
			self.seconds_timestamp =  str(today.strftime(self.seconds_timestamp_format))
			self.shell_seconds_timestamp_format = '%d_%m_%y-%H_%M.%S'
			self.shell_seconds_timestamp =  str(today.strftime(self.shell_seconds_timestamp_format))
			self.time = self.hour + ":" + self.minute
		def compare(self, comparison=None, current=None, format="%d-%m-%y %H:%M"):
			comparison = self.to_seconds(comparison, format=format)
			current = self.to_seconds(current, format=format)
			if comparison >= current:
				return "future"
			elif comparison <= current:
				return "past"
			elif comparison == current:
				return "present"
			else:
				raise ValueError(f"Unexpected error, comparison seconds: {comparison} current seconds: {current}.")
		def increase(self, string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M"):
			seconds += 60*minutes
			seconds += 3600*hours
			seconds += 3600*24*days
			seconds += 3600*24*7*weeks
			s = self.to_seconds(string, format=format)
			s += seconds
			return self.from_seconds(s, format=format)
		def decrease(self, string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M"):
			seconds += 60*minutes
			seconds += 3600*hours
			seconds += 3600*24*days
			seconds += 3600*24*7*weeks
			s = self.to_seconds(string, format=format)
			s -= seconds
			return self.from_seconds(s, format=format)
		def to_seconds(self, string, format="%d-%m-%y %H:%M"):
			return time.mktime(datetime.strptime(string, format).timetuple())
			#
		def from_seconds(self, seconds, format="%d-%m-%y %H:%M"):
			return datetime.fromtimestamp(seconds).strftime(format)
			#
		def convert(self, string, input="%d-%m-%y %H:%M", output="%Y%m%d"):
			string = datetime.strptime(string, input)
			return string.strftime(ouput)
		# support default iteration.
		def __iter__(self):
			return iter([self.year, self.month, self.week, self.hour, self.minutes, self.seconds])
		# support '>=' & '>' operator.
		def __gt__(self, date):
			if not isinstance(date, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return int(self) > int(date)
		def __ge__(self, date):
			if not isinstance(date, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return int(self) >= int(date)
		# support '<=' & '<' operator.
		def __lt__(self, date):
			if not isinstance(date, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return int(self) < int(date)
		def __le__(self, date):
			if not isinstance(date, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {date.__class__}.")
			return int(self) <= int(date)
		# support '==' & '!=' operator.
		def __eq__(self, date):
			if not isinstance(date, self.__class__):
				return False
			return int(self) == int(date)
		def __ne__(self, date):
			if not isinstance(date, self.__class__):
				return True
			return int(self) != int(date)
		# support 'in' operator.
		def __contains__(self, string):
			if isinstance(string, (list, Files.Array)):
				for i in string:
					if i in self.timestamp:
						return True
				return False
			else:
				return string in self.timestamp
		# representation.
		def __repr__(self):
			return str(self)
			#
		# int representation.
		def __int__(self):
			return self.to_seconds(self.seconds_timestamp, format=self.seconds_timestamp_format)
		# float representation.
		def __float__(self):
			return float(self.to_seconds(self.seconds_timestamp, format=self.seconds_timestamp_format))
		# str representation.
		def __str__(self):
			return self.timestamp
		# content count.
		def __len__(self):
			return len(self.timestamp)
		# object id.
		def __id__(self):
			return f"({self.instance()}:{str(self)})"
		# object instance.
		def instance(self):
			return "Date"
			#
		#
	#
	#

# the files class.
class Files():
	#
	# functions.
	def join(path=None, name=None, type=""):
		if type not in ["", "/"] and "." not in type:
			type = "." + type
		if os.path.exists(path) and os.path.isdir(path) and path[len(path)-1] != "/": path += '/'
		return gfp.clean("{}{}{}".format(path, name, type), remove_double_slash=True, remove_last_slash=False)
	def load(path, data="not to be used", format="str", raw=False): # keep data as second param to prevent save load errors.
		# correct format.
		if format in [str, String, "String", "string", "file"]: format = "str"
		if format in [dict, Dictionary, "Dictionary", "dict", "array"]: format = "json"
		if format in [bytes, Bytes, "Bytes"]: format = "bytes"
		#format = str(format)
		# match format.
		path = str(path)
		data = None
		if format == "str":
			file = open(path,mode='rb')
			data = file.read().decode()
			file.close()
		elif format == "json":
			try: 
				with open(path, 'r+') as json_file:
					data = json.load(json_file)
			except PermissionError:
				with open(path, 'r') as json_file:
					data = json.load(json_file)
			except json.decoder.JSONDecodeError as e:
				e = f"Unable to decode file [{path}]. {e}."
				raise exceptions.JSONDecodeError(e)
		elif format == "bytes":
			with open(path, "rb") as file:
				data = file.read()
		else: raise ValueError(f"Unknown format {format}.")
		if raw: return data
		else: return Formats.initialize(data)
	def save(path, data, format="str", sudo=False, indent=4, ensure_ascii=False):
		# correct format.
		if format in [str, String, "String", "string", "file"]: format = "str"
		if format in [dict, Dictionary, "Dictionary", "dict", "array"]: format = "json"
		if format in [bytes, Bytes, "Bytes"]: format = "bytes"
		#format = str(format)
		# match format.
		data = Formats.denitialize(data)
		path = gfp.clean(str(path), remove_double_slash=True, remove_last_slash=False)
		if sudo:
			real_path = str(path)
			tmp_path = path = f"/tmp/{String().generate(length=12)}"
		if format == "str":
			file = open(path, "w+") 
			file.write(data)
			file.close()
		elif format == "json":
			test = json.dumps(data)
			try:
				with open(path, 'w+') as json_file:
					json.dump(data, json_file, ensure_ascii=ensure_ascii, indent=indent)
			except PermissionError:
				with open(path, 'w') as json_file:
					json.dump(data, json_file, ensure_ascii=ensure_ascii, indent=indent)
			except KeyboardInterrupt as e:
				loader = utils.Loader(f"&RED&Do not interrupt!&END& Saving file [{path}].")
				with open(path, 'w+') as json_file:
					json.dump(data, json_file, ensure_ascii=ensure_ascii, indent=indent)
				loader.stop()
				raise KeyboardInterrupt(e)
		elif format == "bytes":
			with open(path, "wb") as file:
				file.write(data)
		else: raise ValueError(f"Unknown format {format}.")
		if sudo:
			if os.path.isdir(path) and path[len(path)-1] != "/": 
				path += "/"
				if real_path[len(real_path)-1] != "/": real_path += "/"
			os.system(f"sudo rsync -aq {path} {real_path} && rm -fr {tmp_path}")
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
		if path == None: raise exceptions.InvalidUsage("Define parameter: path.")
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
		if path == None: raise exceptions.InvalidUsage("Define parameter: path.")
		if permission == None: raise exceptions.InvalidUsage("Define parameter: permission.")
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
		if path == None: raise exceptions.InvalidUsage("Define parameter: path.")
		if owner == None: raise exceptions.InvalidUsage("Define parameter: owner.")
		return gfp.ownership.set(path=path, owner=owner, group=group, recursive=recursive, sudo=sudo)
	def exists(path=None, sudo=False):
		if path == None: raise exceptions.InvalidUsage("Define parameter: path.")
		return gfp.exists(path=path, sudo=sudo)
		#
	def directory( 
		# the path (leave None to use self.path) (#1).
		path=None,
	):
		path = gfp.clean(path=path, remove_double_slash=True, remove_last_slash=True)
		return os.path.isdir(path)
		#
	#
	# the file object class.
	class File(object):
		def __init__(self, path=None, data=None, load=False, default=None):
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
		def load(self, default=None):
			utils.__check_memory_only__(str(self.file_path.path))
			if not os.path.exists(str(self.file_path.path)) and default != None: 
				self.save(data=default)
			self.data = Files.load(self.file_path.path, format=str)
			return self.data
		def load_line(self, line_number, default=None):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(str(default), self.file_path.path)
			data = Files.load(self.file_path.path, format=str)
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
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) > len(string.data)
		def __ge__(self, string):
			if not isinstance(string, str):
				return len(self) >= len(string)
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) >= len(string.data)
		# support '<=' & '<' operator.
		def __lt__(self, string):
			if not isinstance(string, str):
				return len(self) < len(string)
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
			return len(self) < len(string.data)
		def __le__(self, string):
			if not isinstance(string, str):
				return len(self) <= len(string)
			elif not isinstance(string, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {string.__class__}.")
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

			# check self instance.
			if isinstance(array, Files.Array):
				array = array.array
			elif not isinstance(array, list):
				raise exceptions.InstanceError(f"Parameter [{self.__name__}.array] must be a [Array] or [list], not [{array.__class__.__name__}].")

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
			return Files.save(path, array, format="json", indent=indent, ensure_ascii=ensure_ascii, sudo=sudo)
		def load(self, default=None):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default)
			self.array = Files.load(self.file_path.path, format="json")
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
			else: raise exceptions.InstanceError("Parameter [item] must either be None, String or Array.")
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
		# support "+", -, =-, =+" .
		def __add__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			return self.array + array
		def __iadd__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			self.array += array
			return self
		def __sub__(self, array):
			if isinstance(array, list):
				a=1
			elif isinstance(array, self.__class__):
				array = array.array
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {array.__class__}.")
			return self.array + array
		# support default iteration.
		def __iter__(self):
			return iter(self.array)
		# support '>=' & '>' operator.
		def __gt__(self, array):
			if not isinstance(array, list):
				return len(self.array) > len(array)
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) > len(array.array)
		def __ge__(self, array):
			if not isinstance(array, list):
				return len(self.array) >= len(array)
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) >= len(array.array)
		# support '<=' & '<' operator.
		def __lt__(self, array):
			if not isinstance(array, list):
				return len(self.array) < len(array)
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
			return len(self.array) < len(array.array)
		def __le__(self, array):
			if not isinstance(array, list):
				return len(self.array) <= len(array)
			elif not isinstance(array, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {array.__class__}.")
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
		# support item assignment.
		def __setitem__(self, index, value):
			#if "/" in item
			try:
				self.array[Formats.denitialize(index)] = Formats.initialize(value)
			except IndexError:
				self.array.append(Formats.initialize(value))
		def __getitem__(self, index):
			#if "/" in item
			if isinstance(index, slice):
				return self.array[Formats.denitialize(index)]
			else:
				v = self.array[Formats.denitialize(index)]
				if isinstance(v, list): return v
				return v
		def __delitem__(self, index:int):
			#if "/" in item
			return self.array.pop(index)
		# representation.
		def __repr__(self):
			return str(self)
			#
		# str representation.
		def __str__(self):
			return str(self.array)
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
							raise exceptions.InstanceError(f"Parameter [{self.__name__}.dictionary] must be a [Dictionary] or [dict], not [{dictionary.__class__.__name__}].")

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
			return Files.save(path, dictionary, format="json", indent=indent, ensure_ascii=ensure_ascii, sudo=sudo)
		def load(self, default=None):
			utils.__check_memory_only__(self.file_path.path)
			if not os.path.exists(self.file_path.path) and default != None: 
				self.save(default)
			self.dictionary = Files.load(self.file_path.path, format="json")
			return self.dictionary
		def load_line(self, line_number):
			utils.__check_memory_only__(self.file_path.path)
			data = Files.load(str(self.file_path.path))
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
			def __iterate_dict__(dictionary, default):
				#print("\niterating new dictionary: [{}] & default [{}]\n".format(dictionary, default))
				for identifier, item in default.items():
					if isinstance(item, dict):
						try: dictionary[identifier] = __iterate_dict__(dictionary[identifier], item)
						except KeyError: dictionary[identifier] = dict(item)
					elif isinstance(item, list):
						try: dictionary[identifier]
						except KeyError: dictionary[identifier] = list(item)
					else:
						try: dictionary[identifier]
						except KeyError: dictionary[identifier] = item
				return dictionary

			# init.
			if dictionary == None: dictionary = self.dictionary
			
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
			for key, value in dictionary.items():
				if key not in banned:
					format = Formats.get(value, serialize=True)
					if format in ["dict"]:
						try: ldictionary_ = dictionary_[key]
						except: ldictionary_ = {}
						value = self.append(value, overwrite=overwrite, sum=sum, banned=banned, dictionary_=ldictionary_)
					if "*" in sum or format in sum:
						if format in ["str", "int", "float", "list"]:
							try: dictionary_[key] += value
							except KeyError: dictionary_[key] = value
						else: # already summed.
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
					value = self.dictionary[key]
				except KeyError: 
					try:
						value = defaults[key]
					except KeyError: 
						set = False
				if not set:
					raise exceptions.UnpackError(f"Dictionary does not contain attribute [{key}].")
				unpacked.append(value)
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
			else: raise exceptions.InstanceError(f"Parameter [item] must either be [None], [String] or [Array], not [{item.__class__}].")
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
			reversed_dict = []
			for key in self.keys(reversed=True, dictionary=dictionary):
				reversed_dict[key] = dictionary[key]
			if update:
				self.dictionary = reversed_dict
			return reversed_dict
		def sort(self, alphabetical=True, ascending=False, reversed=False, update=True, dictionary=None):
			if dictionary == None: dictionary = self.dictionary
			new = {}
			if alphabetical or ascending:
				_sorted_ = Array(path=False, array=list(dictionary.keys())).sort(alphabetical=alphabetical, ascending=ascending, reversed=reversed)
			else: raise ValueError("Unknown behaviour, alphabetical=False.")
			for key in _sorted_:
				new[Formats.denitialize(key)] = dictionary[Formats.denitialize(key)]
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
		# system functions.
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			return self.append(dictionary=dictionary, overwrite=["*"], update=False)
		def __iadd__(self, dictionary):
			if isinstance(dictionary, dict):
				a=1
			elif isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			self.append(dictionary=dictionary, overwrite=["*"], update=True)
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
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
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			self.remove(keys=keys, update=True)
			return self
		# support +.
		def __concat__(self, string):
			if isinstance(dictionary, dict):
				a=1
			elif isinstance(dictionary, self.__class__):
				dictionary = dictionary.dictionary
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not add object {self.__class__} & {dictionary.__class__}.")
			return self.append(dictionary=dictionary, overwrite=["*"], update=False)
		# support default iteration.
		def __iter__(self):
			return iter(self.dictionary)
		# support '>=' & '>' operator.
		def __gt__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) > len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) > len(dictionary.dictionary)
		def __ge__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) >= len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) >= len(dictionary.dictionary)
		# support '<=' & '<' operator.
		def __lt__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) < len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
			return len(self.dictionary) < len(dictionary.dictionary)
		def __le__(self, dictionary):
			if isinstance(dictionary, dict):
				return len(self.dictionary) <= len(dictionary)
			elif not isinstance(dictionary, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {dictionary.__class__}.")
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
			self.dictionary[Formats.denitialize(key)] = Formats.initialize(value)
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
			del self.dictionary[key]
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
			return str(self.dictionary)
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
				if sudo: os.system('sudo mkdir '+path)
				else: os.system('mkdir '+path)

			#   -   copy files:
			commands = []
			for l_path in file_paths: 
				if sudo:
					command = None
					if os.path.isdir(l_path): command = 'sudo cp -r {0} {1} '.format(l_path, path+Formats.FilePath(l_path).name())
					else: command = 'sudo cp {0} {1}'.format(l_path, path+Formats.FilePath(l_path).name())
					commands.append(command)
				else:
					command = None
					if os.path.isdir(l_path): command = 'cp -r {0} {1} '.format(l_path, path+Formats.FilePath(l_path).name())
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
		# returnable functions.
		def paths(self, dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], banned_basenames=["__pycache__"], extensions=["*"]):
			if dirs_only and files_only: raise ValueError("Both parameters dirs_only & piles_only are True.")
			if path == None: path = self.file_path.path
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
					if not dirs_only and not os.path.isdir(l_path):
						if name not in banned_names and ("*" in extensions or gfp.extension(name=name) in extensions ):
							l_banned = False
							for i in banned_basenames:
								if f"/{i}/" in l_path: l_banned = True ; break
							if l_path not in banned and not l_banned and l_path+"/" not in banned:
								paths.append(l_path)
					if not files_only and os.path.isdir(l_path):
						l_path += "/"
						if name not in banned_names and (dirs_only or "*" in extensions or "dir" in extensions ):
							l_banned = False
							for i in banned_basenames:
								if f"/{i}/" in l_path: l_banned = True ; break
							if l_path not in banned and not l_banned and l_path+"/" not in banned:
								paths.append(l_path)
			return paths
		def names(self, dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], extensions=["*"], remove_extensions=False):
			names = []
			for _path_ in self.paths(dirs_only=dirs_only, files_only=files_only, empty_dirs=empty_dirs, recursive=recursive, path=path, banned=banned, banned_names=banned_names, extensions=extensions):
				if remove_extensions:
					name = gfp.name(path=_path_)
					names.append(name[:-len(gfp.extension(name=name))])
				else:
					names.append(gfp.name(path=_path_))
			return names
		def oldest_path(self):
			files = []
			for i in os.listdir(self.file_path.path):
				if i not in [".DS_Store"]:
					path = f'{self.file_path.path}/{i}'.replace("//",'/')
					files.append(path)
			if len(files) == 0: return False
			return min(files, key=os.path.getctime)
		def random_path(self):
			files = []
			for i in os.listdir(self.file_path.path):
				if i not in [".DS_Store"]:
					path = f'{self.file_path.path}/{i}'.replace("//",'/')
					files.append(path)
			if len(files) == 0: return False
			return files[random.randrange(0, len(files))]
		def generate_path(self, length=24, type="/"):
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
		def join(self, name=None, type=""):
			return self.file_path.join(name, type)
		def contains(self, name=None, type="/", recursive=False):
			return self.join(name, type) in self.paths(recursive=recursive)
			#
		def subpath(self, fullpath):
			return self.file_path.clean(path=fullpath.replace(self.path, ""), remove_double_slash=True)
		def fullpath(self, subpath):
			return self.file_path.clean(path=f"{self.path}/{subpath}", remove_double_slash=True)
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
					directory = info["directory"] = os.path.isdir(str(path))
				if "content" in metrics:
					if directory == None: raise exceptions.InvalidUsage("Metric [directory] is required when obtaining metric [content].")
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
				raise exceptions.InvalidUsage(f'No metrics are specified, metric options: [{Array(options).string(joiner=" ")}].')
			for i in metrics:
				if i not in options:
					raise exceptions.InvalidUsage(f'Metric [{i}] is not a valid metric option, options: [{Array(options).string(joiner=" ")}].')
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

		# return references of each file that includes one of the matches.
		def find(self, matches:list, path=None, recursive=False, log_level=0):
			if path == None: path = self.path
			gfp = Formats.FilePath("")
			c, references = 0, {}
			for string in matches:
				if not os.path.exists(path):
					raise ValueError(f"Path {path} does not exist.")
				elif not os.path.isdir(path):
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
				elif not os.path.isdir(path):
					raise ValueError(f"Path {path} is not a directory.")
				for path in self.paths(recursive=recursive, banned_names=[".DS_Store", ".git"], path=path):
					if not os.path.isdir(path):
						try:
							data = Files.load(path)
						except UnicodeDecodeError: a=1
						if from_ in data: 
							if log_level >= 0:
								loader = utils.Loader(f"Updating file {path}.")
							Files.save(path, data.replace(from_, to))
							if log_level >= 0:
								loader.stop()
							updates.append(path)
							c += 1
			return updates
		# support default iteration.
		def __iter__(self):
			return iter(self.paths())
		# support '>=' & '>' operator.
		def __gt__(self, directory):
			if not isinstance(directory, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) > len(directory.paths())
		def __ge__(self, directory):
			if not isinstance(directory, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) >= len(directory.paths())
		# support '<=' & '<' operator.
		def __lt__(self, directory):
			if not isinstance(directory, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
			return len(self.paths()) < len(directory.paths())
		def __le__(self, directory):
			if not isinstance(directory, self.__class__):
				raise exceptions.FormatError(f"Can not compare object {self.__class__} & {directory.__class__}.")
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
	#
	# the image object class.
	class Image(object):
		def __init__(self, path=None, image=None, load=False):
			# init.
			if path == False: self.file_path = self.fp = None # used in local memory (not fysical)
			else: self.file_path = self.fp = Formats.FilePath(path)
			self.image = image
			if load: self.load()
		def load(self, path=None):
			if path == None: path = self.file_path.path
			self.image = Image.open(path)
		def edit_pixel(self, pixel=[0, 0], new_pixel_tuple=None):
			pixel = self.image.load()
			pix[15, 15] = value
			self.image.save(self.file_path.path)
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
		#
	#
	# the zip object class.
	class Zip(object):
		def __init__(self, path=None, check=False):
			
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
			os.system(f"mkdir {tmp.path}")
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
		#
		#
	#
	# the bytes object class.
	class Bytes(object):
		def __init__(self, 
			# the bytes (param #1).
			data=b"",
			# the file path.
			path=None,
		):
		   
		   # check self instance.
			if isinstance(data, Files.Bytes):
				data = data.bytes

		   # init.
			if path in [None, False]:
				self.file_path = self.fp = None
			else:
				self.file_path = self.fp = Formats.FilePath(path)
			self.bytes = bytes  
			
			#
		def load(self):
			bytes = Files.load(self.file_path.path, format="bytes")
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
		#
		#
	#
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

# initialized objects.
gfp = Formats.FilePath("") # is required (do not remove).
gd = gdate = Formats.Date()

#