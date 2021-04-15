#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_

# the installation object class.
class Installation(object):
	def __init__(self):	

		if OS in ["macos"]: 
			self.bashrc = File(path=f"/Users/{USER}/.zshrc", load=True)
			self.link = f"source {SOURCE_PATH}/lib/bash/import\nsource {SOURCE_PATH}/lib/bash/env"
		else: 
			self.bashrc = File(path=f"/home/{USER}/.bashrc", load=True)
			self.link = f". {SOURCE_PATH}/lib/bash/import\n. {SOURCE_PATH}/lib/bash/env"
		#
	def link(self):
		self.bashrc.load()
		if self.link not in self.bashrc.data:
			self.bashrc.data += f"\n\n# DevOS:\n{self.link}\n"
			self.bashrc.save()
		return _response_.success(f"Successfully linked {ALIAS}.")
	def unlink(self):
		self.bashrc.load()
		if self.link in file.data:
			data = ""
			for line in self.bashrc.data.split("\n"):
				if "# DevOS:" in line or "# dev0s:" in line or "# dev0s." in line or self.link in line:
					a=1
				else:
					data += line+"\n"
			self.bashrc.save(data)
		return _response_.success(f"Successfully unlinked {ALIAS}.")
	def install(self):
		os.system("rm -fr /tmp/dev0s && git clone -q https://github.com/vandenberghinc/dev0s.git /tmp/dev0s && bash /tmp/dev0s/requirements/installer")
		return _response_.success(f"Successfully installed {ALIAS}.")
	def uninstall(self):
		print(f"{color.orange}Root permissions{color.end} required to uninstall DevOS.")
		os.system(f"sudo rm -fr /usr/local/lib/{ALIAS}")
		return _response_.success(f"Successfully uninstalled {ALIAS}.")
	# system functions.
	def __installed__(self):
		return Files.exists(f"/usr/local/lib/{ALIAS}")

