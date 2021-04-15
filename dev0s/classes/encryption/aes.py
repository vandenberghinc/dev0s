#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_
from dev0s.classes.defaults.objects import *
from dev0s.classes import utils
from dev0s.classes.encryption import rsa

# imports.
import base64, string, random
from Crypto.Cipher import AES as _AES_
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2

# unpack format & encrypted.
def unpack(content):
	if " " not in content:
		raise ValueError("Encrypted format is incorrectly packed.")
	format = ""
	for i in content:
		if i not in [" "]: format += i
		else: break
	if format == "":
		raise ValueError("Encrypted format is incorrectly packed.")
	return format, content[len(format)+1:]

# the symetric aes 254 object class.
class AES(object):
	def __init__(self, passphrase=None):
		
		# docs.
		DOCS = {
			"module":"dev0s.encryption.AES", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# check params.
		response = _response_.parameters.check({
			"passphrase:str":passphrase,})
		if not response.success: raise ValueError(response.error)

		# arguments.
		self.passphrase = passphrase

		# variables.
		self.block_size = 16
		self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
		self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]
		#
	def encrypt(self, raw):
		if raw in ["", b"", None, False]:
			return _response_.error("Can not encrypt null data.")
		raw = Formats.denitialize(raw)
		response = self.get_key()
		if not response.success: return response
		key = response["key"]
		salt = response["salt"]
		if isinstance(raw, bytes):
			raw = raw.decode()
		raw = self.pad(raw)
		iv = Random.new().read(_AES_.block_size)
		cipher = _AES_.new(key, _AES_.MODE_CBC, iv)
		encrypted = base64.b64encode(iv + salt + cipher.encrypt(raw.encode()))
		if raw != b"" and encrypted == b"":
			return _response_.error("Failed to encrypt the specified data with the current passphrase / salt.")
		return _response_.success("Successfully encrypted the specified data.", {
			"encrypted":encrypted,
		})
	def decrypt(self, enc):
		if enc in ["", b"", None, False]:
			return _response_.error("Can not decrypt null data.")
		enc = Formats.denitialize(enc)
		if isinstance(enc, str):
			enc = enc.encode()
		enc = base64.b64decode(enc)
		iv_salt = enc[:32]
		iv = iv_salt[:16]
		salt = iv_salt[16:]
		response = self.get_key(salt=salt)
		if not response.success: return response
		key = response["key"]
		cipher = _AES_.new(key, _AES_.MODE_CBC, iv)
		decrypted = self.unpad(cipher.decrypt(enc[32:]))
		if enc != b"" and decrypted == b"":
			return _response_.error("Failed to decrypt the specified data with the current passphrase / salt.")
		return _response_.success("Successfully decrypted the specified data.", {
			"decrypted":decrypted,
		})
	def get_key(self, salt=None):
		if salt == None:
			salt = self.generate_salt()["salt"]
		if isinstance(salt, str):
			salt = salt.encode()
		kdf = PBKDF2(self.passphrase, salt, 64, 1000)
		key = kdf[:32]
		return _response_.success("Successfully loaded the aes key.", {
			"key":key,
			"salt":salt,
		})
	def generate_salt(self):
		length=16
		chars = ''.join([string.ascii_uppercase, string.ascii_lowercase, string.digits])
		salt = ''.join(random.choice(chars) for x in range(length))
		return _response_.success("Successfully generated a salt.", {
			"salt":salt,
		})

