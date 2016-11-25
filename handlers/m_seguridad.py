from handlers.base import BaseHandler
from helper import *
import logging
import requests
import json

logger = logging.getLogger('boilerplate.' + __name__)

class SeguridadIndexHandler(BaseHandler):
	def get(self):
		helper = Helper()
		if self.get_secure_cookie("usuario")  or helper.get('ambiente') != 'produccion':
			helper.set('modulos', json.loads(helper.listar_modulos()))
			helper.set('menus', json.loads(helper.listar_menu("Seguridad")))
			helper.set('activo', 'Seguridad')

			self.render("seguridad/maestros/index.html", helper = helper)
		else:
			self.redirect('/login')