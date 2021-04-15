
# imports
from dev0s.classes.defaults.exceptions import Exceptions
from dev0s.classes.defaults.color import color
from dev0s.classes.defaults.files import *
from dev0s.classes.response import ResponseObject
from dev0s.classes.response import response as _response_
from dev0s.classes.defaults import objects
from dev0s.classes.defaults.defaults import defaults

# pip imports.
import pexpect
import signal as _signal_

# kill pids.
def kill(
	# option 1:
	# the process id.
	pid=None, 
	# option 2:
	# all processes that includes.
	includes=None,
	# root permission required.
	sudo=False,
	# loader.
	log_level=0,
):

	# docs.
	DOCS = {
		"module":"dev0s.code.kill", 
		"initialized":False,
		"description":[], 
		"chapter": "Code", }

	# kill includes.
	loader = None
	if includes != None:
		response = processes(includes=includes, sudo=sudo)
		if not response.success: return response
		c = 0
		for pid, info in response.processes.items():
			response = kill(sudo=sudo, pid=pid, loader=loader)
			if not response.success: return response
			c += 1
		if c == 0:
			return _response_.error(f"No processes found.")
		elif c == 1:
			return _response_.success(f"Successfully killed {c} process.")
		else:
			return _response_.success(f"Successfully killed {c} processes.")

	# kill pid.
	else:
		if log_level >= 3:
			loader = console.Loader(f"Killing process {pid}.")
		_sudo_ = Boolean(sudo).string(true="sudo ", false="")
		output = utils.__execute_script__(f"{_sudo_}kill {pid}")
		if output in ["terminated",""]:
			if output in [""]:
				response = processes(includes=pid)
				if not response.success: response
				try: 
					response.processes[pid]
					if log_level >= 3: loader.stop(success=False)
					return _response_.error(f"Failed to stop process {pid}.", log_level=log_level)
				except KeyError: a=1
			if log_level >= 3: loader.stop()
			return _response_.success(f"Successfully killed process {pid}.")
		else:
			if log_level >= 3: loader.stop(success=False)
			return _response_.error(f"Failed to stop process {pid}, error: {output}", log_level=log_level)

# list all processes.
def processes(
	# root permission.
	sudo=False,
	# all processes that include a str.
	includes=None,
	# banned process names.
	banned=["grep"],
):

	# docs.
	DOCS = {
		"module":"dev0s.code.processes", 
		"initialized":False,
		"description":[], 
		"chapter": "Code", }

	_sudo_ = Boolean(sudo).string(true="sudo ", false="")
	if isinstance(includes, str):
		command = f"""{_sudo_}ps -ax | grep "{includes}" | """
	else:
		command = f"""{_sudo_}ps -ax | """
	#output = utils.__execute_script__(command + """awk '{print $1"|"$2"|"$3"|"$4"}' """)
	output = utils.__execute_script__(command + """awk '{$3="";print $0}' """)
	processes = {}
	for line in output.split("\n"):
		if line not in ["", " "]:
			array = line.split(" ")
			pid = array.pop(0)
			tty = array.pop(0)
			for i in array:
				process = array[0]
				if process not in ["", " "]: break
				else: array.pop(0)
			command = Array(array).string(joiner=" ")
			#try:
			#	pid,tty,_,process,command = line.split("|")
			#except ValueError: raise ValueError(f"Unable to unpack process line: [{line}], expected format: [4] seperator: [|].")
			if process not in banned:
				processes[pid] = {
					"pid":pid,
					"tty":tty,
					"process":process,
					"command":command,
				}
	return _response_.success(f"Successfully listed {len(processes)} processes.", {
		"processes":processes,
	})

