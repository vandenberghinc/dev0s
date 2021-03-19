#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# exceptions:
class Exceptions():
	class JSONDecodeError(Exception):
		pass
	class DuplicateError(Exception):
		pass
	class ParseError(Exception):
		pass
	class InstanceError(Exception):
		pass
	class FormatError(Exception):
		pass
	class UnpackError(Exception):
		pass
	class InvalidUsage(Exception):
		pass
	class InvalidFormatError(Exception):
		pass
	class ArgumentFormatError(Exception):
		pass
	class EmptyArgumentError(Exception):
		pass
	class ArgumentError(Exception):
		pass
	class UnknownArgumentError(Exception):
		pass
	class NetworkError(Exception):
		pass
	class InvalidOperatingSystem(Exception):
		pass
	class AbortError(Exception):
		pass