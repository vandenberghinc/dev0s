# dev0s
Author(s):  Daan van den Bergh.<br>
Copyright:  © 2020 Daan van den Bergh All Rights Reserved.<br>
Supported Operating Systems: macos & linux.<br>
<br>
<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/vandenberghinc/public-storage/master/vandenberghinc/icon/icon.png" alt="Bergh-Encryption" width="50"> 
</p>

## Table of content:
  * [Description](#description)
  * [Installation](#installation)
  * [Custom Code Examples.](#custom-code-examples.)
  * [Code Examples](#code-examples)

# Description:
DevOS library.

# Installation:
Install the package.

	curl -s https://raw.githubusercontent.com/vandenberghinc/dev0s/master/dev0s/requirements/installer.remote | bash 

# Custom Code Examples.

#### Imports.
Importing the dev0s library.

```python

# import the package
from dev0s.shortcuts import *

```

#### dev0s.response usage.
An example function that returns a ResponseObject class.

```python

# import the package
from dev0s import *

# universal responses.
def my_function():

	# return an error response from a function.
	return dev0s.response.error("Failed to retrieve your personal API key")

	# return a success response from a function.
	return dev0s.response.success("Success retrieved your personal API key", {
		"api_key":api_key,
	})

# check if a response was successfull.
response = my_function()
if response.success:
	message = response["message"]
else:
	error = response["error"]

```

#### dev0s.cli.CLI Usage.

##### Simple Example.

Simple CLI.CLI code example.

```python
# the cli object class.
class CLI(dev0s.cli.CLI):
	def __init__(self):
		
		# defaults.
		dev0s.cli.CLI.__init__(self,
			modes={
				"--config":"Edit the ssht00ls configuration file (nano).",
				"-h / --help":"Show the documentation.",
			},
			alias="ssht00ls",
			executable=__file__,
		)

		#
	def start(self):
		
		# check arguments.
		self.arguments.check()

		# help.
		if self.arguments.present(['-h', '--help']):
			self.docs(success=True)

		# config.
		elif self.arguments.present('--config'):
			os.system(f"nano {CONFIG.file_path.path}")

		# invalid.
		else: self.invalid()

		#

# main.
if __name__ == "__main__":
	cli = CLI()
	cli.start()
```

##### Advanced Example.

Advanced CLI.CLI code example.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s import * ; dev0s.defaults.insert(dev0s.defaults.source_path(__file__, back=2))
from ssht00ls.classes.config import *
import ssht00ls

# the cli object class.
class CLI(dev0s.cli.CLI):
	def __init__(self):
		
		# defaults.
		dev0s.cli.CLI.__init__(self,
			modes={
				"Aliases:":"*chapter*",
				"    --create-alias":"Create a ssh alias.",
				"        --server myserver":"Specify the server's name.",
				"        --username myuser":"Specify the username.",
				"        --ip 0.0.0.0":"Specify the server's ip.",
				"        --port 22":"Specify the server's port.",
				"        for ssh keys:":"",
				"        --key /path/to/key/private_key":"Specify the path to the private key.",
				"        --passphrase 'MyPassphrase123'":"Specify the keys pasphrase (optional).",
				"        for smart cards:":"",
				"        --smart-cards":"Enable the smart cards boolean.",
				"        --pin 123456":"Specify the smart cards pin code (optional).",
				"Keys:":"*chapter*",
				"    --generate":"Generate a ssh key.",
				"        --path /keys/mykey/":"Specify the keys directory path.",
				"        --passphrase Passphrase123":"Specify the keys passphrase.",
				"        --comment 'My Key'":"Specify the keys comment.",
				"Sessions:":"*chapter*",
				"    --command <alias> 'ls .'":"Execute a command over ssh.",
				"    --session <alias>":"Start a ssh session.",
				"        --options '' ":"Specify additional ssh options (optional).",
				"Push & pull:":"*chapter*",
				"    --pull <path> <alias>:<remote>":"Pull a file / directory.",
				"        --delete":"Also update the deleted files (optional).",
				"        --safe":"Enable version control.",
				"        --forced":"Enable forced mode.",
				"    --push <alias>:<remote> <path>":"Push a file / directory.",
				"        --delete":"Also update the deleted files (optional).",
				"        --safe":"Enable version control.",
				"        --forced":"Enable forced mode.",
				"Mounts:":"*chapter*",
				"    --mount <alias>:<remote> <path>":"Mount a remote directory.",
				"    --unmount <path>":"Unmount a mounted remote directory.",
				"        --sudo":"Root permission required.",
				"        --forced":"Enable forced mode.",
				"    --index <path> / <alias>:<remote>":"Index the specified path / alias:remote.",
				"Agent:":"*chapter*",
				"    --start-agent":"Start the ssht00ls agent manually.",
				"    --stop-agent":"Stop the ssht00ls agent.",
				"Daemons:":"*chapter*",
				"    --start-daemon <alias>:<remote> <path>":"Start a ssync daemon manually.",
				"    --stop-daemon <path>":"Stop a ssync daemon.",
				"Basic:":"*chapter*",
				"    --kill <identifier>":"Kill all ssh processes that include the identifier.",
				"    --config":"Edit the ssht00ls configuration file (nano).",
				"    -h / --help":"Show the documentation.",
			},
			options={
				"-j / --json":"Print the response in json format.",
			},
			notes={
				"SSHT00LS_CONFIG":"Specify the $SSHT00LS_CONFIG environment variable to use a different ssht00ls config file.",
			},
			alias=ALIAS,
			executable=__file__,
		)

		#
	def start(self):
		
		# check arguments.
		self.arguments.check(exceptions=["--log-level", "--create-alias"], json=JSON)

		# help.
		if self.arguments.present(['-h', '--help']):
			self.docs(success=True, json=JSON)

		# check create ssh config.
		elif self.arguments.present('--create-alias'):
			
			# create an ssh alias for the key.
			if not self.arguments.present('--smart-card'):
				key = self.arguments.get('--key')
				response = ssht00ls.aliases.create( 
					# the alias.
					alias=self.arguments.get('--alias', chapter="aliases", mode="--create-alias"), 
					# the username.
					username=self.arguments.get('--username'), chapter="aliases", mode="--create-alias", 
					# the public ip of the server.
					public_ip=self.arguments.get('--public-ip', chapter="aliases", mode="--create-alias"),
					# the public port of the server.
					public_port=self.arguments.get('--public-port', chapter="aliases", mode="--create-alias"),
					# the private ip of the server.
					private_ip=self.arguments.get('--private-ip', chapter="aliases", mode="--create-alias"),
					# the private port of the server.
					private_port=self.arguments.get('--private-port', chapter="aliases", mode="--create-alias"),
					# the path to the private key.
					key=key,
					passphrase=getpass.getpass("Enter the passphrase of key [{key}]:"),
					# smart card.
					smartcard=False,)

			# create an ssh alias for a smart card.
			else:
				response = ssht00ls.aliases.create( 
					# the alias.
					alias=self.arguments.get('--alias', chapter="aliases", mode="--create-alias"), 
					# the username.
					username=self.arguments.get('--username', chapter="aliases", mode="--create-alias"), 
					# the public ip of the server.
					public_ip=self.arguments.get('--public-ip', chapter="aliases", mode="--create-alias"),
					# the public port of the server.
					public_port=self.arguments.get('--public-port', chapter="aliases", mode="--create-alias"),
					# the private ip of the server.
					private_ip=self.arguments.get('--private-ip', chapter="aliases", mode="--create-alias"),
					# the private port of the server.
					private_port=self.arguments.get('--private-port', chapter="aliases", mode="--create-alias"),
					# the path to the private key.
					key=smartcard.path,
					# smart card.
					smartcard=True,
					pin=self.arguments.get('--pin', required=False, default=None, chapter="aliases", mode="--create-alias"), )

			# log to console.
			self.stop(response=response, json=JSON)

		# check create ssh config.
		elif self.arguments.present('--generate'):
			
			# generate a key.
			passphrase = self.arguments.get("--passphrase", required=required).replace("\\", "").replace("\ ", "")
			if passphrase in ["", None, "null", "None", "none"]: passphrase = None
			response = ssht00ls.keys.generate(
				path=self.arguments.get("--path", chapter="keys", mode="--generate"), 
				passphrase=passphrase, 
				comment=self.arguments.get("--comment", chapter="keys", mode="--generate"),)
			self.stop(response=response, json=JSON)

		# kill ssh processes.
		elif self.arguments.present('--kill'):
			response = ssht00ls.utils.kill_ssh(
				identifier=self.arguments.get("--kill"), 
				sudo=self.arguments.present("--sudo"),)
			self.stop(response=response, json=JSON)

		# pull.
		elif self.arguments.present('--pull'):
			remote = self.arguments.get("--pull", index=1, chapter="push & pull", mode="--pull")
			path = self.arguments.get("--pull", index=2, chapter="push & pull", mode="--pull")
			if ":" not in remote:
				self.docs(
					error=f"Invalid <alias>:<remote> <path> format.", 
					chapter="push & pull", 
					mode="--pull", 
					notes={
						"<alias>:<path>":"Pack the alias & tuple together as one argument in the following format [<alias>:<path>]."
					},
					json=JSON,)
			alias,remote = remote.split(":")
			exclude = None
			if self.arguments.present("--exclude"): 
				exclude = self.arguments.get("--exclude", chapter="push & pull", mode="--pull").split(",")
			elif self.arguments.present("--no-exclude"): exclude = []
			response = ssht00ls.ssync.pull(
				alias=alias, 
				remote=remote, 
				path=path,
				exclude=exclude, 
				forced=self.arguments.present("--forced"), 
				delete=self.arguments.present("--delete"), 
				safe=self.arguments.present("--safe"), )
			self.stop(response=response, json=JSON)

		# push.
		elif self.arguments.present('--push'):
			path = self.arguments.get("--push", index=1, chapter="push & pull", mode="--push")
			remote = self.arguments.get("--push", index=2, chapter="push & pull", mode="--push")
			if ":" not in remote:
				self.docs(
					error=f"Invalid <alias>:<remote> <path>.", 
					chapter="push & pull", 
					mode="--push", 
					notes={
						"<alias>:<path>":"Pack the alias & tuple together as one argument in the following format [<alias>:<path>]."
					},
					json=JSON,)
			alias,remote = remote.split(":")
			exclude = None
			if self.arguments.present("--exclude"): 
				exclude = self.arguments.get("--exclude", chapter="push & pull", mode="--push").split(",")
			elif self.arguments.present("--no-exclude"): exclude = []
			response = ssht00ls.ssync.push(
				alias=alias, 
				remote=remote, 
				path=path,
				exclude=exclude, 
				forced=self.arguments.present("--forced"), 
				delete=self.arguments.present("--delete"), 
				safe=self.arguments.present("--safe"), )
			self.stop(response=response, json=JSON)

		# mount.
		elif self.arguments.present('--mount'):
			remote = self.arguments.get("--mount", index=1, chapter="mounts", mode="--mount", notes={})
			path = self.arguments.get("--mount", index=2, chapter="mounts", mode="--mount", notes={})
			if ":" not in remote:
				self.docs(
					error=f"Invalid <alias>:<remote> <path>.", 
					chapter="mounts", 
					mode="--mount", 
					notes={
						"<alias>:<path>":"Pack the alias & tuple together as one argument in the following format [<alias>:<path>]."
					},
					json=JSON,)
			alias,remote = remote.split(":")
			response = ssht00ls.ssync.mount(
				alias=alias, 
				remote=remote, 
				path=path,
				forced=self.arguments.present("--forced"), )
			self.stop(response=response, json=JSON)

		# unmount.
		elif self.arguments.present('--unmount'):
			path = self.arguments.get("--unmount", index=1, chapter="mounts", mode="--unmount")
			response = ssht00ls.ssync.unmount(
				path=path,
				forced=self.arguments.present("--forced"), 
				sudo=self.arguments.present("--sudo"), )
			self.stop(response=response, json=JSON)

		# index.
		elif self.arguments.present('--index'):
			index = self.arguments.get("--index", chapter="mounts", mode="--index")
			if ":" in index:
				alias,remote = index.split(":")
				response = ssht00ls.ssync.index(path=remote, alias=alias)
			else:
				response = ssht00ls.ssync.index(path=index)
			self.stop(response=response, json=JSON)

		# start daemon.
		elif self.arguments.present('--start-daemon'):
			remote = self.arguments.get("--start-daemon", index=1, chapter="daemons", mode="--start-daemon")
			path = self.arguments.get("--start-daemon", index=2, chapter="daemons", mode="--start-daemon")
			if ":" not in remote:
				self.docs(
					error=f"Invalid <alias>:<remote> <path>.", 
					chapter="damons", 
					mode="--start-daemon", 
					notes={
						"<alias>:<path>":"Pack the alias & tuple together as one argument in the following format [<alias>:<path>]."
					},
					json=JSON,)
			alias,remote = remote.split(":")
			response = ssht00ls.ssync.daemon(alias=alias, remote=remote, path=path)
			self.stop(response=response, json=JSON)

		# stop daemon.
		elif self.arguments.present('--stop-daemon'):
			path = self.arguments.get("--stop-daemon", index=1, chapter="daemon", mode="--stop-daemon")
			response = ssht00ls.ssync.stop_daemon(path)
			self.stop(response=response, json=JSON)

		# config.
		elif self.arguments.present('--config'):
			if JSON:
				print(CONFIG.dictionary)
			else:
				os.system(f"nano {CONFIG.file_path.path}")

		# invalid.
		else: self.invalid()

		#
	
# main.
if __name__ == "__main__":
	cli = CLI()
	cli.start()

```

# Code Examples:

### Table of content:
- [__AES__](#aes)
  * [encrypt](#encrypt)
  * [decrypt](#decrypt)
  * [get_key](#get_key)
  * [generate_salt](#generate_salt)
- [__Agent__](#agent)
  * [generate](#generate)
  * [activate](#activate)
  * [encrypt](#encrypt-1)
  * [decrypt](#decrypt-1)
  * [activated](#properties)
- [__Array__](#array)
  * [load](#load)
  * [save](#save)
- [__AsymmetricAES__](#asymmetricaes)
  * [generate_keys](#generate_keys)
  * [edit_passphrase](#edit_passphrase)
  * [load_keys](#load_keys)
  * [load_private_key](#load_private_key)
  * [load_public_key](#load_public_key)
  * [encrypt](#encrypt-2)
  * [decrypt](#decrypt-2)
  * [encrypt_file](#encrypt_file)
  * [decrypt_file](#decrypt_file)
  * [encrypt_directory](#encrypt_directory)
  * [decrypt_directory](#decrypt_directory)
  * [activated](#properties-1)
- [__Boolean__](#boolean)
  * [string](#string)
  * [instance](#instance)
  * [assign](#assign)
  * [raw](#raw)
- [__Browser__](#browser)
  * [get](#get)
  * [get_element](#get_element)
- [__Bytes__](#bytes)
  * [load](#load-1)
  * [save](#save-1)
  * [instance](#instance-1)
  * [assign](#assign-1)
  * [raw](#raw-1)
- [__CLI__](#cli)
  * [stop](#stop)
  * [docs](#docs)
  * [invalid](#invalid)
- [__Color__](#color)
  * [remove](#remove)
  * [fill](#fill)
  * [boolean](#boolean)
- [__Database__](#database)
  * [activate](#activate-1)
  * [check](#check)
  * [load](#load-2)
  * [save](#save-2)
  * [activated](#properties-2)
- [__Date__](#date)
  * [compare](#compare)
  * [increase](#increase)
  * [decrease](#decrease)
  * [to_seconds](#to_seconds)
  * [from_seconds](#from_seconds)
  * [convert](#convert)
  * [instance](#instance-2)
- [__Defaults__](#defaults)
  * [operating_system](#operating_system)
  * [alias](#alias)
  * [source_path](#source_path)
  * [log_level](#log_level)
  * [pwd](#pwd)
  * [insert](#insert)
  * [site_packages](#site_packages)
  * [install_requirements](#install_requirements)
  * [interactive](#interactive)
- [__Dictionary__](#dictionary)
  * [load](#load-3)
  * [save](#save-3)
- [__Directory__](#directory)
  * [create](#create)
  * [delete](#delete)
  * [check](#check-1)
  * [load](#load-4)
  * [save](#save-4)
  * [paths](#paths)
  * [names](#names)
  * [oldest](#oldest)
  * [newest](#newest)
  * [random](#random)
  * [generate](#generate-1)
  * [structured_join](#structured_join)
  * [contains](#contains)
  * [subpath](#subpath)
  * [fullpath](#fullpath)
  * [set_icon](#set_icon)
  * [index](#index)
  * [open](#open)
  * [find](#find)
  * [replace](#replace)
  * [join](#join)
  * [name](#name)
  * [base](#base)
  * [basename](#basename)
  * [instance](#instance-3)
  * [raw](#raw-2)
- [__Disks__](#disks)
  * [list](#list)
  * [erase](#erase)
  * [partition](#partition)
  * [format](#format)
  * [mount](#mount)
  * [unmount](#unmount)
- [__Encryption__](#encryption)
- [__Env__](#env)
  * [fill](#fill-1)
  * [import_](#import_)
  * [export](#export)
  * [get](#get-1)
  * [get_string](#get_string)
  * [get_boolean](#get_boolean)
  * [get_integer](#get_integer)
  * [get_array](#get_array)
  * [get_tuple](#get_tuple)
  * [get_dictionary](#get_dictionary)
  * [set](#set)
  * [set_string](#set_string)
  * [set_boolean](#set_boolean)
  * [set_integer](#set_integer)
  * [set_array](#set_array)
  * [set_tuple](#set_tuple)
  * [set_dictionary](#set_dictionary)
- [__File__](#file)
  * [load](#load-5)
  * [save](#save-5)
- [__FilePath__](#filepath)
  * [join](#join-1)
  * [name](#name-1)
  * [extension](#extension)
  * [base](#base-1)
  * [basename](#basename-1)
  * [size](#size)
  * [space](#space)
  * [convert_bytes](#convert_bytes)
  * [exists](#exists)
  * [mount](#mount-1)
  * [directory](#directory)
  * [mtime](#mtime)
  * [clean](#clean)
  * [absolute](#absolute)
  * [module](#module)
  * [requirements](#requirements)
  * [delete](#delete-1)
  * [move](#move)
  * [copy](#copy)
  * [open](#open-1)
  * [create](#create-1)
  * [check](#check-2)
  * [split](#split)
  * [count](#count)
  * [replace](#replace-1)
  * [lower](#lower)
  * [upper](#upper)
  * [instance](#instance-4)
  * [assign](#assign-2)
  * [raw](#raw-3)
- [__Files__](#files)
  * [join](#join-2)
  * [load](#load-6)
  * [save](#save-6)
  * [delete](#delete-2)
  * [chmod](#chmod)
  * [chown](#chown)
  * [exists](#exists-1)
  * [directory](#directory-1)
  * [mounted](#mounted)
  * [create](#create-2)
  * [copy](#copy-1)
  * [move](#move-1)
- [__FireWall__](#firewall)
  * [enable](#enable)
  * [disable](#disable)
  * [allow](#allow)
  * [deny](#deny)
  * [allow_all](#allow_all)
  * [deny_all](#deny_all)
  * [set_default](#set_default)
  * [info](#info)
- [__Formats__](#formats)
  * [check](#check-3)
  * [get](#get-2)
  * [initialize](#initialize)
  * [denitialize](#denitialize)
- [__Generate__](#generate)
  * [int](#int)
  * [string](#string-1)
- [__Group__](#group)
  * [create](#create-3)
  * [delete](#delete-3)
  * [check](#check-4)
  * [list_users](#list_users)
  * [delete_users](#delete_users)
  * [add_users](#add_users)
  * [check_users](#check_users)
- [__Image__](#image)
  * [load](#load-7)
  * [edit_pixel](#edit_pixel)
  * [convert](#convert-1)
  * [replace_pixels](#replace_pixels)
  * [replace_colors](#replace_colors)
  * [rgb_to_hex](#rgb_to_hex)
  * [hex_to_rgb](#hex_to_rgb)
  * [instance](#instance-5)
  * [raw](#raw-4)
- [__Integer__](#integer)
  * [increase_version](#increase_version)
  * [round](#round)
  * [round_down](#round_down)
  * [generate](#generate-2)
  * [instance](#instance-6)
  * [assign](#assign-3)
  * [raw](#raw-5)
- [__Loader__](#loader)
  * [run](#run)
  * [stop](#stop-1)
  * [mark](#mark)
  * [hold](#hold)
  * [release](#release)
- [__Network__](#network)
  * [info](#info-1)
  * [convert_dns](#convert_dns)
  * [ping](#ping)
  * [port_in_use](#port_in_use)
  * [free_port](#free_port)
- [__Object__](#object)
  * [items](#items)
  * [keys](#keys)
  * [values](#values)
  * [assign](#assign-4)
  * [attributes](#attributes)
  * [dict](#dict)
  * [unpack](#unpack)
- [__OutputObject__](#outputobject)
  * [instance](#instance-7)
  * [response](#response)
- [__Ownership__](#ownership)
  * [get](#get-3)
  * [set](#set-1)
  * [check](#check-5)
- [__Parameters__](#parameters)
  * [get](#get-4)
  * [check](#check-6)
- [__Permission__](#permission)
  * [get](#get-5)
  * [set](#set-2)
  * [check](#check-7)
- [__ProgressLoader__](#progressloader)
  * [next](#next)
  * [stop](#stop-2)
- [__RSA__](#rsa)
  * [generate_keys](#generate_keys-1)
  * [load_keys](#load_keys-1)
  * [load_public_key](#load_public_key-1)
  * [load_private_key](#load_private_key-1)
  * [edit_passphrase](#edit_passphrase-1)
  * [encrypt_string](#encrypt_string)
  * [encrypt_file](#encrypt_file-1)
  * [encrypt_directory](#encrypt_directory-1)
  * [decrypt_string](#decrypt_string)
  * [decrypt_file](#decrypt_file-1)
  * [decrypt_directory](#decrypt_directory-1)
  * [activated](#properties-3)
- [__Requests__](#requests)
  * [encode](#encode)
  * [get](#get-6)
- [__Response__](#response)
  * [success](#success)
  * [error](#error)
  * [log](#log)
  * [load_logs](#load_logs)
  * [reset_logs](#reset_logs)
  * [serialize](#serialize)
  * [response](#response-1)
  * [log_to_file](#log_to_file)
- [__ResponseObject__](#responseobject)
  * [clean](#clean-1)
  * [assign](#assign-5)
  * [crash](#crash)
  * [unpack](#unpack-1)
  * [remove](#remove-1)
  * [iterate](#iterate)
  * [items](#items-1)
  * [keys](#keys-1)
  * [values](#values-1)
  * [reversed](#reversed)
  * [sort](#sort)
  * [dict](#dict-1)
  * [json](#json)
  * [serialize](#serialize-1)
  * [instance](#instance-8)
  * [raw](#raw-6)
  * [response](#response-2)
- [__RestAPI__](#restapi)
  * [request](#request)
- [__Service__](#service)
  * [create](#create-4)
  * [check](#check-8)
  * [delete](#delete-4)
  * [start](#start)
  * [stop](#stop-3)
  * [restart](#restart)
  * [status](#status)
  * [reset_logs](#reset_logs-1)
  * [tail](#tail)
- [__Spawn__](#spawn)
  * [start](#start-1)
  * [expect](#expect)
  * [read](#read)
  * [kill](#kill)
  * [wait](#wait)
  * [crashed](#crashed)
  * [expecting](#properties-4)
- [__String__](#string)
  * [is_numerical](#is_numerical)
  * [bash](#bash)
  * [identifier](#identifier)
  * [variable_format](#variable_format)
  * [class_format](#class_format)
  * [capitalized_scentence](#capitalized_scentence)
  * [capitalized_word](#capitalized_word)
  * [generate](#generate-3)
  * [first_occurence](#first_occurence)
  * [before_after_first_occurence](#before_after_first_occurence)
  * [before_selected_after_first_occurence](#before_selected_after_first_occurence)
  * [before_after_last_occurence](#before_after_last_occurence)
  * [before_selected_after_last_occurence](#before_selected_after_last_occurence)
  * [between](#between)
  * [increase_version](#increase_version-1)
  * [slice_dict](#slice_dict)
  * [slice_array](#slice_array)
  * [slice_tuple](#slice_tuple)
  * [indent](#indent)
  * [line_indent](#line_indent)
  * [slice_indent](#slice_indent)
  * [first](#first)
  * [last](#last)
  * [remove_first](#remove_first)
  * [remove_last](#remove_last)
  * [split](#split-1)
  * [count](#count-1)
  * [replace](#replace-2)
  * [lower](#lower-1)
  * [upper](#upper-1)
  * [instance](#instance-9)
  * [assign](#assign-6)
  * [raw](#raw-7)
- [__Symbol__](#symbol)
- [__System__](#system)
- [__Thread__](#thread)
  * [run](#run-1)
  * [safe_start](#safe_start)
  * [safe_stop](#safe_stop)
  * [send_stop](#send_stop)
  * [send_crash](#send_crash)
  * [log](#log-1)
  * [run_permission](#properties-5)
- [__Traceback__](#traceback)
  * [traceback](#properties-6)
- [__User__](#user)
  * [create](#create-5)
  * [delete](#delete-5)
  * [check](#check-9)
  * [set_password](#set_password)
  * [add_groups](#add_groups)
  * [delete_groups](#delete_groups)
- [__WebServer__](#webserver)
  * [set](#set-3)
  * [get](#get-7)
  * [app](#app)
  * [run](#run-2)
  * [fork](#fork)
  * [stop](#stop-4)
  * [start_thread](#start_thread)
  * [get_thread](#get_thread)
  * [token](#properties-7)
- [__Zip__](#zip)
  * [create](#create-6)
  * [extract](#extract)
  * [instance](#instance-10)
  * [raw](#raw-8)

## AES:
The aes object class.
``` python 

# initialize the dev0s.encryption.AES object class.
aes = dev0s.encryption.AES(passphrase=None)

```

#### Functions:

##### encrypt:
``` python

# call aes.encrypt.
_ = aes.encrypt(raw)

```
##### decrypt:
``` python

# call aes.decrypt.
_ = aes.decrypt(enc)

```
##### get_key:
``` python

# call aes.get_key.
_ = aes.get_key(salt=None)

```
##### generate_salt:
``` python

# call aes.generate_salt.
_ = aes.generate_salt()

```

## Agent:
The agent object class.
``` python 

# initialize the dev0s.encryption.Agent object class.
agent = dev0s.encryption.Agent(
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
    traceback="dev0s.encryption.Agent", )

```

#### Functions:

##### generate:
``` python

# call agent.generate.
_ = agent.generate(
    # the passphrase (optional to prompt) (str).
    passphrase=None,
    # the verify passphrase (optional).
    verify_passphrase=None,
    # interactive (optional).
    interactive=None )

```
##### activate:
``` python

# call agent.activate.
_ = agent.activate(
    # the key's passphrase (optional to retrieve from webserver) (str).
    passphrase=None,
    # interactive (optional)
    interactive=None, )

```
##### encrypt:
``` python

# call agent.encrypt.
_ = agent.encrypt(string, decode=False)

```
##### decrypt:
``` python

# call agent.decrypt.
_ = agent.decrypt(string, decode=False)

```

#### Properties:
```python

# the activated property.
activated = agent.activated
```
```python

# the public key activated property.
public_key_activated = agent.public_key_activated
```
```python

# the private key activated property.
private_key_activated = agent.private_key_activated
```
```python

# the generated property.
generated = agent.generated
```

## Array:
The array object class.
``` python 

# initialize the Array object class.
array = Array(
    # the path.
    path=None,
    # the default data, specify to call array.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call array.load.
_ = array.load()

```
##### save:
``` python

# call array.save.
_ = array.save()

```

## AsymmetricAES:
The asymmetricaes object class.
``` python 

# initialize the dev0s.encryption.AsymmetricAES object class.
asymmetricaes = dev0s.encryption.AsymmetricAES(
    # the public key (str).
    public_key=None,
    # the private key (str).
    private_key=None,
    # the key passphrase (str / null).
    passphrase=None,
    # enable memory when the keys are not saved.
    memory=False, )

```

#### Functions:

##### generate_keys:
``` python

# call asymmetricaes.generate_keys.
_ = asymmetricaes.generate_keys()

```
##### edit_passphrase:
``` python

# call asymmetricaes.edit_passphrase.
_ = asymmetricaes.edit_passphrase(passphrase=None)

```
##### load_keys:
``` python

# call asymmetricaes.load_keys.
_ = asymmetricaes.load_keys()

```
##### load_private_key:
``` python

# call asymmetricaes.load_private_key.
_ = asymmetricaes.load_private_key()

```
##### load_public_key:
``` python

# call asymmetricaes.load_public_key.
_ = asymmetricaes.load_public_key()

```
##### encrypt:
``` python

# call asymmetricaes.encrypt.
_ = asymmetricaes.encrypt(string, decode=False)

```
##### decrypt:
``` python

# call asymmetricaes.decrypt.
_ = asymmetricaes.decrypt(string, decode=False)

```
##### encrypt_file:
``` python

# call asymmetricaes.encrypt_file.
_ = asymmetricaes.encrypt_file(input=None, output=None, remove=False, base64_encoding=False)

```
##### decrypt_file:
``` python

# call asymmetricaes.decrypt_file.
_ = asymmetricaes.decrypt_file(input=None, output=None, remove=False, base64_encoding=False)

```
##### encrypt_directory:
``` python

# call asymmetricaes.encrypt_directory.
_ = asymmetricaes.encrypt_directory(input=None, output=None, remove=False)

```
##### decrypt_directory:
``` python

# call asymmetricaes.decrypt_directory.
_ = asymmetricaes.decrypt_directory(input=None, output=None, remove=False)

```

#### Properties:
```python

# the activated property.
activated = asymmetricaes.activated
```
```python

# the public key activated property.
public_key_activated = asymmetricaes.public_key_activated
```
```python

# the private key activated property.
private_key_activated = asymmetricaes.private_key_activated
```

## Boolean:
The boolean object class.
``` python 

# initialize the Boolean object class.
boolean = Boolean(boolean=False)

```

#### Functions:

##### string:
``` python

# call boolean.string.
_ = boolean.string(true="True", false="False")

```
##### instance:
``` python

# call boolean.instance.
_ = boolean.instance()

```
##### assign:
``` python

# call boolean.assign.
_ = boolean.assign(boolean)

```
##### raw:
``` python

# call boolean.raw.
_ = boolean.raw()

```

## Browser:
The browser object class.
``` python 

# initialize the dev0s.system.Brwoser object class.
browser = dev0s.system.Brwoser(
    # the driver.
    driver="chromedriver", )

```

#### Functions:

##### get:
``` python

# call browser.get.
_ = browser.get(url)

```
##### get_element:
``` python

# call browser.get_element.
_ = browser.get_element(
    # the element type.
    element="input",
    # the attribute name.
    attribute="name",
    # the attributes value.
    value="username",
    # the parent element (default is browser.driver).
    parent=None, )

```

## Bytes:
The bytes object class.
``` python 

# initialize the Bytes object class.
bytes = Bytes(
    # the bytes (param #1).
    data=b"",
    # the file path.
    path=None, )

```

#### Functions:

##### load:
``` python

# call bytes.load.
_ = bytes.load(sudo=False)

```
##### save:
``` python

# call bytes.save.
_ = bytes.save(bytes=None, sudo=False)

```
##### instance:
``` python

# call bytes.instance.
_ = bytes.instance()

```
##### assign:
``` python

# call bytes.assign.
_ = bytes.assign(b)

```
##### raw:
``` python

# call bytes.raw.
_ = bytes.raw()

```

## CLI:
The cli object class.
``` python 

# initialize the CLI object class.
cli = CLI(alias=None, modes={}, options={}, notes={}, executable=__file__, author="Daan van den Bergh")

```

#### Functions:

##### stop:
``` python

# call cli.stop.
_ = cli.stop(
    # success exit.
    success=True,
    # optional order 1 success message (overwrites success to response.success).
    response={},
    # optional order 2 success message (overwrites success to True).
    message=None,
    # optional order 3 message.
    error=None,
    # json format.
    json=False, )

```
##### docs:
``` python

# call cli.docs.
_ = cli.docs(
    # the chapter (optional).
    chapter=None,
    # the mode (optional).
    mode=None,
    # success exit.
    success=True,
    # optional order 1 success message (overwrites success to response.success).
    response={},
    # optional order 2 success message (overwrites success to True).
    message=None,
    # optional order 3 message.
    error=None,
    # json format.
    json=False,
    # stop after show.
    stop=True,
    # overwrite default notes (dict) (specify to use).
    notes=None, )

```
##### invalid:
``` python

# call cli.invalid.
_ = cli.invalid(error="Selected an invalid mode.", chapter=None, mode=None, json=False)

```

## Color:
The color object class.
``` python 

# import the color object class.
from dev0s import color

```

#### Functions:

##### remove:
``` python

# call color.remove.
_ = color.remove(string)

```
##### fill:
``` python

# call color.fill.
_ = color.fill(string)

```
##### boolean:
``` python

# call color.boolean.
_ = color.boolean(boolean, red=True)

```

## Database:
The database object class.
``` python 

# initialize the dev0s.encryption.Database object class.
database = dev0s.encryption.Database(
    # the aes object class.
    aes=None,
    # the root path of the database.
    path=None, )

```

#### Functions:

##### activate:
``` python

# call database.activate.
_ = database.activate(
    # the key;s passphrase (optional).
    passphrase=None, )

```
##### check:
``` python

# call database.check.
_ = database.check(
    # the subpath of the content (! param number 1).
    path=None,
    # the default content data (! param number 2).
    default=None,
    # save the changes.
    save=True, )

```
##### load:
``` python

# call database.load.
_ = database.load(
    # the subpath of the content (! param number 1).
    path=None,
    # the default data, specify to call database.check() automatically on the data object.
    default=None, )

```
##### save:
``` python

# call database.save.
_ = database.save(
    # the content object (! param number 1).
    content=None, )

```

#### Properties:
```python

# the activated property.
activated = database.activated
```
```python

# the public key activated property.
public_key_activated = database.public_key_activated
```
```python

# the private key activated property.
private_key_activated = database.private_key_activated
```

## Date:
The date object class.
``` python 

# initialize the Date object class.
date = Date(
    #
    # Leave all parameters None to initialize a Date() object with the current date.
    #
    # Initialize a future / previous date.
    #   option 1:
    #     specify the timestamp to initialize a previous / future date (format required).
    timestamp=None,
    #     required for parameter [timestamp].
    format="%d-%m-%y %H:%M",
    #   options 2:
    #     initialize by seconds.
    seconds=None, )

```

#### Functions:

##### compare:
``` python

# call date.compare.
_ = date.compare(comparison=None, current=None, format="%d-%m-%y %H:%M")

```
##### increase:
``` python

# call date.increase.
_ = date.increase(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### decrease:
``` python

# call date.decrease.
_ = date.decrease(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### to_seconds:
``` python

# call date.to_seconds.
_ = date.to_seconds(string, format="%d-%m-%y %H:%M")

```
##### from_seconds:
``` python

# call date.from_seconds.
_ = date.from_seconds(seconds, format="%d-%m-%y %H:%M")

```
##### convert:
``` python

# call date.convert.
_ = date.convert(string, input="%d-%m-%y %H:%M", output="%Y%m%d")

```
##### instance:
``` python

# call date.instance.
_ = date.instance()

```

## Defaults:
The defaults object class.
``` python 

# import the dev0s.defaults object class.
from dev0s.shortcuts import *

```

#### Functions:

##### operating_system:
``` python

# call defaults.operating_system.
_ = defaults.operating_system(supported=["*"])

```
##### alias:
``` python

# call defaults.alias.
_ = defaults.alias(
    # the source name.
    alias=None,
    # the source path.
    executable=None,
    # can use sudo.
    sudo=False,
    # overwrite.
    overwrite=False,
    # the venv path (leave None to ignore).
    venv=None, )

```
##### source_path:
``` python

# call defaults.source_path.
_ = defaults.source_path(path, back=1)

```
##### log_level:
``` python

# call defaults.log_level.
_ = defaults.log_level(default=0)

```
##### pwd:
``` python

# call defaults.pwd.
_ = defaults.pwd()

```
##### insert:
``` python

# call defaults.insert.
_ = defaults.insert(path)

```
##### site_packages:
``` python

# call defaults.site_packages.
_ = defaults.site_packages()

```
##### install_requirements:
``` python

# call defaults.install_requirements.
_ = defaults.install_requirements(
    # the requirements (#1).
    #    str instance: path to file.
    #    list instance: pip requirements in list
    requirements,
    # the silent option.
    silent=False,
    # the log level (Leave None to use defaults.options.log_level).
    log_level=None, )

```
##### interactive:
``` python

# call defaults.interactive.
_ = defaults.interactive(default=False)

```

## Dictionary:
The dictionary object class.
``` python 

# initialize the Dictionary object class.
dictionary = Dictionary(
    # the path.
    path=None,
    # the default data, specify to call dictionary.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call dictionary.load.
_ = dictionary.load()

```
##### save:
``` python

# call dictionary.save.
_ = dictionary.save()

```

## Directory:
The directory object class.
``` python 

# initialize the Directory object class.
directory = Directory(
    # the dirs file path (param #1).
    path=None,
    # the hierarchy to check / create.
    hierarchy={},
    # load the content.
    #load=False,
    # load recursive.
    #recursive=False, )

```

#### Functions:

##### create:
``` python

# call directory.create.
_ = directory.create(file_paths=[], path=None, sudo=False, owner=None, group=None, permission=None)

```
##### delete:
``` python

# call directory.delete.
_ = directory.delete(forced=False)

```
##### check:
``` python

# call directory.check.
_ = directory.check(
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
    silent=False, )

```
##### load:
``` python

# call directory.load.
_ = directory.load(path=None, format=str, default=None, sudo=False)

```
##### save:
``` python

# call directory.save.
_ = directory.save(path=None, data=None, format=str, sudo=False)

```
##### paths:
``` python

# call directory.paths.
_ = directory.paths(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], banned_basenames=["__pycache__"], extensions=["*"])

```
##### names:
``` python

# call directory.names.
_ = directory.names(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], extensions=["*"], remove_extensions=False)

```
##### oldest:
``` python

# call directory.oldest.
_ = directory.oldest()

```
##### newest:
``` python

# call directory.newest.
_ = directory.newest()

```
##### random:
``` python

# call directory.random.
_ = directory.random()

```
##### generate:
``` python

# call directory.generate.
_ = directory.generate(length=24, type="/")

```
##### structured_join:
``` python

# call directory.structured_join.
_ = directory.structured_join(name, type="", structure="alphabetical", create_base=False, sudo=False, owner=None, group=None, permission=None)

```
##### contains:
``` python

# call directory.contains.
_ = directory.contains(name=None, type="/", recursive=False)

```
##### subpath:
``` python

# call directory.subpath.
_ = directory.subpath(fullpath)

```
##### fullpath:
``` python

# call directory.fullpath.
_ = directory.fullpath(subpath)

```
##### set_icon:
``` python

# call directory.set_icon.
_ = directory.set_icon(
    # the path to the .png / .jpg icon.
    icon=None,
    # the directory path (leave None to use directory.fp.path).
    path=None, )

```
##### index:
``` python

# call directory.index.
_ = directory.index(
    # the wanted options.
    metrics=[],
    options=["size", "mtime", "content", "name", "basename", "extension", "mount", "directory"],
    # optional path (leave None to use directory.path).
    path=None, )

```
##### open:
``` python

# call directory.open.
_ = directory.open(path=None, sudo=False)

```
##### find:
``` python

# call directory.find.
_ = directory.find(matches:list, path=None, recursive=False, log_level=0)

```
##### replace:
``` python

# call directory.replace.
_ = directory.replace(replacements:list, path=None, recursive=False, log_level=0)

```
##### join:
``` python

# call directory.join.
_ = directory.join(name=None, type="")

```
##### name:
``` python

# call directory.name.
_ = directory.name()

```
##### base:
``` python

# call directory.base.
_ = directory.base()

```
##### basename:
``` python

# call directory.basename.
_ = directory.basename()

```
##### instance:
``` python

# call directory.instance.
_ = directory.instance()

```
##### raw:
``` python

# call directory.raw.
_ = directory.raw()

```

## Disks:
The disks object class.
``` python 

# import the dev0s.system.disks object class.
from dev0s.shortcuts import *

```

#### Functions:

##### list:
``` python

# call disks.list.
_ = disks.list()

```
##### erase:
``` python

# call disks.erase.
_ = disks.erase(
    # the device without partition number (/dev/sdb).
    device=None, )

```
##### partition:
``` python

# call disks.partition.
_ = disks.partition(
    # the device without partition number (/dev/sdb).
    device=None, )

```
##### format:
``` python

# call disks.format.
_ = disks.format(
    # the device with partition number (/dev/sdb1).
    device=None,
    # the assigned label (name).
    label=None, )

```
##### mount:
``` python

# call disks.mount.
_ = disks.mount(
    # the device with partition number (/dev/sdb1).
    device=None,
    # the mountpoint path.
    path=None, )

```
##### unmount:
``` python

# call disks.unmount.
_ = disks.unmount(
    # the mountpoint path.
    path=None, )

```

## Encryption:
The encryption object class.
``` python 

# initialize the Encryption object class.
encryption = Encryption

```
## Env:
The env object class.
``` python 

# import the dev0s.system.env object class.
from dev0s.shortcuts import *

```

#### Functions:

##### fill:
``` python

# call env.fill.
_ = env.fill(string)

```
##### import_:
``` python

# call env.import_.
_ = env.import_(env=None)

```
##### export:
``` python

# call env.export.
_ = env.export(
    # the environment to export (dict).
    env=None,
    # the export path (str) or paths (list).
    # the paths must have .json / .sh extension or be named 'json' / 'bash' when parameter [format] is undefined.
    export=None,
    # the export format (str) (leave None to be detected by parameter [export]).
    format=None, )

```
##### get:
``` python

# call env.get.
_ = env.get(id, default=None, format="str")

```
##### get_string:
``` python

# call env.get_string.
_ = env.get_string(id, default=None)

```
##### get_boolean:
``` python

# call env.get_boolean.
_ = env.get_boolean(id, default=None)

```
##### get_integer:
``` python

# call env.get_integer.
_ = env.get_integer(id, default=None)

```
##### get_array:
``` python

# call env.get_array.
_ = env.get_array(id, default=None)

```
##### get_tuple:
``` python

# call env.get_tuple.
_ = env.get_tuple(id, default=None)

```
##### get_dictionary:
``` python

# call env.get_dictionary.
_ = env.get_dictionary(id, default=None)

```
##### set:
``` python

# call env.set.
_ = env.set(id, value, format="unknown")

```
##### set_string:
``` python

# call env.set_string.
_ = env.set_string(id, value)

```
##### set_boolean:
``` python

# call env.set_boolean.
_ = env.set_boolean(id, value)

```
##### set_integer:
``` python

# call env.set_integer.
_ = env.set_integer(id, value)

```
##### set_array:
``` python

# call env.set_array.
_ = env.set_array(id, value)

```
##### set_tuple:
``` python

# call env.set_tuple.
_ = env.set_tuple(id, value)

```
##### set_dictionary:
``` python

# call env.set_dictionary.
_ = env.set_dictionary(id, value, subkey="")

```

## File:
The file object class.
``` python 

# initialize the File object class.
file = File(
    # the path.
    path=None,
    # the default data, specify to call file.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call file.load.
_ = file.load()

```
##### save:
``` python

# call file.save.
_ = file.save()

```

## FilePath:
The file_path object class.
``` python 

# initialize the FilePath object class.
file_path = FilePath(path, default=False, check=False, load=False)

```

#### Functions:

##### join:
``` python

# call file_path.join.
_ = file_path.join(name=None, type="/")

```
##### name:
``` python

# call file_path.name.
_ = file_path.name(path=None, remove_extension=False,)

```
##### extension:
``` python

# call file_path.extension.
_ = file_path.extension(name=None, path=None)

```
##### base:
``` python

# call file_path.base.
_ = file_path.base(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the dirs back.
    back=1, )

```
##### basename:
``` python

# call file_path.basename.
_ = file_path.basename(back=1, path=None)

```
##### size:
``` python

# call file_path.size.
_ = file_path.size(format=str,  mode="auto", path=None, options=["auto", "bytes", "kb", "mb", "gb", "tb"])

```
##### space:
``` python

# call file_path.space.
_ = file_path.space(format=str,  mode="auto", path=None, options=["auto", "bytes", "kb", "mb", "gb", "tb"])

```
##### convert_bytes:
``` python

# call file_path.convert_bytes.
_ = file_path.convert_bytes(bytes:int, format=str, mode="auto", options=["auto", "bytes", "kb", "mb", "gb", "tb"])

```
##### exists:
``` python

# call file_path.exists.
_ = file_path.exists(
    # the path (leave None to use file_path.path) (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mount:
``` python

# call file_path.mount.
_ = file_path.mount(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### directory:
``` python

# call file_path.directory.
_ = file_path.directory(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### mtime:
``` python

# call file_path.mtime.
_ = file_path.mtime(format='%d-%m-%y %H:%M.%S', path=None)

```
##### clean:
``` python

# call file_path.clean.
_ = file_path.clean(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the clean options.
    remove_double_slash=True,
    remove_first_slash=False,
    remove_last_slash=False,
    ensure_first_slash=False,
    ensure_last_slash=False, )

```
##### absolute:
``` python

# call file_path.absolute.
_ = file_path.absolute(
    # the path (leave None to use file_path.path) (param #1).
    path=None, )

```
##### module:
``` python

# call file_path.module.
_ = file_path.module(path=None)

```
##### requirements:
``` python

# call file_path.requirements.
_ = file_path.requirements(path=None, format="pip", include_version=True)

```
##### delete:
``` python

# call file_path.delete.
_ = file_path.delete(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the options.
    forced=False,
    sudo=False,
    silent=False, )

```
##### move:
``` python

# call file_path.move.
_ = file_path.move(path=None, sudo=False, silent=False)

```
##### copy:
``` python

# call file_path.copy.
_ = file_path.copy(path=None, sudo=False, silent=False)

```
##### open:
``` python

# call file_path.open.
_ = file_path.open(sudo=False)

```
##### create:
``` python

# call file_path.create.
_ = file_path.create(
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
    sudo=False, )

```
##### check:
``` python

# call file_path.check.
_ = file_path.check(
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
    recursive=False, # for directories only (for permission & ownership check) )

```
##### split:
``` python

# call file_path.split.
_ = file_path.split(path)

```
##### count:
``` python

# call file_path.count.
_ = file_path.count(path)

```
##### replace:
``` python

# call file_path.replace.
_ = file_path.replace(from_, to_)

```
##### lower:
``` python

# call file_path.lower.
_ = file_path.lower(path)

```
##### upper:
``` python

# call file_path.upper.
_ = file_path.upper(path)

```
##### instance:
``` python

# call file_path.instance.
_ = file_path.instance()

```
##### assign:
``` python

# call file_path.assign.
_ = file_path.assign(path, load=False)

```
##### raw:
``` python

# call file_path.raw.
_ = file_path.raw()

```

## Files:
The files object class.
``` python 

# initialize the Files object class.
files = Files(path=None, name=None, type="")

```

#### Functions:

##### join:
``` python

# call files.join.
_ = Files.join(path=None, name=None, type="")

```
##### load:
``` python

# call files.load.
_ = Files.load(path, data="not to be used", format="str", raw=False, sudo=False)

```
##### save:
``` python

# call files.save.
_ = Files.save(
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
    __real_path__=None, )

```
##### delete:
``` python

# call files.delete.
_ = Files.delete(
    # the path (param #1).
    path=None,
    # root permission required.
    sudo=False,
    # forced mode.
    forced=False,
    # hide logs.
    silent=False, )

```
##### chmod:
``` python

# call files.chmod.
_ = Files.chmod(
    # the path (param #1).
    path=None,
    # the new permission.
    permission=None,
    # recursive for entire dir.
    recursive=False,
    # root permission required.
    sudo=False, )

```
##### chown:
``` python

# call files.chown.
_ = Files.chown(
    # the path (param #1).
    path=None,
    # the new owner.
    owner=None,
    # the new group (optional).
    group=None,
    # recursive for entire dir.
    recursive=False,
    # root permission required.
    sudo=False, )

```
##### exists:
``` python

# call files.exists.
_ = Files.exists(path=None, sudo=False)

```
##### directory:
``` python

# call files.directory.
_ = Files.directory(
    # the path (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mounted:
``` python

# call files.mounted.
_ = Files.mounted(
    # the path (#1).
    path=None, )

```
##### create:
``` python

# call files.create.
_ = Files.create(
    # the path to the file (str) (REQUIRED) (#1).
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
    sudo=False, )

```
##### copy:
``` python

# call files.copy.
_ = Files.copy(
    # the from & to path (#1 & #2).
    from_, to_,
    # root permission required.
    sudo=False,
    # root permission required.
    log_level=0, )

```
##### move:
``` python

# call files.move.
_ = Files.move(
    # the from & to path (#1 & #2).
    from_, to_,
    # root permission required.
    sudo=False,
    # root permission required.
    log_level=0, )

```

## FireWall:
The fire_wall object class.
``` python 

# import the dev0s.network.firewall object class.
from dev0s.shortcuts import *

```

#### Functions:

##### enable:
``` python

# call fire_wall.enable.
_ = fire_wall.enable()

```
##### disable:
``` python

# call fire_wall.disable.
_ = fire_wall.disable()

```
##### allow:
``` python

# call fire_wall.allow.
_ = fire_wall.allow(port)

```
##### deny:
``` python

# call fire_wall.deny.
_ = fire_wall.deny(port)

```
##### allow_all:
``` python

# call fire_wall.allow_all.
_ = fire_wall.allow_all()

```
##### deny_all:
``` python

# call fire_wall.deny_all.
_ = fire_wall.deny_all()

```
##### set_default:
``` python

# call fire_wall.set_default.
_ = fire_wall.set_default(deny=True)

```
##### info:
``` python

# call fire_wall.info.
_ = fire_wall.info()

```

## Formats:
The formats object class.
``` python 

# initialize the Formats object class.
formats = Formats(i.upper())

```

#### Functions:

##### check:
``` python

# call formats.check.
_ = Formats.check(
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
    none_allowed_dictionaries=None, )

```
##### get:
``` python

# call formats.get.
_ = Formats.get(value, serialize=False)

```
##### initialize:
``` python

# call formats.initialize.
_ = Formats.initialize(
    # the object / value (#1 param).
    obj=None,
    # list / dict with objects.
    objects=None,
    # initialize file paths.
    file_paths=False,
    # the forced format.
    format=None, )

```
##### denitialize:
``` python

# call formats.denitialize.
_ = Formats.denitialize(
    # the object / value (#1 param).
    obj=None,
    # list / dict with objects.
    objects=None,
    # initialize file paths.
    file_paths=True, )

```

## Generate:
The generate object class.
``` python 

# initialize the Generate object class.
generate = Generate()

```

#### Functions:

##### int:
``` python

# call generate.int.
_ = generate.int(length=6)

```
##### string:
``` python

# call generate.string.
_ = generate.string(length=6, capitalize=True, digits=True)

```

## Group:
The group object class.
``` python 

# initialize the dev0s.system.Group object class.
group = dev0s.system.Group(
    
    # string format.
    name=None,
    users=[], # all authorized user identifiers.
    # boolean format.
    get_users=False, # (only gets filled if the storages group exists.) )

```

#### Functions:

##### create:
``` python

# call group.create.
_ = group.create(users=None)

```
##### delete:
``` python

# call group.delete.
_ = group.delete()

```
##### check:
``` python

# call group.check.
_ = group.check()

```
##### list_users:
``` python

# call group.list_users.
_ = group.list_users()

```
##### delete_users:
``` python

# call group.delete_users.
_ = group.delete_users(users=[])

```
##### add_users:
``` python

# call group.add_users.
_ = group.add_users(users=[])

```
##### check_users:
``` python

# call group.check_users.
_ = group.check_users(users=[])

```

## Image:
The image object class.
``` python 

# initialize the Image object class.
image = Image(path=None, image=None, load=False)

```

#### Functions:

##### load:
``` python

# call image.load.
_ = image.load(path=None)

```
##### edit_pixel:
``` python

# call image.edit_pixel.
_ = image.edit_pixel(pixel=[0, 0], new_pixel_tuple=None)

```
##### convert:
``` python

# call image.convert.
_ = image.convert(input='logo.png', output='logo.ico')

```
##### replace_pixels:
``` python

# call image.replace_pixels.
_ = image.replace_pixels(input_path=None, output_path=None, input_hex=None, output_hex=None)

```
##### replace_colors:
``` python

# call image.replace_colors.
_ = image.replace_colors(input_path=None, output_path=None, hex=None)

```
##### rgb_to_hex:
``` python

# call image.rgb_to_hex.
_ = image.rgb_to_hex(tuple)

```
##### hex_to_rgb:
``` python

# call image.hex_to_rgb.
_ = image.hex_to_rgb(_hex_)

```
##### instance:
``` python

# call image.instance.
_ = image.instance()

```
##### raw:
``` python

# call image.raw.
_ = image.raw()

```

## Integer:
The integer object class.
``` python 

# initialize the Integer object class.
integer = Integer(value=0, format="auto")

```

#### Functions:

##### increase_version:
``` python

# call integer.increase_version.
_ = integer.increase_version()

```
##### round:
``` python

# call integer.round.
_ = integer.round(decimals)

```
##### round_down:
``` python

# call integer.round_down.
_ = integer.round_down(decimals)

```
##### generate:
``` python

# call integer.generate.
_ = integer.generate(length=6)

```
##### instance:
``` python

# call integer.instance.
_ = integer.instance()

```
##### assign:
``` python

# call integer.assign.
_ = integer.assign(value)

```
##### raw:
``` python

# call integer.raw.
_ = integer.raw()

```

## Loader:
The loader object class.
``` python 

# initialize the Loader object class.
loader = Loader(message, autostart=True, log_level=0, interactive=True)

```

#### Functions:

##### run:
``` python

# call loader.run.
_ = loader.run()

```
##### stop:
``` python

# call loader.stop.
_ = loader.stop(message=None, success=True, response=None, quiet=False)

```
##### mark:
``` python

# call loader.mark.
_ = loader.mark(new_message=None, old_message=None, success=True, response=None)

```
##### hold:
``` python

# call loader.hold.
_ = loader.hold()

```
##### release:
``` python

# call loader.release.
_ = loader.release()

```

## Network:
The network object class.
``` python 

# import the dev0s.network object class.
from dev0s.shortcuts import *

```

#### Functions:

##### info:
``` python

# call network.info.
_ = network.info()

```
##### convert_dns:
``` python

# call network.convert_dns.
_ = network.convert_dns(dns, timeout=1)

```
##### ping:
``` python

# call network.ping.
_ = network.ping(ip, timeout=1)

```
##### port_in_use:
``` python

# call network.port_in_use.
_ = network.port_in_use(port, host="127.0.0.1")

```
##### free_port:
``` python

# call network.free_port.
_ = network.free_port(start=6080)

```

## Object:
The object object class.
``` python 

# initialize the Object object class.
object = Object(
    # attributes (dict) (#1)
    attributes={},
    # the imported traceback.
    traceback="Object",
    # the raw traceback.
    raw_traceback="Object", )

```

#### Functions:

##### items:
``` python

# call object.items.
_ = object.items(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### keys:
``` python

# call object.keys.
_ = object.keys(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### values:
``` python

# call object.values.
_ = object.values()

```
##### assign:
``` python

# call object.assign.
_ = object.assign(
    # the dictionary to self assign.
    dictionary,
    # serialize dictionary from str to object.
    serialize=True,
    # the keys to get from the dict (leave default to unpack the present keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### attributes:
``` python

# call object.attributes.
_ = object.attributes(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### dict:
``` python

# call object.dict.
_ = object.dict(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### unpack:
``` python

# call object.unpack.
_ = object.unpack(
    # the key / keys / defaults parameter (#1).
    # str instance:
    #   unpack the str key
    # list instance:
    #   unpack all keys in the list.
    # dict instance:
    #   unpack all keys from the dict & when not present return the key's value as default.
    keys, )

```

## OutputObject:
The output_object object class.
``` python 

# initialize the OutputObject object class.
output_object = OutputObject(
    #
    # The return object from function: dec0s.code.execute
    # The OutputObject object is very similair to the ResponseObject.
    #
    # the success message (param #1).
    message=None,
    # the attributes (param #2).
    attributes={},
    # the error message (param #3).
    error=None,
    # the log level.
    log_level=defaults.options.log_level, )

```

#### Functions:

##### instance:
``` python

# call output_object.instance.
_ = output_object.instance()

```
##### response:
``` python

# call output_object.response.
_ = output_object.response()

```

## Ownership:
The ownership object class.
``` python 

# initialize the Ownership object class.
ownership = Ownership(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call ownership.get.
_ = ownership.get(path=None)

```
##### set:
``` python

# call ownership.set.
_ = ownership.set(
    # the permission (str) (#1).
    owner=None,
    # the group (str) (optional) (#2).
    group=None,
    # the path (optional) (overwrites ownership.path) (#3).
    path=None,
    # root permission required.
    sudo=False,
    # recursive.
    recursive=False,
    # silent.
    silent=False, )

```
##### check:
``` python

# call ownership.check.
_ = ownership.check(owner=None, group=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## Parameters:
The parameters object class.
``` python 

# import the dev0s.response.parameters object class.
from dev0s.shortcuts import *

```

#### Functions:

##### get:
``` python

# call parameters.get.
_ = parameters.get(
    # the django request (1).
    request=None,
    # the identifiers (#2).
    #    str instance: return the parameters value.
    #    list instance: return a parameters object & return an error response when a parameter is undefined.
    #    dict instance: return a parameters object & return the parameter's value from the dict as a default when undefined.
    parameters=[],
    # traceback id.
    traceback=None, )

```
##### check:
``` python

# call parameters.check.
_ = parameters.check(
    # the parameters (dict) (#1).
    parameters={"parameter":None},
    # the recognizer value for when the parameters are supposed to be empty.
    default=None,
    # the traceback id.
    traceback=None, )

```

## Permission:
The permission object class.
``` python 

# initialize the Permission object class.
permission = Permission(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call permission.get.
_ = permission.get(path=None)

```
##### set:
``` python

# call permission.set.
_ = permission.set(
    # the permission (int) (#1).
    permission=None,
    # the path (optional) (overwrites permission.path) (#2).
    path=None,
    # root permission required.
    sudo=False,
    # recursive.
    recursive=False,
    # silent.
    silent=False, )

```
##### check:
``` python

# call permission.check.
_ = permission.check(permission=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## ProgressLoader:
The progress_loader object class.
``` python 

# initialize the ProgressLoader object class.
progress_loader = ProgressLoader(message, index=0, max=10, log_level=0)

```

#### Functions:

##### next:
``` python

# call progress_loader.next.
_ = progress_loader.next(count=1, decimals=2)

```
##### stop:
``` python

# call progress_loader.stop.
_ = progress_loader.stop(message=None, success=True, response=None)

```

## RSA:
The rsa object class.
``` python 

# initialize the dev0s.encryption.RSA object class.
rsa = dev0s.encryption.RSA(
    # option 1:
    #     the key directory.
    directory=None,
    # option 2:
    public_key=None,
    private_key=None,
    memory=False, # enable memory when the keys are not saved.
    # the key's passphrase (Leave None for no passphrase).
    passphrase=None, )

```

#### Functions:

##### generate_keys:
``` python

# call rsa.generate_keys.
_ = rsa.generate_keys(log_level=0)

```
##### load_keys:
``` python

# call rsa.load_keys.
_ = rsa.load_keys()

```
##### load_public_key:
``` python

# call rsa.load_public_key.
_ = rsa.load_public_key()

```
##### load_private_key:
``` python

# call rsa.load_private_key.
_ = rsa.load_private_key()

```
##### edit_passphrase:
``` python

# call rsa.edit_passphrase.
_ = rsa.edit_passphrase(passphrase=None)

```
##### encrypt_string:
``` python

# call rsa.encrypt_string.
_ = rsa.encrypt_string(string, layers=1, decode=True)

```
##### encrypt_file:
``` python

# call rsa.encrypt_file.
_ = rsa.encrypt_file(path, layers=1)

```
##### encrypt_directory:
``` python

# call rsa.encrypt_directory.
_ = rsa.encrypt_directory(path, recursive=False, layers=1)

```
##### decrypt_string:
``` python

# call rsa.decrypt_string.
_ = rsa.decrypt_string(string, layers=1, decode=True)

```
##### decrypt_file:
``` python

# call rsa.decrypt_file.
_ = rsa.decrypt_file(path, layers=1)

```
##### decrypt_directory:
``` python

# call rsa.decrypt_directory.
_ = rsa.decrypt_directory(path, recursive=False, layers=1)

```

#### Properties:
```python

# the activated property.
activated = rsa.activated
```
```python

# the private key activated property.
private_key_activated = rsa.private_key_activated
```
```python

# the public key activated property.
public_key_activated = rsa.public_key_activated
```

## Requests:
The requests object class.
``` python 

# import the dev0s.requests object class.
from dev0s.shortcuts import *

```

#### Functions:

##### encode:
``` python

# call requests.encode.
_ = requests.encode(data)

```
##### get:
``` python

# call requests.get.
_ = requests.get(
    # the url (str) (#1).
    url=None,
    # the sended post data (dict) (#2).
    data={},
    # serialize output to dictionary.
    serialize=False, )

```

## Response:
The response object class.
``` python 

# import the dev0s.response object class.
from dev0s.shortcuts import *

```

#### Functions:

##### success:
``` python

# call response.success.
_ = response.success(
    # the message (must be param #1).
    message,
    # additional returnable functions (must be param #2).
    variables={},
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use response.log_level).
    required_log_level=None,
    # save the error to the logs file.
    save=False,
    # return as a django Jsonresponse.
    django=False, )

```
##### error:
``` python

# call response.error.
_ = response.error(
    # the error message.
    error="",
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use response.log_level).
    required_log_level=None,
    # save the error to the erros file.
    save=False,
    # return as a django Jsonresponse.
    django=False,
    # raise error for developer traceback.
    traceback=ERROR_TRACEBACK, )

```
##### log:
``` python

# call response.log.
_ = response.log(
    # option 1:
    # the message (#1 param).
    message=None,
    # option 2:
    # the error.
    error=None,
    # option 3:
    # the response dict (leave message None to use).
    response={},
    # print the response as json.
    json=False,
    # optionals:
    # the active log level.
    log_level=0,
    # the required log level for when printed to console (leave None to use response.log_level).
    required_log_level=None,
    # save to log file.
    save=False,
    # save errors always (for options 2 & 3 only).
    save_errors=None,
    # the log mode (leave None for default).
    mode=None, )

```
##### load_logs:
``` python

# call response.load_logs.
_ = response.load_logs(format="webserver", options=["webserver", "cli", "array", "string"])

```
##### reset_logs:
``` python

# call response.reset_logs.
_ = response.reset_logs()

```
##### serialize:
``` python

# call response.serialize.
response = response.serialize(
    # the response (#1) (dict) (str repr of dict) (ResponseObject) (generator) .
    response={},
    # init to response object.
    init=True, )

```
##### response:
``` python

# call response.response.
_ = response.response(
    # the blank response (dict, str, generator) (#1).
    response={
        "success":False,
        "message":None,
        "error":None,
    }, )

```
##### log_to_file:
``` python

# call response.log_to_file.
_ = response.log_to_file(message, raw=False)

```

## ResponseObject:
The response_object object class.
``` python 

# initialize the ResponseObject object class.
response_object = ResponseObject(
    #
    # Should be initialized with response.success or response.error.
    #
    # the response attributes (dict or dict in str format).
    attributes={
        "success":False,
        "message":None,
        "error":None,
    }, )

```

#### Functions:

##### clean:
``` python

# call response_object.clean.
_ = response_object.clean(
    # the clean options, select * for all, options: [traceback].
    options=["*"],
    # serialize to ResponseObject (with serialize False the ResponseObject's values are not updated).
    serialize=True, )

```
##### assign:
``` python

# call response_object.assign.
_ = response_object.assign(dictionary)

```
##### crash:
``` python

# call response_object.crash.
_ = response_object.crash(error="ValueError", traceback=True, json=False, error_only=False)

```
##### unpack:
``` python

# call response_object.unpack.
_ = response_object.unpack(
    # the key / keys / defaults parameter (#1).
    # str instance:
    #   unpack the str key
    # list instance:
    #   unpack all keys in the list.
    # dict instance:
    #   unpack all keys from the dict & when not present return the key's value as default.
    keys, )

```
##### remove:
``` python

# call response_object.remove.
_ = response_object.remove(keys=[], values=[], save=False)

```
##### iterate:
``` python

# call response_object.iterate.
_ = response_object.iterate(sorted=False, reversed=False)

```
##### items:
``` python

# call response_object.items.
_ = response_object.items(sorted=False, reversed=False, dictionary=None)

```
##### keys:
``` python

# call response_object.keys.
_ = response_object.keys(sorted=False, reversed=False)

```
##### values:
``` python

# call response_object.values.
_ = response_object.values(sorted=False, reversed=False, dictionary=None)

```
##### reversed:
``` python

# call response_object.reversed.
_ = response_object.reversed(dictionary=None)

```
##### sort:
``` python

# call response_object.sort.
_ = response_object.sort(alphabetical=True, ascending=False, reversed=False, dictionary=None)

```
##### dict:
``` python

# call response_object.dict.
_ = response_object.dict(sorted=False, reversed=False, json=False)

```
##### json:
``` python

# call response_object.json.
_ = response_object.json(sorted=False, reversed=False, indent=4, dictionary=None, )

```
##### serialize:
``` python

# call response_object.serialize.
_ = response_object.serialize(sorted=False, reversed=False, json=False, dictionary=None)

```
##### instance:
``` python

# call response_object.instance.
_ = response_object.instance()

```
##### raw:
``` python

# call response_object.raw.
_ = response_object.raw()

```
##### response:
``` python

# call response_object.response.
_ = response_object.response()

```

## RestAPI:
The restapi object class.
``` python 

# initialize the dev0s.requests.RestAPI object class.
restapi = dev0s.requests.RestAPI(
    # the root url (optional).
    url=None,
    # the default data send with every request (will be appended to local data).
    data={
        "api_key":None,
    }, )

```

#### Functions:

##### request:
``` python

# call restapi.request.
_ = restapi.request(url="/", data={})

```

## Service:
The service object class.
``` python 

# initialize the dev0s.system.Service object class.
service = dev0s.system.Service(
    # the service id.
    id=None,
    # the user & group on which the service will be run.
    user=None,
    group=None,
    # the start command.
    start=None,
    # the service description.
    description="",
    # restart on crash.
    restart=True,
    # the restart limit.
    restart_limit=5,
    # the restart delay.
    restart_delay=10,
    # the path to the log file.
    logs=None,
    # the path to the error file.
    errors=None,
    # the object's log level.
    log_level=0,
    # the import traceback.
    traceback="dev0s.system.Service", )

```

#### Functions:

##### create:
``` python

# call service.create.
_ = service.create()

```
##### check:
``` python

# call service.check.
_ = service.check()

```
##### delete:
``` python

# call service.delete.
_ = service.delete()

```
##### start:
``` python

# call service.start.
_ = service.start()

```
##### stop:
``` python

# call service.stop.
_ = service.stop()

```
##### restart:
``` python

# call service.restart.
_ = service.restart()

```
##### status:
``` python

# call service.status.
_ = service.status()

```
##### reset_logs:
``` python

# call service.reset_logs.
_ = service.reset_logs()

```
##### tail:
``` python

# call service.tail.
_ = service.tail(global_=False, debug=False)

```

## Spawn:
The spawn object class.
``` python 

# initialize the Spawn object class.
spawn = Spawn(
    #
    # Should be initialized with function: dev0s.code.execute
    #
    # the full command (str) (#1).
    command="ls",
    # asynchronous.
    async_=False,
    # the log level.
    log_level=defaults.options.log_level,
    # additional attributes.
    attributes={},
    # system options.
    response_str=None, )

```

#### Functions:

##### start:
``` python

# call spawn.start.
_ = spawn.start()

```
##### expect:
``` python

# call spawn.expect.
_ = spawn.expect(
    # the expected data parameter (#1).
    #    str instantce: expect a single identifier.
    #    list instance: expect one of the provided identifiers & return the found one if success.
    expect=["Password*"],
    # the optional data to send (#2).
    #    none instance: do not send anything.
    #    str instance: the data to send.
    #    list/tuple instance: send value of index from expected expect (required expect to be a list, Array & the indexes of [expect, send] be match).
    send=None,
    # the timeout (float).
    timeout=1.0, )

```
##### read:
``` python

# call spawn.read.
_ = spawn.read(
    # with await False it reads only the printed output regardless the status & never throws timeout.
    wait=False,
    # the timeout, leave None for no timeout.
    timeout=None,
    # the live boolean (bool) (prints live logs to console when enabled) (leave None to use spawn.log_level >= 1).
    live=None,
    # system variables.
    #   safe True always a response.output variable upon error the response.output is "".
    __safe__=False, )

```
##### kill:
``` python

# call spawn.kill.
_ = spawn.kill()

```
##### wait:
``` python

# call spawn.wait.
_ = spawn.wait(
    # the live boolean (bool) (prints live logs to console when enabled) (leave None to use spawn.log_level >= 1).
    live=None,
    sleeptime=1,
    # the timeout (leave None to ignore).
    timeout=None, )

```
##### crashed:
``` python

# call spawn.crashed.
_ = spawn.crashed()

```

#### Properties:
```python

# the expecting property.
expecting = spawn.expecting
```
```python

# the running property.
running = spawn.running
```
```python

# the exit status property.
exit_status = spawn.exit_status
```
```python

# the output property.
output = spawn.output
```
```python

# the pid property.
pid = spawn.pid
```

## String:
The string object class.
``` python 

# initialize the String object class.
string = String(string="")

```

#### Functions:

##### is_numerical:
``` python

# call string.is_numerical.
_ = string.is_numerical()

```
##### bash:
``` python

# call string.bash.
_ = string.bash()

```
##### identifier:
``` python

# call string.identifier.
_ = string.identifier()

```
##### variable_format:
``` python

# call string.variable_format.
_ = string.variable_format(
    exceptions={
        "smart_card":"smartcard",
        "smart_cards":"smartcards" ,
        "web_server":"webserver" ,
    }, )

```
##### class_format:
``` python

# call string.class_format.
_ = string.class_format()

```
##### capitalized_scentence:
``` python

# call string.capitalized_scentence.
_ = string.capitalized_scentence()

```
##### capitalized_word:
``` python

# call string.capitalized_word.
_ = string.capitalized_word()

```
##### generate:
``` python

# call string.generate.
_ = string.generate(
    # the length of the generated string.
    length=6,
    # include digits.
    digits=False,
    # include capital letters.
    capitalize=False,
    # include special characters.
    special=False, )

```
##### first_occurence:
``` python

# call string.first_occurence.
_ = string.first_occurence(charset=[" ", "\n"], reversed=False, string=None)

```
##### before_after_first_occurence:
``` python

# call string.before_after_first_occurence.
_ = string.before_after_first_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_first_occurence:
``` python

# call string.before_selected_after_first_occurence.
_ = string.before_selected_after_first_occurence(slicer=" ", string=None)

```
##### before_after_last_occurence:
``` python

# call string.before_after_last_occurence.
_ = string.before_after_last_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_last_occurence:
``` python

# call string.before_selected_after_last_occurence.
_ = string.before_selected_after_last_occurence(slicer=" ", string=None)

```
##### between:
``` python

# call string.between.
_ = string.between(identifiers=["{","}"], depth=1, include=True, string=None)

```
##### increase_version:
``` python

# call string.increase_version.
_ = string.increase_version()

```
##### slice_dict:
``` python

# call string.slice_dict.
_ = string.slice_dict(depth=1)

```
##### slice_array:
``` python

# call string.slice_array.
_ = string.slice_array(depth=1)

```
##### slice_tuple:
``` python

# call string.slice_tuple.
_ = string.slice_tuple(depth=1)

```
##### indent:
``` python

# call string.indent.
_ = string.indent(indent=4)

```
##### line_indent:
``` python

# call string.line_indent.
_ = string.line_indent(line="")

```
##### slice_indent:
``` python

# call string.slice_indent.
_ = string.slice_indent(indent=4, depth=1, string=None, remove_indent=True)

```
##### first:
``` python

# call string.first.
_ = string.first(count)

```
##### last:
``` python

# call string.last.
_ = string.last(count)

```
##### remove_first:
``` python

# call string.remove_first.
_ = string.remove_first(count)

```
##### remove_last:
``` python

# call string.remove_last.
_ = string.remove_last(count)

```
##### split:
``` python

# call string.split.
_ = string.split(string)

```
##### count:
``` python

# call string.count.
_ = string.count(string)

```
##### replace:
``` python

# call string.replace.
_ = string.replace(from_, to_)

```
##### lower:
``` python

# call string.lower.
_ = string.lower(string)

```
##### upper:
``` python

# call string.upper.
_ = string.upper(string)

```
##### instance:
``` python

# call string.instance.
_ = string.instance()

```
##### assign:
``` python

# call string.assign.
_ = string.assign(string)

```
##### raw:
``` python

# call string.raw.
_ = string.raw()

```

## Symbol:
The symbol object class.
``` python 

# import the symbol object class.
from dev0s import symbol

```
## System:
The system object class.
``` python 

# initialize the System object class.
system = System

```
## Thread:
The thread object class.
``` python 

# initialize the Thread object class.
thread = Thread(
    # the threads id (#1).
    id="Thread",
    # the imported traceback.
    traceback="Thread",
    # the raw traceback.
    raw_traceback="Thread",
    # the threads log level.
    log_level=-1, )

```

#### Functions:

##### run:
``` python

# call thread.run.
_ = thread.run()

```
##### safe_start:
``` python

# call thread.safe_start.
_ = thread.safe_start(timeout=120, sleeptime=1)

```
##### safe_stop:
``` python

# call thread.safe_stop.
_ = thread.safe_stop(timeout=120, sleeptime=1)

```
##### send_stop:
``` python

# call thread.send_stop.
_ = thread.send_stop(
    # all optional.
    # option 1: the success message.
    message=None, # (1)
    args={}, # (2)
    # option 2: the error message.
    error=None,
    # option 3: the response object.
    response=None,
    # save the message/error/response.
    save=False,
    # the active log level (int) (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when to print to console (leave None to use _response_.log_level ; default: 0).
    required_log_level=_response_.log_level, )

```
##### send_crash:
``` python

# call thread.send_crash.
_ = thread.send_crash(
    # all optional.
    # option 1: the success message.
    message=None, # (1)
    args={}, # (2)
    # option 2: the error message.
    error=None,
    # option 3: the response object.
    response=None,
    # save the message/error/response.
    save=False,
    # the active log level (int) (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when to print to console (leave None to use _response_.log_level ; default: 0).
    required_log_level=_response_.log_level, )

```
##### log:
``` python

# call thread.log.
_ = thread.log(
    # option 1:
    # the message (#1 param).
    message=None,
    # option 2:
    # the error.
    error=None,
    # option 3:
    # the response dict (leave message None to use).
    response={},
    # print the response as json.
    json=JSON,
    # optionals:
    # the active log level (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when printed to console.
    required_log_level=0,
    # save to log file.
    save=False,
    # save errors always (for options 2 & 3 only).
    save_errors=None,
    # the log mode (leave None for default).
    mode=None, )

```

#### Properties:
```python

# the run permission property.
run_permission = thread.run_permission
```
```python

# the running property.
running = thread.running
```
```python

# the stopped property.
stopped = thread.stopped
```
```python

# the crashed property.
crashed = thread.crashed
```
```python

# the response property.
response = thread.response
```

## Traceback:
The traceback object class.
``` python 

# initialize the Traceback object class.
traceback = Traceback(
    # the imported traceback (#1).
    traceback="Traceback",
    # the raw traceback (#2).
    raw_traceback="Object", )

```
#### Properties:
```python

# the traceback property.
traceback = traceback.traceback
```

## User:
The user object class.
``` python 

# initialize the dev0s.system.User object class.
user = dev0s.system.User(
    # the users username.
    username=None, )

```

#### Functions:

##### create:
``` python

# call user.create.
_ = user.create()

```
##### delete:
``` python

# call user.delete.
_ = user.delete()

```
##### check:
``` python

# call user.check.
_ = user.check(silent=False)

```
##### set_password:
``` python

# call user.set_password.
_ = user.set_password(password=None)

```
##### add_groups:
``` python

# call user.add_groups.
_ = user.add_groups(groups=[])

```
##### delete_groups:
``` python

# call user.delete_groups.
_ = user.delete_groups(groups=[])

```

## WebServer:
The webserver object class.
``` python 

# initialize the dev0s.database.WebServer object class.
webserver = dev0s.database.WebServer(
    id="webserver",
    host="127.0.0.1",
    port=52379,
    sleeptime=3,
    log_level=0,
    # do not use.
    serialized={}, )

```

#### Functions:

##### set:
``` python

# call webserver.set.
_ = webserver.set(group=None, id=None, data=None, timeout=3)

```
##### get:
``` python

# call webserver.get.
_ = webserver.get(group=None, id=None, timeout=3)

```
##### app:
``` python

# call webserver.app.
_ = webserver.app()

```
##### run:
``` python

# call webserver.run.
_ = webserver.run()

```
##### fork:
``` python

# call webserver.fork.
_ = webserver.fork(timeout=15, sleeptime=1)

```
##### stop:
``` python

# call webserver.stop.
_ = webserver.stop()

```
##### start_thread:
``` python

# call webserver.start_thread.
_ = webserver.start_thread(thread, group="daemons", id=None)

```
##### get_thread:
``` python

# call webserver.get_thread.
_ = webserver.get_thread(group="daemos", id=None)

```

#### Properties:
```python

# the token property.
token = webserver.token
```
```python

# the running property.
running = webserver.running
```

## Zip:
The zip object class.
``` python 

# initialize the Zip object class.
zip = Zip(path=None, check=False)

```

#### Functions:

##### create:
``` python

# call zip.create.
_ = zip.create(
    # source can either be a string or an array.
    source=None,
    # remove the source file(s).
    remove=False,
    # sudo required to move/copy source files.
    sudo=False, )

```
##### extract:
``` python

# call zip.extract.
_ = zip.extract(
    # the base extract directory.
    base=None,
    # remove the zip after extraction.
    remove=False,
    # if sudo required for removing file path.
    sudo=False,)

```
##### instance:
``` python

# call zip.instance.
_ = zip.instance()

```
##### raw:
``` python

# call zip.raw.
_ = zip.raw()

```

#### argument_present:
The argument_present function.
``` python

# call argument_present.
_ = argument_present(arguments, default=False, count=1)

```
#### arguments_present:
The arguments_present function.
``` python

# call arguments_present.
_ = arguments_present(arguments, default=False, count=1)

```
#### check_group:
The check_group function.
``` python

# call check_group.
_ = check_group(id, users=[], create=False, overwrite=False)

```
#### check_os:
The check_os function.
``` python

# call check_os.
_ = check_os(supported=["linux"], error=False)

```
#### check_user:
The check_user function.
``` python

# call check_user.
_ = check_user(id, create=False)

```
#### coming_soon:
The coming_soon function.
``` python

# call coming_soon.
_ = coming_soon()

```
#### execute:
The execute function.
``` python

# call execute.
_ = execute(
    # Notes:
    #   returns a dev0s.code.OutputObject object (very similair to ResponseObject).
    #
    # Mode:
    #   option 1:
    #     the command in str format, the command is saved to a script & then executed)

```
#### get_argument:
The get_argument function.
``` python

# call get_argument.
_ = get_argument(argument, required=True, index=1, count=1, default=None, )

```
#### input:
The input function.
``` python

# call input.
_ = input(message, yes_no=False, check=False, password=False, default=None)

```
#### kill:
The kill function.
``` python

# call kill.
_ = kill(
    # option 1:
    # the process id.
    pid=None,
    # option 2:
    # all processes that includes.
    includes=None,
    # root permission required.
    sudo=False,
    # loader.
    log_level=0, )

```
#### log:
The log function.
``` python

# call log.
_ = log(msg, back=0)

```
#### processes:
The processes function.
``` python

# call processes.
_ = processes(
    # root permission.
    sudo=False,
    # all processes that include a str.
    includes=None,
    # banned process names.
    banned=["grep"], )

```
#### unpack:
The unpack function.
``` python

# call unpack.
_ = unpack(content)

```