# execute.
def execute(
	# Notes:
	#   returns a dev0s.code.OutputObject object (very similair to ResponseObject).
	#
	# Mode:
	#   option 1:
	#     the command in str format, the command is saved to a script & then executed).
	command="ls .",
	#     joiner for when command is in list format.
	joiner=" ",
	#   option 2: the path to script.
	path=None,
	#
	# Executement:
	#   the executable.
	executable="sh",
	#   the arguments passed to the (saved) script.
	arguments=[], 
	#
	# Options:
	#   asynchronous process.
	async_=False,
	#	await asynchronous child (sync process always awaits).
	wait=False,
	#	kill process when finished (async that is not awaited is never killed).
	kill=True,
	#   the subprocess shell parameter.
	shell=False,
	#   serialize output to dict (expect literal dictionary / json output).
	serialize=False,
	#
	# Input (sync only):
	#   send input to the command.
	#	  undefined: send no input & automatically await the process since input is always sync.
	#	  dict instance: selects "and" mode ; send expected inputs and their value & return error when one of them is missing.
	#	  list[dict] instance: send all dictionaries in the list (default dict behaviour so one of the keys in each dict is expected).
	input=None,
	#   the input timeout (float) (list with floats by index from input)
	timeout=1.0,
	#   do not throw an error when the input is missing or not expected when optional is disabled (bool).
	optional=False, 
	#
	# Logging.
	# the loader (str, Loader).
	loader=None,
	# stop the loader at the end of the request (bool).
	stop_loader=True,
	#   the log level.
	log_level=defaults.options.log_level,
	#
	# System functions.
	#   add additional attributes to the spawn object.
	__spawn_attributes__={},
	#
):	
	# docs.
	DOCS = {
		"module":"dev0s.code.execute", 
		"initialized":False,
		"description":[], 
		"chapter": "Code", }

	# checks,
	if input != None and not isinstance(input, (dict, Dictionary, list, Array)): 
		raise Exceptions.InvalidUsage(f"<dev0s.code.execute>: Parameter [input] requires to be be a [dict, Dictionary, list, Array], not [{iput.__class__.__name__}].")

	# loader.
	if isinstance(loader, (str,String)) and 2 > log_level >= 0:
		loader = console.Loader(loader)

	# vars.
	delete = False
	if path == None:
		delete = True
		path = f"/tmp/tmp_script_{String('').generate()}"
		if isinstance(command, list): command = Array(array=command).string(joiner=joiner)
		Files.save(path, command)
		response_str = f"command ({command})"
	else:
		response_str = f"script ({path})"

	# execute with input.
	#if isinstance(input, (dict, Dictionary, list, Array)):

	# checks.
	#if async_: 
	#	raise Exceptions.InvalidUsage(f"<dev0s.code.execute>: Parameters [input] & [async] are not compatible, select either one.")

	# spawn.
	l = []
	for i in arguments: l.append(f'"{i}"')
	arguments = Array(l).string(joiner=' ')
	if log_level >= 8: print(f"Spawn: [ $ {executable} {path} {arguments}]",)
	spawn = Spawn(
		command=f"{executable} {path} {arguments}",
		#async_=async_, # does not work.
		response_str=response_str,
		log_level=log_level,
		attributes=__spawn_attributes__,
	)
	spawn.echo = False
	if isinstance(timeout, (int,float,Integer)):
		spawn.timeout = int(timeout)
	
	# start.
	response = spawn.start()
	if not response.success: 
		if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
		return OutputObject(error=f"Failed to start {response_str}, error: {response.error}", log_level=log_level)
	
	# check crashed
	response = spawn.crashed()
	if not response.success:  
		if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
		return OutputObject(error=response.error, log_level=log_level)

	# has already exited.
	elif spawn.exit_status in [0]:
		
		# get output.
		response = spawn.wait(timeout=1.0)
		if not response.success: 
			if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
			return OutputObject(error=response.error, log_level=log_level) # exit status.
		output = response.output

		#

	# proceed if already finished.
	elif spawn.exit_status not in [0]:

		# await.
		#success = False
		#for i in range(10):
		#	if spawn.running: 
		#		success = True
		#		break
		#	time.sleep(1)
		#if not success: 
		#	if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
		#	return OutputObject(error=f"Unable to start {response_str}.", log_level=log_level)

		# str input.
		if isinstance(input, (list, Array)):
			if len(input) > 0:
				str_input = Array(list(input[0].keys())).string(joiner=", ")
			else:
				str_input = Array(input).string(joiner=", ")
		elif isinstance(input, (dict, Dictionary)):
			str_input = Array(list(input.keys())).string(joiner=", ")
		else: 
			str_input = f"[{input}]"

		# send optional input.
		error_end_of_file = None
		if not async_ and isinstance(input, (list, Array, dict, Dictionary)) and len(input) > 0:

			# expect one of the keys in the dictionary.
			def process_dict_input(dictionary):

				# vars.
				expect = list(dictionary.keys())
				send = list(dictionary.values())

				# expect .
				if log_level >= 8:
					print(f"Expecting one of the following inputs: {expect}.")
				response = spawn.expect(expect=expect, send=send, timeout=timeout)
				if not response.success:
					if "None of the specified inputs were expected." in response.error:
						if optional:
							return _response_.error(f"Unable to find the expected input but still success since it is optional.")
						else:
							return _response_.error(f"Specified input [{Array(expect).string(joiner=', ')}] was not expected.")
					else: return response
				if log_level >= 8:
					print("Send response message:",response.message)

				# success.
				return _response_.success("Success.")

			""" check expecting. """
			expecting = True
			if not spawn.expecting:
				expecting = False
				if not optional:
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					if log_level >= 3:
						return OutputObject(error=f"Failed to send expected input {str_input} to {response_str}, child is not expecting any input [{spawn.child}].", log_level=log_level)
					else:
						return OutputObject(error=f"Failed to send expected input {str_input} to {response_str}, child is not expecting any input.", log_level=log_level)

			# limit not expecting by optional.
			if expecting:

				# send all dicts in the list (list instance).
				error_end_of_file = False
				if isinstance(input, (list, Array)):
					for _input_ in input:
						response = process_dict_input(_input_)
						if not response.success: 
							if "End of file" in response.error:
								error_end_of_file = True
							else: 
								# str input.
								if isinstance(_input_, (list, Array)):
									str_input = Array(_input_).string(joiner=", ")
								elif isinstance(_input_, (dict, Dictionary)):
									str_input = Array(list(_input_.keys())).string(joiner=", ")
								else: 
									str_input = f"[{_input_}]"
								if optional:
									break
								else:
									if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
									return OutputObject(error=f"Failed to send one of the expected input(s) {str_input}, error: {response.error}", log_level=log_level)

				# send one of the keys (dict instance).
				elif isinstance(input, (dict, Dictionary)):
					response = process_dict_input(input)
					if not response.success: 
						if "End of file" in response.error:
							error_end_of_file = True
						elif not optional:
							if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
							return OutputObject(error=f"Failed to send one of the expected input(s) {str_input}, error: {response.error}", log_level=log_level)

				""" check no input left (does not work properly).
				if not error_end_of_file and spawn.expecting:
					try: after = spawn.child.after.decode()
					except : after = spawn.child.after
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					return OutputObject(error=f"Failed to execute {response_str}, still expecting: [{after}].", log_level=log_level)
				"""		

		# do not get or kill when async.
		output = None
		if not async_:

			# check crashed.
			response = spawn.crashed()
			if not response.success:  
				if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
				return OutputObject(error=response.error, log_level=log_level)

			# always await sync.
			response = spawn.wait()
			if not response.success: 
				if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
				return OutputObject(error=response.error, log_level=log_level)
			output = response.output
			if error_end_of_file != None and error_end_of_file: 
				if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
				if log_level >= 3:
					return OutputObject(error=f"Failed to send expected input {str_input} to {response_str} (#234343) (output: {output}) (child: {spawn.child}).", log_level=log_level)
				else:
					return OutputObject(error=f"Failed to send expected input {str_input} to {response_str} (#234343) (output: {output}).", log_level=log_level)

			# check kill.
			if kill and spawn.running:
				if log_level >= 8: print(f"Killing process {response_str}.")
				response = spawn.kill()
				if not response.success: 
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					return OutputObject(error=f"Failed to kill {response_str}, error: {response.error}", log_level=log_level)

		# async.
		elif async_:

			# check exit status.
			response = spawn.read(wait=False)
			if not response.success: 
				if not response.success: 
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					return OutputObject(error=f"Failed to retrieve output from spawn {response_str}, error: {response.error}", log_level=log_level)
			if spawn.child.exitstatus not in [0, None]:
				if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
				return OutputObject(error=f"{response_str} returned exit status: [{spawn.child.exitstatus}] (output: {self.read(wait=False, __safe__=True).output}).", log_level=log_level)

			# await async.
			if wait:

				# await.
				response = spawn.wait()
				if not response.success: 
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					return OutputObject(error=response.error, log_level=log_level) # exit status.
				output = response.output

				if spawn.child.exitstatus not in [0, None]:
					if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
					return OutputObject(error=f"{response_str} returned exit status: [{spawn.child.exitstatus}] (output: {self.read(wait=False, __safe__=True).output}).", log_level=log_level)
				
				# check kill.
				if kill and spawn.running:
					if log_level >= 8: print(f"Killing process {response_str}.")
					response = spawn.kill()
					if not response.success: 
						if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
						return OutputObject(error=f"Failed to kill {response_str}, error: {response.error}", log_level=log_level)

	# handler.
	if delete: Files.delete(path)
	if serialize:
		try: response = _response_.ResponseObject(output)
		except Exception as e: 
			if loader != None: loader.stop(success=False)
			if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
			return OutputObject(error=f"Failed to serialize (output: {output}).", log_level=log_level)
		if not response.success: 
			if stop_loader and isinstance(loader, console.Loader): loader.stop(success=False)
			return OutputObject(error=f"Encoutered an error in the serialized response, error: {response.error}", log_level=log_level)
	if stop_loader and isinstance(loader, console.Loader): loader.stop()
	return OutputObject(message=f"Succesfully executed {response_str}.", log_level=log_level, attributes={
		"output":output,
		"process":spawn,
		"pid":spawn.child.pid,
		"running":spawn.running,
		"exit_status":spawn.exit_status,
	})


	"""
	# excute default without input.
	else:

		# excute.
		if async_:
			proc = subprocess.Popen(
				[executable, path] + arguments,
				shell=shell,)
			return OutputObject(message=f"Succesfully executed {response_str}.", log_level=log_level, attributes={
				"output":"",
				"process":proc,
				"pid":proc.pid,
			})
		try:
			proc = subprocess.run(
				[executable, path] + arguments,
				check=True,
				capture_output=True,
				text=True,
				shell=shell,
			)
		except subprocess.CalledProcessError as error:
			exception = String(str(error))
			if "Command '[" in exception:
				to_replace = f"'{exception.slice_array()}'"
				exception = exception.replace(str(to_replace), "[ ... ]")
			error_, output = error.stderr, error.output
			if isinstance(error_, bytes): error_ = error_.decode()
			if isinstance(output, bytes): output = output.decode()
			if log_level <= 0:
				return OutputObject(error=f"Failed to execute {response_str}, (exception: {exception}), (error: {error_}).", log_level=log_level)
			else:
				return OutputObject(error=f"Failed to execute {response_str}, (exception: {exception}), (output: {output}), (error: {error_}).", log_level=log_level)
		error_, output = proc.stderr, proc.stdout
		if isinstance(error_, bytes): error_ = error_.decode()
		if isinstance(output, bytes): output = output.decode()
		if error_ != "":
			if log_level <= 0:
				return OutputObject(error=f"Failed to execute {response_str}, (error: {error_}).", log_level=log_level)
			else:
				return OutputObject(error=f"Failed to execute {response_str}, (output: {output}), (error: {error_}).", log_level=log_level)
		if len(output) > 0 and output[len(output)-1] == "\n": output = output[:-1]
		if serialize:
			try: response = _response_.ResponseObject(output)
			except Exception as e: 
				if loader != None: loader.stop(success=False)
				return OutputObject(error=f"Failed to serialize (output: {output}).", log_level=log_level)
			return response
		else:
			return OutputObject(message=f"Succesfully executed {response_str}.", log_level=log_level, attributes={
				"output":output,
				"process":proc,
				"pid":None,
			})
	"""

