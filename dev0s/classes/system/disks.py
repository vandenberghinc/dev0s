
# imports
from dev0s.classes.config import *
from dev0s.classes.defaults.objects import *
from dev0s.classes.defaults.defaults import defaults
from dev0s.classes.response import response as _response_

# utils.
def check_os(supported=["linux"], error=False):
	if OS not in supported:
		if error: raise ValueError(f"Unsupported operating system: {OS}.")
		else: return _response_.error(f"Unsupported operating system: {OS}.")
	else:
		if error: return None
		else: return _response_.success(f"Supported operating system: {OS}.")
def coming_soon():
	raise ValueError("COMING SOON.")

# the disks object class.
class Disks(Object):
	def __init__(self):
		
		# docs.
		DOCS = {
			"module":"dev0s.system.disks", 
			"initialized":True,
			"description":[], 
			"chapter": "System", }

		# defaults.
		Object.__init__(self, traceback="dev0s.system.disks")

		#
	def list(self):
		coming_soon()

		# check os.
		response = check_os()
		if not response.success: return response

		#
	def erase(self, 
		# the device without partition number (/dev/sdb).
		device=None,
	):

		# check parameters.
		response = _response_.parameters.check({
			"device:str":device,})
		if not response.success: return response

		# check os.
		if defaults.vars.os not in ["linux"]:
			return _response_.error(f"Unsupported operating system [{defaults.vars.os}].")

		# handler.
		if "SUCCESS!" in output:
			return _response_.success(f"Successfully erase device {device}.")
		else:
			return _response_.error(f"Failed to erase device {device}, output: {output}")

		#
	def partition(self, 
		# the device without partition number (/dev/sdb).
		device=None,
	):
		coming_soon()
		# check parameters.
		response = _response_.parameters.check({
			"device:str":device,})
		if not response.success: return response

		# check os.
		response = check_os()
		if not response.success: return response

		# execute.
		output = utils.__execute_script__(f"""
	        sudo parted {device} mklabel gpt
	        sudo parted -a opt {device} mkpart primary ext4 0% 100%
	        """)
		
		# handler.
		if "SUCCESS!" in output:
			return _response_.success(f"Successfully partitioned device {device}.")
		else:
			return _response_.error(f"Failed to partition device {device}, output: {output}")

		#
	def format(self, 
		# the device with partition number (/dev/sdb1).
		device=None,
		# the assigned label (name).
		label=None,
	):
		coming_soon()
		# check parameters.
		response = _response_.parameters.check({
			"device:str":device,
			"label:str":label,})
		if not response.success: return response
		
		# check os.
		response = check_os()
		if not response.success: return response

		# handler.
		if "SUCCESS!" in output:
			return _response_.success(f"Successfully formatted device {device}.")
		else:
			return _response_.error(f"Failed to format device {device}, output: {output}")

		#
	def mount(self, 
		# the device with partition number (/dev/sdb1).
		device=None, 
		# the mountpoint path.
		path=None,
	):
		coming_soon()
		# check parameters.
		response = _response_.parameters.check({
			"device:str":device,
			"path:str":path,})
		if not response.success: return response
		
		# check os.
		response = check_os()
		if not response.success: return response

		# handler.
		if "SUCCESS!" in output:
			return _response_.success(f"Successfully mounted device {device} to {path}.")
		else:
			return _response_.error(f"Failed to mount device {device} to {path}, output: {output}")

		#
	def unmount(self, 
		# the mountpoint path.
		path=None,
	):
		coming_soon()
		# check parameters.
		response = _response_.parameters.check({
			"path:str":path,})
		if not response.success: return response
		
		# check os.
		response = check_os()
		if not response.success: return response

		# handler.
		if "SUCCESS!" in output:
			return _response_.success(f"Successfully unmounted path {path}.")
		else:
			return _response_.error(f"Failed to unmount path {path}, output: {output}")

		#

# initialized ojects.
disks = Disks()