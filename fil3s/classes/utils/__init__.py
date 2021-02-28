#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from fil3s.classes.config import *
import string
import time

# the get argument func (exact copy from cl1.cl1).
def get_argument(argument, required=True, index=1, count=1, default=None, ):
	if default != None and required: required = False
	
	# set error msg.
	if index == 1:
		empty_error = f"Define argument [{argument}]."
	else:
		empty_error = f"Define argument [{argument}] (index: {index})."

	# check presence.
	if argument not in sys.argv:
		if required:
			raise EmptyArgumentError(empty_error)
		else: return default

	# retrieve.
	y, c = 0, 0
	for x in sys.argv:
		try:
			if x == argument: 
				c += 1
				if count == c:
					return sys.argv[y+index]
		except IndexError:
			if required:
				raise EmptyArgumentError(empty_error)
			else: return default
		y += 1

	# should not happen.
	if required:
		raise EmptyArgumentError(empty_error)
	else: return default

	#

# get integer (exact copy from system.env).
def get_integer(id, default=None):
		e = os.environ.get(id)
		try:
			if "." in str(e):
				return float(e)
			else:
				return int(e)
		except:
			return default

# get log level (exact copy from system.defaults).
def log_level(default=0):
	return int(get_argument("--log-level", required=False, default=get_integer("LOG_LEVEL", default=0)))

# the color object (exact copy from syst3m.color).
class Color(object):
	def __init__(self):
		self.purple = "\033[95m"
		self.cyan = "\033[96m"
		self.darkcyan = "\033[35m"
		self.orange = '\033[33m'
		self.blue = "\033[94m"
		self.green = "\033[92m"
		self.yellow = "\033[93m"
		self.grey = "\033[90m"
		self.marked = "\033[100m"
		self.markedred = "\033[101m"
		self.markedgreen = "\033[102m"
		self.markedcyan= "\033[103m"
		self.unkown = "\033[2m"
		self.red = "\033[91m"
		self.bold = "\033[1m"
		self.underlined = "\033[4m"
		self.end = "\033[0m"
		self.italic = "\033[3m"
	def remove(self, string):
		if string == None: return string
		for x in [color.purple,color.cyan,color.darkcyan,color.orange,color.blue,color.green,color.yellow,color.grey,color.marked,color.markedred,color.markedgreen,color.markedcyan,color.unkown,color.red,color.bold,color.underlined,color.end,color.italic]: string = string.replace(x,'')
		return string
	def fill(self, string):
		if string == None: return string
		for x in [
			["&PURPLE&", color.purple],
			["&CYAN&", color.cyan],
			["&DARKCYAN&", color.darkcyan],
			["&ORANGE&", color.orange],
			["&BLUE&", color.blue],
			["&GREEN&", color.green],
			["&YELLOW&", color.yellow],
			["&GREY&", color.grey],
			["&RED&", color.red],
			["&BOLD&", color.bold],
			["&UNDERLINED&", color.underlined],
			["&END&", color.end],
			["&ITALIC&", color.italic],
		]: string = string.replace(x[0],x[1])
		return string
	def boolean(self, boolean, red=True):
		if boolean: return color.green+str(boolean)+color.end
		else: 
			if red: return color.red+str(boolean)+color.end
			else: return color.yellow+str(boolean)+color.end

# the symbol object (exact copy from syst3m.color).
class Symbol(object):
	def __init__(self):
		self.cornered_arrow = color.grey+'↳'+color.end
		self.cornered_arrow_white = '↳'
		self.good = color.bold+color.green+"✔"+color.end
		self.good_white = "✔"
		self.bad = color.bold+color.red+"✖"+color.end
		self.bad_white = "✖"
		self.medium = color.bold+color.orange+"✖"+color.end
		self.pointer = color.bold+color.purple+"➤"+color.end
		self.star = color.bold+color.yellow+"★"+color.end
		self.ice = color.bold+color.cyan+"❆"+color.end
		self.retry = color.bold+color.red+"↺"+color.end
		self.arrow_left = color.end+color.bold+"⇦"+color.end
		self.arrow_right = color.end+color.bold+"⇨"+color.end
		self.arrow_up = color.end+color.bold+"⇧"+color.end
		self.arrow_down = color.end+color.bold+"⇩"+color.end
		self.copyright = color.bold+color.grey+"©"+color.end
		self.heart = color.bold+color.red+"♥"+color.end
		self.music_note = color.bold+color.purple+"♫"+color.end
		self.celcius = color.bold+color.grey+"℃"+color.end
		self.sun = color.bold+color.yellow+"☀"+color.end
		self.cloud = color.bold+color.grey+"☁"+color.end
		self.moon = color.bold+color.blue+"☾"+color.end
		self.smiley_sad = color.bold+color.red+"☹"+color.end
		self.smiley_happy = color.bold+color.green+"☺"+color.end
		self.infinite = color.bold+color.blue+"∞"+color.end
		self.pi = color.bold+color.green+"π"+color.end
		self.mode = color.bold+color.purple+"ⓜ"+color.end
		self.action = color.bold+color.yellow+"ⓐ"+color.end
		self.info = color.bold+color.grey+"ⓘ"+color.end

	#

# default initialized classes.
color = Color()
symbol = Symbol()

