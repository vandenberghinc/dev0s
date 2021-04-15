#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.encryption import aes, rsa, agent

# the encryption module class.
class Encryption():

	# aes.
	AES = aes.AES
	AsymmetricAES = aes.AsymmetricAES
	Database = aes.Database

	# rsa.
	RSA = rsa.RSA
	#EncryptedDictionary = rsa.EncryptedDictionary

	# agent.
	Agent = agent.Agent

	