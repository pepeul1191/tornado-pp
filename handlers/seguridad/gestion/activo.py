#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from helper import *
import logging
import requests
import json

logger = logging.getLogger('boilerplate.' + __name__)

class SeguridadActivosHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			self.render("seguridad/gestion/activos.html", helper = helper)
		else:
			self.redirect('/login')

class SeguridadActivosListarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			url = helper.get('gestion') + "activo/listar"
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivosAgregarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			activo = json.loads('{"codigo":"","descripcion":""}')

			vulnerabilidades = requests.get(helper.get('maestros') + "vulnerabilidad/listar")
			vulnerabilidades = helper.array_to_json(vulnerabilidades.text)

			amenazas = requests.get(helper.get('maestros') + "amenaza/listar")
			amenazas = helper.array_to_json(amenazas.text)

			controles = requests.get(helper.get('maestros') + "control/listar")
			controles = helper.array_to_json(controles.text)

			riesgos = requests.get(helper.get('maestros') + "riesgo/listar")
			riesgos = helper.array_to_json(riesgos.text)

			self.render("seguridad/gestion/activo.html", helper = helper, vulnerabilidades = vulnerabilidades, controles = controles, amenazas = amenazas, riesgos = riesgos, id = "E", titulo = "Agregar", subtitulo="Añada un activo de información con sus controles, vulnerabilidades, amenazas y riesgos correspondientes", activo = activo, disabled = "")
		else:
			self.redirect('/login')

class SeguridadActivoEditarHandler(BaseHandler):
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

class SeguridadActivoVerHandler(BaseHandler):
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

class SeguridadActivoGuardarHandler(BaseHandler):
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

class SeguridadActivosGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/guardar?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoAsociarControlHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoAsociarVulnerabilidadHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	

class SeguridadActivoAsociarAmenazaHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	

class SeguridadActivoAsociarRiegsoHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "amenaza/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	