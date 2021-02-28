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
source_path = gfp.base(__file__)
try: version = Files.load(source_path+".version.py").replace("\n","").replace(" ","")
except: version = None