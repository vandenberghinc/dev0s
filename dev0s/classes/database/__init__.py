#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from w3bsite.classes.objects import *
from w3bsite.classes.defaults import Defaults
from w3bsite.classes.code.docs import Docs
from w3bsite.classes.exceptions import Exceptions

# the database class.
class Database(Traceback):
	def __init__(self, 
		# the path to the directory (str) (#1)
		path=None, 
		# root permission required.
		sudo=False,
	):
		
		# docs.
		Docs.__init__(self,
			initialized=False,
			module="Database", 
			notes=[], )

		# traceback.
		Traceback.__init__(self, traceback="Database")

		# checks.
		if path == None: raise Exceptions.InvalidUsage(self.__traceback__()+" Define parameter [path].")

		# args.
		self.path = gfp.clean(path)
		self.sudo = sudo

		# attributes.
		self.dir = self.directory = Directory(self.path)

		# checks.
		if not self.dir.fp.exists(sudo=sudo):
			if self.sudo:
				Response.log(f"&ORANGE&Root permission&END& required to create database [{self.path}].")
			Files.create(self.path, sudo=self.sudo)
			Files.chmod(path=self.path, permission=700, sudo=self.sudo)
			Files.chown(path=self.path, owner=Defaults.vars.user, group=Defaults.vars.group, sudo=True)

		# copy objects.
		self.fp = self.file_path = self.dir.fp
		self.ownership = self.fp.ownership
		self.permission = self.fp.permission

		# copy functions.
		self.join = self.dir.join
		self.subpath = self.dir.subpath
		self.fullpath = self.dir.fullpath

		#

	# functions.
	def load(self, path=None):
		if path == None: return Response.error(self.__traceback__(function="load")+" Define parameter: [path].")
		path = gfp.clean(f"{self.path}/{path}")
		try:
			data = Files.load(path=path, format="json")
		except Exception as e: return Response.error(str(e))
		return Response.success(f"Successfully loaded [{path}].", {
			"data":data,
		})
	def save(self, path=None, data=None, overwrite=False):
		if path == None: return Response.error(self.__traceback__(function="save")+" Define parameter: [path].")
		if data == None: return Response.error(self.__traceback__(function="save")+" Define parameter: [data].")
		path = gfp.clean(f"{self.path}/{path}")
		try:
			if not Files.exists(path=gfp.base(path)): Files.create(path=gfp.base(path), directory=True)
		except ValueError: a=1
		if not overwrite:
			def insert(old, new):
				for key,value in new.items():
					if isinstance(value, (dict, Dictionary)):
						if key in old:
							old[key] = insert(old[key], value)
						else:
							old[key] = value
					elif isinstance(value, (list, Array)):
						if key in old:
							for i in value:
								if i not in old[key]: old[key].append(i)
						else:
							old[key] = value
					else:
						old[key] = value
				return old
			try: old_data = Files.load(path=path, format="json")
			except: old_data = {}
			data = insert(old_data, data)
		try:
			Files.save(path=path, data=data, format="json")
		except Exception as e: return Response.error(str(e))
		return Response.success(f"Successfully saved [{path}].")
		else: raise Exceptions.InvalidUsage(self.__traceback__(function="save")+f" Unknown mode [{self.mode}].")
	def delete(self, path=None, data=None):
		if path == None: return Response.error(self.__traceback__(function="delete")+" Define parameter: [path].")
		path = gfp.clean(f"{self.path}/{path}")
		try:
			Files.delete(path=path)
		except Exception as e: return Response.error(str(e))
		if Files.exists(path): return Response.error(f"Failed to delete [{path}].")
		return Response.success(f"Successfully deleted [{path}].")

	# get names.
	def names(self,
		# the sub path (leave None to use the root path)
		path=None,
	):

		# checks.
		if path == None: return Response.error(self.__traceback__(function="names")+" Define parameter: [path].")
		
		# names.
		names = []
		for i in Directory(path=self.join(path)).paths(): names.append(gfp.name(i))

		# handler.
		return names

		#

	# representation.
	def __str__(self):
		return str(self.dir.fp.path)
	def __repr__(self):
		return str(self)

	#

	
			