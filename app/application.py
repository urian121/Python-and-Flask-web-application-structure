
from controllers.controller_home import configurar_rutas
# Importando la clase Flask de flask (librería)
from flask import Flask


# Creando una instancia de la aplicación Flask
# Creando una app instanciando la clase Flask (automáticamente el nombre de la app)
app = Flask(__name__, template_folder='templates')
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

# Rutas
configurar_rutas(app)


# Inicializando app
if __name__ == '__main__':
    app.run()
