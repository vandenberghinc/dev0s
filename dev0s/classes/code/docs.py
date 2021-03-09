#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.config import *

# the docs object class.
# used to assign unique readme building values to a coded class.
class Docs(object):
	def __init__(self,
		# boolean inidicating if the object is initialized by default.
		initialized=True,
		# the full module path in import style (when initializing).
		module="Code.Docs",
		# the notes that will apread above the class_ initialization (leave [] to use default.
		notes=[],
	):
		
		# attributes.
		self.initialized = initialized
		self.module = module
		self.notes = notes

		# checks.
		if self.notes in [None, False, ""]: self.notes = []

		#
