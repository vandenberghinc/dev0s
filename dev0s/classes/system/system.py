#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_
from dev0s.classes import code
from dev0s.classes.defaults.defaults import defaults

"""
missing imports / variables:
	defaults, python_plus
"""

# functions.
def check_user(id, create=False):
	user = User(username=id)
	response = user.check()
	if not response.success:  return response
	if response["success"] and not response["exists"] and create: 
		response = user.create()
		if not response.success: return response
	return _response_.success(f"Successfully checked user [{id}].")
def check_group(id, users=[], create=False, overwrite=False):
	group = Group(name=id, get_users=False)
	response = group.check()
	if not response.success: return response
	if response["success"] and not response["exists"] and create: 
		response = group.create(users=users)
		if not response.success: return response
	elif overwrite:
		response = group.check_users(users=users)
		if not response.success: return response
	return _response_.success(f"Successfully checked group [{id}].")


# the user object.
class User(object):
	# notes about the object
	# this is an example
	def __init__(self, 
		# the users username.
		username=None,
	):

		# docs.
		DOCS = {
			"module":"dev0s.system.User", 
			"initialized":False,
			"description":[], 
			"chapter": "System", }

		# arguments.
		self.username = username
		self.home_directory = f"{defaults.vars.homes}{self.username}/"

		#
	def create(self):
		
		# check duplicates.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		if l_response["exists"]:
			return _response_.error(f"User [{self.username}] already exists.")

		# check home dir.
		if Files.exists(self.home_directory): 
			return _response_.error(f"Home directory [{self.home_directory}] already exists.")

		# handle linux.
		if OS in ["linux"]:
			# ubuntu.
			output = code.execute(f"sudo useradd -s /bin/bash -m {self.username}")

			# success.
			if output == "":
				return _response_.success(f"Successfully created user [{self.username}].")

			else:
				return _response_.error(String(output.output.replace("useradd: ", "").replace("\n", ". ")).capitalized_word())

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		
		

		#
	def delete(self):
		
		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		if not l_response["exists"]:
			return _response_.error(f"User [{self.username}] does not exist.")

		# handle linux.
		if OS in ["linux"]:

			# delete.
			os.system(f"sudo userdel -r {self.username}")
			os.system(f"sudo rm -fr {self.home_directory}")

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# check.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		
		# success.
		if not l_response["exists"]:
			return _response_.success(f"Successfully deleted user [{self.username}].")
		else:
			return _response_.error(f"Failed to delete user [{self.username}].")

		#
	def check(self, silent=False):

		# handle linux.
		exists = False
		if OS in ["linux"]:
			try: 
				output = subprocess.check_output("sudo id {username}".format(username=self.username), shell=True).decode()
				exists = True
			except: exists = False

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# success.
		return _response_.success(f"Successfully checked user [{self.username}].", {
			"exists":exists,
		})

		#
	def set_password(self, password=None):
		
		# check params.
		response = _response_.parameters.check(
			parameters={
				"password":password,
			})
		if not response.success: return response

		# handle linux.
		if OS in ["linux"]:

			# get output.
			output = code.execute(f"export HISTIGNORE='*sudo -S*' && echo '{password}\n{password}\n' | sudo -S -k sudo passwd {self.username}")
			
			# success.
			if "password updated successfully" in output:
				return _response_.success(f"Successfully edited the password of user [{self.username}].")

			# fail.
			else:
				print(output)
				return _response_.error(f"Failed to edit the password of user [{self.username}].")

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		#
	def add_groups(self, groups=[]):

		# iterate groups.
		for group in groups:

			# init group.
			group = GroupObject(name=group)

			# check existance.
			l_response = group.check()
			if l_response["error"] != None: return l_response
			if not response["exists"]: 
				return _response_.error(f"Group [{group.name}] does not exist.")

			# add user.
			l_response = group.add_users(users=[self.username])
			if l_response["error"] != None: return l_response

			#
		
		# success.
		return _response_.success(f"Successfully added user to [{len(groups)}] groups.")

		#
	def delete_groups(self, groups=[]):
		
		# iterate groups.
		for group in groups:
			group = GroupObject(name=group)
			l_response = group.check()
			if l_response["error"] != None: return l_response
			if not response["exists"]: 
				return _response_.error(f"Group [{group.name}] does not exist.")

			# delete user.
			l_response = group.delete_users(users=[self.username])
			if l_response["error"] != None: return l_response

				
		# success.
		return _response_.success(f"Successfully added user to [{len(groups)}] groups.")

		#

