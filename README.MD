### Lo primero seria crear tu entorno virtual, ejecutarndo

`virtualenv env`

### Activas tu entorno virtual

`. env/Scripts/activate`

### Luego instalas el Framework de Flask

`pip instal flask`

### Ahora solo entras a la carpeta app asi:

`cd app/`

### Ya solo queda ejecutar la aplicación

` python app.py`

## Resultado

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/portada-estructura-proyecto-python-flask.PNG)

├── app/
│ ├── controllers/
│ │ ── controller_home.py
│ ├── funciones/
│ │ ── funciones.py
│ ├── routers/
| │ ── router.py
│ ├── static/
│ ├── templates/
├── app.py
└── run.py

├── app/
│ ├── controllers/
│ │ └── controller_home.py
│ ├── funciones/
│ │ └── funciones.py
│ ├── routers/
│ │ └── router.py
│ ├── static/
│ ├── templates/
│ │ └── base_index.html
├── app.py
└── run.py