# the spawn object class (for inputs).
class Spawn(objects.Object):
	def __init__(self,
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
		response_str=None,
	):
		# docs.
		DOCS = {
			"module":"dev0s.code.Spawn", 
			"initialized":False,
			"description":[], 
			"chapter": "Code", }

		# defaults.
		objects.Object.__init__(self, traceback="dev0s.code.execute.spawn")
		self.assign(attributes)

		# args.
		self.command = command
		self.async_ = async_
		self.log_level = log_level
		self.response_str = response_str

		# vars.
		self.child = None
		self.__secrets__ = []

		#

	# start the process.
	def start(self):
		try:
			self.child = pexpect.spawn(self.command)
		except Exception as e:
			return _response_.error(f"Failed to spawn {self.response_str}, error: {e}.")
		# check exit status.
		if self.child.exitstatus not in [0, None]:
			return OutputObject(error=f"{self.response_str} returned exit status: [{spawn.child.exitstatus}] (output: {self.read(wait=False, __safe__=True).output}).")
		self.__output__ = ""
		return _response_.success(f"Successfully spawned {self.response_str}.")
		#

	# check expect input and optionally send input.
	def expect(self,
		# the expected data parameter (#1).
		#	str instantce: expect a single identifier.
		#	list instance: expect one of the provided identifiers & return the found one if success.
		expect=["Password*"],
		# the optional data to send (#2).
		#	none instance: do not send anything.
		#	str instance: the data to send.
		#	list/tuple instance: send value of index from expected expect (required expect to be a list, Array & the indexes of [expect, send] be match).
		send=None,
		# the timeout (float).
		timeout=1.0,
	):
		# check none timeout.
		if timeout == None: timeout = 1.0

		# single expect.
		if isinstance(expect, str):
			if isinstance(send, (list, Array)): 
				raise Exceptions.InvalidUsage(f"{self.__traceback__(function='expect', parameter='send')}: parameter [send] requires to be be a [str, String] when parameter [expect] is a [{expect.__class__.__name__}], not [{send.__class__.__name__}].")

			""" add to lines to output (before) (adds nothing when empty) (do not use self.expecting before adding the output). """
			response = self.read(wait=False)
			if not response.success: return response

			""" check expect & send if provided. """
			c = 1
			try:
				#if self.async_:
				#	g = yield from self.child.expect(expect, timeout=timeout, async_=True)
				#	r = next(g)
				#else:
				r = self.child.expect(expect, timeout=timeout)
				if not isinstance(r, (int, Integer, float)):
					return _response_.error(f"Expected [{expect}] is not the child's expected input (#873465).")
				c = 2
				if self.log_level >= 8: print(f"Found expected: {expect}")
				if send != None:
					if self.log_level >= 8: print(f"Attempting to send: {send}")
					#if self.async_:
					#	g = yield from self.child.sendline(str(send), async_=True)
					#	r = next(g)
					#else:
					r = self.child.sendline(str(send))
					self.__secrets__.append(str(send))
					if self.log_level >= 8: print(f"Succesfully sended: {send}")
			except pexpect.exceptions.TIMEOUT:
				if c == 1:
					return _response_.error(f"Expected [{expect}] is not the child's expected input, error: Timeout (during epxecting).")
				else:
					return _response_.error(f"Failed to send expected [{expect}], error: Timeout (during sending input).")
			except pexpect.exceptions.EOF:
				if c == 1:
					return _response_.error(f"Expected [{expect}] is not the child's expected input, error: End of file (during epxecting).")
				else:
					return _response_.error(f"Failed to send expected [{expect}], error: End of file (during sending input).")
			except Exception as e:
				if c == 1:
					return _response_.error(f"Expected [{expect}] is not the child's expected input, error: {e}.")
				else:
					return _response_.error(f"Failed to send expected [{expect}], error: {e}.")

			
			""" add to lines to output (after) (adds nothing when empty) (do not use self.expecting before adding the output). """
			response = self.read(wait=False)
			if not response.success: return response

			# handler.
			if send != None:
				return _response_.success(f"Successfully send expected input ({expect}).")
			else:
				return _response_.success(f"Successfully retrieved expected input ({expect}).")

		# list expect.
		elif isinstance(expect, (list, Array)):
			index = 0
			for _expect_ in expect:
				if isinstance(send, (list,Array)):
					try:
						_send_ = str(send[index])
					except:
						raise Exceptions.InvalidUsage(f"{self.__traceback__(function='expect', parameter='send')}: parameter [send] and parameter [expect] do not have the same indexes.")
				else:
					_send_ = str(send)
				if self.log_level >= 8: print(f"Checking optional expect: {_expect_}")
				response = self.expect(expect=_expect_, timeout=timeout, send=_send_)
				if not response.success and "is not the child's expected input" not in response.error: return response
				elif response.success:
					return _response_.success(f"Successfully {Boolean(send).string(true='send', false='retrieved')} the expected input(s).", {
						"expected":_expect_,
						"index":index,
					})
				index += 1
			return _response_.error(f"None of the specified input was expected.")

		# invalid usage.
		else:
			raise Exceptions.InvalidUsage(f"{self.__traceback__(function='expect', parameter='expect')}: parameter [expect] requires to be be a [Dictionary], not [{config.__class__.__name__}].")

	# read output.
	def read(self, 
		# with await False it reads only the printed output regardless the status & never throws timeout.
		wait=False, 
		# the timeout, leave None for no timeout.
		timeout=None,
		# the live boolean (bool) (prints live logs to console when enabled) (leave None to use self.log_level >= 3).
		live=None, 
		# system variables.
		#   safe True always a response.output variable upon error the response.output is "".
		__safe__=False,
	):

		# clean line.
		def clean_line(line):
			if isinstance(line, bytes): line = line.decode()
			if line in [" password:"]: return None
			for secret in self.__secrets__:
				for strip_last in [secret]:
					if secret not in ["", " ", "  ", "   ", "    "] and len(line) >= len(strip_last) and line[-len(strip_last):] == strip_last: 
						return line[:-len(strip_last)]
			return line
		def clean_output(output):
			_output_, b = "", output.replace("\r","").replace("\t","").split("\n")
			c, m = 0, len(b)-1
			for line in b: 
				l = clean_line(line)
				if l not in [None]:
					if c < m: _output_ += l+"\n"
					else: _output_ += l
				c += 1
			return _output_
		def log_output(output):
			while True:
				if len(output) >= 1 and output[len(output)-1] == "\n": output = output[:-1]
				else: break	
			print(output)

		# checks.
		if live == None: live = self.log_level >= 3

		# old timeout.
		old = self.child.timeout

		# version 2: reads only the printed lines and stops when the timeout is hit so there is no timeout required. 
		output_logs_allowed = True
		if not wait:
			self.child.timeout = 0.25
			output_logs_allowed = False
			output, c = "", 0
			for line in range(1000000000):
				try:
					#if self.async_:
					#	g = yield from self.child.readline(line, async_=True)
					#	output += next(g).decode()
					#else:
					new = self.child.readline(line).decode()
					if new == "": 
						c += 1
						if c >= 25: break
					else: 
						output_logs_allowed = True
						c = 0
						output += new
				except pexpect.exceptions.TIMEOUT:
					break
				except pexpect.exceptions.EOF:
					break
				except Exception as e:
					if timeout != None: self.child.timeout = old
					e = str(e)
					if self.log_level <= 0: e = str(e).split("\n")[0] # strip the full child from the pexpect error message.
					while True:
						if len(e) >= 1 and e[len(e)-1] == ".": e = e[:-1]
						else: break
					if "Timeout" in str(e):
						response = _response_.error(f"{e} (most likely the command is still expecting input).")
						if __safe__: response.output = ""
						return response
					else:
						response = _response_.error(f"{e}.")	
						if __safe__: response.output = ""
						return response

		# version 1: throws an error when unable to read output if timeout is defined, so it can be used to detect if input is expected. 
		else:

			# handle output.
			self.child.timeout = timeout
			try:
				#output = self.child.read().decode()
				output = ""
				#if self.async_:
				#	g = yield from self.child.readlines(async_=True)
				#	lines = next(x)
				#else:
				lines = self.child.readlines()
				if lines == []:
					output_logs_allowed = False
				else:
					for i in lines: output += i.decode()
			except Exception as e:
				self.child.timeout = old
				e = str(e)
				if self.log_level <= 0: e = str(e).split("\n")[0] # strip the full child from the pexpect error message.
				while True:
					if len(e) >= 1 and e[len(e)-1] == ".": e = e[:-1]
					else: break
				if "Timeout" in str(e):
					response = _response_.error(f"{e} (most likely the command is still expecting input).")
					if __safe__: response.output = ""
					return response
				else:
					response = _response_.error(f"{e}.")
					if __safe__: response.output = ""
					return response

		# clean output.
		output = clean_output(output)
		if output_logs_allowed and live: log_output(output)

		# handler.
		self.child.timeout = old
		self.__output__ += output
		self.__output__ = clean_output(self.__output__)
		return _response_.success("Successfully retrieved the child's output.", {
			"output":str(self.__output__),
			"new_output":output,
		})


		#

	# kill the process.
	def kill(self):
		
		# handle output.
		"""
		killed = None
		try:
			#if self.async_:
			#	g = yield from self.child.terminate(force=True, async_=True)
			#	killed = next(x)
			#else:
			killed = self.child.terminate(force=True)
		except Exception as e:
			return _response_.error(f"Failed to kill process [{self.command}], error: {e}.")
		if killed == None:
			return _response_.error(f"Failed to kill process [{self.command}] (#452983).")
		if not killed:
		"""
		
		# handle output.
		response = kill(pid=self.pid, log_level=self.log_level)
		if not response.success:
			return _response_.error(f"Unable to kill process [{self.command}].")
		else:
			return _response_.success(f"Successfully killed process [{self.command}].")

		#

	# wait for the process to finish.
	def wait(self, 
		# the live boolean (bool) (prints live logs to console when enabled) (leave None to use self.log_level >= 3).
		live=None, 
		sleeptime=1,
		# the timeout (leave None to ignore).
		timeout=None,
	):
		
		# checks.
		if live == None: live = self.log_level >= 3

		# live
		if live:
			while self.running:
				response = self.read(wait=False, live=live)
				if not response.success: return response
				if self.running:
					time.sleep(sleeptime)
			return self.wait(live=False, timeout=timeout)

		# not live.
		else:

			# read & wait with no timeout
			response = self.read(wait=True, timeout=timeout)
			if response.success:
				while True:
					if len(response.output) > 0 and response.output[len(response.output)-1] == "\n": response.output = response.output[:-1]
					else: break
			return response

		#

	# check if process is crashed.
	def crashed(self):
		response = self.read(wait=False)
		if not response.success:  return response
		if self.exit_status not in [0, None]:
			return _response_.error(f"{self.response_str} returned exit status: [{self.exit_status}] (output: {self.read(wait=False, __safe__=True).output}).")
		return _response_.success(f"{self.response_str} is not crashed.")

	# is expecting input.
	@property
	def expecting(self):

		# version 2.
		if self.exit_status not in [None]: return False
		elif self.child.closed: return False
		elif not self.running: return False
		else:


			""" add to lines to output (adds nothing when empty) (to prevent the output reset called the proceeding code) . """
			response = self.read(wait=False)
			if not response.success: return response

			""" output throws timeout error when still expecting & when with success a process has finiished. """
			response = self.read(wait=True, timeout=1.0) 
			if not response.success:
				if "still expecting input" in response.error: return True
				else: raise ValueError(f"Unknown behaviour while detecting @spawn.expecting, error: {response.error}")
			else: return False

			#
		raise ValueError(f"Unable to determine is spawn is expecting, child: {self.child}.")

		""" version 1.
		try:
			# renaming "" to pexpect.EOF removes the output.
			self.child.expect("", timeout=1)
			return False
		except pexpect.exceptions.EOF:
			return True
		except:
			return False
		raise ValueError(f"Unable to determine is spawn is expecting, child: {self.child}.")
		"""

	# is running.
	@property
	def running(self):
		"""if self.async_:
			boolean = yield from self.child.isalive(async_=True)
		else:
			boolean = self.child.isalive()
		"""
		boolean = self.child.isalive()
		return boolean
		#
	# exit status.
	@property
	def exit_status(self):
		"""if self.async_:
			boolean = yield from self.child.exitstatus
		else:
			boolean = self.child.exitstatus
		"""
		boolean = self.child.exitstatus
		return boolean
		#
	# output property.
	@property
	def output(self):
		return self.__output__
	# pid.
	@property
	def pid(self):
		return self.child.pid
	

	#

