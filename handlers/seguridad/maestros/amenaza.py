#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from helper import *
import logging
import requests
import json

logger = logging.getLogger('boilerplate.' + __name__)

class SeguridadAmenazasHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			self.render("seguridad/maestros/amenazas.html", helper = helper)
		else:
			self.redirect('/login')

class SeguridadAmenazasListarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			url = helper.get('maestros') + "amenaza/listar"
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadAmenazaEditarHandler(BaseHandler):
    def get(self, id_amenaza):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('maestros') + "amenaza/obtener/" + str(id_amenaza)
			amenaza = requests.get(url)
			amenaza = json.loads(amenaza.text)

			url = helper.get('maestros') + "amenaza/obtener_grupos/" + str(id_amenaza)
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/amenaza.html", helper = helper, grupo_activos = response, id = amenaza["id"], titulo = "Editar", amenaza = amenaza, subtitulo="Edite la nueva amenza asociada con sus grupos de activos correspondientes", disabled = "")
		else:
			self.write("El usuario debe estar logeado")

class SeguridadAmenazaVerHandler(BaseHandler):
    def get(self, id_amenaza):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('maestros') + "amenaza/obtener/" + str(id_amenaza)
			amenaza = requests.get(url)
			amenaza = json.loads(amenaza.text)

			url = helper.get('maestros') + "amenaza/obtener_grupos/" + str(id_amenaza)
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/amenaza.html", helper = helper, grupo_activos = response, id = amenaza["id"], titulo = "Ver", amenaza = amenaza, subtitulo="Vea la amenza asociada con sus grupos de activos correspondientes", disabled = "disabled")
		else:
			self.write("El usuario debe estar logeado")

class SeguridadAmenazasAgregarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			amenaza = json.loads('{"codigo":"","descripcion":""}')

			url = helper.get('maestros') + "grupo_activo/listar"
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/amenaza.html", helper = helper, grupo_activos = response, id = "E", titulo = "Agregar", subtitulo="Añada una nueva amenza asociada con sus grupos de activos correspondientes", amenaza = amenaza, disabled = "")
		else:
			self.redirect('/login')

class SeguridadAmenazaGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = json.loads(self.get_argument("data"))
			rpta = ""
			if data['id_amenaza'] == 'E':
				url = helper.get('maestros') + "amenaza/crear?codigo=" + str(data['codigo']) + "&descripcion=" + str(data['descripcion'])
				response = requests.get(url)
				rpta = json.loads(response.text)
			else:
				url = helper.get('maestros') + "amenaza/editar?id=" + str(data['id_amenaza']) + "&codigo=" + str(data['codigo']) + "&descripcion=" + str(data['descripcion'])
				response = requests.get(url)
				rpta = json.loads(response.text)

			self.write(rpta)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadAmenazasGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/guardar?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadAmenazaAsociarGrupoHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	