# the group object.
class Group(object):
	def __init__(
		self, 
		# string format.
		name=None,
		users=[], # all authorized user identifiers.
		# boolean format.
		get_users=False, # (only gets filled if the storages group exists.)
	):

		# docs.
		DOCS = {
			"module":"dev0s.system.Group", 
			"initialized":False,
			"description":[], 
			"chapter": "System", }

		# arguments.
		self.name = name
		self.users = users

		# functions.
		if get_users:
			response = self.check()
			if response["success"] and response["exists"]:
				response = self.list_users()
				if response["success"]: self.users = response["users"]

		#
	def create(self, users=None):

		# initialize default response.
		if users == None: users = self.users

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif l_response["exists"]:
			return _response_.error(f"Group [{self.name}] already exists.")

		# handle linux.
		if OS in ["linux"]:
			output = code.execute(f"sudo groupadd {self.name}",)

			# success.
			if output == "":
				return _response_.success(f"Successfully created group [{self.name}].")

			else:
				return _response_.error(String(output.output.replace("groupadd: ", "").replace("\n", ". ")).capitalized_word())

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		#
	def delete(self):

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif l_response["exists"]:
			return _response_.error(f"Group [{self.name}] already exists.")

		# handle linux.
		if OS in ["linux"]:
			os.system(f"sudo groupdel {self.name}")

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif l_response["exists"]:
			return _response_.error(f"Failed to delete group [{self.name}].")
		else:
			return _response_.success(f"Successfully deleted group [{self.name}].")


		#
	def check(self):

		# handle linux.
		exists = False
		if OS in ["linux"]:
			try:
				output = subprocess.check_output("grep '^{name}' /etc/group".format(name=self.name), shell=True).decode()
				exists = True
			except: exists = False

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		
		# success.
		return _response_.success(f"Successfully checked group [{self.name}].", {
			"exists":exists,
		})

		#
	def list_users(self):

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif not l_response["exists"]:
			return _response_.error(f"Group [{self.name}] does not exists.")

		# handle linux.
		users = []
		if OS in ["linux"]:
			try: output = subprocess.check_output("members "+self.name, shell=True).decode().replace("\n", "").split(" ")
			except: output = []
			for i in output:
				if i not in [""]: 
					users.append(i.replace("\n", ""))

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# success.
		self.users = users
		return _response_.success(f"Successfully listed all users {len(users)} of group [{self.name}].", {
			"users":users,
		})

		#
	def delete_users(self, users=[]):

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif not l_response["exists"]:
			return _response_.error(f"Group [{self.name}] does not exists.")

		# handle linux.
		if OS in ["linux"]:
			for user in users:
				output = code.execute(f"sudo deluser {user} {self.name}")
				if output != "" and "Removing user " not in output:
					return _response_.error(String(output.output.replace("deluser: ", "").replace("\n", ". ")).capitalized_word())

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# success.
		return _response_.success(f"Successfully deleted {len(users)} users from group [{self.name}].", {
			"users":users,
		})

		#
	def add_users(self, users=[]):

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif not l_response["exists"]:
			return _response_.error(f"Group [{self.name}] does not exists.")

		# handle linux.
		if OS in ["linux"]:
			for user in users:
				output = code.execute(f"sudo usermod -a -G {self.name} {user}")
				if not output.success: return output
				if output.output != "":
					return _response_.error(String(output.output.replace("usermod: ", "").replace("\n", ". ")).capitalized_word())

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# success.
		return _response_.success(f"Successfully added {len(users)} users to group [{self.name}].", {
			"users":users,
		})

		#
	def check_users(self, users=[]):
		# deletes all users that are not in the specified ones & adds new specified ones.
		#

		# check existance.
		l_response = self.check()
		if l_response["error"] != None: return l_response
		elif not l_response["exists"]:
			return _response_.error(f"Group [{self.name}] does not exists.")

		# handle linux.
		to_delete, to_add  = [], []
		if OS in ["linux"]:
			
			# check to delete:
			response = self.list_users()
			if response["error"] != None: return response
			l_users = response["users"]
			for user in l_users:
				if user not in users: to_delete.append(user)
			if len(to_delete) > 0:
				response = self.delete_users(users=to_delete)
				if response["error"] != None: return response

			# check to add:
			response = self.list_users()
			if response["error"] != None: return response
			l_users = response["users"]
			for user in users:
				if user not in l_users: to_add.append(user)
			if len(to_add) > 0:
				response = self.add_users(users=to_add)
				if response["error"] != None: return response

		# handle macos.
		elif OS in ["macos"]:
			return _response_.error(f"Unsupported operating system [{OS}].")

		# success.
		return _response_.success(f"Successfully added {len(to_add)} & removed {len(to_delete)} users from group [{self.name}].")

		#

"""
# the unix manager.
class UnixManager(object):
	# notes about the object
	# this is an example
	def __init__(self):

		# init:
		self.users_path = "/home/"
		if OS in ["macos"]: self.users_path = "/Users/"
		self.users = {} # can be filles with objects, format = {"$idenfitier":UserObject()}
		self.groups = {} # can be filles with objects, format = {"$idenfitier":GroupObject()}

"""






"""

# -----------------------
# the User() object class.

# initialize a user object.
user = User("testuser")

# check if the user exists.
response = user.check()
if response["success"]: print("User existance:",response["exists"])

# create a user.
response = user.create()

# delete a user.
response = user.delete()

# set a users password.
response = user.set_password(password="Doeman12!")

# add the user to groups.
response = user.add_groups(groups=[])

# delete the user from groups.
response = user.add_groups(groups=[])

# -----------------------
# the Group() object class.

# initialize a group object.
group = Group("testgroup")

# check if the group exists.
response = group.check()
if response["success"]: print("Group existance:",response["exists"])

# create a group.
response = group.create()

# delete a group.
response = group.delete()

# list the current users.
response = group.list_users()
if response["success"]: print(f"Users of group {group.name}:",response["users"])

# add users to the group.
response = group.add_users(users=["testuser"])

# delete users from the group.
response = group.delete_users(users=["testuser"])

# check if specified users are enabled and remove all other users.
response = group.check_users(users=["testuser"])

# -----------------------
# The dictionary response.

# handle response.
if response["error"] != None: print(response["error"])
else: print(response["message"])

"""