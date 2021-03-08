#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Should be imported as:
# 
#

# _____________________________________________________________________
#
# Imports 
#   * imported by import order.
# 	* keep full writen due to import order.
# 

# imports .
from fil3s.classes import exceptions
from fil3s.classes import color
from fil3s.classes import env
from fil3s.classes import files
from fil3s.classes import response
from fil3s.classes import objects
from fil3s.classes import defaults
from fil3s.classes import cli
from fil3s.classes import requests as _requests_
from fil3s.classes import code

# _____________________________________________________________________
#
# Shortcuts (also in order):
#   * should be imported as:
#       from fil3s import *
#

# exceptions.
Exceptions = exceptions.Exceptions

# color.
symbol = color.symbol
color = color.color

# environment.
Environment = env.Environment

# files & formats.
gfp = files.gfp
gdate = files.gdate
Files = files.Files
Formats = files.Formats
FilePath = Formats.FilePath 
String = Formats.String 
Boolean = Formats.Boolean 
Integer = Formats.Integer 
Date = Formats.Date
File = Files.File
Directory = Files.Directory
Zip = Files.Zip
Image = Files.Image
Bytes = Files.Bytes
Dictionary = Files.Dictionary
Array = Files.Array

# objects.
Traceback = objects.Traceback
Object = objects.Object
Thread = objects.Thread

# response.
Response = response.Response
ResponseObject = Response.ResponseObject

# defaults.
Defaults = defaults.Defaults

# cli.
CLI = cli
CLI.CLI = CLI.CLI

# requests.
Requests = _requests_.Requests
RestAPI = Requests.RestAPI

# code.
Code = code.Code
execute = Code.execute
Spawn = Code.Spawn
OutputObject = Code.OutputObject
Version = Code.Version 
Script = Code.Script
Python = Code.Python

# _____________________________________________________________________
#
# Universal:
#   * universal package imports (do not edit).
#

# source, base & version.
source = Directory(gfp.base(__file__))
base = Directory(source.fp.base())
try: version = Version(Files.load(source.join(".version.py")))
except: version = None

#