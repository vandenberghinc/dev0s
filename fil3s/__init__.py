#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from fil3s.classes.defaults import Files,Formats,gfp,gdate
from fil3s.classes.code import Code

# shortcuts.
FilePath = Formats.FilePath 
String = Formats.String 
Boolean = Formats.Boolean 
Integer = Formats.Integer 
Version = Formats.Version 
Date = Formats.Date
File = Files.File
Directory = Files.Directory
Zip = Files.Zip
Image = Files.Image
Bytes = Files.Bytes
Dictionary = Files.Dictionary
Array = Files.Array
Script = Code.Script
Python = Code.Python

# source path & version.
source = Directory(gfp.base(__file__))
base = Directory(source.fp.base())
try: version = Version(Files.load(source.join(".version.py")))
except: version = None