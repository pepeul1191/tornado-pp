from handlers.home import *
from handlers.login import *
from handlers.accesos import *
from handlers.m_seguridad import *
from handlers.seguridad.control import *
from handlers.seguridad.tipo_activo import *

url_patterns = [
    (r"/accesos", AccesosIndexHandler),

    (r"/", HomeIndexHandler),
    (r"/listar", HomeListarHandler),

    (r"/acceder", LoginAccederHandler),
    (r"/login/acceder", LoginAccederHandler),
    (r"/login", LoginIndexHandler),
    (r"/login/error", LoginErrorHandler),
    (r"/login/estado", LoginEstadoHandler),
    (r"/salir", LoginSalirHandler),

    (r"/seguridad", SeguridadIndexHandler),
    (r"/seguridad/maestros/controles", SeguridadControlesHandler),
    (r"/seguridad/maestros/controles/listar", SeguridadControlesListarHandler),
    (r"/seguridad/maestros/controles/guardar", SeguridadControlesGuardarHandler),
    (r"/seguridad/maestros/tipo_activos", SeguridadTipoActivosHandler),
    (r"/seguridad/maestros/tipo_activos/listar", SeguridadTipoActivosListarHandler),
    (r"/seguridad/maestros/tipo_activos/guardar", SeguridadTipoActivosGuardarHandler)
]
