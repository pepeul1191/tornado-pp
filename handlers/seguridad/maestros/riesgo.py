from handlers.base import BaseHandler
from helper import *
import logging
import requests
import json

logger = logging.getLogger('boilerplate.' + __name__)

class SeguridadRiesgosHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			self.render("seguridad/maestros/riesgos.html", helper = helper)
		else:
			self.redirect('/login')

class SeguridadRiesgosListarHandler(BaseHandler):
    def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			url = helper.get('maestros') + "riesgo/listar"
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")

class SeguridadRiesgosGuardarHandler(BaseHandler):
	def post(self):
		helper = Helper()
		if self.get_secure_cookie("usuario") or helper.get('ambiente') != 'produccion':
			data = self.get_argument("data")
			url = helper.get('maestros') + "riesgo/guardar?data=" + data
			response = requests.get(url)

			self.write(response.text)
		else:
			self.write("El usuario debe estar logeado")