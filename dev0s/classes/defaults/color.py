#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.config import *

# the color object.
class Color(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"color", 
			"initialized":True,
			"description":[], 
			"chapter": "Defaults", }

		# attributes.
		self.purple = "\033[95m"
		self.cyan = "\033[96m"
		self.darkcyan = "\033[35m"
		self.orange = '\033[33m'
		self.blue = "\033[94m"
		self.green = "\033[92m"
		self.yellow = "\033[93m"
		self.grey = "\033[90m"
		self.marked = "\033[100m"
		self.markedred = "\033[101m"
		self.markedgreen = "\033[102m"
		self.markedcyan= "\033[103m"
		self.unknown = "\033[2m"
		self.red = "\033[91m"
		self.bold = "\033[1m"
		self.underlined = "\033[4m"
		self.end = "\033[0m"
		self.italic = "\033[3m"

		#
	def remove(self, string):
		if string == None: return string
		for x in [color.purple,color.cyan,color.darkcyan,color.orange,color.blue,color.green,color.yellow,color.grey,color.marked,color.markedred,color.markedgreen,color.markedcyan,color.unknown,color.red,color.bold,color.underlined,color.end,color.italic]: string = string.replace(x,'')
		return string
	def fill(self, string):
		if string == None: return string
		for x in [
			["&PURPLE&", color.purple],
			["&CYAN&", color.cyan],
			["&DARKCYAN&", color.darkcyan],
			["&ORANGE&", color.orange],
			["&BLUE&", color.blue],
			["&GREEN&", color.green],
			["&YELLOW&", color.yellow],
			["&GREY&", color.grey],
			["&RED&", color.red],
			["&BOLD&", color.bold],
			["&UNDERLINED&", color.underlined],
			["&END&", color.end],
			["&ITALIC&", color.italic],
		]: string = string.replace(x[0],x[1])
		return string
	def boolean(self, boolean, red=True):
		if boolean: return color.green+str(boolean)+color.end
		else: 
			if red: return color.red+str(boolean)+color.end
			else: return color.yellow+str(boolean)+color.end

# the symbol object.
class Symbol(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"symbol", 
			"initialized":True,
			"description":[], 
			"chapter": "Defaults", }

		# attributes.
		self.cornered_arrow = color.grey+'↳'+color.end
		self.cornered_arrow_white = '↳'
		self.good = color.bold+color.green+"✔"+color.end
		self.good_white = "✔"
		self.bad = color.bold+color.red+"✖"+color.end
		self.bad_white = "✖"
		self.medium = color.bold+color.orange+"✖"+color.end
		self.pointer = color.bold+color.purple+"➤"+color.end
		self.star = color.bold+color.yellow+"★"+color.end
		self.ice = color.bold+color.cyan+"❆"+color.end
		self.retry = color.bold+color.red+"↺"+color.end
		self.arrow_left = color.end+color.bold+"⇦"+color.end
		self.arrow_right = color.end+color.bold+"⇨"+color.end
		self.arrow_up = color.end+color.bold+"⇧"+color.end
		self.arrow_down = color.end+color.bold+"⇩"+color.end
		self.copyright = color.bold+color.grey+"©"+color.end
		self.heart = color.bold+color.red+"♥"+color.end
		self.music_note = color.bold+color.purple+"♫"+color.end
		self.celcius = color.bold+color.grey+"℃"+color.end
		self.sun = color.bold+color.yellow+"☀"+color.end
		self.cloud = color.bold+color.grey+"☁"+color.end
		self.moon = color.bold+color.blue+"☾"+color.end
		self.smiley_sad = color.bold+color.red+"☹"+color.end
		self.smiley_happy = color.bold+color.green+"☺"+color.end
		self.infinite = color.bold+color.blue+"∞"+color.end
		self.pi = color.bold+color.green+"π"+color.end
		self.mode = color.bold+color.purple+"ⓜ"+color.end
		self.action = color.bold+color.yellow+"ⓐ"+color.end
		self.info = color.bold+color.grey+"ⓘ"+color.end

	#

# default initialized classes.
color = Color()
symbol = Symbol()