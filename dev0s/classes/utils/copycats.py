#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.config import *

# the console.* functions (exact copy).
def argument_present(arguments, default=False, count=1):
	if isinstance(arguments, str):
		c = sys.argv.count(arguments)
		if c > 0 and count <= c:
			return True
		else: return default
	elif isinstance(arguments, list):
		for argument in arguments:
			c = sys.argv.count(argument)
			if c > 0 and count <= c:
				return True
		return default
	else: raise ValueError("Invalid usage, arguments must either be a list or string.")
def arguments_present(arguments, default=False, count=1):
	if isinstance(arguments, str): return argument_present(arguments, default=default, count=count)
	else:
		for argument in arguments:
			if argument_present(argument, default=default, count=count):
				return True
		return default
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

