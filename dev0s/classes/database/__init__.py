#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.objects import *
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.defaults.exceptions import Exceptions
from dev0s.classes.response import response as _response_
from dev0s.classes.requests import requests as _requests_
from dev0s.classes import code
import requests as __requests__

# the database class.
class Database(Traceback):
	def __init__(self, 
		# the path to the directory (str) (#1)
		path=None, 
		# root permission required.
		sudo=False,
	):
		
		# docs.
		DOCS = {
			"module":"dev0s.database.Database", 
			"initialized":False,
			"description":[], 
			"chapter": "Database", }

		# traceback.
		Traceback.__init__(self, traceback="Database")

		# checks.
		if path == None: raise Exceptions.InvalidUsage(self.__traceback__()+" Define parameter [path].")

		# args.
		self.path = gfp.clean(path)
		self.sudo = sudo

		# sys args.
		self.__cache__ = {}

		# attributes.
		self.dir = self.directory = Directory(self.path)

		# checks.
		if not self.dir.fp.exists(sudo=sudo):
			if self.sudo: _response_.log(f"&ORANGE&Root permission&END& required to create database [{self.path}].")
			Files.create(str(self.path), sudo=self.sudo, directory=True, permission=700, owner=defaults.vars.user, group=defaults.vars.group,)

		# copy objects.
		self.fp = self.file_path = self.dir.fp
		self.ownership = self.fp.ownership
		self.permission = self.fp.permission

		# copy functions.
		self.join = self.dir.join
		self.subpath = self.dir.subpath
		self.fullpath = self.dir.fullpath

		#

	# load an object.
	def load(self, 
		# the sub path (str, FilePath) (#1).
		path=None, 
		# the data format [bool, str, int, float, dict, list] (str) (#2).
		format="dict", 
		# the default data (bool, str, int, float, dict, list).
		default=None,
	):
		if path == None: return _response_.error(self.__traceback__(function="load")+" Define parameter: [path].")
		path = str(path)
		subpath = path
		path = gfp.clean(f"{self.path}/{path}")
		format = self.__serialize_format__(format)
		if default != None and not Files.exists(path):
			response = self.save(path=subpath, data=default, format=format)
			if not response.success: return response
		try:
			if format in ["bytes"]:
				obj = Bytes(path=path, load=True)
			elif format in ["bool"]:
				obj = Boolean(path=path, load=True)
			elif format in ["str"]:
				obj = String(path=path, load=True)
			elif format in ["int", "float"]:
				obj = Integer(path=path, load=True)
			elif format in ["list"]:
				obj = Array(path=path, load=True)
			elif format in ["dict"]:
				obj = Dictionary(path=path, load=True)
		except Exception as e: return _response_.error(str(e))
		return _response_.success(f"Successfully loaded [{path}].", {
			"data":obj,
		})

	# save an object.
	def save(self, 
		# the sub path (str, FilePath) (#1).
		path=None, 
		# the data to save (bool, str, int, float, dict, list) (#2)
		data=None, 
		# the data format [bool, str, int, float, dict, list] (str) (#3).
		format="dict",
		# with overwrite disabled the dict format data is inserted into the existing data (bool).
		overwrite=False, 
	):
		if path == None: return _response_.error(self.__traceback__(function="save")+" Define parameter: [path].")
		if data == None: return _response_.error(self.__traceback__(function="save")+" Define parameter: [data].")
		path = str(path)
		path = gfp.clean(f"{self.path}/{path}")
		format = self.__serialize_format__(format)
		try:
			if not Files.exists(path=gfp.base(path)): Files.create(path=gfp.base(path), directory=True)
		except ValueError: a=1
		try:
			if format in ["bytes"]:
				obj = Bytes(data, path=path)
			elif format in ["bool"]:
				obj = Boolean(data, path=path)
			elif format in ["str"]:
				obj = String(data, path=path)
			elif format in ["int", "float"]:
				obj = Integer(data, path=path)
			elif format in ["list"]:
				obj = Array(data, path=path)
			elif format in ["dict"]:
				obj = Dictionary({}, path=path)
			if format in ["dict"]:
				if overwrite:
					obj.save(dictionary=data)
				else:
					if obj.fp.exists():
						obj.load()
					else:
						obj.dictionary = {}
					obj.insert(data)
					obj.save()
			else:
				obj.save()
		except Exception as e: return _response_.error(str(e))
		return _response_.success(f"Successfully saved [{path}].")

	# delete an object.
	def delete(self, 
		# the sub path (str, FilePath) (#1).
		path=None,
	):
		if path == None: return _response_.error(self.__traceback__(function="delete")+" Define parameter: [path].")
		path = gfp.clean(f"{self.path}/{path}")
		try:
			Files.delete(path=path)
		except Exception as e: return _response_.error(str(e))
		if Files.exists(path): return _response_.error(f"Failed to delete [{path}].")
		return _response_.success(f"Successfully deleted [{path}].")
	
	# get the paths of a directory.
	def paths(self,
		# the sub path (leave None to use the root path) (str FilePath)
		path=None,
		# get recursively (bool).
		recursive=False, 
		# get files only (bool).
		files_only=False,
		# get firs only (bool). 
		dirs_only=False, 
		# also get empty dirs (bool).
		empty_dirs=True, 
		# get the full path (bool).
		full_path=False,
		# the banned full paths (list).
		banned=[], 
		# the banned names (list).
		banned_names=[".DS_Store"], 
		# the banend base names (list).
		banned_basenames=["__pycache__"], 
		# the allowed extensions (list).
		extensions=["*"],
	):

		# checks.
		#if path == None: return _response_.error(self.__traceback__(function="names")+" Define parameter: [path].")
		if path == None: path = self.path
		else: path = self.join(path)
		path = str(path)
		if not Files.directory(path):
			raise dev0s.exceptions.InvalidUsage(f"Defined path [{path}] is not a directory.")

		# handler.
		paths = Directory(path).paths(
			# get recursively (bool).
			recursive=recursive,
			# get files only (bool).
			files_only=files_only,
			# get firs only (bool). 
			dirs_only=dirs_only,
			# also get empty dirs (bool).
			empty_dirs=empty_dirs,
			# the banned full paths (list).
			banned=banned,
			# the banned names (list).
			banned_names=banned_names,
			# the banend base names (list).
			banned_basenames=banned_basenames,
			# the allowed extensions (list).
			extensions=extensions, )
		if full_path:
			return paths
		else:
			_paths_ = []
			for i in paths: _paths_.append(self.subpath(i))
			return _paths_
		#

	# get the paths of a directory.
	def names(self,
		# the sub path (leave None to use the root path)
		path=None,
		# get recursively (bool).
		recursive=False, 
		# get files only (bool).
		files_only=False,
		# get firs only (bool). 
		dirs_only=False, 
		# also get empty dirs (bool).
		empty_dirs=True, 
		# remove the extension names (bool).
		remove_extensions=True,
		# the banned full paths (list).
		banned=[], 
		# the banned names (list).
		banned_names=[".DS_Store"], 
		# the banend base names (list).
		banned_basenames=["__pycache__"], 
		# the allowed extensions (list).
		extensions=["*"],
	):

		# checks.
		#if path == None: return _response_.error(self.__traceback__(function="names")+" Define parameter: [path].")
		if path == None: path = self.path
		else: path = self.join(path)
		if not Files.directory(path):
			raise dev0s.exceptions.InvalidUsage(f"Defined path [{path}] is not a directory.")

		# handler.
		return Directory(path).names(
			# get recursively (bool).
			recursive=recursive,
			# get files only (bool).
			files_only=files_only,
			# get firs only (bool). 
			dirs_only=dirs_only,
			# also get empty dirs (bool).
			empty_dirs=empty_dirs,
			# remove the extension names (bool).
			remove_extensions=remove_extensions,
			# the banned full paths (list).
			banned=banned,
			# the banned names (list).
			banned_names=banned_names,
			# the banend base names (list).
			banned_basenames=banned_basenames,
			# the allowed extensions (list).
			extensions=extensions,
		)
		#

	# representation.
	def __str__(self):
		return str(self.dir.fp.path)
	def __repr__(self):
		return str(self)

	# sys functions.
	def __serialize_format__(self, format):
		format = str(format).lower()
		if format in ["bytes", "Bytes", bytes, Bytes]: format = "bytes"
		elif format in ["bool", "Boolean", bool, Boolean]: format = "bool"
		elif format in ["string", "str", "String", str, String]: format = "str"
		elif format in ["int", "integer", int]: format = "int"
		elif format in ["float", float, Integer]: format = "float"
		elif format in ["list", "array", "Array", list, Array]: format = "list"
		elif format in ["dict", "dictionary", "Dictionary", dict, Dictionary]: format = "dict"
		if format not in ["bytes", "bool", "str", "int", "float", "dict", "list"]: raise Exceptions.InvalidUsage(f"{self.__traceback__()}: Format [{format}] is not a valid option, options: [bool, str, int, float, dict, list].")
		return format

	#