# the syst3m.console.Loader object class (exact copy).
class Loader(threading.Thread):
	def __init__(self, message, autostart=True, log_level=0, interactive=True):
		threading.Thread.__init__(self)
		self.message = self.__clean_message__(message)
		self.last_message = str(self.message)
		self.log_level = log_level
		self.interactive = interactive
		if autostart and self.log_level >= 0: 
			if self.interactive:
				try:
					self.start()
				except KeyboardInterrupt as e:
					self.stop(success=False)
					raise KeyboardInterrupt(f"{e}")
			else:
				print(self.message+".")
	def run(self):
		if self.log_level >= 0: 
			self.running = True
			self.released = True
			while self.running:
				if not self.released:
					time.sleep(1)
				else:
					for i in ["|", "/", "-", "\\"]:
						if not self.released: break
						if self.message != self.last_message:
							print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
							self.message = self.__clean_message__(self.message)
						print(f"{self.message} ... {i}", end="\r")
						self.last_message = self.message
						if not self.running: break
						time.sleep(0.33)
		self.running = "stopped"
	def stop(self, message=None, success=True, response=None, quiet=False):
		if self.log_level >= 0:
			if response == None:
				if message == None: message = self.message
			else:
				if response["error"] == None:
					message = response["message"]
				else:
					success = False
					message = "Error: "+response["error"]
			if self.interactive:
				self.running = False
				for i in range(120):
					if self.running == "stopped": break
					time.sleep(0.5)
				if self.running != "stopped": raise ValueError(f"Unable to stop loader [{self.message}].")
			if not quiet:
				if self.interactive:
					print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
					if success:
						print(f"{message} ... done")
					else:
						print(f"{message} ... {color.red}failed{color.end}")
				else:
					if success:
						print(f"{message}. done")
					else:
						print(f"{message}. {color.red}failed{color.end}")
	def mark(self, new_message=None, old_message=None, success=True, response=None):
		if self.log_level >= 0: 
			if response != None:
				if response["error"] == None:
					success = True
				else:
					success = False
			if old_message == None: old_message = self.message
			if self.interactive:
				print(self.__empty_message__(length=len(f"{self.last_message} ...   ")), end="\r")
				if success:
					print(f"{old_message} ... done")
				else:
					print(f"{old_message} ... {color.red}failed{color.end}")
			else:
				if success:
					print(f"{old_message}. done")
				else:
					print(f"{old_message}. {color.red}failed{color.end}")
			if new_message != None: self.message = new_message
	def hold(self):
		if self.log_level >= 0: 
			self.released = False
			time.sleep(0.33)
	def release(self):
		if self.log_level >= 0: 
			self.released = True
			time.sleep(0.33)
	# system functions.
	def __clean_message__(self, message):
		if message[-len(" ..."):] == " ...": message = message[:-4]
		if message[-len("."):] == ".": message = message[:-1]
		if message[0].upper() != message[0]: message = message[1:]+message[0].upper()+message[1:]
		return color.fill(message)
	def __empty_message__(self, length=len("hello world")):
		s = ""
		for i in range(length): s += " "
		return s

# invalid os.
def __invalid_os__(os):
	raise OSError(f"Unsupported operating system [{os}].")
	#

# check memory only path.
def __check_memory_only__(path):
	if path == False: 
		raise ValueError("This object is only used in the local memory and is not supposed to be saved or loaded.")
	#

# the generate object.
class Generate(object):
	def __init__(self):
		a=1
	def pincode(self, length=6, charset=string.digits):
		return ''.join(random.choice(charset) for x in range(length))
		#
	def shell_string(self, length=6, numerical_length=False, special_length=False):
		charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		for x in ast.literal_eval(str(charset)): charset.append(x.upper())
		if numerical_length:
			for x in [
				'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
			]: charset.append(x)
		if special_length:
			for x in [
				'-', '+', '_'
			]: charset.append(x)
		return ''.join(random.choice(charset) for x in range(length))
		#

# execute a shell command.
def __execute__(
	# the command in array.
	command=[],
	# wait till the command is pinished. 
	wait=False,
	# the commands timeout, [timeout] overwrites parameter [wait].
	timeout=None, 
	# the commands output return format: string / array.
	return_format="string", 
	# the subprocess.Popen.shell argument.
	shell=False,
	# pass a input string to the process.
	input=None,
):
	def __convert__(byte_array, return_format=return_format):
		if return_format == "string":
			lines = ""
			for line in byte_array:
				lines += line.decode()
			return lines
		elif return_format == "array":
			lines = []
			for line in byte_array:
				lines.append(line.decode().replace("\n","").replace("\\n",""))
			return lines

	# create process.
	if isinstance(command, str): command = command.split(' ')
	p = subprocess.Popen(
		command, 
		shell=shell,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		stdin=subprocess.PIPE,)
	
	# send input.
	if input != None:
		if isinstance(input, list):
			for s in input:
				p.stdin.write(f'{s}\n'.encode())
		elif isinstance(input, str):
			p.stdin.write(f'{input}\n'.encode())
		else: raise ValueError("Invalid format for parameter [input] required format: [string, array].")
		p.stdin.flush()
	
	# timeout.
	if timeout != None:
		time.sleep(timeout)
		p.terminate()
	
	# await.
	elif wait:
		p.wait()

	# get output.
	output = __convert__(p.stdout.readlines(), return_format=return_format)
	if return_format == "string" and output == "":
		output = __convert__(p.stderr.readlines(), return_format=return_format)
	elif return_format == "array" and output == []:
		output = __convert__(p.stderr.readlines(), return_format=return_format)
	return output
	
	
# default initialized classes.
generate = Generate()
