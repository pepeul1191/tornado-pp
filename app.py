#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns

from helper import *

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)

def main():
	app = TornadoBoilerplate()
	http_server = tornado.httpserver.HTTPServer(app)
	options.port  = int(raw_input('Ingrese el puerto:'))
	http_server.listen(options.port)
	print "Instancia del servidor Tornado ejecutándose en el puerto : " + str(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
