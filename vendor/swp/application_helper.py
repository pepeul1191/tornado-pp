#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vendor/swp/application_helper.py

import requests
import json
import pprint

class ApplicationHelper:
	def menu_izquierdo(self, modulo):
		resp = requests.get('http://localhost:5001/menu/accesos_modulo/' + modulo)
		if resp.status_code != 200:
		    print resp

		return resp.json()


if __name__ == '__main__':
	ah = ApplicationHelper()
	rpta = ah.menu_izquierdo("Accesos")
	for todo_item in rpta:
		print todo_item