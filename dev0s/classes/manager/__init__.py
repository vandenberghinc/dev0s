#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.manager import installation
from dev0s.classes import console

# the manager object class.
class Manager(object):
	def __init__(self):	
		
		# objects.
		self.installation = installation.Installation()
		self.lib = f"{SOURCE_PATH}/lib/"
		self.user_lib = "/usr/local/lib/"
		self.user_bin = "/usr/local/bin/"
		for path in [self.user_bin, self.user_lib]:
			if not Files.exists(path): os.system(f"sudo mkdir -p {path} && sudo chown {OWNER}:{GROUP} {path} && sudo chmod 770 {path}")
		self.check()

		#
	def check(self):

		# only if installed.
		if self.installation.__installed__():

			# check python lib.
			gfp = FilePath("")
			for lib in Files.Directory(f"{self.lib}/python/").paths(recursive=False, files_only=True, banned_names=[".DS_Store", "example"]):
				current = File(path=gfp.clean(path=lib, remove_last_slash=True))
				installed = File(path=gfp.clean(path=f"{self.user_bin}/{gfp.name(path=lib)}", remove_last_slash=True))
				install = False
				if not installed.file_path.exists(): install = True
				elif installed.load() != current.load(): install = True
				if install: 
					loader = console.Loader(f"Installing library {installed.file_path.name()}")
					os.system(f"sudo rm -fr {installed.file_path.path} && sudo cp -r {current.file_path.path} {installed.file_path.path} && sudo chmod +x {installed.file_path.path} && sudo chown {OWNER}:{GROUP} {installed.file_path.path}")
					if not installed.file_path.exists(): loader.stop(success=False)
					else: loader.stop()

# initialized objects.
manager = Manager()