#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_
from dev0s.classes.defaults.objects import *
from dev0s.classes import utils
from dev0s.classes import console

# new imports.
import zlib, base64, binascii, glob
from Crypto.PublicKey import RSA as _RSA_
from Crypto.Cipher import PKCS1_OAEP

# inc imports.
from dev0s.shortcuts import *

# the encryption class.
class RSA(object):
	def __init__(self, 
		# option 1:
		# 	the key directory.
		directory=None,
		# option 2:
		public_key=None,
		private_key=None,
		memory=False, # enable memory when the keys are not saved.
		# the key's passphrase (Leave None for no passphrase).
		passphrase=None,
	):

		# docs.
		DOCS = {
			"module":"dev0s.encryption.RSA", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# defaults.
		self.passphrase = passphrase
		self.memory = memory
		self.private_key_object = None
		self.public_key_object = None
		
		# options.
		if self.memory:
			self.directory = False
			self.id = public_key
			self.private_key_data = self.private_key = private_key
			self.public_key_data = self.public_key = public_key
		else:
			if directory != None:
				self.id = directory
				self.directory = directory
				self.private_key = directory+"/private_key.pem"
				self.public_key = directory+"/public_key.pem"
			else:
				self.directory = FilePath(private_key).base()
				self.private_key = private_key
				self.public_key = public_key
				self.id = str(self.public_key)

		#
			
	# key management.
	def generate_keys(self, log_level=0):

		# set dir,
		directory = str(self.directory)
		private_key_path = str(self.private_key)
		public_key_path = str(self.public_key)

		# checks.
		if not self.memory:
			if log_level >= 0: 
				loader = console.Loader(f"Generating key {self.directory}")
			if Files.exists(private_key_path):
				loader.stop(success=False)
				return _response_.error(f"Private key [{private_key_path}] already exists.")
			if Files.exists(public_key_path):
				loader.stop(success=False)
				return _response_.error(f"Public key [{public_key_path}] already exists.")
			if not Files.exists(directory):
				Files.create(directory, directory=True)
		else:
			if log_level >= 0: loader = console.Loader("Generating key")
		
		# generate.
		key_pair = _RSA_.generate(4096, e=65537)
		public_key = key_pair.publickey()
		public_key_pem = public_key.exportKey()
		private_key_pem = None
		if self.passphrase == None: 
			private_key_pem = key_pair.exportKey()
		else:  
			private_key_pem = key_pair.exportKey(passphrase=self.passphrase)

		# save.
		if not self.memory:
			Files.create(path=directory, directory=True)
			Files.save(private_key_path, private_key_pem.decode())
			Files.save(public_key_path, public_key_pem.decode())
			Files.chmod(directory, permission=700)
			Files.chmod(private_key_path, permission=600)
			Files.chmod(public_key_path, permission=644)
		# response.
		loader.stop()
		return _response_.success(f"Successfully generated key {directory}.", {
			"private_key":private_key_pem.decode(),
			"public_key":public_key_pem.decode(),
		})

		#
	def load_keys(self):

		# load keys.
		if not self.memory:
			self.private_key_data = Files.load(self.private_key)
			self.public_key_data = Files.load(self.public_key)
		else:
			self.private_key_data = self.private_key
			self.public_key_data = self.public_key


		# initialize keys.
		try:
			if self.passphrase == None:
				self.public_key_object = _RSA_.importKey(str(self.public_key_data))
				self.private_key_object = _RSA_.importKey(str(self.private_key_data))
			else:
				self.public_key_object = _RSA_.importKey(str(self.public_key_data))
				self.private_key_object = _RSA_.importKey(str(self.private_key_data), passphrase=self.passphrase)
		except ValueError as e:
			self.public_key_object = None
			self.private_key_object = None
			if "Padding is incorrect" in str(e):
				return _response_.error("Provided an incorrect passphrase.")
			else: return _response_.error(f"ValueError: {e}")
		
		# response.
		return _response_.success("Successfully loaded the key pair.")

		#
	def load_public_key(self):

		# load keys.
		if not self.memory:
			self.public_key_data = Files.load(self.public_key)
		else:
			self.public_key_data = self.public_key

		# initialize keys.
		try:
			self.public_key_object = _RSA_.importKey(str(self.public_key_data))
		except ValueError as e:
			self.public_key_object = None
			if "Padding is incorrect" in str(e):
				return _response_.error("Provided an incorrect passphrase.")
			else: 
				return _response_.error(f"ValueError: {e}")
		
		# response.
		return _response_.success("Successfully loaded the key pair.")

		#
	def load_private_key(self):

		# load keys.
		if not self.memory:
			self.private_key_data = Files.load(self.private_key)
		else:
			self.private_key_data = self.private_key

		# initialize keys.
		if self.passphrase == None:
			try:
				self.private_key_object = _RSA_.importKey(str(self.private_key_data))
			except ValueError as e:
				self.private_key_object = None
				if "Padding is incorrect" in str(e):
					return _response_.error("Provided an incorrect passphrase.")
				else: 
					return _response_.error(f"ValueError: {e}")
				return response
		else:
			try:
				self.private_key_object = _RSA_.importKey(str(self.private_key_data), passphrase=self.passphrase)
			except ValueError as e:
				self.private_key_object = None
				if "Padding is incorrect" in str(e):
					return _response_.error("Provided an incorrect passphrase.")
				else: 
					return _response_.error(f"ValueError: {e}")
				return response
		
		# response.
		return _response_.success("Successfully loaded the key pair.")

		#
	def edit_passphrase(self, passphrase=None):
		if not self.memory:
			private_key = "/tmp/private_key"
			Files.save(private_key, self.private_key_data)
			os.system(f"chmod 700 {private_key}")
		else:
			private_key = self.private_key

		if passphrase == None:
			passphrase = '""'
		output = utils.__execute__(["ssh-keygen", "-p", "-P", f"{self.passphrase}", "-N", f"{passphrase}", "-f", f"{private_key}"])

		# response.
		if "Your identification has been saved with the new passphrase." in output:
			self.private_key_data = str(Files.load(private_key))
			if not self.memory:
				os.system(f"rm -fr {private_key}")
			self.passphrase = passphrase
			if self.passphrase == '""': self.passphrase = None
			return _response_.success(f"Successfully edit the passphrase of key [{self.id}].")
		else:
			return _response_.error(f"Failed to edit the passphrase of key [{self.id}], error: {output}.")

		#
	
	# encrypting.
	def encrypt_string(self, string, layers=1, decode=True):

		# checks.
		if not self.public_key_activated:
			return _response_.error("Can not encrypt data since the public key is not activated yet.")

		# encrypt.
		encrypted = self.__encrypt_blob__(string, self.public_key_object)

		# layers.
		if layers-1 > 0:
			return self.encrypt_string(encrypted, layers=layers-1)
		else:
			
			if decode:
				encrypted = encrypted.decode()
			return _response_.success(f"Successfully encrypted the string.", {
				"encrypted":encrypted
			})

		#
	def encrypt_file(self, path, layers=1):

		# checks.
		if not self.public_key_activated:
			return _response_.error("Can not encrypt data since the public key is not activated yet.")

		# encrypt.
		bytes = Files.load(path, format="bytes")
		encrypted = self.__encrypt_blob__(bytes, self.public_key_object)
		Files.save(path, encrypted, format="bytes")

		# layers.
		if layers-1 > 0:
			return self.encrypt_file(path, layers=layers-1)
		else:
			return _response_.success(f"Successfully encrypted file [{path}].")

		#
	def encrypt_directory(self, path, recursive=False, layers=1):


		# checks.
		if not self.public_key_activated:
			return _response_.error("Can not encrypt data since the public key is not activated yet.")

		# recursively encrypt all files.
		if recursive:

			# recursive.
			for i in os.listdir(path):
				i = f'{path}/{i}'.replace("//",'/')
				if os.path.isdir(i):
					response = self.encrypt_directory(i, recursive=True)
					if response["error"] != None:
						return response
				else:
					response = self.encrypt_file(i)
					if response["error"] != None:
						return response

			# success.
			if layers-1 > 0:
				return self.encrypt_directory(path, recursive=True, layers=layers-1)
			else:
				return _response_.success(f"Successfully encrypted directory [{path}] (recursively).")


		# encrypt the directory and save to x.encrypted.zip file.
		else:

			# checks.
			file_path = FilePath(path)
			if not file_path.exists():
				return _response_.error(f"Directory [{path}] does not exist.")
			if not file_path.directory():
				return _response_.error(f"Directory path [{path}] is not a directory.")

			# create zip.
			if path[len(path)-1] == "/": zip_path = path[:-1]
			else: zip_path = str(path)
			zip_path = f'{zip_path}.encrypted.zip'
			zip = Zip(path=zip_path)
			zip.create(source=path)

			# encrypt zip.
			response = self.encrypt_file(zip.file_path.path, layers=layers)
			if response["success"]:
				file_path.delete(forced=True)
				return response
			else:
				zip.file_path.delete(forced=True)
				return _response_.error(f"Failed to encrypted directory [{path}].")
				

		#
	
	# decrypting.
	def decrypt_string(self, string, layers=1, decode=True):
		
		# checks.
		if not self.private_key_activated:
			return _response_.error("Can not decrypt data since the private key is not activated yet.")

		# decrypt.
		if isinstance(string,str): string = string.encode()
		decrypted = self.__decrypt_blob__(string, self.private_key_object)
		
		# layers.
		if layers-1 > 0:
			return self.decrypt_string(decrypted, layers=layers-1)
		else:
			if decode: decrypted = decrypted.decode()
			return _response_.success(f"Successfully decrypted the string.", {
				"decrypted":decrypted,
			})

		#
	def decrypt_file(self, path, layers=1):

		# checks.
		if not self.private_key_activated:
			return _response_.error("Can not decrypt data since the private key is not activated yet.")

		# encrypt.
		bytes = Files.load(path, format="bytes")
		decrypted = self.__decrypt_blob__(bytes, self.private_key_object)
		Files.save(path, decrypted, format="bytes")
		
		# layers.
		if layers-1 > 0:
			return self.decrypt_file(path, layers=layers-1)
		else:
			return _response_.success(f"Successfully decrypted file [{path}].")

		#
	def decrypt_directory(self, path, recursive=False, layers=1):

		# checks.
		if not self.private_key_activated:
			return _response_.error("Can not decrypt data since the private key is not activated yet.")

		# defaults.

		# recursively decrypt all files.
		if recursive:
			
			# recursive.
			for i in os.listdir(path):
				i = f'{path}/{i}'.replace("//",'/')
				if os.path.isdir(i):
					response = self.decrypt_directory(i, recursive=True)
					if response["error"] != None:
						return response
				else:
					response = self.decrypt_file(i)
					if response["error"] != None:
						return response

			# success.
			if layers-1 > 0:
				return self.decrypt_directory(path, recursive=True, layers=layers-1)
			else:
				return _response_.success(f"Successfully decrypted directory [{path}] (recursively).")

		# decrypt the encrypted.zip file.
		else:
			path = path.replace('.encrypted.zip', '/')

			# checks.
			file_path = FilePath(path)

			# set zip path.
			if path[len(path)-1] == "/": zip_path = path[:-1]
			else: zip_path = str(path)
			zip_path = f'{zip_path}.encrypted.zip'
			if not Files.exists(zip_path):
				return _response_.error(f"System encrypted zip [{path}] does not exist.")
			
			# decrypt zip.
			response = self.decrypt_file(zip_path, layers=layers)
			if response["error"] != None:
				return _response_.error(f"Failed to decrypted directory [{path}].")

			# extract zip.
			zip = Zip(path=zip_path)
			zip.extract(base=None)
			if Files.exists(path):
				zip.file_path.delete(forced=True)
				return _response_.success(f"Successfully decrypted directory [{path}].")
			else:
				return _response_.error(f"Failed to decrypted directory [{path}].")

		#
	
	# system functions.
	def __encrypt_blob__(self, blob, public_key, silent=True):
		blob = Formats.denitialize(blob)

		#Import the Public Key and use for encryption using PKCS1_OAEP
		rsa_key = public_key
		rsa_key = PKCS1_OAEP.new(rsa_key)

		#compress the data first
		try: 
			blob = zlib.compress(blob.encode())
		except: 
			blob = zlib.compress(blob)
		
		#In determining the chunk size, determine the private key length used in bytes
		#and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
		#in chunks
		chunk_size = 470
		offset = 0
		end_loop = False
		encrypted = bytearray()
		max_offset, progress = len(blob), 0
		if silent == False: print(f'Encrypting {max_offset} bytes.')
		while not end_loop:
			#The chunk
			chunk = blob[offset:offset + chunk_size]

			#If the data chunk is less then the chunk size, then we need to add
			#padding with " ". This indicates the we reached the end of the file
			#so we end loop here
			if len(chunk) % chunk_size != 0:
				end_loop = True
				#chunk += b" " * (chunk_size - len(chunk))
				chunk += bytes(chunk_size - len(chunk))
			#Append the encrypted chunk to the overall encrypted file
			encrypted += rsa_key.encrypt(chunk)

			#Increase the offset by chunk size
			offset += chunk_size
			l_progress = round((offset/max_offset)*100,2)
			if l_progress != progress:
				progress = l_progress
				if silent == False: print('Progress: '+str(progress), end='\r')

		#Base 64 encode the encrypted file
		return base64.b64encode(encrypted)
	def __decrypt_blob__(self, encrypted_blob, private_key, silent=True):
		encrypted_blob = Formats.denitialize(encrypted_blob)

		#Import the Private Key and use for decryption using PKCS1_OAEP
		rsakey = private_key
		rsakey = PKCS1_OAEP.new(rsakey)

		#Base 64 decode the data
		encrypted_blob = base64.b64decode(encrypted_blob)

		#In determining the chunk size, determine the private key length used in bytes.
		#The data will be in decrypted in chunks
		chunk_size = 512
		offset = 0
		decrypted = bytearray()
		max_offset = len(encrypted_blob)
		progress = 0
		if silent == False: print(f'Decrypting {max_offset} bytes.')
		#keep loop going as long as we have chunks to decrypt
		while offset < len(encrypted_blob):
			#The chunk
			chunk = encrypted_blob[offset: offset + chunk_size]

			#Append the decrypted chunk to the overall decrypted file
			decrypted += rsakey.decrypt(chunk)

			#Increase the offset by chunk size
			offset += chunk_size
			l_progress = round((offset/max_offset)*100,2)
			if l_progress != progress:
				progress = l_progress
				if silent == False: print('Progress: '+str(progress), end='\r')

		#return the decompressed decrypted data
		return zlib.decompress(decrypted)

	# propeties.
	@property
	def generated(self):
		if self.memory: return self.private_key != None and self.public_key != None
		else: return Files.exists(self.private_key) and Files.exists(self.public_key)
	@property
	def activated(self):
		return str(self.private_key_object) != str(None) and str(self.public_key_object) != str(None)
	@property
	def private_key_activated(self):
		return str(self.private_key_object) != str(None)
	@property
	def public_key_activated(self):
		return str(self.public_key_object) != str(None)

	#

# the encrypted dictionary class.
class EncryptedDictionary(Dictionary):
	"""
		The saved dictionary remains encrypted while local memory contains the decrypted dict.
		Requires already generated keys.
	"""	
	def __init__(self,
		# the file path.
		path=None, 
		# the dictionary.
		dictionary=None, 
		# specify default to check & create the dict.
		default={}, 
		# load the dictionary.
		load=True,
		# the key's directory path.
		key=None,
		# the key's passphrase.
		passphrase=None,
		# the encryption layers.
		layers=1,
	):

		# docs.
		DOCS = {
			"module":"dev0s.encryption.EncryptedDictionary", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# the dictionary object.
		self.default = default
		self._load_ = load
		self.dictionary = dictionary
		self._dictionary_ = Dictionary(
			path=False, 
			dictionary=self.dictionary, )

		# the file object.
		self._file_ = File(path=path)

		# variables.
		self.file_path = self._file_.file_path

		# the encryption object.
		self.key = key
		self.passphrase = passphrase
		self.layers = layers

	def initialize(self):

		# init encryption,
		self.encryption = RSA(
			directory=self.key,
			passphrase=self.passphrase,)
		response = self.encryption.load_keys()
		if response["error"] != None: return response

		# checks.
		created = False
		if not self._file_.file_path.exists():
			self._file_.save(json.dumps(self.default, indent=4, ensure_ascii=False))
			response = self.encryption.encrypt_file(self.file_path.path, layers=self.layers)
		elif self._load_:
			response = self.load()
			if response["error"] != None: return response
		if not created and self.default != None:
			if self.dictionary == None: 
				response = self.load()
				if response["error"] != None: return response
			response = self.check(default=self.default)
			if response["error"] != None: return response

		# success.
		return _response_.success(f"Successfully initialized encrypted dictionary [{self.file_path.path}].")
		#
	def load(self):

		# decrypt.
		encrypted = self._file_.load()
		response = self.encryption.decrypt_string(encrypted, layers=self.layers)
		if response["error"] != None: return response
		decrypted = response["decrypted"]

		# handle.
		try:
			self.dictionary = json.loads(decrypted)
			return _response_.success(f"Successfully loaded encrypted dictionary [{self.file_path.path}].")
		except: 
			self.dictionary = None
			return _response_.error(f"Failed to load encrypted dictionary [{self.file_path.path}].")

		#
	def save(self, dictionary=None):

		# encrypt.
		if dictionary == None: dictionary = self.dictionary
		response = self.encryption.encrypt_string(
			json.dumps(dictionary, indent=4, ensure_ascii=False), 
			layers=self.layers)
		if response["error"] != None: return response
		encrypted = response["encrypted"]

		# handle.
		try:
			self._file_.save(encrypted)
			return _response_.success(f"Successfully saved encrypted dictionary [{self.file_path.path}].")
		except: 
			self.dictionary = None
			return _response_.error(f"Failed to save encrypted dictionary [{self.file_path.path}].")

		#
	def check(self, default=None, save=True):

		# checks.
		if not isinstance(default, dict): 
			return _response_.error("Parameter [default] must be a dictionary.")
		if not isinstance(self.dictionary, dict): 
			return _response_.error("The dictionary must be initialized & loaded.")

		# handle.
		try:
			old = ast.literal_eval(str(self.dictionary))
			self._dictionary_.dictionary = self.dictionary
			self.dictionary = self._dictionary_.check(default=default)
		except:
			return _response_.error("Failed to check the loaded dictionary.")

		# save.
		if save and old != self.dictionary:
			response = self.save()
			if response["error"] != None: 
				return _response_.error("Failed to check the loaded dictionary, error: "+response['error'])

		# success.
		return _response_.success(f"Successfully saved encrypted dictionary [{self.file_path.path}].")
		