# the output object class (very similair to the ResponseObject).
class OutputObject(ResponseObject):
	def __init__(self, 
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
		log_level=defaults.options.log_level,
	):
		# docs.
		DOCS = {
			"module":"dev0s.code.OutputObject", 
			"initialized":False,
			"description":[], 
			"chapter": "Code", }

		# attributes.
		dictionary = {
			"success":error == None,
			"message":message,
			"error":error,
			"log_level":log_level,
		}
		for key,value in attributes.items():
			dictionary[key] = value
		ResponseObject.__init__(self, dictionary)
		if self.success:
			try: 
				if self.output == None: raise AttributeError("")
			except AttributeError: self.output = ""
		else: self.output = str(self.error) # keep this way for system functions.
		self.lines = self.output.split("\n")

	# representations.
	def __len__(self):
		return len(self.output)
		#
	def __bool__(self):
		return bool(self.success)
		#

		#

	# support '==' & '!=' operator.
	def __eq__(self, dictionary):
		if dictionary.__class__.__name__ in ["str", "String", "NoneType", "int", "float", "Integer"]:
			return str(self.output) != str(dictionary)
		elif isinstance(dictionary, dict):
			return str(self.sort()) == str(Dictionary(dictionary).sort())
		elif isinstance(dictionary, Dictionary):
			return str(self.sort()) == str(dictionary.sort())
		else:
			try:
				return str(self.sort()) == str(dictionary.sort())
			except:
				return False
	def __ne__(self, dictionary):
		if dictionary.__class__.__name__ in ["str", "String", "NoneType", "int", "float", "Integer"]:
			return str(self.output) != str(dictionary)
		elif isinstance(dictionary, dict):
			return str(self.sort()) != str(Dictionary(dictionary).sort())
		elif isinstance(dictionary, Dictionary):
			return str(self.sort()) != str(dictionary.sort())
		else:
			try:
				return str(self.sort()) != str(dictionary.sort())
			except:
				return False

	# support 'in' operator.
	def __contains__(self, string):
		if isinstance(string, (list, Array)):
			for i in string:
				if str(i) in str(self.output):
					return True
			return False
		else:
			return str(string) in str(self.output)
		#

	# object instance.
	def instance(self):
		return "OutputObject"
		#
	# assign to ResponseObject.
	def response(self):
		return _response_.response(self.dict())
		#

	#


#