# the asymmetric aes 254 object class.
class AsymmetricAES(object):
	def __init__(self,
		# the public key (str).
		public_key=None,
		# the private key (str).
		private_key=None,
		# the key passphrase (str, null).
		passphrase=None,
		# enable memory when the keys are not saved.
		memory=False,
	):

		# docs.
		DOCS = {
			"module":"dev0s.encryption.AsymmetricAES", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# attributes.
		self.rsa = rsa.RSA(public_key=public_key, private_key=private_key, passphrase=passphrase, memory=memory)

	# functions.
	def generate_keys(self):
		return self.rsa.generate_keys()
	def load_keys(self):
		return self.rsa.load_keys()
	def load_private_key(self):
		return self.rsa.load_private_key()
		#
	def load_public_key(self):
		return self.rsa.load_public_key()
		#
	def edit_passphrase(self, passphrase=None):
		return self.rsa.edit_passphrase(passphrase=passphrase)
		#
	def encrypt(self, string, decode=False):
		string = Formats.denitialize(string)
		if isinstance(string, bytes):
			string = string.decode()
		
		# encrypt data with aes.
		passphrase = String().generate(length=64, digits=True, capitalize=True)
		aes = AES(passphrase=passphrase)
		response = aes.encrypt(string)
		if not response.success: return response
		aes_encrypted = response["encrypted"]
		if b" " in aes_encrypted:
			return _response_.error("AES encrypt data contains invalid ' ' character(s).")

		# encrypt aes key with rsa.
		response = self.rsa.encrypt_string(passphrase, decode=False)
		if not response.success: return response
		rsa_encrypted = response["encrypted"]

		# pack encrypted.
		encrypted = rsa_encrypted+b" "+aes_encrypted

		# success.
		if decode: encrypted = encrypted.decode()
		return _response_.success("Successfully encrypted the specified data.", {
			"encrypted":encrypted
		})

		#
	def decrypt(self, string, decode=False):

		# split encrypted aes key.
		string = Formats.denitialize(string)
		if isinstance(string, bytes):
			string = string.decode()
		try:
			key,encrypted = unpack(string)
		#except:
		except KeyboardInterrupt:
			return _response_.error("Unable to unpack the encrypted data.")

		# decypt key with rsa.
		response = self.rsa.decrypt_string(key, decode=False)
		if not response.success: return response
		passphrase = response["decrypted"].decode()

		# decrypt with aes.
		aes = AES(passphrase=passphrase)
		response = aes.decrypt(encrypted)
		if not response.success: return response
		decrypted = response["decrypted"]

		# success.
		if decode: decrypted = decrypted.decode()
		return _response_.success("Successfully decrypted the specified data.", {
			"decrypted":decrypted
		})

		#
	def encrypt_file(self, input=None, output=None, remove=False, base64_encoding=False):
		input = Formats.denitialize(input)
		output = Formats.denitialize(output)

		# check params.
		response = _response_.parameters.check({
			"input":input,
			"output":output,})
		if not response.success: return response

		# encrypt.
		data = Files.load(input, format="bytes")
		if base64_encoding:
			data = base64.b64encode(data)
		response = self.encrypt(data, decode=False)
		if not response.success: return response

		# write out.
		try: Files.save(output, response["encrypted"], format="bytes")
		except: return _response_.error(f"Failed to write out encrypted file {output}.")

		# remove.
		if remove and input != output: 
			try: os.remove(input)
			except PermissionError: os.system(f"sudo rm -fr {input}")

		# handler.
		return _response_.success(f"Successfully encrypted file {input} to {output}.")

		#
	def decrypt_file(self, input=None, output=None, remove=False, base64_encoding=False):
		input = Formats.denitialize(input)
		output = Formats.denitialize(output)

		# check params.
		response = _response_.parameters.check({
			"input":input,
			"output":output,})
		if not response.success: return response

		# encrypt.
		response = self.decrypt(Files.load(input, format="bytes"), decode=False)
		if not response.success: return response

		# write out.
		decrypted = response.decrypted
		if base64_encoding:
			decrypted = base64.b64decode(decrypted)
		try: Files.save(output, decrypted, format="bytes")
		except: return _response_.error(f"Failed to write out decrypted file {output}.")

		# remove.
		if remove and input != output: 
			try: os.remove(input)
			except PermissionError: os.system(f"sudo rm -fr {input}")

		# handler.
		return _response_.success(f"Successfully decrypted file {input} to {output}.")

		#
	def encrypt_directory(self, input=None, output=None, remove=False):
		input = Formats.denitialize(input)
		output = Formats.denitialize(output)

		# checks.
		file_path = FilePath(input)
		if not file_path.exists():
			return _response_.error(f"Directory [{input}] does not exist.")
		if not file_path.directory():
			return _response_.error(f"Directory path [{input}] is not a directory.")

		# zip path.
		if output == None:
			if input[len(input)-1] == "/": zip_path = input[:-1]
			else: zip_path = str(input)
			zip_path = f'{zip_path}.enc.zip'
		elif ".enc.zip" not in output:
			return _response_.error(f"Invalid output format [{output}], the format must end with [***.enc.zip]")
		else:
			zip_path = output

		# check output.
		if Files.exists(zip_path):
			return _response_.error(f"output path [{zip_path}] already exists.")

		# create zip.
		zip = Zip(path=zip_path)
		zip.create(source=input)

		# encrypt zip.
		response = self.encrypt_file(input=zip.file_path.path, output=zip.file_path.path, remove=False, base64_encoding=True)
		if response.success and Files.exists(zip.file_path.path) :
			if remove and input != output:
				try: 
					os.system(f"rm -fr {input}")
					if Files.exists(input): raise PermissionError("")
				except PermissionError: os.system(f"sudo rm -fr {input}")
			return _response_.success(f"Successfully encrypted directory [{input}].")
		else:
			zip.file_path.delete(forced=True)
			return _response_.error(f"Failed to encrypt directory [{input}].")

		#
	def decrypt_directory(self, input=None, output=None, remove=False):
		input = Formats.denitialize(input)
		output = Formats.denitialize(output)
		
		# checks.
		file_path = FilePath(input)
		if not file_path.exists():
			return _response_.error(f"Input [{input}] does not exist.")
		if file_path.directory():
			return _response_.error(f"Input path [{input}] is a directory.")

		# dir path.
		if output == None:
			if ".enc.zip" not in input:
				return _response_.error(f"Invalid input format [{input}], the format must end with [***.enc.zip]")
			dir_path = output.replace(".enc.zip", "/").replace("//","/").replace("//","/").replace("//","/")
		else:
			if ".enc.zip" in output:
				return _response_.error(f"Invalid output format [{output}], the format can not end with [***.enc.zip]")
			dir_path = output.replace(".enc.zip", "/")

		# check output.
		l_dir_path = dir_path
		if l_dir_path[len(l_dir_path)-1] == "/": l_dir_path = l_dir_path[:-1]
		if Files.exists(l_dir_path):
			return _response_.error(f"Output path [{l_dir_path}] already exists.")
		
		# decrypt zip.
		tmp_zip = f"/tmp/{FilePath(input).name()}"
		if Files.exists(tmp_zip): os.system(f"rm -fr {tmp_zip}")
		response = self.decrypt_file(input=input, output=tmp_zip, remove=False, base64_encoding=True)
		if not response.success:
			return _response_.error(f"Failed to decrypted directory [{input}], error: {response.error}")

		# extract zip.
		tmp_extract = f"/tmp/{String('').generate(length=32,capitalize=True,digits=True)}/"
		if Files.exists(tmp_extract): os.system(f"rm -fr {tmp_extract}")
		os.mkdir(tmp_extract)
		zip = Zip(path=tmp_zip)
		zip.extract(base=tmp_extract)
		paths = Files.Directory(path=tmp_extract).paths()
		if len(paths) == 1:
			os.system(f"mv {paths[0]} {output}")
			if Files.exists(output):
				os.system(f"rm -fr {tmp_extract}")
				os.system(f"rm -fr {tmp_zip}")
				if remove and input != output:
					try: os.remove(input)
					except PermissionError: os.system(f"sudo rm -fr {input}")
				return _response_.success(f"Successfully decrypted directory [{input}].")
			else:
				os.system(f"rm -fr {tmp_extract}")
				os.system(f"rm -fr {tmp_zip}")
				return _response_.error(f"Failed to decrypt directory [{input}].")
		else:
			os.system(f"rm -fr {tmp_extract}")
			os.system(f"rm -fr {tmp_zip}")
			return _response_.error(f"Failed to decrypt directory [{input}].")

		#

	# properties.
	@property
	def generated(self):
		return self.rsa.generated
	@property
	def activated(self):
		return self.rsa.activated
	@property
	def public_key_activated(self):
		return self.rsa.public_key_activated
	@property
	def private_key_activated(self):
		return self.rsa.private_key_activated

# the aes database object class.
class Database(object):
	def __init__(self,
		# the aes object class.
		aes=None,
		# the root path of the database.
		path=None,
	):

		# docs.
		DOCS = {
			"module":"dev0s.encryption.Database", 
			"initialized":False,
			"description":[], 
			"chapter": "Encryption", }

		# defaults.
		#self.__class__.__name__ = "Database"

		# check params.
		response = _response_.parameters.check({
			"aes:object":aes,
			"path:str":path,})
		if not response.success: raise ValueError(response.error)

		# arguments.
		self.aes = aes
		self.path = f"{gfp.clean(path, remove_first_slash=False, remove_last_slash=True, remove_double_slash=True)}/"
		self.file_path = self.fp = FilePath(self.path)
		if not self.fp.exists():
			os.system(f"mkdir {self.fp.path}")
			self.fp.ownership.set(owner=defaults.vars.owner)
			self.fp.permission.set(permission=770)

		#

	# functions.
	def activate(self, 
		# the key;s passphrase (optional).
		passphrase=None,
	):

		# passphrase.
		if passphrase != None:
			self.aes.rsa.passphrase = passphrase
			
		# check root.
		if not Files.exists(f"{self.path}"):
			return _response_.error(f"Encrypted database root [{self.path}] does not exist.")

		# activate keys.
		response = self.aes.load_keys()
		if not response.success: return response

		# success.
		return _response_.success(f"Successfully activated encrypted database [{self.path}].")

		#
	def check(self, 
		# the subpath of the content (! param number 1).
		path=None, 
		# the default content data (! param number 2).
		default=None,
		# save the changes.
		save=True,
	):
		if not self.activated: return _response_.error(f"Encrypted database {self.path} is not activated yet, call database.activate() first.")
		response = _response_.parameters.check({
			"path:str":path,
			"default:str,dict,list,int,float":default,
			"save:bool":save,})
		if not response.success: return response
		response = self.load(path=path, default=default)
		if not response.success: return response
		format, content = response.unpack(["format", "content"])
		response = content.check(default=default, save=save)
		if not response.success: return response
		return _response_.success(f"Successfully checked content {path}.", {
			"content":content,
			"format":format,
		})
	def load(self, 
		# the subpath of the content (! param number 1).
		path=None, 
		# the default data, specify to call self.check() automatically on the data object.
		default=None,
	):
		if not self.activated: return _response_.error(f"Encrypted database [{self.path}] is not activated yet, call database.activate() first.")
		response = _response_.parameters.check({
			"path:str":path,})
		if not response.success: return response
		path = gfp.clean(f"{self.path}/{path}", remove_last_slash=True, remove_double_slash=True)
		if not os.path.exists(str(path)):
			if default == None:
				return _response_.error(f"Specified path [{path}] does not exist.")
			elif isinstance(default, (str, String, File)):
				if isinstance(default, File):
					default = default.data
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"File",
					"content":self.File(path=path, default=str(default), aes=self.aes),
				})
			elif isinstance(default, (list, Array)):
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"Array",
					"content":self.Array(path=path, default=default, aes=self.aes),
				})
			elif isinstance(default, (dict, Dictionary)):
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"Dictionary",
					"content":self.Dictionary(path=path, default=default, aes=self.aes),
				})
		else:
			try:
				format, _ = unpack(Files.load(path))
			except Exception as e: return _response_.error(f"Failed to load content {path}, {e}.")
			if format in ["list", "Array"]:
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"Array",
					"content":self.Array(path=path, default=default, aes=self.aes),
				})
			elif format in ["dict", "Dictionary"]:
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"Dictionary",
					"content":self.Dictionary(path=path, default=default, aes=self.aes),
				})
			elif format in ["file", "File"]:
				return _response_.success(f"Successfully parsed {path}.", {
					"format":"File",
					"content":self.File(path=path, default=default, aes=self.aes),
				})
			else:
				return _response_.error(f"Unknown format [{format}] for path [{path}].")
	def save(self, 
		# the content object (! param number 1).
		content=None,
	):
		if not self.activated: return _response_.error(f"Encrypted database {self.path} is not activated yet, call database.activate() first.")
		response = _response_.parameters.check({
			"content:object":content,})
		if not response.success: return response
		response = content.save()
		if not response.success: return response
		return _response_.success(f"Successfully saved content {path}.")

	# properties.
	@property
	def activated(self):
		return self.aes.activated
	@property
	def public_key_activated(self):
		return self.aes.public_key_activated
	@property
	def private_key_activated(self):
		return self.aes.private_key_activated
	

	# a file data object
	class File(File):
		def __init__(self,
			# the path.
			path=None, 
			# the default data, specify to call self.check() automatically.
			default=None,
			# the aes object.
			aes=None,
		):
			# docs.
			DOCS = {
				"module":"dev0s.encryption.Database.File", 
				"initialized":False,
				"description":[], 
				"chapter": "Encryption", }
				
			# attributes
			self.path = f"{gfp.clean(path, remove_first_slash=False, remove_last_slash=True, remove_double_slash=True)}"
			self.base = FilePath(self.path).base()
			self.aes = aes
			self.loaded = False
			File.__init__(self, path=self.path)
			if default != None: self.check(default=default, save=True)
		def load(self):
			try:
				format, content = unpack(Files.load(self.path))
			except Exception as e: return _response_.error(f"Failed to load content {self.path}, {e}.")
			response = self.aes.decrypt(content.encode())
			if not response.success: return response
			decrypted = response.decrypted.decode()
			self.data = decrypted
			self.format = format
			self.loaded = True
			return _response_.success(f"Successfully loaded content {self.path}.")
		def save(self):
			if not self.loaded:
				return _response_.error("The data object is not loaded yet, you must call content.load() first.")
			content = Formats.denitialize(self.content)
			response = self.aes.encrypt(content)
			if not response.success: return response
			try:
				content = Files.save(str(self.path), f"{self.format} ".encode()+response.encrypted, format="bytes")
			except Exception as e: return _response_.error(f"Failed to save content {self.path}, {e}.")
			return _response_.success(f"Successfully saved content {self.path}.")

	# a array data object
	class Array(Array):
		def __init__(self,
			# the path.
			path=None, 
			# the default data, specify to call self.check() automatically.
			default=None,
			# the aes object.
			aes=None,
		):
			# docs.
			DOCS = {
				"module":"dev0s.encryption.Database.Array", 
				"initialized":False,
				"description":[], 
				"chapter": "Encryption", }

			# attributes.
			self.path = f"{gfp.clean(path, remove_first_slash=False, remove_last_slash=True, remove_double_slash=True)}"
			self.base = FilePath(self.path).base()
			self.aes = aes
			self.loaded = False
			Array.__init__(self, path=self.path)
			if default != None: self.check(default=default, save=True)
		def load(self):
			try:
				format, content = unpack(Files.load(self.path))
			except Exception as e: return _response_.error(f"Failed to load content {self.path}, {e}.")
			response = self.aes.decrypt(content.encode())
			if not response.success: return response
			decrypted = response.decrypted.decode()
			try:
				content = json.loads(decrypted)
			except Exception as e: return _response_.error(f"Failed to serialize content {self.path}, {e}.")
			self.array = content
			self.format = format
			self.loaded = True
			return _response_.success(f"Successfully loaded content {self.path}.")
		def save(self):
			if not self.loaded:
				return _response_.error("The data object is not loaded yet, you must call content.load() first.")
			try:
				content = json.dumps(Formats.denitialize(self.array))
			except Exception as e: return _response_.error(f"Failed to dump content {self.path}, {e}.")
			response = self.aes.encrypt(content)
			if not response.success: return response
			try:
				content = Files.save(str(self.path), f"{self.format} ".encode()+response.encrypted, format="bytes")
			except Exception as e: return _response_.error(f"Failed to save content {self.path}, {e}.")
			return _response_.success(f"Successfully saved content {self.path}.")

	# a dictionary data object
	class Dictionary(Dictionary):
		def __init__(self,
			# the path.
			path=None, 
			# the default data, specify to call self.check() automatically.
			default=None,
			# the aes object.
			aes=None,
		):
			# docs.
			DOCS = {
				"module":"dev0s.encryption.Database.Dictionary", 
				"initialized":False,
				"description":[], 
				"chapter": "Encryption", }

			# attributes.
			self.path = f"{gfp.clean(path, remove_first_slash=False, remove_last_slash=True, remove_double_slash=True)}"
			self.base = FilePath(self.path).base()
			self.aes = aes
			self.loaded = False
			Dictionary.__init__(self, path=self.path)
			if default != None: self.check(default=default, save=True)
		def load(self):
			try:
				format, content = unpack(Files.load(self.path))
			except Exception as e: return _response_.error(f"Failed to load content {self.path}, {e}.")
			response = self.aes.decrypt(content.encode())
			if not response.success: return response
			decrypted = response.decrypted.decode()
			try:
				content = json.loads(decrypted)
			except Exception as e: return _response_.error(f"Failed to serialize content {self.path}, {e}.")
			self.dictionary = content
			self.format = format
			self.loaded = True
			return _response_.success(f"Successfully loaded content {self.path}.")
		def save(self):
			if not self.loaded:
				return _response_.error("The data object is not loaded yet, you must call content.load() first.")
			try:
				content = json.dumps(Formats.denitialize(self.dictionary))
			except Exception as e: return _response_.error(f"Failed to dump content {self.path}, {e}.")
			response = self.aes.encrypt(content)
			if not response.success: return response
			try:
				content = Files.save(str(self.path), f"{self.format} ".encode()+response.encrypted, format="bytes")
			except Exception as e: return _response_.error(f"Failed to save content {self.path}, {e}.")
			return _response_.success(f"Successfully saved content {self.path}.")


"""



# initialize.
aes = AES(passphrase="SomePassphrase12345!?")
database = Database(
	path="/tmp/database.enc",
	aes=aes,)

# activate the database.
response = database.activate()

# check data, dict or list.
response = database.check("users/vandenberghinc", {
	"Hello":"World"
})

# load data.
response = database.load("users/vandenberghinc")
content = response.content

# save data.
content.format # dict
content["Hello"] = "World!"
response = database.save(content)

# int & float data.
response = database.check("someint", 1500)
content = response.content
content.format # int
content.content = 1501
response = database.save(content)

# string data.
response = database.check("somestring", "Hello World")
content = response.content
content.format # str
content.content = "Hello World!"
response = database.save(content)





# initialize. 
aes = AES(passphrase="SomePassphrase12345!?")
aes.salt
 
# encrypt message
encrypted = aes.encrypt("This is a secret message".encode())
print(encrypted)
 
# decrypt using password
decrypted = aes.decrypt(encrypted)
print(decrypted)
"""