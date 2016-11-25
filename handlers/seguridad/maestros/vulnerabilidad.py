#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from helper import *
import logging
import requests
import json

logger = logging.getLogger('boilerplate.' + __name__)

class SeguridadVulnerabilidadesHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			self.render("seguridad/maestros/vulnerabilidades.html", helper = helper)
		else:
			self.redirect('/login')

class SeguridadVulnerabilidadesListarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			url = helper.get('maestros') + "vulnerabilidad/listar"
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadVulnerabilidadEditarHandler(BaseHandler):
    def get(self, id_vulnerabilidad):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('maestros') + "vulnerabilidad/obtener/" + str(id_vulnerabilidad)
			vulnerabilidad = requests.get(url)
			vulnerabilidad = json.loads(vulnerabilidad.text)

			url = helper.get('maestros') + "vulnerabilidad/obtener_grupos/" + str(id_vulnerabilidad)
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/vulnerabilidad.html", helper = helper, grupo_activos = response, id = vulnerabilidad["id"], titulo = "Editar", vulnerabilidad = vulnerabilidad, subtitulo="Edite la nueva vulnerabilidad asociada con sus grupos de activos correspondientes", disabled = "")
		else:
			self.write("El usuario debe estar logeado")

class SeguridadVulnerabilidadVerHandler(BaseHandler):
    def get(self, id_vulnerabilidad):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('maestros') + "vulnerabilidad/obtener/" + str(id_vulnerabilidad)
			vulnerabilidad = requests.get(url)
			vulnerabilidad = json.loads(vulnerabilidad.text)

			url = helper.get('maestros') + "vulnerabilidad/obtener_grupos/" + str(id_vulnerabilidad)
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/vulnerabilidad.html", helper = helper, grupo_activos = response, id = vulnerabilidad["id"], titulo = "Ver", vulnerabilidad = vulnerabilidad, subtitulo="Vea la vulnerabilidad asociada con sus grupos de activos correspondientes", disabled = "disabled")
		else:
			self.write("El usuario debe estar logeado")

class SeguridadVulnerabilidadesAgregarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			vulnerabilidad = json.loads('{"codigo":"","descripcion":""}')

			url = helper.get('maestros') + "grupo_activo/listar"
			response = requests.get(url)
			response = helper.array_to_json(response.text)

			self.render("seguridad/maestros/vulnerabilidad.html", helper = helper, grupo_activos = response, id = "E", titulo = "Agregar", subtitulo="Añada una nueva vulnerabilidad asociada con sus grupos de activos correspondientes", vulnerabilidad = vulnerabilidad, disabled = "")
		else:
			self.redirect('/login')

class SeguridadVulnerabilidadGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = json.loads(self.get_argument("data"))
			rpta = ""
			if data['id_vulnerabilidad'] == 'E':
				url = helper.get('maestros') + "vulnerabilidad/crear?codigo=" + str(data['codigo']) + "&descripcion=" + str(data['descripcion'])
				response = requests.get(url)
				rpta = json.loads(response.text)
			else:
				url = helper.get('maestros') + "vulnerabilidad/editar?id=" + str(data['id_vulnerabilidad']) + "&codigo=" + str(data['codigo']) + "&descripcion=" + str(data['descripcion'])
				response = requests.get(url)
				rpta = json.loads(response.text)

			self.write(rpta)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadVulnerabilidadesGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "vulnerabilidad/guardar?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadVulnerabilidadAsociarGrupoHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "vulnerabilidad/asociar_grupo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	