# the webserver database object class.
# keeps all info in python memory only.
class WebServer(Thread):
	def __init__(self,
		id="webserver",
		host="127.0.0.1",
		port=52379,
		sleeptime=3,
		log_level=0,
		# do not use.
		serialized={},
	):

		# docs.
		DOCS = {
			"module":"dev0s.database.WebServer", 
			"initialized":False,
			"description":[], 
			"chapter": "Database", }

		# defaults.
		Thread.__init__(self)

		# check home dir.
		for dir in [
			f"{defaults.vars.home}/.{ALIAS}",
			f"{defaults.vars.home}/.{ALIAS}/.cache",
		]:
			if not Files.exists(dir):
				Files.create(dir, directory=True, owner=defaults.vars.user, permission=700)

		# by serialization.
		if serialized != {}:
			self.assign(serialized, keys={
				"id":"webserver", 
				"host":"127.0.0.1", 
				"port":52379, 
				"sleeptime":3, 
				"log_level":0,
			})
		
		# by args.
		else:
			self.id = id
			self.host = host
			self.port = port
			self.sleeptime = sleeptime
			self.log_level = log_level

		# check parameters.
		_response_.parameters.check(
		    # the parameters (dict) (#1).
		    parameters={
		    	"id:str,String":self.id,
		    	"host:str,String":self.host,
		    	"port:str,String,int,float,Integer":self.port,
		    	"sleeptime:str,String,int,float,Integer":self.sleeptime,
		    	"log_level:str,String,int,float,Integer":self.log_level,
		    },
		    # the traceback id.
		    traceback=self.__traceback__(),).crash(error_only=True)

		# attribibutes.
		self.cache = {}
		self.system_cache = Database(path=Files.join(defaults.vars.home, f"/.{ALIAS}/.cache/{self.id}/")) # only used for tokens, rest is stored in python memory only.

		# checks.
		self.log_level = int(self.log_level)
		self.port = int(self.port)
		self.sleeptime = int(self.sleeptime)
		self.id = self.id.replace(" ","-")
		self.tag = self.id.replace(" ","_")

		#
	
	# cache functions.
	def set(self, group=None, id=None, data=None, timeout=3):
		encoded = _requests_.encode({
			"group":group.replace(" ","_"),
			"id":id.replace(" ","_"),
			"data":data,
			"token":self.token,
			"cache":self.system_cache.path,
			"cache_id":self.id,
		})
		try:
			response = __requests__.get(f'http://{self.host}:{self.port}/set?{encoded}', timeout=timeout)
		except Exception as e:
			return _response_.error(f"Failed to connect with {self.host}:{self.port}, error: {e}")
		try:
			response = self.__serialize__(response.json())
		except:
			return _response_.error(f"Failed to serialize {response}: {response.text}")
		return _response_.response(response)
	def get(self, group=None, id=None, timeout=3):
		encoded = _requests_.encode({
			"group":group.replace(" ","_"),
			"id":id.replace(" ","_"),
			"token":self.token,
			"cache":self.system_cache.path,
			"cache_id":self.id,
		})
		try:
			response = __requests__.get(f'http://{self.host}:{self.port}/get?{encoded}', timeout=timeout)
		except Exception as e:
			return _response_.error(f"Failed to connect with {self.host}:{self.port}, error: {e}")
		try:
			response = self.__serialize__(response.json())
		except:
			return _response_.error(f"Failed to serialize {response}: {response.text}")
		return _response_.response(response,)
		#

	# flask app.
	def app(self):
		app = flask.Flask(__name__)
		cli = sys.modules['flask.cli']
		cli.show_server_banner = lambda *x: None
		@app.route('/get')
		def get():
			token = flask.request.args.get('token')
			if token != Database(path=flask.request.args.get('cache')).load(Files.join(flask.request.args.get('cache_id'), "token")):
				return _response_.error(f"Provided an invalid token {token}.").json()
			group = flask.request.args.get('group')
			id = flask.request.args.get('id')
			if id in ["none", "null", "None"]: id = None
			try:
				if id == None:
					tag = f"{group}"
					value = self.cache[group]
				else:
					tag = f"{group}:{id}"
					value = self.cache[group][id]
			except KeyError:
				return _response_.error(f"There is no data cached for {tag}.").json()
			return _response_.success(f"Successfully retrieved {tag}.", {
				"group":group,
				"id":id,
				"data":value,
			}).json()
		@app.route('/set')
		def set():
			token = flask.request.args.get('token')
			if token != Database(path=flask.request.args.get('cache')).load(Files.join(flask.request.args.get('cache_id'), "token")):
				return _response_.error(f"Provided an invalid token {token}.").json()
			group = flask.request.args.get('group')
			id = flask.request.args.get('id')
			if id in ["none", "null", "None"]: id = None
			value = flask.request.args.get('data')
			if id == None:
				tag = f"{group}"
				self.cache[group] = value
			else:
				tag = f"{group}:{id}"
				try: self.cache[group]
				except KeyError: self.cache[group] = {}
				self.cache[group][id] = value
			return _response_.success(f"Successfully cached {tag}.").json()
		@app.route('/active')
		def active():
			token = flask.request.args.get('token')
			if token != Database(path=flask.request.args.get('cache')).load(Files.join(flask.request.args.get('cache_id'), "token")):
				return _response_.error(f"Provided an invalid token {token}.").json()
			return _response_.success(f"Active.").json()
		#def run__(self, app, host, port):
		#	app.run(host=host, port=port)
		#self.process = multiprocessing.Process(target=app.run, args=(self, app, self.host,self.port,))
		#self.process.start()
		app.run(host=self.host, port=self.port)
		#

	# control functions.
	def run(self):
		self.system_cache.save(path=f"{self.id}/daemon", data="*running*", format="str")
		self.system_cache.save(path=f"{self.id}/token", data=String().generate(length=64, digits=True, capitalize=True), format="str")
		self.app()
		self.system_cache.save(path=f"{self.id}/daemon", data="*stopped*", format="str")
	def fork(self, timeout=15, sleeptime=1):
		if self.running:
			return _response_.success(f"The {self.id} is already running.")
		if self.log_level <= 0:
			print(f"Starting the {self.id}.")
		serialized = self.dict(keys={
			"id":"webserver", 
			"host":"127.0.0.1", 
			"port":52379, 
			"sleeptime":3, 
			"log_level":0,
		})
		for i in ["__cache__", "cache", "system_cache" ,"_stder", "_traceback_", "_name", "_daemonic", "_ident", "_native_id", "_tstate_lock", "_started", "_stderr", "_initialized", "_invoke_excepthook", "__status__", "__running__", "__response__", "_is_stopped", "_args", "_kwargs", "_target", "_raw_traceback_",]:
			try: del serialized[i]
			except: a=1
		serialized = f"{serialized}"
		command = [str(defaults.vars.executable), f"{SOURCE_PATH}classes/database/fork.py", "--serialized", f"'{serialized}'", "--dev0s-webserver-tag", self.tag]
		if self.log_level < 0:
			command += [ "2>", "/dev/null"]
		p = subprocess.Popen(command)
		success = False
		for i in range(int(timeout/sleeptime)):
			if self.running:
				success = True
				break
			time.sleep(sleeptime)
		if success:
			return _response_.success(f"Successfully started the {self.id}.")
		else:
			return _response_.error(f"Failed to start the {self.id}.")
	def stop(self):
		if not self.running: 
			return _response_.success(f"{self.__traceback__(function='stop')}: The {self.id} is not running.")
		processes = code.processes(includes=f"--dev0s-webserver-tag {self.tag}")
		if not processes.success: return response
		if len(processes.processes) <= 1:
			return _response_.error(f"Unable to find the pid of the {self.id}.")
		for pid, info in processes.processes.items():
			if info["process"] not in ["grep"]:
				response = code.kill(pid=pid)
				if not response.success: return response
		return _response_.error(f"Successfully stopped the {self.id}.")
		#

	# threading functions.
	def start_thread(self, thread, group="daemons", id=None):
		response = self.set(group=group, id=id, data=thread)
		if not response.success: return response
		response = thread.start()
		if response != None:
			try: success = bool(response["success"])
			except: success = True
			if not success: return response
		try:
			id = thread.id
		except:
			id = str(thread)
		return _response_.success(f"Successfully started [{id}].")
	def get_thread(self, group="daemos", id=None):
		response = self.get(group=group, id=id)
		if not response.success: 
			if "There is no data cached for" in response.error:
				return _response_.error(f"There is no thread cached for (group: {group}), (id: {id}).")
			else: return response
		thread = response.data
		return _response_.success(f"Successfully retrieved thread [{thread}].", {
			"thread":thread,
		})
		#

	# properties.
	@property
	def token(self):
		if random.randrange(1, 100) <= 5: 
			response = self.system_cache.save(path=f"{self.id}/token", data=String().generate(length=64, digits=True, capitalize=True), format="str")
			if not response.success: response.crash()
		response = self.system_cache.load(path=f"{self.id}/token", format="str")
		if response.success and "None" not in str(response.data):
			return response.data
		else:
			response = self.system_cache.save(path=f"{self.id}/token", data=String().generate(length=64, digits=True, capitalize=True), format="str")
			if not response.success: response.crash()
		response = self.system_cache.load(path=f"{self.id}/token", format="str")
		if response.success and "None" not in str(response.data):
			return response.data
		else: 
			if response.error == None:
				response.error = f"Failed to create a token for webserver [{self.id}] ({self.system_cache.join(self.id+'/token')})."
			response.crash()
	@property
	def running(self):
		return self.__running__()
	def __running__(self, timeout=3):
		encoded = _requests_.encode({
			"token":self.token,
			"cache":self.system_cache.path,
			"cache_id":self.id,
		})
		try:
			__requests__.get(f'http://{self.host}:{self.port}/active?{encoded}', timeout=timeout)
			return True
		except __requests__.exceptions.ConnectionError:
			return False
		#

	# system functions.
	def __serialize__(self, dictionary, safe=False):
		if isinstance(dictionary, (Dictionary, dict)):
			new = {}
			for key, value in dictionary.items():
				if value in ["False", "false"]: new[key] = False
				elif value in ["True", "true"]: new[key] = True
				elif value in ["None", "none", "null", "nan"]: new[key] = None
				elif isinstance(value, (dict, Dictionary, list, Array)):
					new[key] = self.__serialize__(value, safe=safe)
				elif isinstance(value, object):
					if not safe:
						new[key] = value
				else:
					try: 
						int(value)
						new[key] = int(value)
					except: 
						new[key] = value
			return new
		if isinstance(dictionary, (Dictionary, dict)):
			new = []
			for value in dictionary:
				if value in ["False", "false"]: new.append(False)
				elif value in ["True", "true"]: new.append(True)
				elif value in ["None", "none", "null", "nan"]: new.append(None)
				elif isinstance(value, (dict, Dictionary)):
					new.append(self.__serialize__(value, safe=safe))
				elif isinstance(value, object):
					if not safe:
						new.append(value)
				else:
					try: 
						int(value)
						new.append(int(value))
					except: 
						new.append(value)
			return new
		else: raise ValueError(f"Parameter [dictionary] requires to be a [dict, Dictionary, list, Array], not [{dictionary.__class__.__name__}].")

	#

#
			
