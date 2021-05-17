
# imports
from dev0s.classes.config import *
from dev0s.classes.defaults.files import Date
from dev0s.classes.defaults.color import color, symbol
import getpass
_input_ = input

# log with safe replace.
def log(msg, back=0):
	if back > 0:
		print(msg, end="\r")
	else:
		print(msg)
	#for _ in range(back):
	#	sys.stdout.write("\033[F") # cursor up one line
	sys.stdout.write("\033[K") # clear to the end of line

# input.
def input(message, yes_no=False, check=False, password=False, default=None):


	# docs.
	DOCS = {
		"module":"dev0s.console.input", 
		"description":[], 
		"chapter": "Console", }
		
	# attributes.
	message = color.fill(message)
	if len(message) > 0 and message[0].upper() != message[0]: message = String(message).capitalized_word()
	if yes_no:
		while True:
			if len(message) > 0 and message[len(message)-1] == " ": message = message[:-1]
			elif len(message) > 0 and message[len(message)-1] == ".": message = message[:-1]
			else: break
		value = _input_(message+" (y/n): ")
		if value in ["yes", 'y', "YES", "Y"]:
			return True
		else:
			return False
	else:
		while True:
			if len(message) > 0 and message[len(message)-1] == " ": message = message[:-1]
			elif len(message) > 0 and message[len(message)-1] == ":": message = message[:-1]
			else: break
		if password:
			value = getpass.getpass(message+": ")
		else:
			value = _input_(message+": ")
			if value in [""]: value = default
		if check:
			if password:
				if getpass.getpass("Enter the same passphrase: ") != password:
					log("Passphrases do not match.")
					return default
				else:
					return password
			else:
				if input(f"({value}) correct?", yes_no=True):
					return value
				else:
					return default
		else:
			return value

# the loader object class.
class Loader(threading.Thread):
	def __init__(self, message, autostart=True, log_level=0, interactive=True):

		# docs.
		DOCS = {
			"module":"Loader", 
			"initialized":False,
			"description":[], 
			"chapter": "Console", }
			
		# attributes.
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
				log(self.message+".")
	def run(self):
		if self.log_level >= 0: 
			self.running = True
			self.released = True
			while self.running:
				if not self.running: break
				elif not self.released:
					time.sleep(1)
				else:
					for i in ["|", "/", "-", "\\"]:
						if not self.released: break
						elif not self.running: break
						if self.message != self.last_message:
							#log(self.__empty_message__(length=len(f"{self.last_message} ...   ")), back=1)
							self.message = self.__clean_message__(self.message)
						log(f"{self.message} ... {i}", back=1)
						self.last_message = self.message
						if not self.released: break
						elif not self.running: break
						time.sleep(0.2)
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
					time.sleep(0.2)
				if self.running != "stopped": raise ValueError(f"Unable to stop loader [{self.message}].")
			if not quiet:
				if self.interactive:
					#log(self.__empty_message__(length=len(f"{self.last_message} ...   ")), back=1)
					if success:
						log(f"{message} ... done")
					else:
						log(f"{message} ... {color.red}failed{color.end}")
				else:
					if success:
						log(f"{message}. done")
					else:
						log(f"{message}. {color.red}failed{color.end}")
	def mark(self, new_message=None, old_message=None, success=True, response=None):
		if self.log_level >= 0: 
			if response != None:
				if response["error"] == None:
					success = True
				else:
					success = False
			if old_message == None: old_message = self.message
			if self.interactive:
				#log(self.__empty_message__(length=len(f"{self.last_message} ...   ")), back=1)
				if success:
					log(f"{old_message} ... done")
				else:
					log(f"{old_message} ... {color.red}failed{color.end}")
			else:
				if success:
					log(f"{old_message}. done")
				else:
					log(f"{old_message}. {color.red}failed{color.end}")
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
		message = color.fill(str(message))
		if message[-len(" ..."):] == " ...": message = message[:-4]
		if message[-len("."):] == ".": message = message[:-1]
		if message[0].upper() != message[0]: message = message[1:]+message[0].upper()+message[1:]
		return message
	def __empty_message__(self, length=len("hello world")):
		s = ""
		for i in range(length): s += " "
		return s

# the loader object class.
class ProgressLoader(threading.Thread):
	def __init__(self, 
		# the message (str).
		message, 
		# the start index (int).
		index=0, 
		# the max index (int).
		max=10, 
		# calculate estimated finish time.
		calc_finish=False,
		# auto start.
		autostart=True,
		# the active log level (int).
		log_level=0,
	):

		# docs.
		DOCS = {
			"module":"ProgressLoader", 
			"initialized":False,
			"description":[], 
			"chapter": "Console", }
			
		# attributes.
		threading.Thread.__init__(self)
		self.message = message
		if self.message[-len(" ..."):] == " ...": self.message = self.message[:-4]
		if self.message[-len("."):] == ".": self.message = self.message[:-1]
		if self.message[0].upper() != self.message[0]: self.message = self.message[1:]+self.message[0].upper()+self.message[1:]
		self.message = color.fill(self.message)
		self.index = index
		self.max = max
		self.calc_finish = calc_finish
		self.start_stamp = None
		self.progress = None
		self.last_message = None
		self.log_level = log_level
		if autostart: self.next(increment=0)

	# next index.
	def next(self, increment=1, decimals=2):
		if self.calc_finish and self.start_stamp == None:
			self.start_stamp = Date()
		self.index += increment
		p = round((self.index / self.max) * 100, decimals)
		if p != self.progress:
			self.progress = p
			self.last_message = f"{self.message} ... {self.progress}%"
			if self.calc_finish and self.progress > 0:
				diff = (Date() - self.start_stamp).to_seconds()
				duration = (diff / (self.progress/100)) * (1.0 - (self.progress/100))
				if duration <= 60:
					duration = f'{int(duration)}s'
				elif duration <= 60*60:
					duration = f'{round(duration/60,1)}m'
				elif duration <= 60*60*24:
					duration = f'{round(duration/(60*60),1)}h'
				elif duration <= 60*60*24*30:
					duration = f'{round(duration/(60*60*24),1)}d'
				elif duration <= 60*60*24*30*12:
					duration = f'{round(duration/(60*60*24*30),1)}m'
				else:
					duration = f'{round(duration/(60*60*24*30*12),1)}y'
				self.last_message += f" ({duration})"
			if self.log_level >= 0:
				log(self.last_message, back=1)
		#

	# stop the loader.
	def stop(self, message=None, success=True, response=None):
		if self.log_level >= 0:
			if response == None:
				if message == None: message = self.message
			else:
				if response["error"] == None:
					message = response["message"]
				else:
					success = False
					message = "Error: "+response["error"]
			if self.last_message != None:
				log(self.__empty_message__(length=len(f"{self.last_message}")), back=1)
			if success:
				log(f"{message} ... done")
			else:
				log(f"{message} ... {color.red}failed{color.end}")
		#

	# create empty message.
	def __empty_message__(self, length=len("hello world")):
		s = ""
		for i in range(length): s += " "
		return s
		#

	#

#

#
