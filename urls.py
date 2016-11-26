from handlers.home import *
from handlers.login import *
from handlers.accesos import *

from handlers.m_seguridad import *
from handlers.seguridad.maestros.control import *
from handlers.seguridad.maestros.tipo_activo import *
from handlers.seguridad.maestros.agente import *
from handlers.seguridad.maestros.amenaza import *
from handlers.seguridad.maestros.capa import *
from handlers.seguridad.maestros.vulnerabilidad import *
from handlers.seguridad.maestros.criticidad import *
from handlers.seguridad.maestros.ubicacion import *
from handlers.seguridad.maestros.riesgo import *
from handlers.seguridad.maestros.grupo_activo import *

from handlers.seguridad.gestion.activo import *

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
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/agentes", SeguridadAgentesHandler),
    (r"/seguridad/maestros/agentes/listar", SeguridadAgentesListarHandler),
    (r"/seguridad/maestros/agentes/guardar", SeguridadAgentesGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/amenazas", SeguridadAmenazasHandler),
    (r"/seguridad/maestros/amenazas/listar", SeguridadAmenazasListarHandler),
    (r"/seguridad/maestros/amenazas/agregar", SeguridadAmenazasAgregarHandler),
    (r"/seguridad/maestros/amenaza/editar/([0-9]+)", SeguridadAmenazaEditarHandler),
    (r"/seguridad/maestros/amenaza/ver/([0-9]+)", SeguridadAmenazaVerHandler),
    (r"/seguridad/maestros/amenazas/guardar", SeguridadAmenazasGuardarHandler),
    (r"/seguridad/maestros/amenaza/guardar", SeguridadAmenazaGuardarHandler),
    (r"/seguridad/maestros/amenaza/asociar_grupo", SeguridadAmenazaAsociarGrupoHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/capas", SeguridadCapasHandler),
    (r"/seguridad/maestros/capas/listar", SeguridadCapasListarHandler),
    (r"/seguridad/maestros/capas/guardar", SeguridadCapasGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/controles", SeguridadControlesHandler),
    (r"/seguridad/maestros/controles/listar", SeguridadControlesListarHandler),
    (r"/seguridad/maestros/controles/guardar", SeguridadControlesGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/criticidades", SeguridadCriticidadesHandler),
    (r"/seguridad/maestros/criticidades/listar", SeguridadCriticidadesListarHandler),
    (r"/seguridad/maestros/criticidades/guardar", SeguridadCriticidadesGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/grupo_activos", SeguridadGrupoActivosHandler),
    (r"/seguridad/maestros/grupo_activos/listar", SeguridadGrupoActivosListarHandler),
    (r"/seguridad/maestros/grupo_activos/guardar", SeguridadGrupoActivosGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/riesgos", SeguridadRiesgosHandler),
    (r"/seguridad/maestros/riesgos/listar", SeguridadRiesgosListarHandler),
    (r"/seguridad/maestros/riesgos/guardar", SeguridadRiesgosGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/tipo_activos", SeguridadTipoActivosHandler),
    (r"/seguridad/maestros/tipo_activos/listar", SeguridadTipoActivosListarHandler),
    (r"/seguridad/maestros/tipo_activos/guardar", SeguridadTipoActivosGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/ubicaciones", SeguridadUbicacionesHandler),
    (r"/seguridad/maestros/ubicaciones/listar", SeguridadUbicacionesListarHandler),
    (r"/seguridad/maestros/ubicaciones/guardar", SeguridadUbicacionesGuardarHandler),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    (r"/seguridad/maestros/vulnerabilidades", SeguridadVulnerabilidadesHandler),
    (r"/seguridad/maestros/vulnerabilidades/listar", SeguridadVulnerabilidadesListarHandler),
    (r"/seguridad/maestros/vulnerabilidades/agregar", SeguridadVulnerabilidadesAgregarHandler),
    (r"/seguridad/maestros/vulnerabilidad/editar/([0-9]+)", SeguridadVulnerabilidadEditarHandler),
    (r"/seguridad/maestros/vulnerabilidad/ver/([0-9]+)", SeguridadVulnerabilidadVerHandler),
    (r"/seguridad/maestros/vulnerabilidades/guardar", SeguridadVulnerabilidadesGuardarHandler),
    (r"/seguridad/maestros/vulnerabilidad/guardar", SeguridadVulnerabilidadGuardarHandler),
    (r"/seguridad/maestros/vulnerabilidad/asociar_grupo", SeguridadVulnerabilidadAsociarGrupoHandler),

    (r"/seguridad/gestion/activos", SeguridadActivosHandler),
    (r"/seguridad/gestion/activos/listar", SeguridadActivosListarHandler),
    (r"/seguridad/gestion/activos/agregar", SeguridadActivosAgregarHandler),
    (r"/seguridad/gestion/activo/editar/([0-9]+)", SeguridadActivoEditarHandler),
    (r"/seguridad/gestion/activo/ver/([0-9]+)", SeguridadActivoVerHandler),
    (r"/seguridad/gestion/activos/guardar", SeguridadActivosGuardarHandler),
    (r"/seguridad/gestion/activo/guardar", SeguridadActivoGuardarHandler),
    (r"/seguridad/gestion/activo/asociar_criticidad", SeguridadActivoAsociarControlHandler),
    (r"/seguridad/gestion/activo/asociar_control", SeguridadActivoAsociarControlHandler),
    (r"/seguridad/gestion/activo/asociar_vulnerabilidad", SeguridadActivoAsociarVulnerabilidadHandler),
    (r"/seguridad/gestion/activo/asociar_amenaza", SeguridadActivoAsociarAmenazaHandler),
    (r"/seguridad/gestion/activo/asociar_riesgo", SeguridadActivoAsociarRiegsoHandler)
]
