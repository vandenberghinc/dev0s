#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.env import Environment
from dev0s.classes.files import *
from dev0s.classes.response import Response
from dev0s.classes.utils.copycats import Docs
from dev0s.classes import utils, objects
from dev0s.classes import cli as CLI
import platform 

# the Defaults class.
class __Defaults__(Docs):
	def __init__(self):

		# docs.
		Docs.__init__(self,
			initialized=True,
			module="Defaults", 
			notes=[], )

		# vars.
		self.vars = objects.Object({
			"os": platform.system().lower(),
			"user": os.environ.get("USER"),
			"owner": os.environ.get("USER"),
			"group": "root",
			"executable":FilePath(sys.executable),
			"media": Directory(f"/media/{os.environ.get('USER')}"),
			"homes": Directory(gfp.base(path=os.environ.get('HOME'))),
			"home": Directory(gfp.clean(os.environ.get('HOME')+"/")),
			"pwd":Directory(gfp.clean(utils.__execute_script__("pwd").replace("\n",""))),
			"site_packages":self.site_packages(),
		})
		if self.vars.os in ["darwin"]:  
			self.vars.os = "macos"
			self.vars.group = "staff"
			self.vars.media = f"/Volumes/"
			self.vars.python3 = f"/usr/bin/python3"
		if self.vars.site_packages.fp.name() not in ["site-packages", "dist-packages"]: 
			self.vars.site_packages = Environment.get("SITE_PACKAGES", default=None)
			if self.vars.site_packages == None:
				raise ValueError(f"<Defaults>: Define environment variable [SITE_PACKAGES] ({ALIAS} developer mode) ({ALIAS} base: {gfp.base(SOURCE_PATH)}).")

		# universal options.
		self.options = objects.Object({
			"log_level": int(CLI.get_argument("--log-level", required=False, default=Environment.get_integer("LOG_LEVEL", default=0))),
			"cli": Environment.get_boolean("CLI", default=False),
			"json": CLI.arguments_present(["-j", "--json"]),
			"interactive": not CLI.arguments_present(["--non-interactive"]) and Environment.get("INTERACTIVE", format=bool, default=False) == True,
			"forced": CLI.arguments_present(["--forced", "-f", "--force"], default=Environment.get("FORCED", default=False, format=bool)),
			"quiet": CLI.arguments_present(["--quiet", "-q", "-s", "--silent"], default=Environment.get("QUIET", default=False, format=bool)),
		})

		# logging.
		if self.options.log_level >= 1:
			print(f"{ALIAS}:")
			print(f"  * vars: ")
			print(f"    - os: {self.vars.os}")
			print(f"    - user: {self.vars.user}")
			print(f"    - owner: {self.vars.owner}")
			print(f"    - group: {self.vars.group}")
			print(f"    - executable: {self.vars.executable}")
			print(f"    - media: {self.vars.media}")
			print(f"    - homes: {self.vars.homes}")
			print(f"    - home: {self.vars.home}")
			print(f"    - pwd: {self.vars.pwd}")
			print(f"    - site_packages: {self.vars.site_packages}")
			print(f"  * options: ")
			print(f"    - log_level: {self.options.log_level}")
			print(f"    - cli: {self.options.cli}")
			print(f"    - json: {self.options.json}")
			print(f"    - interactive: {self.options.interactive}")
			print(f"    - forced: {self.options.forced}")
			print(f"    - quiet: {self.options.quiet}")

	# get operating system.
	def operating_system(self, supported=["*"]):
		os = self.vars.os
		if os in ["macos"] and ("*" in supported or os in supported): return "macos"
		elif os in ["linux"] and ("*" in supported or os in supported): return "linux"
		else: raise ValueError(f"Unsupported operating system: [{os}].")

	# create alias.
	def alias(self,
		# the source name.
		alias=None, 
		# the source path.
		executable=None,
		# can use sudo.
		sudo=False,
		# overwrite.
		overwrite=False,
	):
		l_alias = CLI.get_argument("--create-alias", required=False)
		present = "--create-alias" in sys.argv and l_alias == alias
		base = f"/usr/local/bin"
		if not Files.exists(base):
			base = f"/usr/bin/"
		path = f"{base}/{alias}"
		if ((CLI.argument_present("--force") or CLI.argument_present("--forced") or overwrite) and present) or (present or not Files.exists(path)):
			if l_alias != None: alias = l_alias
			#file = f"""package={executable}/\nargs=""\nfor var in "$@" ; do\n   	if [ "$args" == "" ] ; then\n   		args=$var\n   	else\n   		args=$args" "$var\n   	fi\ndone\npython3 $package $args\n"""
			sudo = Boolean("--sudo" in sys.argv).string(true="sudo ",false="")
			file = f"""#!/usr/bin/env python3\nimport os, sys\npackage="{executable}"\nsys.argv.pop(0)\narguments = sys.argv\ns = ""\nfor i in arguments:\n	if s == "": \n		if " " in i: s = "'"+i+"'"\n		else: s = i\n	else: \n		if " " in i: s += " '"+i+"'"\n		else: s += " "+i\nif os.path.exists("/usr/bin/python3"): os.system("/usr/bin/python3 "+package+" "+s)\nelse:  os.system("python3 "+package+" "+s)\n#os.system("python3 "+package+" "+s)"""
			os.system(f"{sudo}touch {path}")
			os.system(f"{sudo}chmod +x {path}")
			os.system(f"{sudo}chown {self.vars.user}:{self.vars.group} {path}")
			try:
				File(path=f"{path}", data=file).save()
			except:
				print(f"Unable to create alias $ {alias}.")
				return None
			os.system(f"chmod +x {path}")
			if '--silent' not in sys.argv:
				print(f'Successfully created alias: {alias}.')
				print(f"Check out the docs for more info $: {alias} -h")
		if present:
			quit()

	# get source path.
	def source_path(self, path, back=1):
		source = gfp.clean(path=FilePath(path).base(back=back), remove_double_slash=True)
		if len(source) > 0 and source[len(source)-1] != "/": source += "/"
		return source

	# get log level.
	def log_level(self, default=0):
		return int(CLI.get_argument("--log-level", required=False, default=Environment.get_integer("LOG_LEVEL", default=default)))

	# get current working directory.
	def pwd(self):
		return FilePath(utils.__execute_script__("pwd").replace("\n","")).clean()

	# insert package libraries.
	def insert(self, path):
		path = gfp.clean(path).replace(".","/")
		return sys.path.insert(1, path)

	# get the python site packages location
	def site_packages(self):
		path = FilePath(SOURCE_PATH).base()
		if FilePath(path).name() in ["site-packages", "dist-packages"]:
			return Directory(path)
		return Directory(sysconfig.get_paths()["purelib"])

	# install requirements.
	def install_requirements(self,
		# the requirements (#1).
		#	str instance: path to file.
		#	list instance: pip requirements in list
		requirements,
		# the silent option.
		silent=False,
		# the log level (Leave None to use self.options.log_level).
		log_level=None,
	):
		if log_level == None: log_level = self.options.log_level
		options = ""
		if isinstance(requirements, (str, String)):
			
			msg = f"Installing pip requirements [{requirements}]."
			if not os.path.exists(requirements):
				raise ValueError(f"Requirements file [{requirements}] does not exist.")
			if not os.path.isdir(requirements):
				options += "-r "
		elif isinstance(requirements, (list, Array)):
			msg = f"Installing {len(requirements)} pip requirement(s)."
			requirements = Array(requirements).string(joiner=" ")
		if log_level >= 0: print(msg)
		os.system(f"{Defaults.vars.executable} -m pip install {options}{requirements} {Boolean(silent).string(true='2> /dev/null', false='')} --user {self.vars.user}")

# initialized classes.
Defaults = __Defaults__()
#