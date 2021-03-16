#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
import os, sys, requests, ast, json, pathlib, platform, random, shutil, zipfile, pwd, grp, subprocess, time, threading, sysconfig, urllib, flask, multiprocessing, socket
from datetime import datetime

# settings.
ALIAS = "dev0s"

# update.
if "--update" in sys.argv and ALIAS in sys.argv[0]:
	os.system(f"curl -s https://raw.githubusercontent.com/vandenberghinc/{ALIAS}/master/{ALIAS}/requirements/installer.remote | bash ")
	sys.exit(0)

# functions.
def __get_operating_system__():
	os = platform.system().lower()
	if os in ["darwin"]: return "macos"
	elif os in ["linux"]: return "linux"
	else: raise ValueError(f"Unsupported operating system: [{os}].")
def __get_source_path__(package_name, index=1):
	executable_dir = str(pathlib.Path(__file__).absolute()).replace(os.path.basename(pathlib.Path(__file__)), '').replace("//","/")
	if executable_dir[len(executable_dir)-1] == "/": executable_dir = executable_dir[:-1]
	source, c = "/", 1
	for id in executable_dir.split("/"):
		if id == package_name:
			if c == index:
				source += id+"/"
				break
			else: c += 1
		else: source += id+"/"
	base = source[:-1].split("/")
	base = source.replace(f'/{base[len(base)-1]}/', '/')
	return source, base
def __save_file__(path, data):
	file = open(path, "w+") 
	file.write(data)
	file.close()
def __load_file__(path, data="not to be used", format="str"): # keep data as second param to prevent save load errors.
        # correct format.
        if format in ["string", "file"]: format = "str"
        if format in ["dict", "array"]: format = "json"
        # match format.
        if format == "str":
            file = open(path,mode='rb')
            data = file.read().decode()
            file.close()
            return data
        elif format == "json":
            data = None
            with open(path, "r") as json_file:
                data = json.load(json_file)
            return data
        elif format == "bytes":
            data = None
            with open(path, "rb") as file:
                data = file.read()
            return data
        else: raise ValueError(f"Unknown format {format}.")

# source.
SOURCE_PATH, BASE = __get_source_path__(ALIAS, index=1)
OS = __get_operating_system__()

# file settings.
USER = OWNER = os.environ.get("USER")
GROUP = "root"
HOME = os.environ.get('HOME')+"/"
if OS in ["macos"]:  GROUP = "wheel"

# options.
ERROR_TRACEBACK = os.environ.get("R3SPONSE_ERROR_TRACEBACK")
if str(ERROR_TRACEBACK) in ["True", "true", True]: ERROR_TRACEBACK = True
else: ERROR_TRACEBACK = False
