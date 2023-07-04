from funciones.funciones import *
# from funciones.funciones import inicio, editProfile, not_found, server_error


def configurar_rutas(app):
    app.add_url_rule('/', 'inicio', inicio)
    #   app.add_url_rule('/tienda', methods=['GET'], endpoint='inicio', view_func=inicio)
    app.add_url_rule('/info', 'editProfile', editProfile)
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)


def saludar():
    return 'hola'
