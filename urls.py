from handlers.foo import FooHandler
from handlers.home import *
from handlers.login import *

url_patterns = [
    (r"/foo", FooHandler),
    
    (r"/", HomeIndexHandler),
    (r"/listar", HomeListarHandler),

    (r"/acceder", LoginAccederHandler),
    (r"/login/acceder", LoginAccederHandler),
    (r"/login", LoginIndexHandler),
    (r"/login/error", LoginErrorHandler),
    (r"/login/estado", LoginEstadoHandler),
    (r"/salir", LoginSalirHandler)
]
