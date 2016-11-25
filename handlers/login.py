#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
import logging
import requests
import json
from helper import *
from cypher import Cipher
import datetime

logger = logging.getLogger('boilerplate.' + __name__)

class LoginIndexHandler(BaseHandler):
    def get(self):
		helper = Helper()
		self.render("login/index.html", error=0, helper=helper)

class LoginAccederHandler(BaseHandler):
    def post(self):
		usuario = self.get_argument("usuario")
		contrasenia =  self.get_argument("contrasenia")
		cipher = Cipher()
		helper = Helper()
		url = helper.get("accesos") + "usuario/validar?usuario=" + str(usuario) + "&contrasenia=" + str(cipher.encoded(contrasenia))
		response = requests.post(url)
		if str(response.text) == "1":
			self.set_secure_cookie("usuario", usuario)
			self.set_secure_cookie("tiempo", str(datetime.datetime.now()))
			self.redirect('/')
			return
		else:
			self.redirect('/login/error')
			return

class LoginErrorHandler(BaseHandler):
    def get(self):
		helper = Helper()
		self.render("login/index.html", error=1, helper=helper)

class LoginEstadoHandler(BaseHandler):
	def get(self):
		rpta = ""
		if not self.get_secure_cookie("usuario"):
			rpta = "<h1>El usuario no se encuentra logueado</h1>"
		else:
			rpta = "<h1>Usuario Logeado</h1><ul><li>" + str(self.get_secure_cookie("usuario")) + "</li><li>" +  str(self.get_secure_cookie("tiempo")) + "</li></ul>"

		self.write(rpta)

class LoginSalirHandler(BaseHandler):
	def get(self):
		if self.get_secure_cookie("usuario"):
			self.clear_cookie("usuario")
		if self.get_secure_cookie("tiempo"):
			self.clear_cookie("tiempo")
	
		self.redirect('/login')
		return