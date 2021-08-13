
# imports
from dev0s.classes.config import *
from dev0s.classes.defaults.files import Date, Speed
from dev0s.classes.defaults.color import color, symbol
import getpass
_input_ = input

# log with safe replace.
def log(msg, back=0, log_timestamps=False):
	if log_timestamps: msg = f"{Date().seconds_timestamp} - {msg}"
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

# log a divider.
def divider(dump=True):
	divider = ""
	for _ in range(int(os.get_terminal_size().columns)): divider += "-"
	if dump: print(divider)
	return divider

# the loader object class.
class Loader(threading.Thread):
	def __init__(self, 
		# the loader message (str) (#1).
		message:str, 
		# auto start the loader (bool).
		autostart=True, 
		# the log level (int).
		log_level=0, 
		# interactive (bool).
		interactive=True, 
		# log the timestamps (bool).
		log_timestamps=True,
	):

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
		self.log_timestamps = log_timestamps
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
						log(f"{self.message} ... {i}", back=1, log_timestamps=self.log_timestamps) 
						self.last_message = self.message
						if not self.released: break
						elif not self.running: break
						time.sleep(0.2)
		self.running = "stopped"
		sys.exit(0)
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
						log(f"{message} ... done", log_timestamps=self.log_timestamps)
					else:
						log(f"{message} ... {color.red}failed{color.end}", log_timestamps=self.log_timestamps)
				else:
					if success:
						log(f"{message}. done", log_timestamps=self.log_timestamps)
					else:
						log(f"{message}. {color.red}failed{color.end}", log_timestamps=self.log_timestamps)
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
					log(f"{old_message} ... done", log_timestamps=self.log_timestamps)
				else:
					log(f"{old_message} ... {color.red}failed{color.end}", log_timestamps=self.log_timestamps)
			else:
				
				if success:
					log(f"{old_message}. done", log_timestamps=self.log_timestamps)
				else:
					log(f"{old_message}. {color.red}failed{color.end}", log_timestamps=self.log_timestamps)
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
class ProgressLoader(object):
	def __init__(self, 
		# the message (str) (#1).
		message:str, 
		# the start index (pass shared multiprocessing variable to use with mp) (int).
		index=0, 
		# the max index (int).
		max=10, 
		# calculate estimated finish time.
		calc_finish=False,
		# auto start.
		autostart=True,
		# log the timestamps.
		log_timestamps=True,
		# log the duration when finished.
		log_duration=False,
		# the memory (dict) (for multiprocessing) (leave None to ignore).
		# uses the key (loader_index) as the loader's index value.
		# increment the loader index from within the processes and call loader.wait() to await till the loader is finished.
		memory=None,
		# the total amount of processes (int) (required for multiprocessing)
		processes=None,
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
		self.log_timestamps = log_timestamps
		self.log_duration = log_duration
		self.memory = memory
		self.processes = processes
		if self.memory not in [None, False]:
			if self.processes in [None, False] or self.processes < 0: raise ValueError("Multiprocessing is enabled by defining the memory parameter while likely forgot to define the number of processes parameter (processes:int).")
			if self.index != 0: raise ValueError("A multiprocessing progress loader should always start with index 0.")
			if "loader_index" not in list(self.memory.keys()): 
				raise ValueError("The multiprocessing memory dict must include the key (loader_index) with a multiprocessing dict as value.")
			for id in range(self.processes): self.memory["loader_index"][id] = 0
			try: self.memory["loader_index"][0]
			except KeyError:
				raise ValueError("The multiprocessing memory dict must include the key (loader_index) with a multiprocessing dict as value.")
		if autostart: self.next(increment=0)

	# next index.
	def next(self, increment=1, decimals=2):
		if self.calc_finish and self.start_stamp == None:
			self.start_stamp = Speed.mark()
		if self.memory in [None, False]:
			self.index += increment
			try:
				p = round((self.index / self.max) * 100, decimals)
			except ZeroDivisionError:
				p = 0.0
		else:
			if increment > 0: raise ValueError("Unable to increment the index with loader.next() when multiprocessing is enabled.")
			t = 0
			for id in range(self.processes): t += self.memory["loader_index"][id]
			try:
				p = round((t / self.max) * 100, decimals)
			except ZeroDivisionError:
				p = 0.0
		if p != self.progress:
			self.progress = p
			if self.log_timestamps:
				self.last_message = f"{Date().seconds_timestamp} - {self.message} ... {self.progress}%"
			else:
				self.last_message = f"{self.message} ... {self.progress}%"
			if self.calc_finish and self.progress > 0:
				diff = Speed.calculate(self.start_stamp)
				duration = Date().normalize_seconds( (diff / (self.progress/100)) * (1.0 - (self.progress/100)) )
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
			s = ""
			if success:
				s = f"{message} ... done"
				if self.log_duration:
					duration = Date().normalize_seconds(Speed.calculate(self.start_stamp))
					s += f" (duration: {duration})"
			else:
				s = f"{message} ... {color.red}failed{color.end}"
			log(s, log_timestamps=self.log_timestamps)
		#

	# wait till the loader is finished the progress (for multiprocessing).
	# make sure self.max is the actual max otherwise it will run forever if timeout is None.
	def wait(self,
		# the sleep time (int).
		sleeptime=15,
		# timeout in seconds (leave None for no timeout) (int).
		timeout=None,
	):
		seconds = 0
		while True:
			self.next(increment=0)
			if self.progress >= 100: return True
			if timeout != None and seconds > timeout: break
			seconds += sleeptime
			time.sleep(sleeptime)
		raise ValueError("Timeout expired.")

	# create empty message.
	def __empty_message__(self, length=len("hello world")):
		s = ""
		for i in range(length): s += " "
		return s
		#

	#

#

#
