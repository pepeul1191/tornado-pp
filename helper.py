#!/usr/bin/env python
# -*- coding: utf-8 -*-

# helper.py

import requests

class Helper:
	def __init__(self):
		self.accesos = "http://127.0.0.1:3000/"

	def listar_modulos(self):
		url = self.accesos + "modulo/listar"
		response = requests.get(url)
		return response.text

	def listar_menu(self, modulo):
		url = self.accesos + "item/listar/menu/" + modulo
		response = requests.get(url)
		return response.text

	@staticmethod
	def get_url(key):
		diccionario = {'BASE_URL': 'http://localhost:8888/', 'STATIC_URL': 'http://localhost:3001/dashboard'}
		return diccionario[key]