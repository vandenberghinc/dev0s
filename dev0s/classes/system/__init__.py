#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports (over here to prevent circular).
from dev0s.classes.system import disks, env, service, system, browser

# the system module class.
class System():

	# disks.
	disks = disks.disks

	# env.
	env = env.env

	# service.
	Service = service.Service

	# system.
	check_user = system.check_user
	check_group = system.check_group
	User = system.User
	Group = system.Group

	# browser.
	Browser = browser.Browser