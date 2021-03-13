#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# _____________________________________________________________________
#
# Shortcuts 
#   * imported by import order.
#   * should be imported as.
# 		from dev0s.shortcuts import *
# 
#

# default pip imports.
import os, sys

# import.
import dev0s

# utils.
utils = dev0s.utils

# exceptions.
exceptions = dev0s.exceptions

# color.
color = dev0s.color
symbol = dev0s.symbol

# console.
Loader = dev0s.console.Loader
ProgressLoader = dev0s.console.ProgressLoader

# files & formats.
Files = dev0s.files.Files
Formats = dev0s.files.Formats
gfp = dev0s.files.gfp
gdate = dev0s.files.gdate
Files = dev0s.files.Files
Formats = dev0s.files.Formats
FilePath = Formats.FilePath 
String = Formats.String 
Boolean = Formats.Boolean 
Integer = Formats.Integer 
Date = Formats.Date
Generate = Formats.Generate
Interval = Formats.Interval
File = Files.File
Directory = Files.Directory
Zip = Files.Zip
Image = Files.Image
Bytes = Files.Bytes
Dictionary = Files.Dictionary
Array = Files.Array

# response.
ResponseObject = dev0s.response.ResponseObject

# objects.
Traceback = dev0s.objects.Traceback
Object = dev0s.objects.Object
Thread = dev0s.objects.Thread

# class database.
Database = dev0s.database.Database

# requests.
RestAPI = dev0s.requests.RestAPI

# code.
OutputObject = dev0s.code.OutputObject
Spawn = dev0s.code.Spawn
Version = dev0s.code.Version 
Script = dev0s.code.Script
Python = dev0s.code.Python

#