#!/usr/bin/env python
# -*- coding: utf-8 -*-

# helper.py

import requests
import json

class Helper:
	def __init__(self):
		self.diccionario = {
			'BASE_URL': 'http://localhost:8888/',
			'STATICS_URL' : 'http://localhost:8001/dashboard/',
			'accesos' : 'http://127.0.0.1:3000/',
			'maestros' : 'http://127.0.0.1:3001/',
			'ambiente': 'desarrollo'
		}

	def listar_modulos(self):
		url = self.get('accesos') + "modulo/listar"
		response = requests.get(url)
		return response.text

	def listar_menu(self, modulo):
		url = self.get('accesos') + "item/listar/menu/" + modulo
		response = requests.get(url)
		return response.text

	def set(self, key, value):
		self.diccionario[key] = value

	def get(self, key):
		return self.diccionario[key]

	def array_to_json(self, string):
		rpta = []
		temps = json.loads(string)

		for temp in temps:
			rpta.append(json.loads(temp))

		return rpta
