#!/usr/bin/env python
# -*- coding: utf-8 -*-

# libs/cyper.py

from Crypto.Cipher import AES
import base64

class Cipher:
	def __init__(self):
		secret_key = '1234567890123456'
		self.cipher = AES.new(secret_key,AES.MODE_ECB)

	def encoded(self, palabra):
		return base64.b64encode(self.cipher.encrypt(palabra.rjust(32)))

	def decoded(self, palabra):
		return cipher.decrypt(base64.b64decode(palabra)).strip()