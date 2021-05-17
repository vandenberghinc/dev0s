#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_
from dev0s.classes.defaults.objects import *
from dev0s.classes import database as _database_
import getpass

# lib imports.
from dev0s.classes.encryption import aes

# the agent object class.
class Agent(Traceback):
	def __init__(self,
		# the encryption & webserver's id (str).
		id="dev0s-agent",
		# the path to the encrypted database (str, String, FilePath).
		database=None,
		# the webserver's host (str).
		host="127.0.0.1",
		# the webserver's port (int).
		port=56000,
		# the path to the private key / the raw private key (str).
		private_key=None,
		# the path to the public key / the raw public key (str).
		public_key=None,
		# the passphrase (optional to prompt) (str).
		passphrase=None,
		# the encryption key in memory only (enable when you passed the private_key & public_key in raw format and the file path) (bool).
		memory=False,
		# the interactive mode (prompt for password) (bool).
		interactive=True,
		# the object traceback (str).
		traceback="dev0s.encryption.Agent",
	):

		# docs.
		DOCS = {
			"module":"dev0s.encryption.Agent", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# traceback.
		Traceback.__init__(self, traceback=traceback)

		# checks.
		response = _response_.parameters.check(
			traceback=self.__traceback__(),
			parameters={
				"id:str,String":id,
				"database:str,String,FilePath":database,
				"host:str,String":host,
				"port:str,String,int,Integer":port,
				"private_key:str,String":private_key,
				"public_key:str,String":public_key,
				#"passphrase:str,String":passphrase,
				"memory:bool,Boolean":memory,
				"interactive:bool,Boolean":interactive,
				"traceback:str,String":traceback,
			})
		if not response.success: response.crash()

		# check instances.
		if not Files.exists(str(database)):
			_response_.log(f"{color.orange}Root permission{color.end} required to create database [{database}].")
			Files.create(str(database), sudo=True, permission=700, owner=defaults.vars.owner, group=defaults.vars.group, directory=True)


		# init.
		self.id = str(id)
		self.host = str(host)
		self.port = int(port)
		self.private_key = private_key
		self.public_key = public_key
		self.memory = bool(memory)
		self.passphrase = passphrase
		self.interactive = bool(interactive)
		self.db_path = str(database)

		# vars.
		self._activated = False

		# objects.
		self.webserver = _database_.WebServer(
			id=self.id,
			host=self.host,
			port=self.port,
		)
		self.aes = self.encryption = aes.AsymmetricAES(
			public_key=self.public_key,
			private_key=self.private_key,
			passphrase=self.passphrase,
			memory=self.memory,)
		self.db = self.database = aes.Database(path=str(self.db_path), aes=self.encryption)

		#

	# generate encryption.
	def generate(self,
		# the passphrase (optional to prompt) (str).
		passphrase=None,
		# the verify passphrase (optional).
		verify_passphrase=None,
		# interactive (optional).
		interactive=None
	):

		# checks.
		if passphrase == None: passphrase = self.passphrase
		if interactive == None: interactive = self.interactive
		if passphrase == None:
			if not interactive:
				return _response_.error(self.__traceback__(function="generate")+": Define parameter [passphrase].")
			else:
				passphrase = getpass.getpass(f"Enter the passphrase of the {self.id} encryption:")
		elif len(passphrase) < 8: 
			return _response_.error("The passphrase must contain at least 8 characters.")
		elif passphrase.lower() == passphrase: 
			return _response_.error("The passphrase must contain capital characters.")
		elif (interactive and passphrase != getpass.getpass("Enter the same passphrase:")) or (verify_passphrase != None and passphrase != verify_passphrase): 
			return _response_.error("The passphrase must contain at least 8 characters.")

		# check webserver.
		if not self.webserver.running:
			#if not interactive:
			#	return _response_.error(f"{self.traceback}: The webserver is not running.")
			#else:
			if defaults.options.log_level >= 1: _response_.log(f"{ALIAS}: forking {self.id} webserver.")
			response = self.webserver.fork()
			if not response.success: return response

		# generate.
		self.encryption.rsa.passphrase = passphrase
		response = self.encryption.generate_keys()
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while generating the master encryption key: {response['error']}")
		self.passphrase = passphrase
		if self.memory:
			self.encryption.rsa.private_key = response.private_key
			self.encryption.rsa.public_key = response.public_key
		response = self.encryption.load_keys()
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while activating the {self.id} encryption: {response['error']}")

		# cache.
		response = self.webserver.set(group="passphrases", id="master", data=passphrase)
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while caching the passphrase (#1): {response['error']}")

		# database.
		self.db = aes.Database(path=str(self.db_path), aes=self.encryption)
		response = self.db.activate()
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while activating the encrypted cache: {response['error']}")

		# hander.
		return _response_.success("Successfully generated the encryption.")

		#

	# activate encryption.
	def activate(self,
		# the key's passphrase (optional to retrieve from webserver) (str).
		passphrase=None,
		# interactive (optional) 
		interactive=None,
	):
		if passphrase == None: passphrase = self.passphrase
		if interactive == None: interactive = self.interactive
		new = False
		if passphrase in [False, None, "", "null", "None", "none"]:
			
			# check webserver.
			if not self.webserver.running:
				if not interactive:
					return _response_.error(f"{self.traceback}: The webserver is not running.")
				else:
					if defaults.options.log_level >= 1: _response_.log(f"{ALIAS}: forking {self.id} webserver.")
					response = self.webserver.fork()
					if not response.success: return response

			# get pass.
			response, passphrase = self.webserver.get(group="passphrases", id="master"), None
			if not response.success and "There is no data cached for" not in response["error"]: return response
			elif response["success"]: passphrase = response["data"]
			if passphrase in [False, None, "", "null", "None", "none"]:
				if not interactive:
					return _response_.error(self.__traceback__(function="activate")+": Define parameter [passphrase].")
				else:
					new = True
					passphrase = getpass.getpass(f"Enter the passphrase of the {self.id} encryption:")

		# activate.
		self.encryption.rsa.passphrase = passphrase
		response = self.encryption.load_keys()
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while activating the {self.id} encryption: {response['error']}")
		self.passphrase = passphrase
		self.db.aes.rsa.passphrase = passphrase
		response = self.db.activate()
		if not response["success"]: 
			return _response_.error(f"Encoutered an error while activating the encrypted cache: {response['error']}")

		# chache.
		if new:
			response = self.webserver.set(group="passphrases", id="master", data=passphrase)
			if not response["success"]: 
				return _response_.error(f"Encoutered an error while caching the passphrase (#2): {response['error']}")

		# handler.
		return _response_.success("Successfully activated the encryption.")

		#

	# copy functions (only these!).
	def encrypt(self, string, decode=False):
		return self.encryption.encrypt(string, decode=decode)
		#
	def decrypt(self, string, decode=False):
		return self.encryption.decrypt(string, decode=decode)
		#

	# properties.
	@property
	def activated(self):
		return self.encryption.activated and self.db.aes.activated
		#
	@property
	def public_key_activated(self):
		return self.encryption.public_key_activated and self.db.aes.public_key_activated
		#
	@property
	def private_key_activated(self):
		return self.encryption.private_key_activated and self.db.aes.private_key_activated
		#
	@property
	def generated(self):
		if self.memory:
			return self.encryption.rsa.private_key != None and self.encryption.rsa.public_key != None
		else:
			return self.encryption.rsa.private_key != None and self.encryption.rsa.public_key != None and Files.exists(self.encryption.rsa.private_key) and Files.exists(self.encryption.rsa.public_key)
		#

	# repr.
	def __repr__(self):
		return f"<{self.traceback} (id: {self.id}) (activated: {self.activated}) (generated: {self.generated}) >"
		#

	#
	
