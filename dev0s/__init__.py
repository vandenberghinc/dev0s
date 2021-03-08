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
from dev0s.classes import exceptions
from dev0s.classes import color
from dev0s.classes import console
from dev0s.classes import env
from dev0s.classes import files
from dev0s.classes import response
from dev0s.classes import objects
from dev0s.classes import defaults
from dev0s.classes import cli
from dev0s.classes import requests as _requests_
from dev0s.classes import code

# _____________________________________________________________________
#
# Shortcuts (also in order):
#   * should be imported as:
#       from dev0s import *
#

# exceptions.
Exceptions = exceptions.Exceptions

# color.
symbol = color.symbol
color = color.color

# console.
Console = console.Console
Loader = Console.Loader
ProgressLoader = Console.ProgressLoader

# environment.
Environment = env.Environment

# files & formats.
gfp = files.gfp
gdate = files.gdate
Files = files.Files
Formats = files.Formats
Generate = Formats.Generate
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