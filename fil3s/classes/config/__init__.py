#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
import os, sys, requests, ast, json, pathlib, platform, random, shutil, zipfile, pwd, grp, subprocess, time, threading
from datetime import datetime

# functions.
def __get_operating_system__():
	os = platform.system().lower()
	if os in ["darwin"]: return "macos"
	elif os in ["linux"]: return "linux"
	else: raise ValueError(f"Unsupported operating system: [{os}].")
def __get_source_path__(package_name, index=1):
	executive_dir = str(pathlib.Path(__file__).absolute()).replace(os.path.basename(pathlib.Path(__file__)), '').replace("//","/")
	if executive_dir[len(executive_dir)-1] == "/": executive_dir = executive_dir[:-1]
	source, c = "/", 1
	for id in executive_dir.split("/"):
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
ALIAS = "fil3s"
SOURCE_NAME = "fil3s"
SOURCE_PATH, BASE = __get_source_path__(SOURCE_NAME, index=1)
OS = __get_operating_system__()

# file settings.
USER = OWNER = os.environ.get("USER")
GROUP = "root"
HOME = f"/home/{OWNER}/"
if OS in ["macos"]: 
	GROUP = "wheel"
	HOME = f"/Users/{OWNER}/"

