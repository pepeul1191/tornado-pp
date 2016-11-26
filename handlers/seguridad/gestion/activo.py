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

			activo = json.loads('{"codigo":"","descripcion":"","criticidad_id":"","capa_id":"","ubicacion_id":"","tipo_activo_id":"","agente_id":""}')

			#Llaves foraneas
			criticidades = requests.get(helper.get('maestros') + "criticidad/listar")
			criticidades = helper.array_to_json(criticidades.text)

			capas = requests.get(helper.get('maestros') + "capa/listar")
			capas = helper.array_to_json(capas.text)

			ubicaciones = requests.get(helper.get('maestros') + "ubicacion/listar")
			ubicaciones = helper.array_to_json(ubicaciones.text)

			tipo_activos = requests.get(helper.get('maestros') + "tipo_activo/listar")
			tipo_activos = helper.array_to_json(tipo_activos.text)

			agentes = requests.get(helper.get('maestros') + "agente/listar")
			agentes = helper.array_to_json(agentes.text)

			# Listas muchos a muchos
			vulnerabilidades = requests.get(helper.get('maestros') + "vulnerabilidad/listar")
			vulnerabilidades = helper.array_to_json(vulnerabilidades.text)

			amenazas = requests.get(helper.get('maestros') + "amenaza/listar")
			amenazas = helper.array_to_json(amenazas.text)

			controles = requests.get(helper.get('maestros') + "control/listar")
			controles = helper.array_to_json(controles.text)

			riesgos = requests.get(helper.get('maestros') + "riesgo/listar")
			riesgos = helper.array_to_json(riesgos.text)

			self.render("seguridad/gestion/activo.html", helper = helper, vulnerabilidades = vulnerabilidades, controles = controles, amenazas = amenazas, riesgos = riesgos, id = "E", titulo = "Agregar", subtitulo="Añada un activo de información con sus controles, vulnerabilidades, amenazas y riesgos correspondientes", activo = activo, disabled = "", criticidades = criticidades, capas = capas, ubicaciones = ubicaciones, tipo_activos = tipo_activos, agentes = agentes)
		else:
			self.redirect('/login')

class SeguridadActivoEditarHandler(BaseHandler):
    def get(self, id_activo):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('gestion') + "activo/obtener/" + str(id_activo)
			activo = requests.get(url)
			activo = json.loads(activo.text)

			#Llaves foraneas
			criticidades = requests.get(helper.get('maestros') + "criticidad/listar")
			criticidades = helper.array_to_json(criticidades.text)

			capas = requests.get(helper.get('maestros') + "capa/listar")
			capas = helper.array_to_json(capas.text)

			ubicaciones = requests.get(helper.get('maestros') + "ubicacion/listar")
			ubicaciones = helper.array_to_json(ubicaciones.text)

			tipo_activos = requests.get(helper.get('maestros') + "tipo_activo/listar")
			tipo_activos = helper.array_to_json(tipo_activos.text)

			agentes = requests.get(helper.get('maestros') + "agente/listar")
			agentes = helper.array_to_json(agentes.text)

			# Listas muchos a muchos
			vulnerabilidades = requests.get(helper.get('gestion') + "activo/obtener_vulnerabilidades/" + str(id_activo))
			vulnerabilidades = helper.array_to_json(vulnerabilidades.text)

			amenazas = requests.get(helper.get('gestion') + "activo/obtener_amenazas/" + str(id_activo))
			amenazas = helper.array_to_json(amenazas.text)

			controles = requests.get(helper.get('gestion') + "activo/obtener_controles/" + str(id_activo))
			controles = helper.array_to_json(controles.text)

			riesgos = requests.get(helper.get('gestion') + "activo/obtener_riesgos/" + str(id_activo))
			riesgos = helper.array_to_json(riesgos.text)

			self.render("seguridad/gestion/activo.html", helper = helper, vulnerabilidades = vulnerabilidades, controles = controles, amenazas = amenazas, riesgos = riesgos, id = activo['id'], titulo = "Editar", subtitulo="Edite el activo de información con sus controles, vulnerabilidades, amenazas y riesgos correspondientes", activo = activo, disabled = "", criticidades = criticidades, capas = capas, ubicaciones = ubicaciones, tipo_activos = tipo_activos, agentes = agentes)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoVerHandler(BaseHandler):
    def get(self, id_activo):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			url = helper.get('gestion') + "activo/obtener/" + str(id_activo)
			activo = requests.get(url)
			activo = json.loads(activo.text)

			#Llaves foraneas
			criticidades = requests.get(helper.get('maestros') + "criticidad/listar")
			criticidades = helper.array_to_json(criticidades.text)

			capas = requests.get(helper.get('maestros') + "capa/listar")
			capas = helper.array_to_json(capas.text)

			ubicaciones = requests.get(helper.get('maestros') + "ubicacion/listar")
			ubicaciones = helper.array_to_json(ubicaciones.text)

			tipo_activos = requests.get(helper.get('maestros') + "tipo_activo/listar")
			tipo_activos = helper.array_to_json(tipo_activos.text)

			agentes = requests.get(helper.get('maestros') + "agente/listar")
			agentes = helper.array_to_json(agentes.text)

			# Listas muchos a muchos
			vulnerabilidades = requests.get(helper.get('gestion') + "activo/obtener_vulnerabilidades/" + str(id_activo))
			vulnerabilidades = helper.array_to_json(vulnerabilidades.text)

			amenazas = requests.get(helper.get('gestion') + "activo/obtener_amenazas/" + str(id_activo))
			amenazas = helper.array_to_json(amenazas.text)

			controles = requests.get(helper.get('gestion') + "activo/obtener_controles/" + str(id_activo))
			controles = helper.array_to_json(controles.text)

			riesgos = requests.get(helper.get('gestion') + "activo/obtener_riesgos/" + str(id_activo))
			riesgos = helper.array_to_json(riesgos.text)

			self.render("seguridad/gestion/activo.html", helper = helper, vulnerabilidades = vulnerabilidades, controles = controles, amenazas = amenazas, riesgos = riesgos, id = activo['id'], titulo = "Ver", subtitulo="Vea el activo de información con sus controles, vulnerabilidades, amenazas y riesgos correspondientes", activo = activo, disabled = "disabled", criticidades = criticidades, capas = capas, ubicaciones = ubicaciones, tipo_activos = tipo_activos, agentes = agentes)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = json.loads(self.get_argument("data"))
			rpta = ""
			if data['id_activo'] == 'E':
				url = helper.get('gestion') + "activo/crear?data=" + self.get_argument("data")
				response = requests.post(url)
				rpta = json.loads(response.text)
			else:
				url = helper.get('gestion') + "activo/editar?data=" + self.get_argument("data")
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
			url = helper.get('gestion') + "activo/guardar?data=" + data
			response = requests.post(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoAsociarControlHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('gestion') + "activo/asociar_control?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadActivoAsociarVulnerabilidadHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('gestion') + "activo/asociar_vulnerabilidad?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	

class SeguridadActivoAsociarAmenazaHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('gestion') + "activo/asociar_amenaza?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	

class SeguridadActivoAsociarRiegsoHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('gestion') + "activo/asociar_riesgo?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")	