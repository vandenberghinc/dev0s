#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_
from dev0s.classes import code
from dev0s.classes.defaults.defaults import defaults

# the cleanup object class.
class CleanUp(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"dev0s.system.cleanup", 
			"initialized":True,
			"description":[], 
			"chapter": "CleanUp", }

		#

	# clean the ram memory.
	def ram(self):

		# linux.
		if defaults.vars.os in ["linux"]:
			path = f"/tmp/ram_cleanup.sh"
			Files.save(path, '''

				#!/bin/bash
				## Bash Script to clear cached memory on (Ubuntu/Debian) Linux
				## By Philipp Klaus
				## see <http://blog.philippklaus.de/2011/02/clear-cached-memory-on-ubuntu/>
				
				if [ "$(whoami)" != "root" ]
				then
				  echo "You have to run this script as Superuser!"
				  exit 1
				fi

				# Get Memory Information
				freemem_before=$(cat /proc/meminfo | grep MemFree | tr -s ' ' | cut -d ' ' -f2) && freemem_before=$(echo "$freemem_before/1024.0" | bc)
				cachedmem_before=$(cat /proc/meminfo | grep "^Cached" | tr -s ' ' | cut -d ' ' -f2) && cachedmem_before=$(echo "$cachedmem_before/1024.0" | bc)

				# Output Information
				#echo -e "This script will clear cached memory and free up your ram.\\n\\nAt the moment you have $cachedmem_before MiB cached and $freemem_before MiB free memory."

				# Test sync
				if [ "$?" != "0" ]
				then
				  echo "Something went wrong, It's impossible to sync the filesystem."
				  exit 1
				fi

				# Clear Filesystem Buffer using "sync" and Clear Caches
				sync && echo 3 > /proc/sys/vm/drop_caches

				freemem_after=$(cat /proc/meminfo | grep MemFree | tr -s ' ' | cut -d ' ' -f2) && freemem_after=$(echo "$freemem_after/1024.0" | bc)

				# Output Summadry
				#echo -e "This freed $(echo "$freemem_after - $freemem_before" | bc) MiB, so now you have $freemem_after MiB of free RAM."

			''')
			Files.chmod(path, "+x")
			output = code.execute(f"sudo {path}")
			#Files.delete(path, forced=True)
			if not output.success: return output

		# macos.
		#elif defaults.vars.os in ["linux"]:

		# invalid os.
		else: raise ValueError(f"Unsupported operating system: {defaults.vars.os}.")
		

		# handler.
		return _response_.success("Successfully cleared the RAM memory.")

	#

	# clean the swap memory.
	def swap(self):

		# linux.
		if defaults.vars.os in ["linux"]:
			output = code.execute(f"""
				sudo swapoff -a
				sudo swapon -a
			""")
			if not output.success: return output

		# macos.
		#elif defaults.vars.os in ["linux"]:

		# invalid os.
		else: raise ValueError(f"Unsupported operating system: {defaults.vars.os}.")
		

		# handler.
		return _response_.success("Successfully cleared the swap memory.")

	#





		
