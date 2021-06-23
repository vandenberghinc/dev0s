#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# insert the package for universal imports.
def __get_source_path__(
	# the path (leave None to use self.path) (param #1).
	path=None,
	# the dirs back.
	back=1,
):
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
import sys ; sys.path.insert(1, __get_source_path__(__file__, back=2))

# imports.
from dev0s.classes.config import *
from dev0s.shortcuts import *
import getpass

# the cli object class.
class CLI(dev0s.cli.CLI):
	def __init__(self):
		
		# cli.
		dev0s.cli.CLI.__init__(self,
			modes={
				"Encryption":"*chapter*",
				"    --encrypt /path/to/input /path/to/output [optional: --remove]":"Encrypt the provided file path.",
				"    --decrypt /path/to/input /path/to/output [optional: --remove]":"Decrypt the provided file path.",
				"    --encrypt-env . [optional: --remove]":"Encrypt the specified enviroment (automatically fills: --key ./key --input ./data/ --output ./data.enc.zip).",
				"    --decrypt-env . [optional: --remove]":"Decrypt the specified enviroment (automatically fills: --key ./key --input ./data.enc.zip --output ./data/).",
				"    --generate-keys":"Generate a key pair.",
				"    --generate-passphrase [optional: --length 32]":"Generate a passphrase.",
				"    --generate-aes [optional: --length 64]":"Generate an aes passphrase.",
				"System":"*chapter*",
				"    --user myuser":"Configure a system user (linux).",
				"        --check":"Check the existance of the specified user.",
				"        --create":"Create the specified user.",
				"        --delete":"Delete the specified user.",
				"        --password MyPassword":"Set the password of the specifed user (leave password blank for safe prompt).",
				"        --add-groups group1,group2":"Add the specified user to groups.",
				"        --delete-groups group1,group2":"Remove the specified user from groups.",
				"    --group mygroup":"Configure a system group (linux).",
				"        --check":"Check the existance of the specified group.",
				"        --create":"Create the specified group.",
				"        --delete":"Delete the specified group.",
				"        --list-users":"List the users of the specified group.",
				"        --add-users user1,user2":"Add users from the specified group.",
				"        --delete-users user1,user2":"Delete users from the specified group.",
				"        --force-users user1,user2":"Add the specified users to the group and remove all others.",
				"    --disk-space":"Get the free disk space.",
				"    --size /path/to/file":"Get the size of a file / directory.",
				"Metrics":"*chapter*",
				"    --metrics":"Access the metrics.",
				"      --ram":"Parse the RAM metrics (linux).",
				"CleanUp":"*chapter*",
				"    --cleanup":"Access the cleanup.",
				"      --ram ":"Clean up the RAM memory (linux).",
				"      --swap ":"Clean up the RAM swap memory (linux).",
				"Network":"*chapter*",
				"    --network":"Access the network.",
				"        --info":"Retrieve the current network information.",
				"    --firewall":"Access the firewall (linux only).",
				"        --info":"Retrieve the current firewall information.",
				"        --disable":"Disable the firewall.",
				"        --enable":"Enable the firewall.",
				"        --set-default false":"Set the default firewall behaviour (deny/allow).",
				"        --allow 22":"Allow a port in the firewall settings.",
				"        --deny 22":"Deny a port in the firewall settings.",
				"Installation":"*chapter*",
				"    --install":f"Install the {ALIAS} library.",
				"    --uninstall":f"Uninstall the {ALIAS} library.",
				"    --reinstall":f"Reinstall the {ALIAS} library.",
				"    --link":f"Link (activate) the {ALIAS} library.",
				"    --unlink":f"Unlink (deactivate) the {ALIAS} library.",
				"    --update":f"Update the {ALIAS} library.",
				"Defaults":"*chapter*",
				"    --version":"Show the dev0s version.",
				"    -h / --help":"Show the documentation.",
			},
			options={
			},
			executable=__file__,
			alias=ALIAS,)

		#
	def start(self):
		
		# check arguments.
		self.arguments.check(exceptions=["--log-level", "--create-alias", "--version", "--non-interactive", "--remove"], json=dev0s.defaults.options.json)

		# ____________________________________________________________________________________________________
		#
		# BASICS
		#

		# help.
		if self.arguments.present(['-h', '--help']):
			self.docs(success=True, json=dev0s.defaults.options.json)

		# version.
		elif self.arguments.present(['--version']):
			print(f"{ALIAS} version:",Files.load(f"{SOURCE_PATH}/.version").replace("\n",""))

		# ____________________________________________________________________________________________________
		#
		# ENCRYPTION
		#

		# encrypt.
		elif self.arguments.present('--encrypt'):
			input = self.arguments.get('--encrypt', index=1, json=dev0s.defaults.options.json)
			output = self.arguments.get('--encrypt', index=2, json=dev0s.defaults.options.json)
			encryption = self.get_encryption(prompt_passphrase=False)
			response = encryption.load_public_key()
			dev0s.response.log(response=response, json=dev0s.defaults.options.json)
			if not response.success: sys.exit(1)
			if os.path.isdir(input): 
				response = encryption.encrypt_directory(input=input, output=output, remove=self.arguments.present("--remove"))
			else: 
				response = encryption.encrypt_file(input=input, output=output, remove=self.arguments.present("--remove"))
			self.stop(response=response, json=dev0s.defaults.options.json)

		# decrypt.
		elif self.arguments.present('--decrypt'):
			input = self.arguments.get('--decrypt', index=1, json=dev0s.defaults.options.json)
			output = self.arguments.get('--decrypt', index=2, json=dev0s.defaults.options.json)
			encryption = self.get_encryption()
			response = encryption.load_private_key()
			dev0s.response.log(response=response, json=dev0s.defaults.options.json)
			if not response.success: sys.exit(1)
			if os.path.isdir(input) or (".enc.zip" in input and ".enc.zip" not in output): 
				response = encryption.decrypt_directory(input=input, output=output, remove=self.arguments.present("--remove"))
			else: 
				response = encryption.decrypt_file(input=input, output=output, remove=self.arguments.present("--remove"))
			self.stop(response=response, json=dev0s.defaults.options.json)

		# encrypt env.
		elif self.arguments.present('--encrypt-env'):
			env = self.arguments.get('--encrypt-env', json=dev0s.defaults.options.json)
			key = f"{env}/key/".replace("//","/").replace("//","/").replace("//","/")
			input = f"{env}/data/".replace("//","/").replace("//","/").replace("//","/")
			output = f"{env}/data.enc.zip".replace("//","/").replace("//","/").replace("//","/")
			encryption = self.get_encryption(prompt_passphrase=False, key=key)
			response = encryption.load_public_key()
			dev0s.response.log(response=response, json=dev0s.defaults.options.json)
			if not response.success: sys.exit(1)
			response = encryption.encrypt_directory(input=input, output=output, remove=self.arguments.present("--remove"))
			self.stop(response=response, json=dev0s.defaults.options.json)

		# decrypt env.
		elif self.arguments.present('--decrypt-env'):
			env = self.arguments.get('--decrypt-env')
			key = f"{env}/key/".replace("//","/").replace("//","/").replace("//","/")
			input = f"{env}/data.enc.zip".replace("//","/").replace("//","/").replace("//","/")
			output = f"{env}/data/".replace("//","/").replace("//","/").replace("//","/")
			encryption = self.get_encryption(key=key)
			response = encryption.load_private_key()
			dev0s.response.log(response=response, json=dev0s.defaults.options.json)
			if not response.success: sys.exit(1)
			response = encryption.decrypt_directory(input=input, output=output, remove=self.arguments.present("--remove"))
			self.stop(response=response, json=dev0s.defaults.options.json)

		# generate-keys.
		elif self.arguments.present('--generate-keys'):
			encryption = self.get_encryption(check_passphrase=True)
			response = encryption.generate_keys()
			self.stop(response=response, json=dev0s.defaults.options.json)

		# generate-aes.
		elif self.arguments.present('--generate-aes'):
			self.stop(message=f"Generated AES Passphrase: {utils.__generate__(length=int(self.arguments.get('--length', required=False, default=64)), capitalize=True, digits=True)}", json=dev0s.defaults.options.json)

		# generate passphrase.
		elif self.arguments.present('--generate-passphrase'):
			self.stop(message=f"Generated passphrase: {String('').generate(length=length, capitalize=True, digits=True)}", json=dev0s.defaults.options.json)

		# ____________________________________________________________________________________________________
		#
		# SYSTEM.
		#

		# user.
		elif self.arguments.present(['--user']):
			dev0s.defaults.operating_system(supported=["linux"])

			# initialize a user object.
			user = dev0s.system.User(self.arguments.get("--user"))

			# check if the user exists.
			if self.arguments.present(['--check']):
				response = user.check()
				dev0s.response.log(response=response)
				if response.success: print("User existance:",response["exists"])

			# create a user.
			elif self.arguments.present(['--create']):
				response = user.create()
				self.stop(response=response)

			# delete a user.
			elif self.arguments.present(['--delete']):
				response = user.delete()
				self.stop(response=response)

			# set a users password.
			elif self.arguments.present(['--password']):
				password = self.get_password(retrieve=True, message=f"Enter a new password of user [{user.username}]:")
				response = user.set_password(password=password)
				self.stop(response=response)

			# add the user to groups.
			elif self.arguments.present(['--add-groups']):
				groups = self.arguments.get("--delete-groups").split(",")
				response = user.add_groups(groups=groups)
				self.stop(response=response)

			# delete the user from groups.
			elif self.arguments.present(['--delete-groups']):
				groups = self.arguments.get("--delete-groups").split(",")
				response = user.add_groups(groups=groups)
				self.stop(response=response)


			# invalid.
			else:  self.invalid()

		# group.
		elif self.arguments.present(['--group']):
			dev0s.defaults.operating_system(supported=["linux"])

			# initialize a group object.
			group = dev0s.system.Group(self.arguments.get("--group"))

			# check if the group exists.
			if self.arguments.present(['--check']):
				response = group.check()
				dev0s.response.log(response=response)
				if response.success: 
					print("Group existance:",response["exists"])

			# create a group.
			elif self.arguments.present(['--create']):
				response = group.create()
				self.stop(response=response)

			# delete a group.
			elif self.arguments.present(['--delete']):
				response = group.delete()
				self.stop(response=response)

			# list the current users.
			elif self.arguments.present(['--list-users']):
				response = group.list_users()
				self.stop(response=response)
				if response.success: 
					print(f"Users of group {group.name}:",response["users"])

			# add users to the group.
			elif self.arguments.present(['--add-users']):
				users = self.arguments.get("--add-users").split(",")
				response = group.add_users(users=users)
				self.stop(response=response)

			# delete users from the group.
			elif self.arguments.present(['--delete-users']):
				users = self.arguments.get("--delete-users").split(",")
				response = group.delete_users(users=users)
				self.stop(response=response)

			# check if the specified users are enabled and remove all other users.
			elif self.arguments.present(['--force-users']):
				users = self.arguments.get("--force-users").split(",")
				response = group.check_users(users=users)
				self.stop(response=response)


			# invalid.
			else:  self.invalid()

		# free disk space.
		elif self.arguments.present(["--disk-space"]):
			path = self.arguments.get("--disk-space", required=False, default="/")
			fp = FilePath(path)
			if not fp.exists(): 
				print(f"File path [{fp.path}] does not exist.")
				sys.exit(1)
			loader = dev0s.console.Loader(f"Retrieving size of {fp.path} ...")
			info = fp.space()
			loader.stop()
			print(f"{fp.path}\n * total: {info['total']}\n * used: {info['used']}\n * free: {info['free']}")
			
		# size.
		elif self.arguments.present(["--size"]):
			fp = FilePath(self.arguments.get("--size"))
			if not fp.exists(): 
				print(f"File path [{fp.path}] does not exist.")
				sys.exit(1)
			else:
				loader = dev0s.console.Loader(f"Retrieving size of {fp.path} ...")
				size = fp.size()
				loader.stop()
				print(f"{fp.path}\n * size: {size}")

		# ____________________________________________________________________________________________________
		#
		# METRICS
		#

		# network.
		elif self.arguments.present(['--metrics']):

			# ram.
			if self.arguments.present(['--ram']):
				response = dev0s.system.metrics.ram()
				dev0s.response.log(response=response)
				if response.success: 
					del response["message"] ; del response["error"] ; del response["success"]
					print("RAM metrics:")
					print(response.json(indent=2).replace("{","").replace("}","").replace('"',"").replace(',',"").replace('\n    \n',"\n")[1:-4])


			# invalid.
			else:  self.invalid()

		# ____________________________________________________________________________________________________
		#
		# CLEANUP
		#

		# cleanup.
		elif self.arguments.present(['--cleanup', '--clean-up']):

			# ram.
			if self.arguments.present(['--ram']):
				self.stop(response=dev0s.system.cleanup.ram())

			# swap.
			elif self.arguments.present(['--swap']):
				self.stop(response=dev0s.system.cleanup.swap())

			# invalid.
			else:  self.invalid()

		# ____________________________________________________________________________________________________
		#
		# NETWORK
		#

		# network.
		elif self.arguments.present(['--network']):

			# info.
			if self.arguments.present(['--info']):
				response = dev0s.network.info()
				dev0s.response.log(response=response)
				if response.success: 
					del response["message"] ; del response["error"] ; del response["success"]
					print("Network info:")
					print(response.json(indent=3)[:-2].replace('",',"").replace('"',"").replace('\n  ',"\n * ")[2:])


			# invalid.
			else:  self.invalid()

		# firewall.
		elif self.arguments.present(['--firewall']):

			# check os.
			dev0s.defaults.operating_system(supported=["linux"])

			# retrieve the firewall information.
			if self.arguments.present(['--info']):
				response = dev0s.network.firewall.info()
				dev0s.response.log(response=response)
				if response.success: 
					del response["message"] ; del response["error"] ; del response["success"]
					print(response.json(indent=3).replace("{\n","").replace("\n}","").replace('",',"").replace('"',"").replace('\n  ',"\n * "))

			# disable the firewall.
			elif self.arguments.present(['--disable']):
				response = dev0s.network.firewall.disable()
				dev0s.response.log(response=response)

			# enable the firewall.
			elif self.arguments.present(['--enable']):
				response = dev0s.network.firewall.enable()
				dev0s.response.log(response=response)

			# set the default port action.
			elif self.arguments.present(['--set-default']):
				deny = self.arguments.get("--set-default")
				if deny in ["True", "true", True]: deny = True
				else: deny = False
				response = dev0s.network.firewall.set_default(deny=deny)
				dev0s.response.log(response=response)

			# allow a port.
			elif self.arguments.present(['--allow']):
				port = int(self.arguments.get("--allow"))
				response = dev0s.network.firewall.allow(port)
				dev0s.response.log(response=response)

			# deny a port.
			elif self.arguments.present(['--deny']):
				port = int(self.arguments.get("--deny"))
				response = dev0s.network.firewall.deny(port)
				dev0s.response.log(response=response)


			# invalid.
			else:  self.invalid()

		# ____________________________________________________________________________________________________
		#
		# INSTALLATION.
		#

		# install.
		elif self.arguments.present('--install'):
			response = manager.installation.install()
			if response.message != None and "Successfully installed " not in response.message: dev0s.response.log(response=response)

		# uninstall.
		elif self.arguments.present('--uninstall'):
			response = manager.installation.uninstall()
			dev0s.response.log(response=response)

		# reinstall.
		elif self.arguments.present('--reinstall'):
			response = manager.installation.uninstall()
			dev0s.response.log(response=response)
			response = manager.installation.install()
			if response.message != None and "Successfully installed " not in response.message: dev0s.response.log(response=response)

		# link.
		elif self.arguments.present('--link'):
			response = manager.installation.link()
			dev0s.response.log(response=response)

		# unlink.
		elif self.arguments.present('--unlink'):
			response = manager.installation.unlink()
			dev0s.response.log(response=response)

		# ____________________________________________________________________________________________________
		#
		# INVALID.
		#
		else: self.invalid()

		#
	def get_encryption(self, prompt_passphrase=True, check_passphrase=False, key=None):
		# key.
		public_key = self.arguments.get('--public-key', required=False)
		private_key = self.arguments.get('--private-key', required=False)
		if public_key == None and private_key == None:
			if key == None: key = self.arguments.get('--key', required=True, json=dev0s.defaults.options.json)
			public_key = f"{key}/public_key"
			private_key = f"{key}/private_key"
		# passphrase.
		passphrase = None
		if prompt_passphrase:
			passphrase = self.arguments.get('-p', required=False)
			if passphrase == None:
				passphrase = self.arguments.get('--passphrase', required=False)
			if passphrase == None:
				passphrase = getpass.getpass("Enter the key's passphrase (leave blank to use no passphrase):")
				if check_passphrase and passphrase != getpass.getpass("Enter the same passphrase:"):
					print("Error: passphrases do not match.")
					sys.exit(1)
			if passphrase in ["", "none", "null"]: passphrase = None
		# encryption.
		return dev0s.encryption.AsymmetricAES(
			public_key=public_key,
			private_key=private_key,
			passphrase=passphrase,)
# main.
if __name__ == "__main__":
	cli = CLI()
	cli.start()
