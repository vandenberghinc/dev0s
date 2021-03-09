#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# insert the package for universal imports.
import os, sys
from dev0s import *

# settings.
#SOURCE_PATH = Defaults.source_path(__file__, back=1)
#BASE = Defaults.source_path(SOURCE_PATH)
#OS = Defaults.operating_system(supported=["linux", "macos"])
#sys.path.insert(1, BASE)

# imports.
from dev0s.classes.config import *
from dev0s.classes.manager import manager

# the cli object class.
class CLI_(CLI.CLI):
	def __init__(self):
		
		# cli.
		CLI.CLI.__init__(self,
			modes={
				"Installation":"",
				"    --install":"Install the DevOS library.",
				"    --uninstall":"Uninstall the DevOS library.",
				"    --reinstall":"Reinstall the DevOS library.",
				"    --link":"Link (activate) the DevOS library.",
				"    --unlink":"Unlink (deactivate) the DevOS library.",
				"    --update":"Update the DevOS library.",
				"Defaults":"",
				"    --version":"Show the dev0s version.",
				"    -h / --help":"Show the documentation.",
			},
			options={
			},
			executable=__file__,
			alias=ALIAS,)
		s = self.documentation.split("\nAuthor:")
		before = s[1]
		self.documentation = s[0]
		self.documentation += "\nAdditional Libraries:"
		self.documentation += "\n    $ syst3m --help : Show the syst3m documentation."
		self.documentation += "\n    $ netw0rk --help : Show the netw0rk documentation."
		self.documentation += "\n    $ encrypti0n --help : Show the encrypti0n documentation."
		self.documentation += "\n    $ ssht00ls --help : Show the ssht00ls documentation."
		self.documentation += "\nAuthor:"+before

		#
	def start(self):
		
		# check arguments.
		self.arguments.check(exceptions=["--log-level", "--create-alias", "--version"], json=JSON)

		#
		# BASICS
		#

		# help.
		if self.arguments.present(['-h', '--help']):
			self.docs(success=True, json=JSON)

		# version.
		elif self.arguments.present(['--version']):
			print(f"{ALIAS} version:",Files.load(f"{SOURCE_PATH}/.version.py").replace("\n",""))

		# install.
		elif self.arguments.present('--install'):
			response = manager.installation.install()
			if response.message != None and "Successfully installed " not in response.message: Response.log(response=response)

		# uninstall.
		elif self.arguments.present('--uninstall'):
			response = manager.installation.uninstall()
			Response.log(response=response)

		# reinstall.
		elif self.arguments.present('--reinstall'):
			response = manager.installation.uninstall()
			Response.log(response=response)
			response = manager.installation.install()
			if response.message != None and "Successfully installed " not in response.message: Response.log(response=response)

		# link.
		elif self.arguments.present('--link'):
			response = manager.installation.link()
			Response.log(response=response)

		# unlink.
		elif self.arguments.present('--unlink'):
			response = manager.installation.unlink()
			Response.log(response=response)

		# invalid.
		else: self.invalid()

		#
	def invalid(self):
		print(self.documentation)
		print("Selected an invalid mode.")
		sys.exit(1)
	
# main.
if __name__ == "__main__":
	cli = CLI_()
	cli.start()
